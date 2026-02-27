# /// script
# requires-python = ">=3.12"
# dependencies = ["typer>=0.9.0", "rich>=13.0.0"]
# ///
"""Create empty extraction JSON scaffolds for each chunk.

Reads chunks-manifest.csv and corpus-registry.csv, creates
extractions/{stem}_chunk{N}.json with source metadata and empty extracts[].

Usage:
    uv run utils/analyse/t9_4_scaffold_extraction.py              # scaffold all
    uv run utils/analyse/t9_4_scaffold_extraction.py --only 07    # one source
"""

import csv
import json
import sys
from pathlib import Path
from typing import Annotated

import typer
from rich.console import Console

__version__ = "1.0.0"

ROOT = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(ROOT / "utils"))
from log_action import log_action  # noqa: E402

CORPUS = ROOT / "research" / "pipeline-canon" / "corpus"
REGISTRY_CSV = CORPUS / "corpus-registry.csv"
CHUNKS_DIR = ROOT / "research" / "pipeline-canon" / "chunks"
MANIFEST_CSV = CHUNKS_DIR / "chunks-manifest.csv"
EXTRACTIONS_DIR = ROOT / "research" / "pipeline-canon" / "extractions"

console = Console()

app = typer.Typer(help=__doc__, add_completion=False, no_args_is_help=False)


def version_callback(value: bool) -> None:
    if value:
        Console().print(f"t9_4_scaffold_extraction {__version__}")
        raise typer.Exit()


@app.command()
def main(
    only: Annotated[str | None, typer.Option("--only", help="Process only this source ID.")] = None,
    dry_run: Annotated[bool, typer.Option("--dry-run", help="Preview without writing.")] = False,
    version: Annotated[bool | None, typer.Option("--version", callback=version_callback, is_eager=True, help="Show version.")] = None,
) -> None:
    """Create empty extraction JSON scaffolds for each chunk."""
    if not MANIFEST_CSV.exists():
        console.print("[red]chunks-manifest.csv not found. Run chunk_corpus.py first.")
        raise typer.Exit(1)

    # Read registry into dict keyed by file
    reg = {}
    with open(REGISTRY_CSV, newline="") as f:
        for row in csv.DictReader(f):
            reg[row["file"]] = row

    # Read manifest
    with open(MANIFEST_CSV, newline="") as f:
        manifest = list(csv.DictReader(f))

    if only:
        manifest = [r for r in manifest if r["source_id"] == only or r["source_file"].startswith(f"{only}-")]

    if not dry_run:
        EXTRACTIONS_DIR.mkdir(parents=True, exist_ok=True)
    created = 0
    skipped = 0

    console.rule(f"[bold]SCAFFOLD EXTRACTIONS — {len(manifest)} chunks")

    for row in manifest:
        chunk_stem = row["chunk_file"].replace(".md", "")
        out_path = EXTRACTIONS_DIR / f"{chunk_stem}.json"

        if out_path.exists():
            skipped += 1
            continue

        source_meta = reg.get(row["source_file"], {})
        scaffold = {
            "source_id": row["source_id"],
            "source_file": row["source_file"],
            "source_title": source_meta.get("title", ""),
            "author": source_meta.get("author", ""),
            "year": source_meta.get("year", ""),
            "chunk": f"{row['chunk_num']}/{row['total_chunks']}",
            "chunk_file": row["chunk_file"],
            "chunk_words": int(row["words"]),
            "extracts": [],
        }

        if dry_run:
            console.print(f"  [cyan]WOULD CREATE[/] {out_path.name}")
        else:
            out_path.write_text(json.dumps(scaffold, indent=2, ensure_ascii=False) + "\n")
        created += 1

    console.print(f"  Created: {created}")
    console.print(f"  Skipped (exist): {skipped}")
    if dry_run:
        console.print("  [dim](dry run — no files written)[/]")

    if not dry_run:
        log_action(Path(__file__).name, f"Created {created} extraction scaffolds, skipped {skipped} existing")


if __name__ == "__main__":
    app()
