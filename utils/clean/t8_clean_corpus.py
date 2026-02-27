# /// script
# requires-python = ">=3.12"
# dependencies = ["rich", "typer>=0.9.0"]
# ///
"""T8 CLEAN — Deterministic cleaning of converted corpus files.

Copies .md sources from sources/{lang}/ to corpus/, applies regex-based
cleaning passes (junk lines, encoding, pandoc markup, HTML), then
generates corpus-registry.csv as the single source of truth for T9+.

Usage:
    uv run utils/clean/t8_clean_corpus.py              # full run
    uv run utils/clean/t8_clean_corpus.py --dry-run    # show what would happen
    uv run utils/clean/t8_clean_corpus.py --registry-only  # regenerate CSV only
"""

from __future__ import annotations

import csv
import re
import shutil
import sys
from pathlib import Path
from typing import Annotated

import typer
from rich.console import Console
from rich.table import Table

__version__ = "1.0.0"

ROOT = Path(__file__).resolve().parent.parent.parent
SOURCES = ROOT / "research" / "pipeline-canon" / "sources"
CORPUS = ROOT / "research" / "pipeline-canon" / "corpus"
MANIFEST = SOURCES / "convert-manifest.csv"
REGISTRY = ROOT / "research" / "pipeline-canon" / "source-registry.md"
CSV_OUT = CORPUS / "corpus-registry.csv"

console = Console()

app = typer.Typer(help=__doc__, add_completion=False, no_args_is_help=False)

# Sources excluded from corpus
EXCLUDED_IDS = {
    105,  # Columbia Teaching Guides (243w, links to #37/#38)
    106,  # MOOC Overview (446w, module list only)
    116,  # ICFJ course stub (192w, portal page)
    58,   # Manual Jornalismo Dados 2 (646w, TOC only — full text in #22)
    45,   # Guide du datajournalisme (FR DDJ Handbook 1 — duplicate of #7 EN)
    55,   # Manual de Periodismo de Datos (ES DDJ Handbook 1 — duplicate of #7 EN)
    57,   # Manual de Jornalismo de Dados 1 (PT DDJ Handbook 1 — duplicate of #7 EN)
}

# ── Registry parsing ─────────────────────────────────────────────────


def parse_registry() -> dict[str, dict]:
    """Parse source-registry.md table rows -> dict keyed by source number."""
    text = REGISTRY.read_text()
    entries: dict[str, dict] = {}
    for line in text.splitlines():
        line = line.strip()
        if not line.startswith("|"):
            continue
        cells = [c.strip() for c in line.split("|")[1:-1]]
        if len(cells) < 10:
            continue
        num = cells[0].strip()
        if num in ("---", "#", "") or all(c.startswith("-") for c in cells):
            continue
        entries[num] = {
            "title": cells[1],
            "author": cells[2],
            "year": cells[3],
            "lang": cells[4].upper().strip(),
            "type": cells[5].lower().strip(),
            "included": cells[9].strip(),
        }
    return entries


def parse_manifest() -> dict[str, dict]:
    """Read convert-manifest.csv, deduplicate by output_path."""
    rows: dict[str, dict] = {}
    with open(MANIFEST, newline="") as f:
        for row in csv.DictReader(f):
            key = row["output_path"]
            if key not in rows:
                rows[key] = row
    return rows


# ── Cleaning passes ──────────────────────────────────────────────────

# Pass 1: Junk lines
RE_PAGE_NUMBER = re.compile(r"^\s*\d{1,4}\s*$")
RE_ISSN = re.compile(r"^\s*ISSNe?\s+[\d\-]+", re.IGNORECASE)
RE_DOI = re.compile(r"^\s*(https?://)?doi\.org/", re.IGNORECASE)
RE_VIEW_CITING = re.compile(r"^\s*View (citing|related) articles", re.IGNORECASE)
RE_FULL_TERMS = re.compile(r"^\s*Full Terms & Conditions", re.IGNORECASE)
RE_COPYRIGHT = re.compile(r"^\s*(Copyright\s+)?©\s*\d{4}", re.IGNORECASE)
RE_ALL_RIGHTS = re.compile(r"^\s*All rights reserved", re.IGNORECASE)
RE_ISBN = re.compile(r"^\s*ISBN[:\s]", re.IGNORECASE)
RE_VOL_ISSUE = re.compile(r"^\s*Vol\.\s+\d+\s+N[ºo°]\s*\d+", re.IGNORECASE)

