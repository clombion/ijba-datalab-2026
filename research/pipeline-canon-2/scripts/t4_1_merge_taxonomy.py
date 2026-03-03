# /// script
# requires-python = ">=3.12"
# dependencies = ["typer>=0.9.0", "rich>=13.0.0"]
# ///
"""Merge case study and podcast practices into a unified taxonomy CSV.

Reads filled practice files from both sources, assigns practice_ids (P001, P002...),
and outputs taxonomy.csv. Flags potential duplicates where practice_name matches
(case-insensitive) AND pipeline_steps overlap.

Input: practices/case_studies.json, practices/podcast_filtered.json
Prerequisites: t2_1_scaffold_case_studies, t3_4_filter_relevant in manifest
Output: taxonomy.csv

Usage:
    uv run research/pipeline-canon-2/scripts/t4_1_merge_taxonomy.py
    uv run research/pipeline-canon-2/scripts/t4_1_merge_taxonomy.py --dry-run

Exit codes:
    0  Success
    1  General error
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
CASE_STUDIES_FILE = PIPELINE_ROOT / "practices" / "case_studies.json"
PODCAST_FILE = PIPELINE_ROOT / "practices" / "podcast_filtered.json"
OUTPUT_FILE = PIPELINE_ROOT / "taxonomy.csv"
REQUIRES_STEPS = ["t2_1_scaffold_case_studies", "t3_4_filter_relevant"]

TAXONOMY_FIELDS = [
    "practice_id", "practice_name", "description", "source_type", "source_id",
    "pipeline_steps", "replaces_category", "tools_mentioned", "accessibility_level",
    "verification_method", "example", "practice_rationale",
]

console = Console(stderr=True)
app = typer.Typer(help=__doc__, add_completion=False)


def _extract_practices(data: list[dict], source_type: str) -> list[dict]:
    """Extract non-null practices from a filled JSON file."""
    practices = []
    for entry in data:
        source_id = entry.get("source_id", "")
        for p in entry.get("practices", []):
            if p is None:
                continue
            practices.append({
                "source_type": source_type,
                "source_id": source_id if source_type == "case_study" else entry.get("episode", ""),
                **p,
            })
    return practices


def version_callback(value: bool) -> None:
    if value:
        print(f"t4-1-merge-taxonomy {__version__}")
        raise typer.Exit()


@app.command()
def main(
    dry_run: Annotated[bool, typer.Option("--dry-run", help="Show counts without writing.")] = False,
    force: Annotated[bool, typer.Option("--force", help="Overwrite existing output.")] = False,
    version: Annotated[bool | None, typer.Option("--version", callback=version_callback, is_eager=True, help="Show version.")] = None,
) -> None:
    """Merge practices into unified taxonomy CSV."""
    from manifest import check_manifest_prerequisites
    check_manifest_prerequisites(REQUIRES_STEPS)

    for path, label in [(CASE_STUDIES_FILE, "case studies"), (PODCAST_FILE, "podcast filtered")]:
        if not path.exists():
            console.print(f"[red]Input not found ({label}): {path}[/red]")
            raise typer.Exit(66)

    if OUTPUT_FILE.exists() and not force:
        console.print(f"[yellow]Output already exists: {OUTPUT_FILE}[/yellow]")
        raise typer.Exit(5)

    with open(CASE_STUDIES_FILE, encoding="utf-8") as f:
        cs_data = json.load(f)
    with open(PODCAST_FILE, encoding="utf-8") as f:
        pod_data = json.load(f)

    cs_practices = _extract_practices(cs_data, "case_study")
    pod_practices = _extract_practices(pod_data, "podcast")

    all_practices = cs_practices + pod_practices

    # Assign practice_ids
    for i, p in enumerate(all_practices):
        p["practice_id"] = f"P{i + 1:03d}"
        # Normalize list fields to comma-separated strings for CSV
        if isinstance(p.get("pipeline_steps"), list):
            p["pipeline_steps"] = ",".join(p["pipeline_steps"])
        if isinstance(p.get("tools_mentioned"), list):
            p["tools_mentioned"] = ",".join(p["tools_mentioned"])

    # Check for potential duplicates
    duplicates: list[tuple[str, str]] = []
    for i, a in enumerate(all_practices):
        for j, b in enumerate(all_practices):
            if j <= i:
                continue
            name_a = a.get("practice_name", "").strip().lower()
            name_b = b.get("practice_name", "").strip().lower()
            if name_a == name_b:
                steps_a = set(a.get("pipeline_steps", "").split(","))
                steps_b = set(b.get("pipeline_steps", "").split(","))
                if steps_a & steps_b:
                    duplicates.append((a["practice_id"], b["practice_id"]))

    console.print(f"Case study practices: {len(cs_practices)}")
    console.print(f"Podcast practices: {len(pod_practices)}")
    console.print(f"Total: {len(all_practices)}")
    if duplicates:
        console.print(f"[yellow]Potential duplicates: {len(duplicates)}[/yellow]")
        for a, b in duplicates:
            console.print(f"  {a} <-> {b}")

    if dry_run:
        console.print("[yellow]Dry run — no file written.[/yellow]")
        print(json.dumps({"case_study": len(cs_practices), "podcast": len(pod_practices), "total": len(all_practices), "duplicates": len(duplicates)}))
        raise typer.Exit(0)

    with open(OUTPUT_FILE, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=TAXONOMY_FIELDS, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(all_practices)

    console.print(f"[green]Written: {OUTPUT_FILE} ({len(all_practices)} practices)[/green]")

    from log_action import log_action
    from manifest import append_manifest

    append_manifest("t4_1_merge_taxonomy", "taxonomy.csv", ["practices/case_studies.json", "practices/podcast_filtered.json"])
    log_action("t4_1_merge_taxonomy.py", f"Merged {len(all_practices)} practices ({len(cs_practices)} case study, {len(pod_practices)} podcast), {len(duplicates)} potential duplicates")

    print(json.dumps({"total": len(all_practices), "duplicates": len(duplicates)}))


if __name__ == "__main__":
    app()
