# /// script
# requires-python = ">=3.12"
# dependencies = ["rich", "typer>=0.9.0"]
# ///
"""T12 Analyse — deterministic cross-tabulations of horizon-table.csv.

Reads horizon-table.csv (4,351 extracts) and generates 6 analysis CSVs
into research/pipeline-canon/analysis/ plus console summary stats.

Usage:
    uv run utils/analyse/t12_1_analyse_horizon.py
"""

import csv
import sys
from collections import Counter, defaultdict
from pathlib import Path
from typing import Annotated

import typer
from rich.console import Console
from rich.table import Table

__version__ = "1.0.0"

ROOT = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(ROOT / "utils"))
from log_action import log_action  # noqa: E402

HORIZON_CSV = ROOT / "research" / "pipeline-canon" / "horizon-table.csv"
OUT_DIR = ROOT / "research" / "pipeline-canon" / "analysis"

PIPELINE_STEPS = ["Define", "Find", "Get", "Verify", "Clean", "Analyse", "Present"]
RELEVANCE_LABELS = ["endures", "needs_update", "displaced"]
EXTRACT_TYPES = ["epistemological", "procedural", "organizational", "tool-specific"]

console = Console()

app = typer.Typer(help=__doc__, add_completion=False, no_args_is_help=False)


def version_callback(value: bool) -> None:
    if value:
        console.print(f"t12_1_analyse_horizon {__version__}")
        raise typer.Exit()


