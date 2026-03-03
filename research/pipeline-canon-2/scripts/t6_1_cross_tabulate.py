# /// script
# requires-python = ">=3.12"
# dependencies = ["typer>=0.9.0", "rich>=13.0.0"]
# ///
"""Cross-tabulate mapping and taxonomy data for analysis.

Produces 7+ analysis CSVs testing hypotheses H1-H4:
- step_mapping_status.csv — matched/partial/unmatched/deleted per step
- step_disruption_type.csv — disruption type per step
- practice_frequency.csv — which practices appear most, by step
- accessibility_coverage.csv — accessibility level distribution per step
- unmatched_extracts.csv — all unmatched with notes (H3)
- code_required_practices.csv — practices requiring code (H2)
- pattern_clusters.csv — natural groupings of practices (H1)

Input: mapping.csv, taxonomy.csv
Prerequisites: t5_4_merge_mapping, t4_1_merge_taxonomy in manifest

Usage:
    uv run research/pipeline-canon-2/scripts/t6_1_cross_tabulate.py
    uv run research/pipeline-canon-2/scripts/t6_1_cross_tabulate.py --dry-run

Exit codes:
    0  Success
    1  General error
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
MAPPING_CSV = PIPELINE_ROOT / "mapping.csv"
TAXONOMY_CSV = PIPELINE_ROOT / "taxonomy.csv"
ANALYSIS_DIR = PIPELINE_ROOT / "analysis"
REQUIRES_STEPS = ["t5_4_merge_mapping", "t4_1_merge_taxonomy"]
PIPELINE_STEPS = ["Define", "Find", "Get", "Verify", "Clean", "Analyse", "Present"]

console = Console(stderr=True)
app = typer.Typer(help=__doc__, add_completion=False)


def _write_csv(path: Path, fieldnames: list[str], rows: list[dict]) -> None:
    with open(path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def version_callback(value: bool) -> None:
    if value:
        print(f"t6-1-cross-tabulate {__version__}")
        raise typer.Exit()


@app.command()
def main(
    dry_run: Annotated[bool, typer.Option("--dry-run", help="Show what would be produced.")] = False,
    version: Annotated[bool | None, typer.Option("--version", callback=version_callback, is_eager=True, help="Show version.")] = None,
) -> None:
    """Cross-tabulate mapping and taxonomy data."""
    from manifest import check_manifest_prerequisites
    check_manifest_prerequisites(REQUIRES_STEPS)

    for path, label in [(MAPPING_CSV, "mapping.csv"), (TAXONOMY_CSV, "taxonomy.csv")]:
        if not path.exists():
            console.print(f"[red]Input not found ({label}): {path}[/red]")
            raise typer.Exit(66)

    with open(MAPPING_CSV, newline="", encoding="utf-8") as f:
        mappings = list(csv.DictReader(f))
    with open(TAXONOMY_CSV, newline="", encoding="utf-8") as f:
        taxonomy = list(csv.DictReader(f))

    # Index taxonomy by practice_id
    tax_by_id = {t["practice_id"]: t for t in taxonomy}

    console.print(f"Mappings: {len(mappings)}")
    console.print(f"Taxonomy: {len(taxonomy)}")

    # 1. step_mapping_status — status distribution per step
    status_rows = []
    for step in PIPELINE_STEPS:
        step_maps = [m for m in mappings if m["pipeline_step"] == step]
        counts: Counter[str] = Counter(m["mapping_status"] for m in step_maps)
        status_rows.append({
            "pipeline_step": step,
            "total": len(step_maps),
            "matched": counts.get("matched", 0),
            "partial": counts.get("partial", 0),
            "unmatched": counts.get("unmatched", 0),
            "deleted": counts.get("deleted", 0),
        })

    # 2. step_disruption_type — disruption type per step
    disruption_rows = []
    for step in PIPELINE_STEPS:
        step_maps = [m for m in mappings if m["pipeline_step"] == step]
        counts = Counter(m["disruption_type"] for m in step_maps)
        disruption_rows.append({
            "pipeline_step": step,
            "total": len(step_maps),
            "tool_defunct": counts.get("tool_defunct", 0),
            "method_automated": counts.get("method_automated", 0),
            "method_simplified": counts.get("method_simplified", 0),
            "assumption_changed": counts.get("assumption_changed", 0),
        })

    # 3. practice_frequency — practice usage counts by step
    freq_rows = []
    for step in PIPELINE_STEPS:
        step_maps = [m for m in mappings if m["pipeline_step"] == step]
        pid_counter: Counter[str] = Counter()
        for m in step_maps:
            pids = m.get("practice_ids", "")
            if pids:
                for pid in pids.split(","):
                    pid = pid.strip()
                    if pid:
                        pid_counter[pid] += 1
        for pid, count in pid_counter.most_common():
            tax = tax_by_id.get(pid, {})
            freq_rows.append({
                "pipeline_step": step,
                "practice_id": pid,
                "practice_name": tax.get("practice_name", ""),
                "count": count,
                "pct_of_step": round(count / max(len(step_maps), 1) * 100, 1),
            })

    # 4. accessibility_coverage — per step
    acc_rows = []
    for step in PIPELINE_STEPS:
        step_maps = [m for m in mappings if m["pipeline_step"] == step]
        # Gather accessibility from referenced practices
        acc_counter: Counter[str] = Counter()
        for m in step_maps:
            pids = m.get("practice_ids", "")
            if pids:
                for pid in pids.split(","):
                    pid = pid.strip()
                    tax = tax_by_id.get(pid, {})
                    acc = tax.get("accessibility_level", "unknown")
                    acc_counter[acc] += 1
        acc_rows.append({
            "pipeline_step": step,
            "spreadsheet": acc_counter.get("spreadsheet", 0),
            "gui_tool": acc_counter.get("gui_tool", 0),
            "structured_prompt": acc_counter.get("structured_prompt", 0),
            "code_required": acc_counter.get("code_required", 0),
        })

    # 5. unmatched_extracts — H3 test
    unmatched_rows = []
    for m in mappings:
        if m.get("mapping_status") == "unmatched":
            unmatched_rows.append({
                "source_id": m["source_id"],
                "pipeline_step": m["pipeline_step"],
                "extract_type": m["extract_type"],
                "llm_relevance": m["llm_relevance"],
                "extract": m["extract"],
                "notes": m.get("notes", ""),
            })

    # 6. code_required_practices — H2 test
    code_rows = []
    for t in taxonomy:
        if t.get("accessibility_level") == "code_required":
            code_rows.append({
                "practice_id": t["practice_id"],
                "practice_name": t["practice_name"],
                "pipeline_steps": t["pipeline_steps"],
                "description": t["description"],
                "verification_method": t.get("verification_method", ""),
            })

    # 7. pattern_clusters — H1 test: group practices by (step, replaces_category)
    cluster_counter: Counter[tuple[str, str]] = Counter()
    for t in taxonomy:
        steps = t.get("pipeline_steps", "")
        replaces = t.get("replaces_category", "")
        for step in steps.split(","):
            step = step.strip()
            if step:
                cluster_counter[(step, replaces)] += 1

    cluster_rows = []
    for (step, replaces), count in cluster_counter.most_common():
        cluster_rows.append({
            "pipeline_step": step,
            "replaces_category": replaces,
            "practice_count": count,
        })

    summary = {
        "total_mappings": len(mappings),
        "total_taxonomy": len(taxonomy),
        "unmatched_count": len(unmatched_rows),
        "code_required_count": len(code_rows),
        "pattern_clusters": len(cluster_rows),
        "h2_code_required": len(code_rows),
        "h3_unmatched": len(unmatched_rows),
        "h4_deleted": sum(1 for m in mappings if m.get("mapping_status") == "deleted"),
    }

    console.print(f"\nH2 (code_required practices): {summary['h2_code_required']}")
    console.print(f"H3 (unmatched extracts): {summary['h3_unmatched']}")
    console.print(f"H4 (deleted/displaced): {summary['h4_deleted']}")
    console.print(f"Pattern clusters: {summary['pattern_clusters']}")

    if dry_run:
        console.print("[yellow]Dry run — no files written.[/yellow]")
        print(json.dumps(summary))
        raise typer.Exit(0)

    ANALYSIS_DIR.mkdir(parents=True, exist_ok=True)

    outputs = [
        ("step_mapping_status.csv", ["pipeline_step", "total", "matched", "partial", "unmatched", "deleted"], status_rows),
        ("step_disruption_type.csv", ["pipeline_step", "total", "tool_defunct", "method_automated", "method_simplified", "assumption_changed"], disruption_rows),
        ("practice_frequency.csv", ["pipeline_step", "practice_id", "practice_name", "count", "pct_of_step"], freq_rows),
        ("accessibility_coverage.csv", ["pipeline_step", "spreadsheet", "gui_tool", "structured_prompt", "code_required"], acc_rows),
        ("unmatched_extracts.csv", ["source_id", "pipeline_step", "extract_type", "llm_relevance", "extract", "notes"], unmatched_rows),
        ("code_required_practices.csv", ["practice_id", "practice_name", "pipeline_steps", "description", "verification_method"], code_rows),
        ("pattern_clusters.csv", ["pipeline_step", "replaces_category", "practice_count"], cluster_rows),
    ]

    for filename, fields, rows in outputs:
        _write_csv(ANALYSIS_DIR / filename, fields, rows)
        console.print(f"  {filename}: {len(rows)} rows")

    console.print(f"[green]Written: {ANALYSIS_DIR}/ (7 files)[/green]")

    from log_action import log_action
    from manifest import append_manifest

    for filename, _, _ in outputs:
        append_manifest("t6_1_cross_tabulate", f"analysis/{filename}", ["mapping.csv", "taxonomy.csv"])

    log_action("t6_1_cross_tabulate.py", f"Cross-tabulated {len(mappings)} mappings: {summary['h3_unmatched']} unmatched, {summary['h2_code_required']} code-required, {summary['h4_deleted']} deleted")

    print(json.dumps(summary))


if __name__ == "__main__":
    app()
