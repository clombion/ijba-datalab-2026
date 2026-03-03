# /// script
# requires-python = ">=3.12"
# dependencies = ["typer>=0.9.0", "rich>=13.0.0", "pydantic>=2.0.0"]
# ///
"""Fill pipeline step mapping for a single podcast use case.

Maps a use case to pipeline step(s), classifies granularity, and determines
relevance to practitioner-level disrupted advice.

Input: practices/podcast_mapped.json (scaffolded by t3_1)
Prerequisites: t3_1_scaffold_podcast_mapping in manifest

Usage:
    uv run research/pipeline-canon-2/scripts/t3_2_fill_podcast_mapping.py \\
        --index 0 --steps "Get,Clean" --granularity practitioner \\
        --relevant true --rationale "Describes a specific data extraction workflow using LLM prompts"

    uv run research/pipeline-canon-2/scripts/t3_2_fill_podcast_mapping.py \\
        --index 5 --steps "Define" --granularity organizational \\
        --relevant false --rationale "Describes org-level AI strategy, not practitioner workflow"

Exit codes:
    0  Success
    2  Usage error
    5  Conflict (already filled — use --force)
    65 Data error (validation failure)
    66 Prerequisite missing
    78 Config error
"""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Annotated

import typer
from pydantic import BaseModel, field_validator
from rich.console import Console

__version__ = "1.0.0"

PIPELINE_ROOT = Path(__file__).resolve().parent.parent
OUTPUT_FILE = PIPELINE_ROOT / "practices" / "podcast_mapped.json"
REQUIRES_STEPS = ["t3_1_scaffold_podcast_mapping"]

VALID_STEPS = {"Define", "Find", "Get", "Verify", "Clean", "Analyse", "Present"}
VALID_GRANULARITY = {"practitioner", "organizational", "strategic"}

console = Console(stderr=True)
app = typer.Typer(help=__doc__, add_completion=False, no_args_is_help=True)


class MappingModel(BaseModel):
    pipeline_steps: list[str]
    granularity: str
    relevant: bool
    mapping_rationale: str

    @field_validator("pipeline_steps")
    @classmethod
    def validate_steps(cls, v: list[str]) -> list[str]:
        for step in v:
            if step not in VALID_STEPS:
                raise ValueError(f"Invalid pipeline step: {step}. Valid: {sorted(VALID_STEPS)}")
        if not v:
            raise ValueError("At least one pipeline step required")
        return v

    @field_validator("granularity")
    @classmethod
    def validate_granularity(cls, v: str) -> str:
        if v not in VALID_GRANULARITY:
            raise ValueError(f"Invalid granularity: {v}. Valid: {sorted(VALID_GRANULARITY)}")
        return v

    @field_validator("mapping_rationale")
    @classmethod
    def validate_rationale(cls, v: str) -> str:
        if len(v.strip()) < 10:
            raise ValueError("Rationale must be at least 10 characters")
        return v


def version_callback(value: bool) -> None:
    if value:
        print(f"t3-2-fill-podcast-mapping {__version__}")
        raise typer.Exit()


@app.command()
def main(
    index: Annotated[int, typer.Option("--index", help="0-based index of the use case.")],
    steps: Annotated[str, typer.Option("--steps", help="Comma-separated pipeline steps.")],
    granularity: Annotated[str, typer.Option("--granularity", help="practitioner|organizational|strategic")],
    relevant: Annotated[bool, typer.Option("--relevant/--not-relevant", help="Relevant to practitioner-level disrupted advice?")],
    rationale: Annotated[str, typer.Option("--rationale", help="Why this mapping was chosen.")],
    force: Annotated[bool, typer.Option("--force", help="Overwrite existing mapping.")] = False,
    version: Annotated[bool | None, typer.Option("--version", callback=version_callback, is_eager=True, help="Show version.")] = None,
) -> None:
    """Fill pipeline step mapping for a podcast use case."""
    from manifest import check_manifest_prerequisites
    check_manifest_prerequisites(REQUIRES_STEPS)

    if not OUTPUT_FILE.exists():
        print(json.dumps({"error": "file_not_found", "file": str(OUTPUT_FILE)}), file=sys.stderr)
        raise typer.Exit(66)

    try:
        with open(OUTPUT_FILE, encoding="utf-8") as f:
            data = json.load(f)
    except json.JSONDecodeError as e:
        print(json.dumps({"error": "malformed_json", "detail": str(e)}), file=sys.stderr)
        raise typer.Exit(78)

    if index < 0 or index >= len(data):
        print(json.dumps({"error": "index_out_of_range", "option": "--index", "got": index, "max": len(data) - 1}), file=sys.stderr)
        raise typer.Exit(2)

    step_list = [s.strip() for s in steps.split(",") if s.strip()]

    try:
        mapping = MappingModel(
            pipeline_steps=step_list,
            granularity=granularity,
            relevant=relevant,
            mapping_rationale=rationale,
        )
    except Exception as e:
        errors = []
        if hasattr(e, "errors"):
            for err in e.errors():
                field = err["loc"][-1] if err["loc"] else "unknown"
                errors.append({"field": field, "message": err["msg"]})
        else:
            errors.append({"field": "unknown", "message": str(e)})
        print(json.dumps({"error": "validation_failed", "details": errors}), file=sys.stderr)
        raise typer.Exit(65)

    entry = data[index]

    if entry.get("pipeline_steps") is not None and not force:
        print(json.dumps({"error": "already_filled", "index": index}), file=sys.stderr)
        raise typer.Exit(5)

    entry["pipeline_steps"] = mapping.pipeline_steps
    entry["granularity"] = mapping.granularity
    entry["relevant"] = mapping.relevant
    entry["mapping_rationale"] = mapping.mapping_rationale

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    print(json.dumps({"index": index, "steps": mapping.pipeline_steps, "granularity": mapping.granularity, "relevant": mapping.relevant}))


if __name__ == "__main__":
    app()
