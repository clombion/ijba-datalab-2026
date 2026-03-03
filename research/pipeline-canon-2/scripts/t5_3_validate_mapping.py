# /// script
# requires-python = ">=3.12"
# dependencies = ["typer>=0.9.0", "rich>=13.0.0"]
# ///
"""Validate mapping files for completeness, consistency, and drift.

Checks: all fields non-null, valid enums, practice_ids reference valid taxonomy.
Consistency: displaced → deleted status; unmatched → notes explain gap.
Drift detection: distribution changes, dominant practice_ids, rationale length.

Input: mapping/{Step}.json
Prerequisites: t5_1_scaffold_mapping in manifest

Usage:
    uv run research/pipeline-canon-2/scripts/t5_3_validate_mapping.py
    uv run research/pipeline-canon-2/scripts/t5_3_validate_mapping.py --only Get
    uv run research/pipeline-canon-2/scripts/t5_3_validate_mapping.py --json

Exit codes:
    0  PASS
    1  FAIL
    66 Input not found
"""

from __future__ import annotations

import json
import statistics
from collections import Counter
from pathlib import Path
from typing import Annotated

import typer
from rich.console import Console

__version__ = "1.0.0"

PIPELINE_ROOT = Path(__file__).resolve().parent.parent
MAPPING_DIR = PIPELINE_ROOT / "mapping"
REQUIRES_STEPS = ["t5_1_scaffold_mapping"]
PIPELINE_STEPS = ["Define", "Find", "Get", "Verify", "Clean", "Analyse", "Present"]
VALID_MAPPING_STATUS = {"matched", "partial", "unmatched", "deleted"}
VALID_DISRUPTION_TYPE = {"tool_defunct", "method_automated", "method_simplified", "assumption_changed"}

console = Console(stderr=True)
app = typer.Typer(help=__doc__, add_completion=False)


def version_callback(value: bool) -> None:
    if value:
        print(f"t5-3-validate-mapping {__version__}")
        raise typer.Exit()


def _validate_step(step_file: Path) -> dict:
    """Validate a single step's mapping file."""
    with open(step_file, encoding="utf-8") as f:
        data = json.load(f)

    step = data.get("step", "")
    extracts = data.get("extracts", [])
    taxonomy = data.get("taxonomy", [])
    taxonomy_ids = {t.get("practice_id", "") for t in taxonomy}

    errors: list[dict] = []
    warnings: list[dict] = []
    status_counts: Counter[str] = Counter()
    disruption_counts: Counter[str] = Counter()
    pid_counts: Counter[str] = Counter()
    rationale_lengths: list[int] = []
    unfilled = 0

    for i, ext in enumerate(extracts):
        ms = ext.get("mapping_status")
        dt = ext.get("disruption_type")
        pids = ext.get("practice_ids")
        rat = ext.get("mapping_rationale")
        notes = ext.get("notes")

        # Check filled
        if ms is None:
            unfilled += 1
            continue

        # Validate enums
        if ms not in VALID_MAPPING_STATUS:
            errors.append({"type": "invalid_status", "index": i, "value": ms})
        else:
            status_counts[ms] += 1

        if dt not in VALID_DISRUPTION_TYPE:
            errors.append({"type": "invalid_disruption", "index": i, "value": dt})
        else:
            disruption_counts[dt] += 1

        # Referential integrity
        if pids:
            for pid in pids:
                if pid not in taxonomy_ids:
                    errors.append({"type": "invalid_practice_id", "index": i, "value": pid})
                pid_counts[pid] += 1

        # Consistency: displaced → deleted
        if ext.get("llm_relevance") == "displaced" and ms != "deleted":
            warnings.append({"type": "displaced_not_deleted", "index": i, "status": ms})

        # Consistency: matched/partial need practice_ids
        if ms in {"matched", "partial"} and not pids:
            errors.append({"type": "matched_no_pids", "index": i})

        # Consistency: unmatched needs notes
        if ms == "unmatched" and (not notes or len(notes.strip()) < 5):
            errors.append({"type": "unmatched_no_notes", "index": i})

        # Track rationale length
        if rat:
            rationale_lengths.append(len(rat))

    # Drift detection
    total_filled = len(extracts) - unfilled
    if total_filled > 0:
        # Dominant practice check
        for pid, count in pid_counts.most_common(3):
            pct = count / total_filled * 100
            if pct > 50:
                warnings.append({"type": "dominant_practice", "practice_id": pid, "pct": round(pct, 1)})

        # Rationale length drift
        if rationale_lengths:
            mean_len = statistics.mean(rationale_lengths)
            if mean_len < 20:
                warnings.append({"type": "short_rationales", "mean_length": round(mean_len, 1)})

            # First-half vs second-half comparison
            if len(rationale_lengths) >= 10:
                mid = len(rationale_lengths) // 2
                first_half = statistics.mean(rationale_lengths[:mid])
                second_half = statistics.mean(rationale_lengths[mid:])
                if first_half > 0 and second_half / first_half < 0.5:
                    warnings.append({"type": "rationale_length_drift", "first_half": round(first_half, 1), "second_half": round(second_half, 1)})

    return {
        "step": step,
        "total": len(extracts),
        "filled": total_filled,
        "unfilled": unfilled,
        "status_distribution": dict(status_counts),
        "disruption_distribution": dict(disruption_counts),
        "top_practices": dict(pid_counts.most_common(5)),
        "errors": errors,
        "warnings": warnings,
    }


@app.command()
def main(
    only: Annotated[str | None, typer.Option("--only", help="Validate only this step (e.g. Get).")] = None,
    json_output: Annotated[bool, typer.Option("--json", help="Machine-readable JSON output.")] = False,
    version: Annotated[bool | None, typer.Option("--version", callback=version_callback, is_eager=True, help="Show version.")] = None,
) -> None:
    """Validate mapping files."""
    from manifest import check_manifest_prerequisites
    check_manifest_prerequisites(REQUIRES_STEPS)

    steps = [only] if only else PIPELINE_STEPS
    all_errors = False
    results = []

    for step in steps:
        step_file = MAPPING_DIR / f"{step}.json"
        if not step_file.exists():
            if only:
                console.print(f"[red]File not found: {step_file}[/red]")
                raise typer.Exit(66)
            continue
        result = _validate_step(step_file)
        results.append(result)
        if result["errors"]:
            all_errors = True

    if json_output:
        overall = {"status": "FAIL" if all_errors else "PASS", "steps": results}
        print(json.dumps(overall, indent=2))
    else:
        for r in results:
            console.print(f"\n[bold]{r['step']}[/bold]: {r['filled']}/{r['total']} filled")
            if r["status_distribution"]:
                console.print(f"  Status: {r['status_distribution']}")
            if r["disruption_distribution"]:
                console.print(f"  Disruption: {r['disruption_distribution']}")
            if r["top_practices"]:
                console.print(f"  Top practices: {r['top_practices']}")
            if r["errors"]:
                console.print(f"  [red]{len(r['errors'])} errors[/red]")
                for e in r["errors"][:5]:
                    console.print(f"    {e}")
            if r["warnings"]:
                console.print(f"  [yellow]{len(r['warnings'])} warnings[/yellow]")
                for w in r["warnings"]:
                    console.print(f"    {w}")

        if all_errors:
            console.print("\n[red]FAIL[/red]")
        else:
            console.print("\n[green]PASS[/green]")

    raise typer.Exit(1 if all_errors else 0)


if __name__ == "__main__":
    app()
