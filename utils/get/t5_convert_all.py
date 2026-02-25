#!/usr/bin/env -S uv run
# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "pymupdf==1.27.1",
#     "pymupdf4llm==0.3.4",
#     "typer>=0.9.0",
#     "rich>=13.0.0",
# ]
# ///
"""Batch-convert all acquired sources to Markdown for LLM extraction.

Routes each source file to the right converter based on extension:
  - PDF  → pymupdf4llm (reuses pdf2md.py logic)
  - EPUB → pandoc -f epub -t markdown
  - ipynb → pandoc -f ipynb -t markdown
  - HTML → pandoc -f html -t markdown
  - RST  → pandoc -f rst -t markdown
  - .md  → copy as-is (already target format)
  - .txt → copy with .md extension
  - Directories → custom concatenation per source

Writes a manifest CSV logging every conversion.

Usage:
    uv run utils/convert_all.py                    # convert everything
    uv run utils/convert_all.py --dry-run          # preview without writing
    uv run utils/convert_all.py --only-lang en     # only English sources
    uv run utils/convert_all.py --force            # re-convert even if .md exists
"""

from __future__ import annotations

import csv
import re
import shutil
import subprocess
import sys
from collections.abc import Callable
from datetime import datetime, timezone
from pathlib import Path
from typing import Annotated

import typer
from rich.console import Console
from rich.table import Table

# ---------------------------------------------------------------------------
# pdf2md reuse — import convert/verify from sibling script
# ---------------------------------------------------------------------------

_UTILS_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(_UTILS_DIR))
from pdf2md import convert as pdf_convert, verify as pdf_verify  # noqa: E402

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

SOURCES_ROOT = Path(__file__).resolve().parent.parent / "research" / "pipeline-canon" / "sources"
MANIFEST_PATH = SOURCES_ROOT / "convert-manifest.csv"

LANG_DIRS = ["en", "es", "fr", "pt"]

# Extensions to skip in NICAR batch processing
SKIP_EXTENSIONS = {
    ".png", ".jpg", ".jpeg", ".gif", ".svg", ".ico", ".webp", ".bmp",
    ".mp3", ".mp4", ".webm", ".wav", ".ogg",
    ".ttf", ".woff", ".woff2", ".eot", ".otf",
    ".css", ".js", ".ts", ".mjs",
    ".csv", ".json", ".geojson", ".xlsx", ".xls", ".xml",
    ".yml", ".yaml", ".toml", ".cfg", ".ini", ".lock",
    ".py", ".r", ".R", ".sh", ".sql", ".makefile",
    ".zip", ".gz", ".tar", ".bz2",
    ".sample", ".output", ".pyc", ".pyo",
    ".gitignore", ".gitmodules", ".gitattributes",
    ".rproj", ".rmd",  # .Rmd handled separately for Wells book
    ".key", ".pptx", ".docx",
    ".pdf.xlsx",  # artifact
}

# NICAR year mapping for consolidation: directory prefix → (year, output_slug)
NICAR_YEAR_MAP = {
    "nicar14-notes": (2014, "97a-nicar-2014"),
    "nicar15-notes": (2015, "97b-nicar-2015"),
    "nicar16-notes": (2016, "97c-nicar-2016"),
    "nicar18-notes": (2018, "97d-nicar-2018"),
    "2020": (2020, "97e-nicar-2020"),
    "2021": (2021, "97f-nicar-2021"),
    "2022": (2022, "97g-nicar-2022"),
    "2023": (2023, "97h-nicar-2023"),
    "2024": (2024, "97i-nicar-2024"),
    "2025": (2025, "97j-nicar-2025"),
}

console = Console()
err_console = Console(stderr=True)

# ---------------------------------------------------------------------------
# Manifest tracking
# ---------------------------------------------------------------------------

ManifestRow = dict[str, str]


def word_count(text: str) -> int:
    return len(text.split())


