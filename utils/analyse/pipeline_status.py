# /// script
# requires-python = ">=3.12"
# dependencies = ["rich", "typer>=0.9.0"]
# ///
"""Pipeline status tracker — shows progress and suggests next actions.

Usage:
    uv run utils/analyse/pipeline_status.py                    # full status
    uv run utils/analyse/pipeline_status.py --next 10          # next 10 to process
    uv run utils/analyse/pipeline_status.py --stage chunks     # chunking status
    uv run utils/analyse/pipeline_status.py --stage extract    # T9 status
    uv run utils/analyse/pipeline_status.py --stage relevance  # T10 status
"""

import csv
import json
import re
import sys
from collections import defaultdict
from pathlib import Path
from typing import Annotated

import typer
from rich.console import Console
from rich.table import Table

__version__ = "1.0.0"

ROOT = Path(__file__).resolve().parent.parent.parent
CORPUS = ROOT / "research" / "pipeline-canon" / "corpus"
REGISTRY_CSV = CORPUS / "corpus-registry.csv"
CHUNKS_DIR = ROOT / "research" / "pipeline-canon" / "chunks"
MANIFEST_CSV = CHUNKS_DIR / "chunks-manifest.csv"
EXTRACTIONS_DIR = ROOT / "research" / "pipeline-canon" / "extractions"
RELEVANCE_DIR = ROOT / "research" / "pipeline-canon" / "relevance"

app = typer.Typer(help=__doc__, add_completion=False, no_args_is_help=False)


def version_callback(value: bool) -> None:
    if value:
        from rich.console import Console
        Console().print(f"pipeline_status {__version__}")
        raise typer.Exit()


def read_registry() -> list[dict]:
    if not REGISTRY_CSV.exists():
        from rich.console import Console
        Console().print(f"[red]corpus-registry.csv not found: {REGISTRY_CSV}")
        raise typer.Exit(1)
    rows = []
    with open(REGISTRY_CSV, newline="") as f:
        for row in csv.DictReader(f):
            rows.append(row)
    return rows


def read_manifest() -> dict[str, list[dict]]:
    """Group manifest rows by source_file."""
    groups: dict[str, list[dict]] = defaultdict(list)
    if not MANIFEST_CSV.exists():
        return groups
    with open(MANIFEST_CSV, newline="") as f:
        for row in csv.DictReader(f):
            groups[row["source_file"]].append(row)
    return groups


def count_extracts(path: Path) -> int:
    if not path.exists():
        return -1
    data = json.loads(path.read_text())
    return len(data.get("extracts", []))


def show_chunk_status(console: Console, registry: list[dict], manifest: dict) -> None:
    chunked = set(manifest.keys())
    total = len(registry)
    done = sum(1 for r in registry if r["file"] in chunked)
    total_chunks = sum(len(v) for v in manifest.values())

    console.rule("[bold]Chunking Status")
    console.print(f"  Sources: {done}/{total} chunked")
    console.print(f"  Total chunks: {total_chunks}")

    if MANIFEST_CSV.exists():
        # Context status summary
        ok = needed = 0
        with open(MANIFEST_CSV, newline="") as f:
            for row in csv.DictReader(f):
                cs = row.get("context_status", "")
                if cs == "context_ok":
                    ok += 1
                elif cs == "context_needed":
                    needed += 1
        if ok or needed:
            console.print(f"  context_ok: {ok}, context_needed: {needed}")

    missing = [r["file"] for r in registry if r["file"] not in chunked]
    if missing:
        console.print(f"  [yellow]Not chunked:[/] {', '.join(missing[:10])}{'...' if len(missing) > 10 else ''}")


