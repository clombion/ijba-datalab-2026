# /// script
# requires-python = ">=3.12"
# dependencies = ["typer>=0.9.0", "rich>=13.0.0"]
# ///
"""T9 CHUNK — Deterministic chunking of corpus files for LLM extraction.

Type-aware strategies split large files into ≤40K-word chunks.
Outputs chunks/{stem}_chunk{N}.md + chunks/chunks-manifest.csv.

Usage:
    uv run utils/analyse/t9_1_chunk_corpus.py                  # chunk all
    uv run utils/analyse/t9_1_chunk_corpus.py --only 97e       # one source (matches file prefix)
    uv run utils/analyse/t9_1_chunk_corpus.py --dry-run        # show plan without writing
    uv run utils/analyse/t9_1_chunk_corpus.py --max-words 40000
"""

import csv
import re
import sys
from pathlib import Path
from typing import Annotated

import typer
from rich.console import Console
from rich.table import Table

__version__ = "1.0.0"

ROOT = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(ROOT / "utils"))
from log_action import log_action  # noqa: E402
CORPUS = ROOT / "research" / "pipeline-canon" / "corpus"
REGISTRY_CSV = CORPUS / "corpus-registry.csv"
CHUNKS_DIR = ROOT / "research" / "pipeline-canon" / "chunks"
MANIFEST_CSV = CHUNKS_DIR / "chunks-manifest.csv"

console = Console()

DEFAULT_MAX_WORDS = 40_000

# NICAR files: 97e, 97i, 97j
NICAR_FILES = {"97e", "97i", "97j"}
# Wells (118 chapters, # headings)
WELLS_FILE = "33"
# DDJ Handbook 2 (##### chapters)
DDJ2_FILE = "22"
# Files with no usable headings → word_boundary
WORD_BOUNDARY_FILES = {"82", "132"}

# NICAR filtering patterns
# Top-level tipsheet heading: ## 2020-advanced-sql.md
RE_NICAR_TIPSHEET = re.compile(r"^## (\d{4}-[^/]+\.md)\s*$")
# Subdirectory file dump: ## 2020-batch-pdfs-pdfplumber/pdfs/file.pdf
RE_NICAR_SUBPATH = re.compile(r"^## \d{4}-.+/.+")
# Any file extension in heading (binary dump indicator)
RE_NICAR_BINARY_EXT = re.compile(r"\.(pdf|csv|ipynb|xlsx?|png|jpg|gif|zip|tar|gz|json|geojson|shp|rds|rda|Rmd|r|py|sql|txt|html?|xml)\s*$", re.IGNORECASE)
NICAR_SECTION_MAX_WORDS = 10_000

app = typer.Typer(help=__doc__, add_completion=False, no_args_is_help=False)


def version_callback(value: bool) -> None:
    if value:
        Console().print(f"t9_1_chunk_corpus {__version__}")
        raise typer.Exit()


def read_registry() -> list[dict]:
    rows = []
    with open(REGISTRY_CSV, newline="") as f:
        for row in csv.DictReader(f):
            rows.append(row)
    return rows


def get_file_id(filename: str) -> str:
    """Extract the ID prefix from a filename like '97e-nicar-2020.md' → '97e'."""
    m = re.match(r"(\d+[a-z]?)", filename)
    return m.group(1) if m else filename


def extract_heading_outline(text: str, level: str = "##") -> list[str]:
    """Extract heading lines at the given level."""
    pattern = re.compile(rf"^{re.escape(level)}\s+(.+)$", re.MULTILINE)
    return [m.group(1).strip() for m in pattern.finditer(text)]


def detect_strategy(file_id: str, text: str, max_words: int) -> str:
    words = len(text.split())
    if file_id in NICAR_FILES:
        return "nicar_filter"
    if file_id == WELLS_FILE:
        return "heading_h1"
    if file_id == DDJ2_FILE:
        return "heading_h5"
    if file_id in WORD_BOUNDARY_FILES:
        return "word_boundary"
    if words <= max_words:
        return "single"
    # Check for ## headings
    h2_count = len(re.findall(r"^## ", text, re.MULTILINE))
    if h2_count >= 3:
        return "heading_h2"
    return "word_boundary"


# ── Chunking strategies ──────────────────────────────────────────────


def chunk_single(text: str, max_words: int) -> list[str]:
    return [text]


