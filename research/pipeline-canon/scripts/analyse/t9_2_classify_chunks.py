# /// script
# requires-python = ">=3.12"
# dependencies = ["typer>=0.9.0", "rich>=13.0.0"]
# ///
"""Classify chunks as context_ok or context_needed based on heading quality.

Reads each chunk file, inspects its headings, and updates chunks-manifest.csv
with a context_status column.

Usage:
    uv run research/pipeline-canon/scripts/analyse/t9_2_classify_chunks.py                # classify all
    uv run research/pipeline-canon/scripts/analyse/t9_2_classify_chunks.py --only 07      # one source
"""

import csv
import re
import sys
from pathlib import Path
from typing import Annotated

import typer
from rich.console import Console

__version__ = "1.0.0"

PIPELINE_ROOT = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(PIPELINE_ROOT / "scripts"))
from log_action import log_action  # noqa: E402

CHUNKS_DIR = PIPELINE_ROOT / "chunks"
MANIFEST_CSV = CHUNKS_DIR / "chunks-manifest.csv"

console = Console()

# NICAR filename heading: ## 2024-ai-101.md
RE_NICAR_FILENAME = re.compile(r"^\d{4}-.+")
# Backtick-wrapped headings (OCR garbage)
RE_BACKTICK_HEADING = re.compile(r"`[^`]+`")

app = typer.Typer(help=__doc__, add_completion=False, no_args_is_help=False)


def version_callback(value: bool) -> None:
    if value:
        Console().print(f"t9_2_classify_chunks {__version__}")
        raise typer.Exit()


def classify_chunk(chunk_path: Path) -> str:
    """Classify a chunk as context_ok or context_needed."""
    text = chunk_path.read_text()

    # Extract headings from chunk body (skip metadata header)
    headings = []
    for line in text.splitlines():
        if line.startswith("<!--"):
            continue
        m = re.match(r"^#{1,6}\s+(.+)", line)
        if m:
            headings.append(m.group(1).strip())

    if not headings:
        return "context_needed"

    # All headings are NICAR filename patterns
    nicar_count = sum(1 for h in headings if RE_NICAR_FILENAME.match(h))
    if nicar_count == len(headings):
        return "context_needed"

    # All headings contain backticks (OCR garbage)
    backtick_count = sum(1 for h in headings if RE_BACKTICK_HEADING.search(h))
    if backtick_count == len(headings):
        return "context_needed"

    # Check if chunk came from word_boundary strategy (read from manifest later)
    # For now, headings exist and look reasonable
    return "context_ok"


@app.command()
def main(
    only: Annotated[str | None, typer.Option("--only", help="Process only this source ID.")] = None,
    dry_run: Annotated[bool, typer.Option("--dry-run", help="Preview without writing.")] = False,
    version: Annotated[bool | None, typer.Option("--version", callback=version_callback, is_eager=True, help="Show version.")] = None,
) -> None:
    """Classify chunks as context_ok or context_needed."""
    if not MANIFEST_CSV.exists():
        console.print("[red]chunks-manifest.csv not found. Run chunk_corpus.py first.")
        raise typer.Exit(1)

    # Read manifest
    with open(MANIFEST_CSV, newline="") as f:
        rows = list(csv.DictReader(f))

    if only:
        rows = [r for r in rows if r["source_id"] == only or r["source_file"].startswith(f"{only}-")]

    ok_count = 0
    needed_count = 0
    needed_files = []

    console.rule(f"[bold]CLASSIFY CHUNKS — {len(rows)} chunks")

    for row in rows:
        chunk_path = CHUNKS_DIR / row["chunk_file"]
        if not chunk_path.exists():
            console.print(f"  [red]MISSING[/] {row['chunk_file']}")
            continue

        # word_boundary strategy → always context_needed
        if row.get("strategy") == "word_boundary":
            status = "context_needed"
        else:
            status = classify_chunk(chunk_path)

        row["context_status"] = status

        if status == "context_needed":
            needed_count += 1
            needed_files.append(row["chunk_file"])
            console.print(f"  [yellow]NEEDED[/] {row['chunk_file']}")
        else:
            ok_count += 1

    # Write updated manifest
    if not dry_run:
        fields = list(rows[0].keys()) if rows else []
        with open(MANIFEST_CSV, "w", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=fields)
            writer.writeheader()
            writer.writerows(rows)

    console.rule("[bold]Summary")
    console.print(f"  context_ok: {ok_count}")
    console.print(f"  context_needed: {needed_count}")
    if needed_files:
        console.print(f"  Needed: {', '.join(needed_files)}")
    if dry_run:
        console.print("  [dim](dry run — no files written)[/]")

    if not dry_run:
        log_action(Path(__file__).name, f"{ok_count} chunks context_ok, {needed_count} chunks context_needed\ncontext_needed: {', '.join(needed_files)}")


if __name__ == "__main__":
    app()