def load_existing_manifest() -> dict[str, ManifestRow]:
    """Load existing manifest keyed by output_path. Returns empty dict if missing."""
    if not MANIFEST_PATH.exists():
        return {}
    by_output: dict[str, ManifestRow] = {}
    with open(MANIFEST_PATH, newline="") as f:
        for row in csv.DictReader(f):
            by_output[row["output_path"]] = row
    return by_output


def make_row(
    source_path: Path,
    output_path: Path,
    fmt: str,
    wc: int,
    warnings: str = "",
    status: str = "ok",
) -> ManifestRow:
    return {
        "source_path": str(source_path.relative_to(SOURCES_ROOT)),
        "output_path": str(output_path.relative_to(SOURCES_ROOT)),
        "format": fmt,
        "word_count": str(wc),
        "warnings": warnings,
        "status": status,
        "timestamp": datetime.now(timezone.utc).isoformat(timespec="seconds"),
    }


# ---------------------------------------------------------------------------
# Converters
# ---------------------------------------------------------------------------


FALLBACK_DELTA_PCT = 25.0


def pdf_raw_extract(pdf_path: str) -> str:
    """Fallback: extract text via pymupdf get_text() when pymupdf4llm drops pages."""
    import pymupdf as _pymupdf

    with _pymupdf.open(pdf_path) as doc:
        parts = []
        for page in doc:
            text = page.get_text().strip()
            if text:
                parts.append(text)
    return "\n\n---\n\n".join(parts)


def convert_pdf(src: Path, dst: Path) -> ManifestRow:
    """Convert PDF using pdf2md.py's convert() + verify().

    If pymupdf4llm loses >25% of words vs raw extraction, falls back to
    plain get_text() — this handles PDFs with one-line-per-block layouts
    that pymupdf4llm can't reconstruct.
    """
    md_text = pdf_convert(str(src), use_layout=False, margins=50)
    warns, stats = pdf_verify(str(src), md_text)

    # Fallback: if pymupdf4llm dropped too many words, use raw extraction
    if stats.delta_pct > FALLBACK_DELTA_PCT:
        raw_text = pdf_raw_extract(str(src))
        raw_wc = word_count(raw_text)
        if raw_wc > stats.md_words:
            console.print(
                f"  [yellow]pymupdf4llm lost {stats.delta_pct}% — "
                f"falling back to raw extraction "
                f"({stats.md_words:,} → {raw_wc:,} words)[/]"
            )
            md_text = raw_text
            warns, stats = pdf_verify(str(src), md_text)

    dst.write_text(md_text)
    warn_str = "; ".join(warns) if warns else ""
    status = "warning" if warns else "ok"

    console.print(
        f"  PDF → {stats.md_words:,} words"
        f"  (delta {stats.delta_pct}%"
        f", {stats.missing_headings} missing headings)"
    )
    return make_row(src, dst, "pdf", stats.md_words, warn_str, status)