def read_horizon() -> list[dict]:
    rows = []
    with open(HORIZON_CSV, newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            rows.append(row)
    return rows


def write_csv(path: Path, fieldnames: list[str], rows: list[dict], *, dry_run: bool = False) -> None:
    if not dry_run:
        with open(path, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames, extrasaction="ignore")
            writer.writeheader()
            writer.writerows(rows)
    prefix = "[DRY RUN] " if dry_run else ""
    console.print(f"  {prefix}✓ {path.relative_to(ROOT)} ({len(rows)} rows)")


def step_distribution(rows: list[dict], *, dry_run: bool = False) -> Counter:
    """Per-step counts, %, secondary_step counts (H1)."""
    total = len(rows)
    primary = Counter(r["pipeline_step"] for r in rows)
    secondary = Counter(r["secondary_step"] for r in rows if r["secondary_step"])

    out = []
    for step in PIPELINE_STEPS:
        n = primary.get(step, 0)
        out.append({
            "pipeline_step": step,
            "primary_count": n,
            "primary_pct": round(100 * n / total, 1) if total else 0,
            "secondary_count": secondary.get(step, 0),
            "combined_count": n + secondary.get(step, 0),
        })
    write_csv(
        OUT_DIR / "step_distribution.csv",
        ["pipeline_step", "primary_count", "primary_pct", "secondary_count", "combined_count"],
        out,
        dry_run=dry_run,
    )
    return primary


def type_x_relevance(rows: list[dict], *, dry_run: bool = False) -> defaultdict:
    """extract_type × llm_relevance cross-tab with row % (H2)."""
    counts = defaultdict(Counter)
    type_totals = Counter()
    for r in rows:
        et = r["extract_type"]
        lr = r["llm_relevance"]
        counts[et][lr] += 1
        type_totals[et] += 1

    out = []
    for et in EXTRACT_TYPES:
        t = type_totals.get(et, 0)
        row = {"extract_type": et, "total": t}
        for lr in RELEVANCE_LABELS:
            n = counts[et].get(lr, 0)
            row[lr] = n
            row[f"{lr}_pct"] = round(100 * n / t, 1) if t else 0
        out.append(row)

    fields = ["extract_type", "total"]
    for lr in RELEVANCE_LABELS:
        fields.extend([lr, f"{lr}_pct"])
    write_csv(OUT_DIR / "type_x_relevance.csv", fields, out, dry_run=dry_run)
    return counts


def step_x_relevance(rows: list[dict], *, dry_run: bool = False) -> tuple[defaultdict, Counter]:
    """pipeline_step × llm_relevance cross-tab with row % (H3)."""
    counts = defaultdict(Counter)
    step_totals = Counter()
    for r in rows:
        ps = r["pipeline_step"]
        lr = r["llm_relevance"]
        counts[ps][lr] += 1
        step_totals[ps] += 1

    out = []
    for ps in PIPELINE_STEPS:
        t = step_totals.get(ps, 0)
        row = {"pipeline_step": ps, "total": t}
        for lr in RELEVANCE_LABELS:
            n = counts[ps].get(lr, 0)
            row[lr] = n
            row[f"{lr}_pct"] = round(100 * n / t, 1) if t else 0
        # redefinition = needs_update + displaced
        redef = counts[ps].get("needs_update", 0) + counts[ps].get("displaced", 0)
        row["redef_count"] = redef
        row["redef_pct"] = round(100 * redef / t, 1) if t else 0
        out.append(row)

    fields = ["pipeline_step", "total"]
    for lr in RELEVANCE_LABELS:
        fields.extend([lr, f"{lr}_pct"])
    fields.extend(["redef_count", "redef_pct"])
    write_csv(OUT_DIR / "step_x_relevance.csv", fields, out, dry_run=dry_run)
    return counts, step_totals


def themes_by_step(rows: list[dict], *, dry_run: bool = False) -> set[str]:
    """Top 10 themes per pipeline step (split semicolons, count) (RQ1)."""
    step_themes = defaultdict(Counter)
    all_themes = set()
    for r in rows:
        ps = r["pipeline_step"]
        if r["themes"]:
            for theme in r["themes"].split("; "):
                theme = theme.strip()
                if theme:
                    step_themes[ps][theme] += 1
                    all_themes.add(theme)

    out = []
    for ps in PIPELINE_STEPS:
        for rank, (theme, count) in enumerate(step_themes[ps].most_common(10), 1):
            out.append({
                "pipeline_step": ps,
                "rank": rank,
                "theme": theme,
                "count": count,
            })
    write_csv(
        OUT_DIR / "themes_by_step.csv",
        ["pipeline_step", "rank", "theme", "count"],
        out,
        dry_run=dry_run,
    )
    return all_themes


def displaced_extracts(rows: list[dict], *, dry_run: bool = False) -> list[dict]:
    """All displaced rows with full context (RQ2 qualitative)."""
    displaced = [r for r in rows if r["llm_relevance"] == "displaced"]
    fields = [
        "source_id", "source_title", "author", "year", "pipeline_step",
        "extract_type", "themes", "extract", "relevance_rationale", "notes",
    ]
    write_csv(OUT_DIR / "displaced_extracts.csv", fields, displaced, dry_run=dry_run)
    return displaced


def source_coverage(rows: list[dict], *, dry_run: bool = False) -> defaultdict:
    """Which sources cover which steps, source count per step (RQ1)."""
    step_sources = defaultdict(set)
    source_info = {}
    for r in rows:
        ps = r["pipeline_step"]
        sid = r["source_id"]
        step_sources[ps].add(sid)
        if sid not in source_info:
            source_info[sid] = {
                "source_id": sid,
                "source_title": r["source_title"],
                "author": r["author"],
            }

    out = []
    for ps in PIPELINE_STEPS:
        out.append({
            "pipeline_step": ps,
            "source_count": len(step_sources[ps]),
            "source_ids": "; ".join(sorted(step_sources[ps], key=int)),
        })
    write_csv(
        OUT_DIR / "source_coverage.csv",
        ["pipeline_step", "source_count", "source_ids"],
        out,
        dry_run=dry_run,
    )
    return step_sources


def print_summary(rows: list[dict], primary_counts: Counter, type_rel: defaultdict, step_rel: defaultdict, step_totals: Counter, all_themes: set[str], displaced_rows: list[dict], step_sources: defaultdict) -> None:
    """Print summary stats to console."""
    total = len(rows)
    sources = len({r["source_id"] for r in rows})

    console.rule("[bold]T12 HORIZON TABLE ANALYSIS")
    console.print(f"  Total extracts: {total}")
    console.print(f"  Sources: {sources}")
    console.print(f"  Unique themes: {len(all_themes)}")
    console.print()

    # Step distribution (H1)
    t = Table(title="Step Distribution (H1)")
    t.add_column("Step")
    t.add_column("Count", justify="right")
    t.add_column("%", justify="right")
    for step in PIPELINE_STEPS:
        n = primary_counts.get(step, 0)
        t.add_row(step, str(n), f"{100*n/total:.1f}%")
    console.print(t)
    console.print()

    # Extract type × relevance (H2)
    t = Table(title="Extract Type × Relevance (H2)")
    t.add_column("Type")
    t.add_column("Total", justify="right")
    for lr in RELEVANCE_LABELS:
        t.add_column(lr, justify="right")
        t.add_column(f"% {lr}", justify="right")
    for et in EXTRACT_TYPES:
        et_total = sum(type_rel[et].values())
        row_data = [et, str(et_total)]
        for lr in RELEVANCE_LABELS:
            n = type_rel[et].get(lr, 0)
            row_data.extend([str(n), f"{100*n/et_total:.1f}%" if et_total else "0%"])
        t.add_row(*row_data)
    console.print(t)
    console.print()

    # Redefinition candidates (H3)
    t = Table(title="Redefinition Candidates (H3: >30% needs_update+displaced)")
    t.add_column("Step")
    t.add_column("Total", justify="right")
    t.add_column("Redef", justify="right")
    t.add_column("Redef %", justify="right")
    t.add_column("Flag")
    for step in PIPELINE_STEPS:
        st = step_totals.get(step, 0)
        redef = step_rel[step].get("needs_update", 0) + step_rel[step].get("displaced", 0)
        pct = 100 * redef / st if st else 0
        flag = "⚑ REDEFINE" if pct > 30 else ""
        t.add_row(step, str(st), str(redef), f"{pct:.1f}%", flag)
    console.print(t)
    console.print()

    # Overall relevance
    rel_totals = Counter(r["llm_relevance"] for r in rows)
    console.print("[bold]Overall relevance:")
    for lr in RELEVANCE_LABELS:
        n = rel_totals.get(lr, 0)
        console.print(f"  {lr}: {n} ({100*n/total:.1f}%)")

    # Source coverage per step
    console.print()
    console.print("[bold]Source coverage per step:")
    for step in PIPELINE_STEPS:
        console.print(f"  {step}: {len(step_sources.get(step, set()))} sources")


@app.command()
def main(
    dry_run: Annotated[bool, typer.Option("--dry-run", help="Show what would be written without writing files.")] = False,
    version: Annotated[bool | None, typer.Option("--version", callback=version_callback, is_eager=True, help="Show version.")] = None,
) -> None:
    if not HORIZON_CSV.exists():
        console.print(f"[red]horizon-table.csv not found: {HORIZON_CSV}")
        sys.exit(1)

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    console.rule("[bold]T12 ANALYSE HORIZON TABLE")

    rows = read_horizon()
    console.print(f"  Loaded {len(rows)} extracts from {HORIZON_CSV.relative_to(ROOT)}")
    console.print()

    # Generate all 6 CSVs
    primary_counts = step_distribution(rows, dry_run=dry_run)
    type_rel = type_x_relevance(rows, dry_run=dry_run)
    step_rel, step_totals = step_x_relevance(rows, dry_run=dry_run)
    all_themes = themes_by_step(rows, dry_run=dry_run)
    displaced_rows = displaced_extracts(rows, dry_run=dry_run)
    step_sources = source_coverage(rows, dry_run=dry_run)

    console.print()
    print_summary(rows, primary_counts, type_rel, step_rel, step_totals, all_themes, displaced_rows, step_sources)

    if not dry_run:
        log_action(Path(__file__).name, f"Generated 6 analysis CSVs from {len(rows)} extracts")


if __name__ == "__main__":
    app()