JUNK_LINE_PATTERNS = [
    RE_PAGE_NUMBER,
    RE_ISSN,
    RE_DOI,
    RE_VIEW_CITING,
    RE_FULL_TERMS,
    RE_COPYRIGHT,
    RE_ALL_RIGHTS,
    RE_ISBN,
    RE_VOL_ISSUE,
]


def pass1_strip_junk(lines: list[str]) -> list[str]:
    """Remove junk lines: page numbers, publisher metadata, copyright."""
    out = []
    for line in lines:
        stripped = line.strip()
        if any(pat.match(stripped) for pat in JUNK_LINE_PATTERNS):
            continue
        out.append(line)
    return out


# Pass 2: Encoding fixes
TRANSLATED_MARKER = "<!-- translated -->"


ENCODING_FIXES = {
    "&nbsp;": " ",
    "&amp;": "&",
    "&reg;": "\u00ae",
    "&copy;": "\u00a9",
    "&trade;": "\u2122",
    "&mdash;": "\u2014",
    "&ndash;": "\u2013",
    "&hellip;": "\u2026",
    "&laquo;": "\u00ab",
    "&raquo;": "\u00bb",
    "&ldquo;": "\u201c",
    "&rdquo;": "\u201d",
    "&lsquo;": "\u2018",
    "&rsquo;": "\u2019",
    "&lt;": "<",
    "&gt;": ">",
    "&quot;": '"',
    "\u00a0": " ",  # non-breaking space
    "\ufb01": "fi",  # fi ligature
    "\ufb02": "fl",  # fl ligature
    "\ufb00": "ff",  # ff ligature
    "\ufb03": "ffi",  # ffi ligature
    "\ufb04": "ffl",  # ffl ligature
}


def pass2_fix_encoding(text: str) -> str:
    """Fix HTML entities and encoding artifacts."""
    for old, new in ENCODING_FIXES.items():
        text = text.replace(old, new)
    # Numeric HTML entities &#NNN; or &#xHH;
    text = re.sub(
        r"&#x([0-9a-fA-F]+);",
        lambda m: chr(int(m.group(1), 16)),
        text,
    )
    text = re.sub(
        r"&#(\d+);",
        lambda m: chr(int(m.group(1))),
        text,
    )
    return text


# Pass 3: Structural markup removal

# Pandoc anchors: []{#anything} or []{#anything .class}
RE_PANDOC_ANCHOR = re.compile(r"\[\]\{#[^}]+\}")
# Section number spans: [1]{.header-section-number}
RE_SECTION_NUM = re.compile(r"\[\d+\]\{\.header-section-number\}")
# Span with classes: [text]{.class .class lang="xx"} -> keep text
RE_SPAN_CLASS = re.compile(r"\[([^\]]*)\]\{[^}]+\}")
# Pandoc div open: ::: {#id .class lang="xx"} or :::::::: {.section}
RE_DIV_OPEN = re.compile(r"^:{3,}\s*\{[^}]*\}\s*$")
# Pandoc div close: ::: (alone on line)
RE_DIV_CLOSE = re.compile(r"^:{3,}\s*$")
# Heading ID suffixes: {#some-id .class}
RE_HEADING_ID = re.compile(r"\s*\{#[^}]+\}\s*$")
# Inline attribute blocks: {#id .class} or {width="100%"} after links/images
RE_INLINE_ATTR = re.compile(r"\{[#.][^}]+\}")
# Width/style attributes on images: {width="79%"}
RE_WIDTH_ATTR = re.compile(r"\{width=\"[^\"]+\"\}")
# Orphaned image blocks (HTML)
RE_IMG_DIV = re.compile(
    r'<div\s+class="image(?:block|container)"[^>]*>.*?</div>',
    re.DOTALL | re.IGNORECASE,
)
# Stray HTML tags (div, span, img, br)
RE_STRAY_HTML = re.compile(
    r"</?(?:div|span|img|br|figure|figcaption|section|article)[^>]*>",
    re.IGNORECASE,
)
# Markdown image refs with local paths (images not available in corpus)
RE_MD_IMAGE = re.compile(r"^!\[.*?\]\((?!https?://)[^)]+\).*$")