def run_pandoc(src: Path, from_fmt: str, dst: Path) -> str:
    """Run pandoc and return the markdown text."""
    result = subprocess.run(
        ["pandoc", "-f", from_fmt, "-t", "markdown", "--wrap=none", str(src)],
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        raise RuntimeError(f"pandoc failed on {src}: {result.stderr.strip()}")
    dst.write_text(result.stdout)
    return result.stdout


def convert_epub(src: Path, dst: Path) -> ManifestRow:
    """Convert EPUB via pandoc."""
    md_text = run_pandoc(src, "epub", dst)
    wc = word_count(md_text)
    console.print(f"  EPUB → {wc:,} words")
    return make_row(src, dst, "epub", wc)


def convert_ipynb(src: Path, dst: Path) -> ManifestRow:
    """Convert Jupyter notebook via pandoc (preserves markdown cells + code blocks)."""
    md_text = run_pandoc(src, "ipynb", dst)
    wc = word_count(md_text)
    console.print(f"  ipynb → {wc:,} words")
    return make_row(src, dst, "ipynb", wc)


def convert_html(src: Path, dst: Path) -> ManifestRow:
    """Convert HTML via pandoc."""
    md_text = run_pandoc(src, "html", dst)
    wc = word_count(md_text)
    console.print(f"  HTML → {wc:,} words")
    return make_row(src, dst, "html", wc)


def convert_rst(src: Path, dst: Path) -> ManifestRow:
    """Convert reStructuredText via pandoc."""
    md_text = run_pandoc(src, "rst", dst)
    wc = word_count(md_text)
    console.print(f"  RST → {wc:,} words")
    return make_row(src, dst, "rst", wc)


def copy_md(src: Path, dst: Path) -> ManifestRow:
    """Copy existing .md file (already in target format)."""
    text = src.read_text(errors="replace")
    if src != dst:
        dst.write_text(text)
    wc = word_count(text)
    console.print(f"  MD (as-is) → {wc:,} words")
    return make_row(src, dst, "md", wc)


def copy_txt(src: Path, dst: Path) -> ManifestRow:
    """Copy .txt to .md."""
    text = src.read_text(errors="replace")
    dst.write_text(text)
    wc = word_count(text)
    console.print(f"  TXT → MD → {wc:,} words")
    return make_row(src, dst, "txt", wc)


# ---------------------------------------------------------------------------
# Directory-based source handlers
# ---------------------------------------------------------------------------


def strip_yaml_frontmatter(text: str) -> str:
    """Remove YAML front matter delimited by --- ... ---"""
    if text.startswith("---"):
        end = text.find("\n---", 3)
        if end != -1:
            return text[end + 4:].lstrip("\n")
    return text


def convert_wells_book(src_dir: Path, dst: Path) -> ManifestRow:
    """Concatenate Rob Wells' 27 Rmd chapters in numeric order."""
    # Use the pre-built epub if available (better formatting)
    epub = src_dir / "_book" / "datajournalism.epub"
    if epub.exists():
        console.print("  Using pre-built EPUB from _book/")
        return convert_epub(epub, dst)

    # Fallback: concatenate Rmd sources
    rmd_files = sorted(src_dir.glob("[0-9][0-9]-*.Rmd"))
    index = src_dir / "index.Rmd"

    parts: list[str] = []
    if index.exists():
        parts.append(strip_yaml_frontmatter(index.read_text(errors="replace")))

    for rmd in rmd_files:
        text = strip_yaml_frontmatter(rmd.read_text(errors="replace"))
        parts.append(f"\n\n---\n\n{text}")

    combined = "\n\n".join(parts)
    dst.write_text(combined)
    wc = word_count(combined)
    console.print(f"  Rmd concat ({len(rmd_files)} chapters) → {wc:,} words")
    return make_row(src_dir, dst, "rmd-concat", wc)


def convert_french_guide(src_dir: Path, dst: Path) -> ManifestRow:
    """Concatenate Guide du Datajournalisme pages in numeric order."""
    pages_dir = src_dir / "pages"
    md_files = sorted(pages_dir.glob("*.md"))

    parts: list[str] = []
    for md in md_files:
        text = strip_yaml_frontmatter(md.read_text(errors="replace"))
        parts.append(text)

    combined = "\n\n---\n\n".join(parts)
    dst.write_text(combined)
    wc = word_count(combined)
    console.print(f"  Jekyll concat ({len(md_files)} pages) → {wc:,} words")
    return make_row(src_dir, dst, "jekyll-concat", wc)


def convert_propublica_guide(src_dir: Path, dst: Path) -> ManifestRow:
    """Concatenate ProPublica guide following SUMMARY.md order."""
    summary = src_dir / "SUMMARY.md"
    summary_text = summary.read_text(errors="replace")

    # Parse file references from SUMMARY.md: [Title](path.md)
    link_pattern = re.compile(r"\[([^\]]+)\]\(([^)]+\.md)\)")
    parts: list[str] = []

    for title, rel_path in link_pattern.findall(summary_text):
        md_file = src_dir / rel_path
        if md_file.exists():
            text = md_file.read_text(errors="replace").strip()
            parts.append(text)
        else:
            parts.append(f"# {title}\n\n*[File not found: {rel_path}]*")

    combined = "\n\n---\n\n".join(parts)
    dst.write_text(combined)
    wc = word_count(combined)
    console.print(f"  GitBook concat ({len(parts)} sections) → {wc:,} words")
    return make_row(src_dir, dst, "gitbook-concat", wc)


def convert_maryjo_webster(src_dir: Path, dst: Path) -> ManifestRow:
    """Concatenate MaryJo Webster training materials."""
    parts: list[str] = []

    # README
    readme = src_dir / "README.md"
    if readme.exists():
        parts.append(readme.read_text(errors="replace"))

    # pgp.md (main content)
    pgp = src_dir / "pgp.md"
    if pgp.exists():
        parts.append(pgp.read_text(errors="replace"))

    # HTML pages → convert via pandoc
    for html_file in sorted(src_dir.glob("*.html")):
        if html_file.name.startswith("_"):
            continue
        try:
            result = subprocess.run(
                ["pandoc", "-f", "html", "-t", "markdown", "--wrap=none", str(html_file)],
                capture_output=True, text=True,
            )
            if result.returncode == 0 and result.stdout.strip():
                parts.append(f"# {html_file.stem}\n\n{result.stdout}")
        except Exception as e:
            err_console.print(f"  [red]pandoc failed for {html_file.name}:[/] {e}")

    # R/ subdirectory Rmd files
    r_dir = src_dir / "R"
    if r_dir.exists():
        for rmd in sorted(r_dir.glob("*.Rmd")):
            text = strip_yaml_frontmatter(rmd.read_text(errors="replace"))
            parts.append(f"# {rmd.stem}\n\n{text}")

    # tipsheets/ PDFs
    tipsheets = src_dir / "tipsheets"
    if tipsheets.exists():
        for pdf in sorted(tipsheets.glob("*.pdf")):
            try:
                md_text = pdf_convert(str(pdf), use_layout=False, margins=50)
                parts.append(f"# {pdf.stem}\n\n{md_text}")
            except Exception as e:
                parts.append(f"# {pdf.stem}\n\n*[PDF conversion failed: {e}]*")

    combined = "\n\n---\n\n".join(parts)
    dst.write_text(combined)
    wc = word_count(combined)
    console.print(f"  Training site concat ({len(parts)} parts) → {wc:,} words")
    return make_row(src_dir, dst, "site-concat", wc)


# ---------------------------------------------------------------------------
# NICAR archive processing
# ---------------------------------------------------------------------------


def should_convert_nicar(path: Path) -> str | None:
    """Return pandoc format string if this file should be converted, else None."""
    suffix = path.suffix.lower()
    if suffix in (".md", ".txt"):
        return "text"  # just read as-is
    if suffix == ".pdf":
        return "pdf"
    if suffix == ".ipynb":
        return "ipynb"
    if suffix == ".html":
        return "html"
    if suffix == ".rst":
        return "rst"
    if suffix == ".qmd":
        return "text"  # quarto markdown is still markdown
    if suffix == ".rmd":
        return "text"  # R markdown is still markdown
    return None


def get_nicar_year(path: Path, nicar_dir: Path) -> int | None:
    """Determine the NICAR year from a file path."""
    rel = path.relative_to(nicar_dir)
    top_dir = rel.parts[0] if len(rel.parts) > 1 else None

    if top_dir:
        # Legacy note repos
        for prefix, (year, _) in NICAR_YEAR_MAP.items():
            if top_dir == prefix or top_dir.startswith(prefix):
                return year
        # Year-prefixed dirs: 2020-batch-pdfs-pdfplumber → 2020
        m = re.match(r"^(20\d{2})-", top_dir)
        if m:
            return int(m.group(1))

    # Flat files: 2024-large-scale-scraping.md → 2024
    m = re.match(r"^(20\d{2})-", path.name)
    if m:
        return int(m.group(1))

    return None


def convert_nicar_file(path: Path, fmt: str) -> str | None:
    """Convert a single NICAR file and return markdown text. Returns None on failure."""
    try:
        if fmt == "text":
            return path.read_text(errors="replace")
        elif fmt == "pdf":
            return pdf_convert(str(path), use_layout=False, margins=50)
        elif fmt in ("ipynb", "html", "rst"):
            result = subprocess.run(
                ["pandoc", "-f", fmt, "-t", "markdown", "--wrap=none", str(path)],
                capture_output=True, text=True,
            )
            if result.returncode == 0:
                return result.stdout
            return None
    except Exception as e:
        err_console.print(f"  [red]convert_nicar_file failed for {path.name}:[/] {e}")
        return None


def process_nicar(
    nicar_dir: Path, dry_run: bool = False, force: bool = False,
) -> list[ManifestRow]:
    """Process entire NICAR archive. Returns manifest rows.

    Skips years whose output .md already exists unless --force is set.
    """
    rows: list[ManifestRow] = []
    en_dir = SOURCES_ROOT / "en"

    # Check which year outputs already exist
    existing_years: set[int] = set()
    if not force:
        for prefix, (year, slug) in NICAR_YEAR_MAP.items():
            if (en_dir / f"{slug}.md").exists():
                existing_years.add(year)

    if existing_years and not force:
        # Re-read existing outputs for manifest rows without reconverting
        for prefix, (year, slug) in NICAR_YEAR_MAP.items():
            dst = en_dir / f"{slug}.md"
            if dst.exists():
                text = dst.read_text(errors="replace")
                wc = word_count(text)
                rows.append(make_row(nicar_dir, dst, "nicar-consolidation", wc))

        all_years = set(y for _, (y, _) in NICAR_YEAR_MAP.items())
        missing = all_years - existing_years
        if not missing:
            console.print("  [dim]SKIP[/] all NICAR years already converted")
            return rows
        console.print(
            f"  [dim]SKIP[/] {len(existing_years)} years already converted, "
            f"processing {len(missing)} new"
        )
        # Only clear rows for years we'll reconvert
        rows = [r for r in rows
                if not any(f"97x-nicar-{y}" in r["output_path"]
                           or any(s in r["output_path"]
                                  for _, (yy, s) in NICAR_YEAR_MAP.items() if yy in missing)
                           for y in missing)]

    # Collect all convertible files, grouped by year
    year_files: dict[int, list[tuple[Path, str, str]]] = {}  # year → [(path, fmt, md_text)]

    # Walk NICAR directory, skip .git dirs
    all_files: list[Path] = []
    for item in sorted(nicar_dir.rglob("*")):
        if ".git" in item.parts:
            continue
        if not item.is_file():
            continue
        # Skip meta files at nicar root
        if item.parent == nicar_dir and item.suffix in (".csv", ".url"):
            continue
        all_files.append(item)

    convertible = 0
    skipped = 0
    for path in all_files:
        fmt = should_convert_nicar(path)
        if fmt is None:
            skipped += 1
            continue
        convertible += 1
        year = get_nicar_year(path, nicar_dir)
        if year is None:
            continue
        # Skip years already converted
        if year in existing_years and not force:
            continue
        if year not in year_files:
            year_files[year] = []
        year_files[year].append((path, fmt, ""))

    if not year_files:
        return rows

    console.print(
        f"  NICAR: {convertible} convertible, {skipped} non-text "
        f"— converting {sum(len(v) for v in year_files.values())} files "
        f"across {len(year_files)} years"
    )

    if dry_run:
        for year in sorted(year_files):
            count = len(year_files[year])
            console.print(f"    {year}: {count} files")
        return rows

    # Convert each file and group by year
    year_texts: dict[int, list[tuple[str, str]]] = {}  # year → [(header, md_text)]
    total_converted = 0
    total_failed = 0

    for year in sorted(year_files):
        year_texts[year] = []
        for path, fmt, _ in year_files[year]:
            md_text = convert_nicar_file(path, fmt)
            if md_text and md_text.strip():
                rel = path.relative_to(nicar_dir)
                header = f"## {rel}"
                year_texts[year].append((header, md_text.strip()))
                total_converted += 1
            else:
                total_failed += 1

    console.print(f"  NICAR converted: {total_converted}, failed: {total_failed}")

    # Consolidate into per-year files
    for year in sorted(year_texts):
        if not year_texts[year]:
            continue

        # Find the output slug
        slug = None
        for prefix, (y, s) in NICAR_YEAR_MAP.items():
            if y == year:
                slug = s
                break
        if slug is None:
            slug = f"97x-nicar-{year}"

        dst = en_dir / f"{slug}.md"
        parts = [f"# NICAR {year} Tipsheets & Session Notes\n"]
        for header, text in year_texts[year]:
            parts.append(f"\n{header}\n\n{text}")

        combined = "\n".join(parts)
        dst.write_text(combined)
        wc = word_count(combined)
        console.print(f"  → {dst.name}: {wc:,} words ({len(year_texts[year])} sections)")

        rows.append(make_row(
            nicar_dir, dst, "nicar-consolidation",
            wc, "", "ok",
        ))

    return rows


# ---------------------------------------------------------------------------
# Main orchestration
# ---------------------------------------------------------------------------


def collect_single_files(lang_dir: Path) -> list[Path]:
    """Collect all single files (not directories) in a language directory."""
    if not lang_dir.exists():
        return []
    return sorted(
        f for f in lang_dir.iterdir()
        if f.is_file() and f.suffix != ".url" and not f.name.startswith(".")
    )


def output_path_for(src: Path) -> Path:
    """Determine the .md output path for a source file."""
    return src.with_suffix(".md")


app = typer.Typer(help=__doc__, add_completion=False, no_args_is_help=False)


@app.command()
def main(
    dry_run: Annotated[
        bool, typer.Option("--dry-run", help="Preview without writing files.")
    ] = False,
    force: Annotated[
        bool, typer.Option("--force", help="Re-convert even if .md already exists.")
    ] = False,
    only_lang: Annotated[
        str | None,
        typer.Option("--only-lang", help="Only process one language (en, es, fr, pt)."),
    ] = None,
) -> None:
    """Convert all acquired sources to Markdown."""
    if not SOURCES_ROOT.exists():
        err_console.print(f"[red]Sources root not found:[/] {SOURCES_ROOT}")
        raise typer.Exit(1)

    langs = [only_lang] if only_lang else LANG_DIRS
    existing_manifest = load_existing_manifest() if not force else {}
    rows: list[ManifestRow] = []
    stats = {"converted": 0, "skipped": 0, "failed": 0, "already_md": 0}

    # ── Directory-based sources (special handling) ──────────────────────
    DIR_SOURCES: dict[str, tuple[Path, Callable[..., ManifestRow]]] = {
        "33-data-journalism-wells": (
            SOURCES_ROOT / "en" / "33-data-journalism-wells",
            convert_wells_book,
        ),
        "45-guide-du-datajournalisme": (
            SOURCES_ROOT / "fr" / "45-guide-du-datajournalisme",
            convert_french_guide,
        ),
        "95-maryjo-webster-training": (
            SOURCES_ROOT / "en" / "95-maryjo-webster-training",
            convert_maryjo_webster,
        ),
        "96-propublica-collaborative-dj-guide": (
            SOURCES_ROOT / "en" / "96-propublica-collaborative-dj-guide",
            convert_propublica_guide,
        ),
    }

    for name, (src_dir, handler) in DIR_SOURCES.items():
        if not src_dir.exists():
            continue
        lang = src_dir.parent.name
        if only_lang and lang != only_lang:
            continue

        dst = src_dir.parent / f"{name}.md"
        if dst.exists() and not force:
            rel_dst = str(dst.relative_to(SOURCES_ROOT))
            if rel_dst in existing_manifest:
                rows.append(existing_manifest[rel_dst])
            else:
                text = dst.read_text(errors="replace")
                rows.append(make_row(src_dir, dst, "dir", word_count(text)))
            console.print(f"[dim]SKIP[/] {name} (already converted)")
            stats["skipped"] += 1
            continue

        console.print(f"[bold]{name}[/]")
        if dry_run:
            console.print(f"  → would write {dst.relative_to(SOURCES_ROOT)}")
            continue

        try:
            row = handler(src_dir, dst)
            rows.append(row)
            stats["converted"] += 1
        except Exception as e:
            err_console.print(f"  [red]FAILED:[/] {e}")
            rows.append(make_row(src_dir, dst, "dir", 0, str(e), "failed"))
            stats["failed"] += 1

    # ── Single files per language ───────────────────────────────────────
    for lang in langs:
        lang_dir = SOURCES_ROOT / lang
        files = collect_single_files(lang_dir)

        for src in files:
            suffix = src.suffix.lower()
            dst = output_path_for(src)

            # Already markdown — record in manifest but don't re-copy
            if suffix == ".md":
                if not dry_run:
                    text = src.read_text(errors="replace")
                    wc = word_count(text)
                    rows.append(make_row(src, src, "md", wc))
                stats["already_md"] += 1
                continue

            # Skip if output exists (idempotent)
            if dst.exists() and not force:
                rel_dst = str(dst.relative_to(SOURCES_ROOT))
                if rel_dst in existing_manifest:
                    rows.append(existing_manifest[rel_dst])
                else:
                    text = dst.read_text(errors="replace")
                    rows.append(make_row(src, dst, suffix.lstrip("."), word_count(text)))
                console.print(f"[dim]SKIP[/] {src.name}")
                stats["skipped"] += 1
                continue

            console.print(f"[bold]{lang}/{src.name}[/]")
            if dry_run:
                console.print(f"  → would write {dst.name}")
                continue

            try:
                if suffix == ".pdf":
                    row = convert_pdf(src, dst)
                elif suffix == ".epub":
                    row = convert_epub(src, dst)
                elif suffix == ".txt":
                    row = copy_txt(src, dst)
                elif suffix in (".ipynb",):
                    row = convert_ipynb(src, dst)
                elif suffix in (".html", ".htm"):
                    row = convert_html(src, dst)
                elif suffix in (".rst",):
                    row = convert_rst(src, dst)
                else:
                    console.print(f"  [yellow]Unknown format: {suffix}[/]")
                    stats["skipped"] += 1
                    continue

                rows.append(row)
                stats["converted"] += 1
            except Exception as e:
                err_console.print(f"  [red]FAILED:[/] {e}")
                rows.append(make_row(src, dst, suffix.lstrip("."), 0, str(e), "failed"))
                stats["failed"] += 1

    # ── NICAR archive ───────────────────────────────────────────────────
    nicar_dir = SOURCES_ROOT / "en" / "nicar"
    if nicar_dir.exists() and (not only_lang or only_lang == "en"):
        console.print("\n[bold]NICAR archive[/]")
        nicar_rows = process_nicar(nicar_dir, dry_run=dry_run, force=force)
        rows.extend(nicar_rows)
        stats["converted"] += len(nicar_rows)

    # ── Write manifest ──────────────────────────────────────────────────
    if not dry_run and rows:
        with open(MANIFEST_PATH, "w", newline="") as f:
            writer = csv.DictWriter(
                f,
                fieldnames=[
                    "source_path", "output_path", "format",
                    "word_count", "warnings", "status", "timestamp",
                ],
            )
            writer.writeheader()
            writer.writerows(rows)
        console.print(f"\nManifest written to {MANIFEST_PATH.relative_to(SOURCES_ROOT.parent.parent.parent)}")

    # ── Summary ─────────────────────────────────────────────────────────
    console.print()
    table = Table(title="Conversion Summary")
    table.add_column("Metric", style="bold")
    table.add_column("Count", justify="right")
    table.add_row("Converted", str(stats["converted"]))
    table.add_row("Already .md", str(stats["already_md"]))
    table.add_row("Skipped (exists)", str(stats["skipped"]))
    table.add_row("Failed", str(stats["failed"]))
    table.add_row("Manifest rows", str(len(rows)))

    if rows:
        total_words = sum(int(r["word_count"]) for r in rows)
        table.add_row("Total words", f"{total_words:,}")

    console.print(table)

    if stats["failed"] > 0:
        raise typer.Exit(1)


if __name__ == "__main__":
    app()