def chunk_by_heading(text: str, heading_re: re.Pattern, max_words: int) -> list[str]:
    """Split on heading pattern, accumulate sections to stay under max_words."""
    parts = heading_re.split(text)
    # parts[0] is text before first heading, then alternating heading/body
    sections: list[str] = []
    if parts[0].strip():
        sections.append(parts[0])
    for i in range(1, len(parts), 2):
        heading = parts[i] if i < len(parts) else ""
        body = parts[i + 1] if i + 1 < len(parts) else ""
        sections.append(heading + body)

    chunks: list[str] = []
    current: list[str] = []
    current_words = 0

    for section in sections:
        section_words = len(section.split())
        if current_words + section_words > max_words and current:
            chunks.append("\n".join(current))
            current = [section]
            current_words = section_words
        else:
            current.append(section)
            current_words += section_words

    if current:
        chunks.append("\n".join(current))
    return chunks


def chunk_heading_h2(text: str, max_words: int) -> list[str]:
    return chunk_by_heading(text, re.compile(r"(?=^## )", re.MULTILINE), max_words)


def chunk_heading_h1(text: str, max_words: int) -> list[str]:
    return chunk_by_heading(text, re.compile(r"(?=^# )", re.MULTILINE), max_words)


def chunk_heading_h5(text: str, max_words: int) -> list[str]:
    return chunk_by_heading(text, re.compile(r"(?=^##### )", re.MULTILINE), max_words)


def chunk_word_boundary(text: str, max_words: int) -> list[str]:
    """Split on paragraph boundaries (\\n\\n) to stay under max_words."""
    paragraphs = text.split("\n\n")
    chunks: list[str] = []
    current: list[str] = []
    current_words = 0

    for para in paragraphs:
        para_words = len(para.split())
        if current_words + para_words > max_words and current:
            chunks.append("\n\n".join(current))
            current = [para]
            current_words = para_words
        else:
            current.append(para)
            current_words += para_words

    if current:
        chunks.append("\n\n".join(current))
    return chunks if chunks else [text]


def filter_nicar(text: str) -> tuple[str, int]:
    """Filter NICAR consolidated files.

    The NICAR files are scraped repos where each ## heading is either:
    - A tipsheet entry: `## 2020-advanced-sql.md`
    - A subdirectory file: `## 2020-batch-pdfs/pdfs/file.pdf` (binary dump → skip)
    - A content sub-heading within a tipsheet: `## Page: /` etc.

    Strategy:
    1. Skip all subdirectory/file-path sections (contain `/`)
    2. Skip individual sections >10K words (raw data dumps)
    3. Keep everything else
    """
    sections = re.split(r"(?=^## )", text, flags=re.MULTILINE)
    kept: list[str] = []
    skipped = 0

    for section in sections:
        first_line = section.split("\n", 1)[0].strip()

        # Skip subdirectory file dumps: ## 2020-name/subdir/file.ext
        if RE_NICAR_SUBPATH.match(first_line):
            skipped += 1
            continue

        # Skip individual oversized sections (raw data dumps)
        section_words = len(section.split())
        if section_words > NICAR_SECTION_MAX_WORDS:
            skipped += 1
            continue

        kept.append(section)

    return "\n".join(kept), skipped


def chunk_nicar_filter(text: str, max_words: int) -> tuple[list[str], int]:
    """Filter then chunk NICAR files."""
    filtered, skipped = filter_nicar(text)
    chunks = chunk_heading_h2(filtered, max_words)
    return chunks, skipped


# ── Metadata header ──────────────────────────────────────────────────


def make_chunk_header(chunk_num: int, total_chunks: int, source_file: str, words: int, headings: list[str]) -> str:
    heading_list = "; ".join(headings) if headings else "(none)"
    return (
        f"<!-- chunk: {chunk_num}/{total_chunks} | source: {source_file} | words: {words} -->\n"
        f"<!-- headings: {heading_list} -->\n\n"
    )


def extract_chunk_headings(text: str) -> list[str]:
    """Extract all markdown headings from a chunk."""
    headings = []
    for line in text.splitlines():
        if m := re.match(r"^(#{1,6})\s+(.+)", line):
            headings.append(m.group(2).strip().rstrip("{").strip())
    return headings[:20]  # cap at 20 to keep header reasonable


# ── Main ──────────────────────────────────────────────────────────────