def pass3_remove_markup(text: str) -> str:
    """Remove pandoc structural markup, stray HTML, orphaned images."""
    # Multi-line patterns first
    text = RE_IMG_DIV.sub("", text)

    lines = text.splitlines()
    out = []
    for line in lines:
        # Skip div open/close lines
        if RE_DIV_OPEN.match(line) or RE_DIV_CLOSE.match(line):
            continue
        # Inline replacements
        line = RE_PANDOC_ANCHOR.sub("", line)
        line = RE_SECTION_NUM.sub("", line)
        line = RE_SPAN_CLASS.sub(r"\1", line)
        line = RE_HEADING_ID.sub("", line)
        line = RE_WIDTH_ATTR.sub("", line)
        # Strip {#id .class} from link/image elements but preserve the link text
        line = RE_INLINE_ATTR.sub("", line)
        line = RE_STRAY_HTML.sub("", line)
        # Skip orphaned local image refs (check after other cleanup)
        if RE_MD_IMAGE.match(line.strip()):
            continue
        out.append(line)
    return "\n".join(out)


# Pass 4: Strip code blocks and console output
RE_FENCED_CODE = re.compile(
    r"^(`{3,}|~{3,}).*?\n[\s\S]*?\n\1\s*$",
    re.MULTILINE,
)
RE_INDENTED_CODE = re.compile(
    r"(?:^(?:    |\t).+\n){4,}",
    re.MULTILINE,
)


def pass4_strip_code_blocks(text: str) -> str:
    """Replace fenced/indented code blocks with semantic placeholders."""
    text = RE_FENCED_CODE.sub("[CODE BLOCK REMOVED]", text)
    text = RE_INDENTED_CODE.sub("[CODE BLOCK REMOVED]\n", text)
    return text


# ── Collapse excessive blank lines ──────────────────────────────────

RE_MULTI_BLANK = re.compile(r"\n{4,}")


def collapse_blanks(text: str) -> str:
    """Collapse runs of 3+ blank lines to 2."""
    return RE_MULTI_BLANK.sub("\n\n\n", text)


# ── Full cleaning pipeline ──────────────────────────────────────────


def clean_file(text: str) -> str:
    """Apply all cleaning passes to file content."""
    lines = text.splitlines()
    lines = pass1_strip_junk(lines)
    text = "\n".join(lines)
    text = pass2_fix_encoding(text)
    text = pass3_remove_markup(text)
    text = pass4_strip_code_blocks(text)
    text = collapse_blanks(text)
    return text.strip() + "\n"


# ── Source discovery ────────────────────────────────────────────────


def discover_sources() -> list[dict]:
    """Find all .md files in sources/{en,es,fr,pt}/, extract IDs."""
    sources = []
    for lang_dir in sorted(SOURCES.iterdir()):
        if lang_dir.name.startswith("_") or not lang_dir.is_dir():
            continue
        if lang_dir.name not in ("en", "es", "fr", "pt"):
            continue
        for md_file in sorted(lang_dir.glob("*.md")):
            if not (m := re.match(r"(\d+)", md_file.name)):
                continue
            source_id = int(m.group(1))
            sources.append({
                "id": source_id,
                "lang_dir": lang_dir.name,
                "source_path": md_file,
                "relative": f"{lang_dir.name}/{md_file.name}",
            })
    return sources


