# /// script
# requires-python = ">=3.12"
# dependencies = ["typer>=0.9.0", "rich>=13.0.0"]
# ///
"""Count-gated merge of chunk extractions into per-source extraction JSONs.

Won't merge a source unless ALL its chunks have extraction files.

Usage:
    uv run utils/analyse/t9_7_merge_chunks.py                  # merge all complete
    uv run utils/analyse/t9_7_merge_chunks.py --only 07        # one source
"""

import csv
import json
import sys
from collections import defaultdict
from pathlib import Path
from typing import Annotated

import typer
from rich.console import Console

__version__ = "1.0.0"

ROOT = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(ROOT / "utils"))
from log_action import log_action  # noqa: E402

CHUNKS_DIR = ROOT / "research" / "pipeline-canon" / "chunks"
MANIFEST_CSV = CHUNKS_DIR / "chunks-manifest.csv"
EXTRACTIONS_DIR = ROOT / "research" / "pipeline-canon" / "extractions"

console = Console()

app = typer.Typer(help=__doc__, add_completion=False, no_args_is_help=False)


def version_callback(value: bool) -> None:
    if value:
        Console().print(f"t9_7_merge_chunks {__version__}")
        raise typer.Exit()


@app.command()
def main(
    only: Annotated[str | None, typer.Option("--only", help="Merge only this source ID.")] = None,
    dry_run: Annotated[bool, typer.Option("--dry-run", help="Preview without writing.")] = False,
    version: Annotated[bool | None, typer.Option("--version", callback=version_callback, is_eager=True, help="Show version.")] = None,
) -> None:
    """Merge chunk extractions into per-source extraction JSONs."""
    if not MANIFEST_CSV.exists():
        console.print("[red]chunks-manifest.csv not found.")
        sys.exit(1)

    # Group manifest by source
    sources: dict[str, list[dict]] = defaultdict(list)
    with open(MANIFEST_CSV, newline="") as f:
        for row in csv.DictReader(f):
            sources[row["source_file"]].append(row)

    if only:
        sources = {k: v for k, v in sources.items() if v[0]["source_id"] == only or k.startswith(f"{only}-")}

    console.rule(f"[bold]MERGE CHUNKS — {len(sources)} sources")
    merged = 0
    skipped_incomplete = 0
    skipped_exists = 0

    for source_file, chunks in sorted(sources.items()):
        stem = source_file.replace(".md", "")
        out_path = EXTRACTIONS_DIR / f"{stem}.json"

        # Skip if merged file already exists
        if out_path.exists():
            skipped_exists += 1
            continue

        # Count-gate: check all chunks have extraction files
        total = int(chunks[0]["total_chunks"])
        chunk_files = []
        complete = True
        for c in sorted(chunks, key=lambda x: int(x["chunk_num"])):
            chunk_stem = c["chunk_file"].replace(".md", "")
            extraction_path = EXTRACTIONS_DIR / f"{chunk_stem}.json"
            if not extraction_path.exists():
                complete = False
                break
            chunk_files.append(extraction_path)

        if not complete or len(chunk_files) != total:
            skipped_incomplete += 1
            console.print(f"  [yellow]SKIP[/] {stem} ({len(chunk_files)}/{total} chunks)")
            continue

        # Merge: combine extracts from all chunks
        all_extracts = []
        first_data = None
        total_words = 0
        for cf in chunk_files:
            data = json.loads(cf.read_text())
            if first_data is None:
                first_data = data
            all_extracts.extend(data.get("extracts", []))
            total_words += data.get("chunk_words", 0)

        merged_data = {
            "source_id": first_data["source_id"],
            "source_file": first_data["source_file"],
            "source_title": first_data["source_title"],
            "author": first_data["author"],
            "year": first_data["year"],
            "chunk": None,
            "chunk_words": total_words,
            "extracts": all_extracts,
        }

        if dry_run:
            console.print(f"  [cyan]WOULD MERGE[/] {stem} — {len(all_extracts)} extracts from {total} chunks")
        else:
            out_path.write_text(json.dumps(merged_data, indent=2, ensure_ascii=False) + "\n")
            console.print(f"  [green]OK[/] {stem} — {len(all_extracts)} extracts from {total} chunks")
        merged += 1

    console.rule("[bold]Summary")
    console.print(f"  Merged: {merged}")
    console.print(f"  Incomplete (skipped): {skipped_incomplete}")
    console.print(f"  Already merged (skipped): {skipped_exists}")
    if dry_run:
        console.print("  [dim](dry run — no files written)[/]")

    if merged and not dry_run:
        log_action(Path(__file__).name, f"Merged {merged} sources, skipped {skipped_incomplete} incomplete + {skipped_exists} existing")


if __name__ == "__main__":
    app()