def show_extract_status(console: Console, registry: list[dict], manifest: dict) -> None:
    console.rule("[bold]Extraction Status (T9)")

    total_sources = len(registry)
    sources_with_extracts = 0
    total_extracts = 0
    incomplete = []

    for reg_row in registry:
        source_file = reg_row["file"]
        stem = source_file.replace(".md", "")

        # Check for merged extraction
        merged = EXTRACTIONS_DIR / f"{stem}.json"
        if merged.exists():
            n = count_extracts(merged)
            if n > 0:
                sources_with_extracts += 1
                total_extracts += n
                continue

        # Check chunk-level extractions
        chunks = manifest.get(source_file, [])
        if not chunks:
            incomplete.append((stem, "not chunked"))
            continue

        chunk_extracts = 0
        chunks_done = 0
        for c in chunks:
            chunk_stem = c["chunk_file"].replace(".md", "")
            ext_path = EXTRACTIONS_DIR / f"{chunk_stem}.json"
            n = count_extracts(ext_path)
            if n > 0:
                chunk_extracts += n
                chunks_done += 1
            elif n == 0:
                chunks_done += 1  # scaffolded but empty

        total_chunks = int(chunks[0]["total_chunks"])
        if chunks_done == total_chunks and chunk_extracts > 0:
            sources_with_extracts += 1
            total_extracts += chunk_extracts
        else:
            incomplete.append((stem, f"{chunks_done}/{total_chunks} chunks"))

    console.print(f"  Sources complete: {sources_with_extracts}/{total_sources}")
    console.print(f"  Total extracts: {total_extracts}")
    if incomplete:
        console.print(f"  [yellow]Incomplete ({len(incomplete)}):[/]")
        for name, reason in incomplete[:15]:
            console.print(f"    {name}: {reason}")
        if len(incomplete) > 15:
            console.print(f"    ...and {len(incomplete) - 15} more")


def show_relevance_status(console: Console, registry: list[dict]) -> None:
    console.rule("[bold]Relevance Status (T10)")
    if not RELEVANCE_DIR.exists():
        console.print("  [dim]Not started[/]")
        return

    total = len(registry)
    done = 0
    total_scored = 0

    for reg_row in registry:
        stem = reg_row["file"].replace(".md", "")
        rel_path = RELEVANCE_DIR / f"{stem}.json"
        if rel_path.exists():
            data = json.loads(rel_path.read_text())
            extracts = data.get("extracts", [])
            scored = sum(1 for e in extracts if e.get("llm_relevance"))
            if scored == len(extracts) and extracts:
                done += 1
            total_scored += scored

    console.print(f"  Sources complete: {done}/{total}")
    console.print(f"  Total scored: {total_scored}")


def show_next(console: Console, registry: list[dict], manifest: dict, n: int) -> None:
    console.rule(f"[bold]Next {n} to Process")
    count = 0

    for reg_row in registry:
        if count >= n:
            break
        source_file = reg_row["file"]
        stem = source_file.replace(".md", "")

        # Check if merged extraction exists and is non-empty
        merged = EXTRACTIONS_DIR / f"{stem}.json"
        if merged.exists() and count_extracts(merged) > 0:
            continue

        # Check chunk-level completion
        chunks = manifest.get(source_file, [])
        if not chunks:
            console.print(f"  [red]{stem}[/] — not chunked yet")
            count += 1
            continue

        total_chunks = int(chunks[0]["total_chunks"])
        for c in sorted(chunks, key=lambda x: int(x["chunk_num"])):
            chunk_stem = c["chunk_file"].replace(".md", "")
            ext_path = EXTRACTIONS_DIR / f"{chunk_stem}.json"
            n_ext = count_extracts(ext_path)
            if n_ext <= 0:
                console.print(
                    f"  [cyan]{chunk_stem}[/] — "
                    f"{c['words']}w, chunk {c['chunk_num']}/{total_chunks}"
                )
                break
        count += 1


@app.command()
def main(
    stage: Annotated[str | None, typer.Option("--stage", help="Show status for a specific stage: chunks, extract, relevance.")] = None,
    next: Annotated[int | None, typer.Option("--next", help="Show next N sources to process.")] = None,
    version: Annotated[bool | None, typer.Option("--version", callback=version_callback, is_eager=True, help="Show version.")] = None,
) -> None:
    console = Console()
    registry = read_registry()
    manifest = read_manifest()

    if stage == "chunks" or stage is None:
        show_chunk_status(console, registry, manifest)
    if stage == "extract" or stage is None:
        show_extract_status(console, registry, manifest)
    if stage == "relevance" or stage is None:
        show_relevance_status(console, registry)
    if next:
        show_next(console, registry, manifest, next)


if __name__ == "__main__":
    app()