@app.command()
def main(
    only: Annotated[str | None, typer.Option("--only", help="Process only this source ID.")] = None,
    dry_run: Annotated[bool, typer.Option("--dry-run", help="Preview without writing.")] = False,
    max_words: Annotated[int, typer.Option("--max-words", help="Max words per chunk.")] = DEFAULT_MAX_WORDS,
    version: Annotated[bool | None, typer.Option("--version", callback=version_callback, is_eager=True, help="Show version.")] = None,
) -> None:
    """Deterministic chunking of corpus files for LLM extraction."""
    if not REGISTRY_CSV.exists():
        console.print("[red]corpus-registry.csv not found.")
        raise typer.Exit(1)

    registry = read_registry()
    if only:
        registry = [r for r in registry if get_file_id(r["file"]) == only]

    if not dry_run:
        CHUNKS_DIR.mkdir(parents=True, exist_ok=True)

    manifest_rows: list[dict] = []
    stats = {"single": 0, "heading_h2": 0, "heading_h1": 0, "heading_h5": 0, "nicar_filter": 0, "word_boundary": 0}
    total_chunks = 0
    total_skipped_nicar = 0

    console.rule(f"[bold]T9 CHUNK — {len(registry)} sources, max {max_words:,}w/chunk")

    for row in registry:
        stem = row["file"].replace(".md", "")
        file_id = get_file_id(row["file"])
        corpus_file = CORPUS / row["file"]

        if not corpus_file.exists():
            console.print(f"  [red]MISSING[/] {row['file']}")
            continue

        # Idempotency: skip if chunks already exist
        existing = list(CHUNKS_DIR.glob(f"{stem}_chunk*.md"))
        if existing and not dry_run:
            console.print(f"  [dim]SKIP (chunks exist)[/] {row['file']} ({len(existing)} chunks)")
            # Still add to manifest
            for ef in sorted(existing):
                etext = ef.read_text()
                ewords = len(etext.split())
                eheadings = extract_chunk_headings(etext)
                chunk_num = int(re.search(r"_chunk(\d+)", ef.name).group(1))
                manifest_rows.append({
                    "source_file": row["file"],
                    "source_id": row["id"],
                    "chunk_file": ef.name,
                    "chunk_num": chunk_num,
                    "total_chunks": len(existing),
                    "words": ewords,
                    "strategy": "existing",
                    "context_status": "",
                })
            total_chunks += len(existing)
            continue

        text = corpus_file.read_text()
        words = len(text.split())
        strategy = detect_strategy(file_id, text, max_words)
        stats[strategy] += 1

        nicar_skipped = 0
        match strategy:
            case "nicar_filter":
                chunks, nicar_skipped = chunk_nicar_filter(text, max_words)
                total_skipped_nicar += nicar_skipped
            case "heading_h1":
                chunks = chunk_heading_h1(text, max_words)
            case "heading_h5":
                chunks = chunk_heading_h5(text, max_words)
            case "heading_h2":
                chunks = chunk_heading_h2(text, max_words)
            case "word_boundary":
                chunks = chunk_word_boundary(text, max_words)
            case _:
                chunks = chunk_single(text, max_words)

        n = len(chunks)

        if dry_run:
            extra = f", {nicar_skipped} sections filtered" if nicar_skipped else ""
            console.print(
                f"  [cyan]{row['file']}[/] {words:,}w → {n} chunk(s) "
                f"[dim]({strategy}{extra})[/]"
            )
        else:
            for i, chunk_text in enumerate(chunks, 1):
                chunk_words = len(chunk_text.split())
                headings = extract_chunk_headings(chunk_text)
                header = make_chunk_header(i, n, row["file"], chunk_words, headings)
                chunk_path = CHUNKS_DIR / f"{stem}_chunk{i}.md"
                chunk_path.write_text(header + chunk_text)

                manifest_rows.append({
                    "source_file": row["file"],
                    "source_id": row["id"],
                    "chunk_file": chunk_path.name,
                    "chunk_num": i,
                    "total_chunks": n,
                    "words": chunk_words,
                    "strategy": strategy,
                    "context_status": "",
                })

            extra = f", {nicar_skipped} sections filtered" if nicar_skipped else ""
            console.print(
                f"  [green]OK[/] {row['file']} → {n} chunk(s) "
                f"[dim]({strategy}, {words:,}w{extra})[/]"
            )

        total_chunks += n

    # Write manifest
    if not dry_run and manifest_rows:
        fields = ["source_file", "source_id", "chunk_file", "chunk_num", "total_chunks", "words", "strategy", "context_status"]
        with open(MANIFEST_CSV, "w", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=fields)
            writer.writeheader()
            writer.writerows(manifest_rows)

    # Summary
    console.rule("[bold]Summary")
    tbl = Table(show_header=True)
    tbl.add_column("Strategy")
    tbl.add_column("Sources", justify="right")
    for k, v in sorted(stats.items()):
        if v:
            tbl.add_row(k, str(v))
    console.print(tbl)
    console.print(f"  Total chunks: {total_chunks}")
    if total_skipped_nicar:
        console.print(f"  NICAR sections filtered: {total_skipped_nicar}")
    if not dry_run:
        console.print(f"  Manifest: {MANIFEST_CSV.relative_to(ROOT)}")

    # Log action
    if not dry_run:
        breakdown = ", ".join(f"{v} {k}" for k, v in sorted(stats.items()) if v)
        log_action(Path(__file__).name, f"Chunked {len(registry)} sources into {total_chunks} chunks\nStrategy breakdown: {breakdown}")


if __name__ == "__main__":
    app()
