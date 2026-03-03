# /// script
# requires-python = ">=3.12"
# dependencies = ["typer>=0.9.0", "rich>=13.0.0"]
# ///
"""Merge all per-step mapping files into a single mapping.csv.

Count-gate: all 7 step files must exist and be fully filled. Reads each
mapping/{Step}.json, extracts the filled mappings, and writes a flat CSV.

Input: mapping/{Step}.json (7 files)
Prerequisites: t5_1_scaffold_mapping in manifest
Output: mapping.csv

Usage:
    uv run research/pipeline-canon-2/scripts/t5_4_merge_mapping.py
    uv run research/pipeline-canon-2/scripts/t5_4_merge_mapping.py --dry-run

Exit codes:
    0  Success
    1  General error (including incomplete step files)
    5  Output already exists (use --force)
    66 Input not found
"""

from __future__ import annotations

import csv
import json
from pathlib import Path
from typing import Annotated

import typer
from rich.console import Console

__version__ = "1.0.0"

PIPELINE_ROOT = Path(__file__).resolve().parent.parent
MAPPING_DIR = PIPELINE_ROOT / "mapping"
OUTPUT_FILE = PIPELINE_ROOT / "mapping.csv"
REQUIRES_STEPS = ["t5_1_scaffold_mapping"]
PIPELINE_STEPS = ["Define", "Find", "Get", "Verify", "Clean", "Analyse", "Present"]

MAPPING_FIELDS = [
    "source_id", "pipeline_step", "extract_type", "llm_relevance", "extract",
    "relevance_rationale", "practice_ids", "mapping_rationale", "mapping_status",
    "disruption_type", "notes",
]

console = Console(stderr=True)
app = typer.Typer(help=__doc__, add_completion=False)


def version_callback(value: bool) -> None:
    if value:
        print(f"t5-4-merge-mapping {__version__}")
        raise typer.Exit()


@app.command()
def main(
    dry_run: Annotated[bool, typer.Option("--dry-run", help="Show counts without writing.")] = False,
    force: Annotated[bool, typer.Option("--force", help="Overwrite existing output.")] = False,
    version: Annotated[bool | None, typer.Option("--version", callback=version_callback, is_eager=True, help="Show version.")] = None,
) -> None:
    """Merge all step mapping files into mapping.csv."""
    from manifest import check_manifest_prerequisites
    check_manifest_prerequisites(REQUIRES_STEPS)

    if OUTPUT_FILE.exists() and not force:
        console.print(f"[yellow]Output already exists: {OUTPUT_FILE}[/yellow]")
        raise typer.Exit(5)

    # Check all step files exist
    missing = []
    for step in PIPELINE_STEPS:
        step_file = MAPPING_DIR / f"{step}.json"
        if not step_file.exists():
            missing.append(step)

    if missing:
        console.print(f"[red]Missing step files: {', '.join(missing)}[/red]")
        raise typer.Exit(66)

    # Read and check completeness
    all_rows: list[dict] = []
    incomplete = []

    for step in PIPELINE_STEPS:
        step_file = MAPPING_DIR / f"{step}.json"
        with open(step_file, encoding="utf-8") as f:
            data = json.load(f)

        extracts = data.get("extracts", [])
        unfilled = sum(1 for e in extracts if e.get("mapping_status") is None)
        if unfilled > 0:
            incomplete.append(f"{step}: {unfilled} unfilled")

        for ext in extracts:
            row = {}
            for field in MAPPING_FIELDS:
                val = ext.get(field, "")
                if isinstance(val, list):
                    val = ",".join(val)
                row[field] = val or ""
            all_rows.append(row)

    if incomplete:
        console.print("[red]Incomplete step files:[/red]")
        for msg in incomplete:
            console.print(f"  {msg}")
        console.print("All extracts must be filled before merging.")
        raise typer.Exit(1)

    console.print(f"Total extracts to merge: {len(all_rows)}")
    for step in PIPELINE_STEPS:
        count = sum(1 for r in all_rows if r["pipeline_step"] == step)
        console.print(f"  {step}: {count}")

    if dry_run:
        console.print("[yellow]Dry run — no file written.[/yellow]")
        print(json.dumps({"total": len(all_rows)}))
        raise typer.Exit(0)

    with open(OUTPUT_FILE, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=MAPPING_FIELDS)
        writer.writeheader()
        writer.writerows(all_rows)

    console.print(f"[green]Written: {OUTPUT_FILE} ({len(all_rows)} rows)[/green]")

    from log_action import log_action
    from manifest import append_manifest

    input_paths = [f"mapping/{step}.json" for step in PIPELINE_STEPS]
    append_manifest("t5_4_merge_mapping", "mapping.csv", input_paths)
    log_action("t5_4_merge_mapping.py", f"Merged {len(all_rows)} extract mappings from {len(PIPELINE_STEPS)} step files")

    print(json.dumps({"total": len(all_rows)}))


if __name__ == "__main__":
    app()