# ── Registry CSV generation ─────────────────────────────────────────


def build_registry(
    sources: list[dict],
    reg: dict[str, dict],
    manifest: dict[str, dict],
) -> list[dict]:
    """Build corpus registry rows from cleaned files."""
    rows = []
    for src in sources:
        sid = src["id"]
        if sid in EXCLUDED_IDS:
            continue
        num_str = str(sid)
        reg_entry = reg.get(num_str, {})
        if reg_entry.get("included") != "yes":
            continue

        corpus_file = CORPUS / src["source_path"].name
        if not corpus_file.exists():
            continue

        words = len(corpus_file.read_text().split())

        # Check if this was translated
        orig_lang = reg_entry.get("lang", src["lang_dir"].upper())
        translated = "yes" if orig_lang != "EN" else "no"

        rows.append({
            "id": num_str,
            "file": src["source_path"].name,
            "title": reg_entry.get("title", ""),
            "author": reg_entry.get("author", ""),
            "year": reg_entry.get("year", ""),
            "lang": orig_lang,
            "type": reg_entry.get("type", ""),
            "words": words,
            "translated": translated,
        })
    return rows


def write_registry(rows: list[dict]) -> None:
    """Write corpus-registry.csv."""
    fields = ["id", "file", "title", "author", "year", "lang", "type", "words", "translated"]
    with open(CSV_OUT, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        for row in sorted(rows, key=lambda r: int(r["id"])):
            writer.writerow(row)


# ── NICAR consolidated files ────────────────────────────────────────


def discover_nicar_sources() -> list[dict]:
    """Find NICAR consolidated .md files in sources/en/nicar/."""
    nicar_dir = SOURCES / "en" / "nicar"
    if not nicar_dir.is_dir():
        return []
    sources = []
    for md_file in sorted(nicar_dir.glob("*.md")):
        m = re.match(r"(\d+[a-z]?)", md_file.name)
        if not m:
            continue
        sources.append({
            "id_str": m.group(1),
            "source_path": md_file,
            "relative": f"en/nicar/{md_file.name}",
        })
    return sources


# ── Main ────────────────────────────────────────────────────────────


def version_callback(value: bool) -> None:
    if value:
        from rich.console import Console
        Console().print(f"t8-clean-corpus {__version__}")
        raise typer.Exit()


@app.command()
def main(
    dry_run: Annotated[bool, typer.Option("--dry-run", help="Show what would happen without writing.")] = False,
    registry_only: Annotated[bool, typer.Option("--registry-only", help="Regenerate CSV only.")] = False,
    version: Annotated[bool | None, typer.Option("--version", callback=version_callback, is_eager=True, help="Show version.")] = None,
) -> None:
    if not REGISTRY.exists():
        console.print(f"[red]source-registry.md not found: {REGISTRY}")
        raise typer.Exit(1)
    if not MANIFEST.exists():
        console.print(f"[red]convert-manifest.csv not found: {MANIFEST}")
        raise typer.Exit(1)

    reg = parse_registry()
    manifest = parse_manifest()
    sources = discover_sources()
    nicar_sources = discover_nicar_sources()

    if not registry_only:
        CORPUS.mkdir(parents=True, exist_ok=True)

        # Process regular sources
        cleaned = 0
        excluded = 0
        for src in sources:
            if src["id"] in EXCLUDED_IDS:
                excluded += 1
                console.print(f"  [dim]SKIP (excluded)[/] {src['relative']}")
                continue

            # Check registry inclusion
            num_str = str(src["id"])
            reg_entry = reg.get(num_str, {})
            if reg_entry.get("included") != "yes":
                continue

            # Skip files already translated in corpus/
            out_path = CORPUS / src["source_path"].name
            if out_path.exists() and TRANSLATED_MARKER in out_path.read_text()[:500]:
                console.print(f"  [dim]SKIP (translated)[/] {src['relative']}")
                continue

            source_text = src["source_path"].read_text()
            original_words = len(source_text.split())

            if dry_run:
                cleaned_text = clean_file(source_text)
                cleaned_words = len(cleaned_text.split())
                delta = original_words - cleaned_words
                pct = (delta / original_words * 100) if original_words else 0
                console.print(
                    f"  [cyan]{src['relative']}[/] "
                    f"{original_words:,}w \u2192 {cleaned_words:,}w "
                    f"([yellow]-{delta:,}w, -{pct:.1f}%[/])"
                )
            else:
                cleaned_text = clean_file(source_text)
                out_path.write_text(cleaned_text)
                cleaned_words = len(cleaned_text.split())
                delta = original_words - cleaned_words
                pct = (delta / original_words * 100) if original_words else 0
                console.print(
                    f"  [green]OK[/] {src['relative']} \u2192 {out_path.name} "
                    f"({original_words:,}w \u2192 {cleaned_words:,}w, "
                    f"-{delta:,}w/{pct:.1f}%)"
                )
            cleaned += 1

        # Process NICAR consolidated files
        for nsrc in nicar_sources:
            reg_entry = reg.get(nsrc["id_str"], {})
            if reg_entry.get("included") != "yes":
                continue

            # Skip files already translated in corpus/
            out_path = CORPUS / nsrc["source_path"].name
            if out_path.exists() and TRANSLATED_MARKER in out_path.read_text()[:500]:
                console.print(f"  [dim]SKIP (translated)[/] {nsrc['relative']}")
                continue

            source_text = nsrc["source_path"].read_text()
            original_words = len(source_text.split())

            if dry_run:
                cleaned_text = clean_file(source_text)
                cleaned_words = len(cleaned_text.split())
                delta = original_words - cleaned_words
                pct = (delta / original_words * 100) if original_words else 0
                console.print(
                    f"  [cyan]{nsrc['relative']}[/] "
                    f"{original_words:,}w \u2192 {cleaned_words:,}w "
                    f"([yellow]-{delta:,}w, -{pct:.1f}%[/])"
                )
            else:
                cleaned_text = clean_file(source_text)
                out_path.write_text(cleaned_text)
                cleaned_words = len(cleaned_text.split())
                delta = original_words - cleaned_words
                pct = (delta / original_words * 100) if original_words else 0
                console.print(
                    f"  [green]OK[/] {nsrc['relative']} \u2192 {out_path.name} "
                    f"({original_words:,}w \u2192 {cleaned_words:,}w, "
                    f"-{delta:,}w/{pct:.1f}%)"
                )
            cleaned += 1

        console.rule("[bold]Cleaning summary")
        console.print(f"  Cleaned: {cleaned}")
        console.print(f"  Excluded: {excluded}")

    # Generate registry CSV
    if not dry_run:
        # Re-discover from corpus dir for registry
        corpus_sources = discover_sources()
        nicar_for_reg = discover_nicar_sources()

        # Build registry from all sources
        rows = build_registry(corpus_sources, reg, manifest)

        # Add NICAR sources
        for nsrc in nicar_for_reg:
            reg_entry = reg.get(nsrc["id_str"], {})
            if reg_entry.get("included") != "yes":
                continue
            corpus_file = CORPUS / nsrc["source_path"].name
            if not corpus_file.exists():
                continue
            words = len(corpus_file.read_text().split())
            rows.append({
                "id": nsrc["id_str"],
                "file": nsrc["source_path"].name,
                "title": reg_entry.get("title", ""),
                "author": reg_entry.get("author", ""),
                "year": reg_entry.get("year", ""),
                "lang": reg_entry.get("lang", "EN"),
                "type": reg_entry.get("type", ""),
                "words": words,
                "translated": "no",
            })

        write_registry(rows)
        console.rule("[bold green]Registry")
        console.print(f"  Rows: {len(rows)}")
        console.print(f"  Written to: {CSV_OUT.relative_to(ROOT)}")


if __name__ == "__main__":
    app()
