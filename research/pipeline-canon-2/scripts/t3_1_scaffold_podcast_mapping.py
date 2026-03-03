# /// script
# requires-python = ">=3.12"
# dependencies = ["typer>=0.9.0", "rich>=13.0.0"]
# ///
"""Scaffold podcast use case mapping file.

Reads all episode extraction JSONs from the newsroom-robots corpus, collects
use cases, and scaffolds each with null fields for pipeline step mapping.

Input: research/newsroom-robots/outputs/episode_extractions/*.json
Output: practices/podcast_mapped.json

Usage:
    uv run research/pipeline-canon-2/scripts/t3_1_scaffold_podcast_mapping.py
    uv run research/pipeline-canon-2/scripts/t3_1_scaffold_podcast_mapping.py --dry-run
    uv run research/pipeline-canon-2/scripts/t3_1_scaffold_podcast_mapping.py --status

Exit codes:
    0  Success
    1  General error
    5  Output already exists (use --force)
    66 Input directory not found
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Annotated

import typer
from rich.console import Console

__version__ = "1.0.0"

PIPELINE_ROOT = Path(__file__).resolve().parent.parent
REPO_ROOT = PIPELINE_ROOT.parent.parent
EXTRACTIONS_DIR = REPO_ROOT / "research" / "newsroom-robots" / "outputs" / "episode_extractions"
OUTPUT_FILE = PIPELINE_ROOT / "practices" / "podcast_mapped.json"

console = Console(stderr=True)
app = typer.Typer(help=__doc__, add_completion=False)


def version_callback(value: bool) -> None:
    if value:
        print(f"t3-1-scaffold-podcast-mapping {__version__}")
        raise typer.Exit()


@app.command()
def main(
    dry_run: Annotated[bool, typer.Option("--dry-run", help="Show counts without writing.")] = False,
    status: Annotated[bool, typer.Option("--status", help="Report fill progress.")] = False,
    force: Annotated[bool, typer.Option("--force", help="Overwrite existing output.")] = False,
    version: Annotated[bool | None, typer.Option("--version", callback=version_callback, is_eager=True, help="Show version.")] = None,
) -> None:
    """Scaffold podcast use case mapping file."""
    if status:
        if not OUTPUT_FILE.exists():
            print(json.dumps({"scaffolded": False}))
            raise typer.Exit(0)
        with open(OUTPUT_FILE, encoding="utf-8") as f:
            data = json.load(f)
        total = len(data)
        filled = sum(1 for uc in data if uc.get("pipeline_steps") is not None)
        print(json.dumps({"total": total, "filled": filled, "remaining": total - filled}))
        raise typer.Exit(0)

    if not EXTRACTIONS_DIR.exists():
        console.print(f"[red]Input directory not found: {EXTRACTIONS_DIR}[/red]")
        raise typer.Exit(66)

    if OUTPUT_FILE.exists() and not force:
        console.print(f"[yellow]Output already exists: {OUTPUT_FILE}[/yellow]")
        raise typer.Exit(5)

    # Collect all use cases from all episodes
    use_cases = []
    json_files = sorted(EXTRACTIONS_DIR.glob("*.json"))

    for json_file in json_files:
        with open(json_file, encoding="utf-8") as f:
            episode = json.load(f)

        episode_name = json_file.stem
        episode_meta = episode.get("episode_meta", {})
        episode_title = episode_meta.get("title", episode_name)

        for uc in episode.get("use_cases", []):
            use_cases.append({
                "index": len(use_cases),
                "episode": episode_name,
                "episode_title": episode_title,
                "description": uc.get("description", ""),
                "tool_used": uc.get("tool_used", ""),
                "organization": uc.get("organization", ""),
                "outcome": uc.get("outcome", ""),
                "stage": uc.get("stage", ""),
                # Null fields for LLM to fill
                "pipeline_steps": None,
                "granularity": None,
                "relevant": None,
                "mapping_rationale": None,
            })

    console.print(f"Episodes: {len(json_files)}")
    console.print(f"Use cases: {len(use_cases)}")

    # Stage distribution
    stages: dict[str, int] = {}
    for uc in use_cases:
        s = uc["stage"] or "unknown"
        stages[s] = stages.get(s, 0) + 1
    for s, count in sorted(stages.items()):
        console.print(f"  {s}: {count}")

    if dry_run:
        console.print("[yellow]Dry run — no file written.[/yellow]")
        print(json.dumps({"episodes": len(json_files), "use_cases": len(use_cases), "stages": stages}))
        raise typer.Exit(0)

    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(use_cases, f, indent=2, ensure_ascii=False)

    console.print(f"[green]Written: {OUTPUT_FILE}[/green]")

    from log_action import log_action
    from manifest import append_manifest

    input_paths = [str(p.relative_to(REPO_ROOT)) for p in json_files]
    append_manifest("t3_1_scaffold_podcast_mapping", "practices/podcast_mapped.json", input_paths)
    log_action("t3_1_scaffold_podcast_mapping.py", f"Scaffolded {len(use_cases)} use cases from {len(json_files)} episodes")

    print(json.dumps({"episodes": len(json_files), "use_cases": len(use_cases)}))


if __name__ == "__main__":
    app()
