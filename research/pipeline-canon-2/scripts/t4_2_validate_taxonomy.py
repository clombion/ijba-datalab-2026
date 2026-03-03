# /// script
# requires-python = ">=3.12"
# dependencies = ["typer>=0.9.0", "rich>=13.0.0"]
# ///
"""Validate the unified practice taxonomy.

Checks: all fields non-null, valid enums, at least one pipeline step per practice.
Warnings: identical practice names, practices with no verification method.

Input: taxonomy.csv
Prerequisites: t4_1_merge_taxonomy in manifest

Usage:
    uv run research/pipeline-canon-2/scripts/t4_2_validate_taxonomy.py
    uv run research/pipeline-canon-2/scripts/t4_2_validate_taxonomy.py --json

Exit codes:
    0  PASS
    1  FAIL
    66 Input not found
"""

from __future__ import annotations

import csv
import json
from collections import Counter
from pathlib import Path
from typing import Annotated

import typer
from rich.console import Console

__version__ = "1.0.0"

PIPELINE_ROOT = Path(__file__).resolve().parent.parent
INPUT_FILE = PIPELINE_ROOT / "taxonomy.csv"
REQUIRES_STEPS = ["t4_1_merge_taxonomy"]

VALID_STEPS = {"Define", "Find", "Get", "Verify", "Clean", "Analyse", "Present"}
VALID_ACCESSIBILITY = {"spreadsheet", "gui_tool", "structured_prompt", "code_required"}
VALID_SOURCE_TYPES = {"case_study", "podcast"}
REQUIRED_FIELDS = [
    "practice_id", "practice_name", "description", "source_type", "source_id",
    "pipeline_steps", "replaces_category", "accessibility_level",
    "verification_method", "example", "practice_rationale",
]

console = Console(stderr=True)
app = typer.Typer(help=__doc__, add_completion=False)


def version_callback(value: bool) -> None:
    if value:
        print(f"t4-2-validate-taxonomy {__version__}")
        raise typer.Exit()


@app.command()
def main(
    json_output: Annotated[bool, typer.Option("--json", help="Machine-readable JSON output.")] = False,
    version: Annotated[bool | None, typer.Option("--version", callback=version_callback, is_eager=True, help="Show version.")] = None,
) -> None:
    """Validate taxonomy.csv."""
    from manifest import check_manifest_prerequisites
    check_manifest_prerequisites(REQUIRES_STEPS)

    if not INPUT_FILE.exists():
        console.print(f"[red]Input not found: {INPUT_FILE}[/red]")
        raise typer.Exit(66)

    with open(INPUT_FILE, newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))

    errors: list[dict] = []
    warnings: list[dict] = []

    name_counter: Counter[str] = Counter()
    by_step: dict[str, int] = {}
    by_accessibility: dict[str, int] = {}

    for i, row in enumerate(rows):
        pid = row.get("practice_id", "")

        # Check required fields non-null/non-empty
        for field in REQUIRED_FIELDS:
            val = row.get(field, "").strip()
            if not val:
                errors.append({"type": "empty_field", "practice_id": pid, "field": field, "row": i})

        # Validate source_type
        st = row.get("source_type", "").strip()
        if st and st not in VALID_SOURCE_TYPES:
            errors.append({"type": "invalid_source_type", "practice_id": pid, "value": st})

        # Validate pipeline_steps
        steps_str = row.get("pipeline_steps", "").strip()
        if steps_str:
            steps = [s.strip() for s in steps_str.split(",")]
            for step in steps:
                if step not in VALID_STEPS:
                    errors.append({"type": "invalid_step", "practice_id": pid, "value": step})
                by_step[step] = by_step.get(step, 0) + 1
        else:
            errors.append({"type": "no_steps", "practice_id": pid, "row": i})

        # Validate accessibility_level
        acc = row.get("accessibility_level", "").strip()
        if acc and acc not in VALID_ACCESSIBILITY:
            errors.append({"type": "invalid_accessibility", "practice_id": pid, "value": acc})
        if acc:
            by_accessibility[acc] = by_accessibility.get(acc, 0) + 1

        # Track names for duplicate check
        name = row.get("practice_name", "").strip().lower()
        if name:
            name_counter[name] += 1

        # Warn if no verification method
        if not row.get("verification_method", "").strip():
            warnings.append({"type": "no_verification", "practice_id": pid})

    # Flag duplicate names
    for name, count in name_counter.items():
        if count > 1:
            warnings.append({"type": "duplicate_name", "name": name, "count": count})

    result = {
        "status": "PASS" if not errors else "FAIL",
        "total": len(rows),
        "by_step": dict(sorted(by_step.items())),
        "by_accessibility": dict(sorted(by_accessibility.items())),
        "errors": errors,
        "warnings": warnings,
    }

    if json_output:
        print(json.dumps(result, indent=2))
    else:
        console.print(f"Practices: {len(rows)}")
        console.print("\nBy step:")
        for step in sorted(VALID_STEPS):
            console.print(f"  {step}: {by_step.get(step, 0)}")
        console.print("\nBy accessibility:")
        for acc in sorted(VALID_ACCESSIBILITY):
            console.print(f"  {acc}: {by_accessibility.get(acc, 0)}")

        if errors:
            console.print(f"\n[red]{len(errors)} error(s)[/red]")
            for e in errors[:15]:
                console.print(f"  {e}")
        if warnings:
            console.print(f"\n[yellow]{len(warnings)} warning(s)[/yellow]")
            for w in warnings[:10]:
                console.print(f"  {w}")
        if not errors:
            console.print("\n[green]PASS[/green]")
        else:
            console.print("\n[red]FAIL[/red]")

    raise typer.Exit(1 if errors else 0)


if __name__ == "__main__":
    app()
