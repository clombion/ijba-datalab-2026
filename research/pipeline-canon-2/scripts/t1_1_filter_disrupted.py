# /// script
# requires-python = ">=3.12"
# dependencies = ["typer>=0.9.0", "rich>=13.0.0"]
# ///
"""Filter horizon-table.csv for disrupted extracts (needs_update + displaced).

Reads the full horizon table from pipeline-canon and produces:
- disrupted.csv — all disrupted extracts (expected ~1,328 rows)
- disrupted_by_step/ — one CSV per pipeline step

Input: research/pipeline-canon/horizon-table.csv (4,351 rows, 14 columns)
Requires: horizon-table.csv must exist (no manifest prerequisite — this is the first step)

Usage:
    uv run research/pipeline-canon-2/scripts/t1_1_filter_disrupted.py
    uv run research/pipeline-canon-2/scripts/t1_1_filter_disrupted.py --dry-run
    uv run research/pipeline-canon-2/scripts/t1_1_filter_disrupted.py --csv research/pipeline-canon/horizon-table.csv

Exit codes:
    0  Success
    1  General error
    2  Usage error
    66 Input file not found
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
REPO_ROOT = PIPELINE_ROOT.parent.parent
DEFAULT_CSV = REPO_ROOT / "research" / "pipeline-canon" / "horizon-table.csv"
OUTPUT_CSV = PIPELINE_ROOT / "disrupted.csv"
OUTPUT_BY_STEP = PIPELINE_ROOT / "disrupted_by_step"
DISRUPTED_VALUES = {"needs_update", "displaced"}
PIPELINE_STEPS = ["Define", "Find", "Get", "Verify", "Clean", "Analyse", "Present"]

console = Console(stderr=True)
app = typer.Typer(help=__doc__, add_completion=False)


def version_callback(value: bool) -> None:
    if value:
        print(f"t1-1-filter-disrupted {__version__}")
        raise typer.Exit()


@app.command()
def main(
    csv_path: Annotated[Path, typer.Option("--csv", help="Path to horizon-table.csv")] = DEFAULT_CSV,
    dry_run: Annotated[bool, typer.Option("--dry-run", help="Show counts without writing files.")] = False,
    version: Annotated[bool | None, typer.Option("--version", callback=version_callback, is_eager=True, help="Show version.")] = None,
) -> None:
    """Filter horizon-table.csv for disrupted extracts."""
    if not csv_path.exists():
        console.print(f"[red]Input not found: {csv_path}[/red]")
        raise typer.Exit(66)

    # Read all rows
    with open(csv_path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        fieldnames = reader.fieldnames
        all_rows = list(reader)

    # Filter disrupted
    disrupted = [r for r in all_rows if r.get("llm_relevance", "") in DISRUPTED_VALUES]

    # Group by step
    by_step: dict[str, list[dict]] = {step: [] for step in PIPELINE_STEPS}
    for row in disrupted:
        step = row.get("pipeline_step", "")
        if step in by_step:
            by_step[step].append(row)

    # Report
    console.print(f"Total rows: {len(all_rows)}")
    console.print(f"Disrupted: {len(disrupted)}")
    needs_update = sum(1 for r in disrupted if r["llm_relevance"] == "needs_update")
    displaced = sum(1 for r in disrupted if r["llm_relevance"] == "displaced")
    console.print(f"  needs_update: {needs_update}")
    console.print(f"  displaced: {displaced}")
    console.print("By step:")
    for step in PIPELINE_STEPS:
        console.print(f"  {step}: {len(by_step[step])}")

    if dry_run:
        console.print("[yellow]Dry run — no files written.[/yellow]")
        # Still output JSON summary to stdout
        print(json.dumps({
            "total": len(all_rows),
            "disrupted": len(disrupted),
            "needs_update": needs_update,
            "displaced": displaced,
            "by_step": {s: len(rows) for s, rows in by_step.items()},
        }))
        raise typer.Exit(0)

    # Write disrupted.csv
    OUTPUT_CSV.parent.mkdir(parents=True, exist_ok=True)
    with open(OUTPUT_CSV, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(disrupted)

    # Write per-step CSVs
    OUTPUT_BY_STEP.mkdir(parents=True, exist_ok=True)
    for step in PIPELINE_STEPS:
        step_rows = by_step[step]
        if not step_rows:
            continue
        step_path = OUTPUT_BY_STEP / f"{step}.csv"
        with open(step_path, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(step_rows)

    console.print(f"[green]Written: {OUTPUT_CSV}[/green]")
    console.print(f"[green]Written: {OUTPUT_BY_STEP}/ ({sum(1 for s in PIPELINE_STEPS if by_step[s])} files)[/green]")

    # Manifest
    from log_action import log_action
    from manifest import append_manifest

    append_manifest("t1_1_filter_disrupted", "disrupted.csv", [str(csv_path)])
    for step in PIPELINE_STEPS:
        if by_step[step]:
            append_manifest("t1_1_filter_disrupted", f"disrupted_by_step/{step}.csv", ["disrupted.csv"])

    log_action("t1_1_filter_disrupted.py", f"Filtered {len(disrupted)} disrupted extracts ({needs_update} needs_update, {displaced} displaced)")

    # JSON summary to stdout
    print(json.dumps({
        "total": len(all_rows),
        "disrupted": len(disrupted),
        "needs_update": needs_update,
        "displaced": displaced,
        "by_step": {s: len(rows) for s, rows in by_step.items()},
    }))


if __name__ == "__main__":
    app()
