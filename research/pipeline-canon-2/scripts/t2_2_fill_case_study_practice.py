# /// script
# requires-python = ">=3.12"
# dependencies = ["typer>=0.9.0", "rich>=13.0.0", "pydantic>=2.0.0"]
# ///
"""Fill a single practice into a case study entry.

Adds or updates one practice at a given (source-index, practice-index) position
in practices/case_studies.json. The LLM reads the case study source material
and calls this CLI to record each extracted practice.

Input: practices/case_studies.json (scaffolded by t2_1)
Prerequisites: t2_1_scaffold_case_studies in manifest

Usage:
    uv run research/pipeline-canon-2/scripts/t2_2_fill_case_study_practice.py \\
        --source-index 0 --practice-index 0 \\
        --practice-name "PDF-to-CSV via prompted extraction" \\
        --description "Use LLM prompts to extract structured data from PDF election results" \\
        --steps "Get,Clean" --replaces "Manual PDF transcription" \\
        --tools "ChatGPT,Claude" --accessibility structured_prompt \\
        --verification "Spot-check 10% of rows against source PDF" \\
        --example "OpenElections used GPT-4 to parse Florida county PDF results into CSV" \\
        --rationale "Replaces manual data entry with prompted extraction, verifiable by spreadsheet comparison"

    uv run research/pipeline-canon-2/scripts/t2_2_fill_case_study_practice.py \\
        --source-index 0 --practice-index 0 --force \\
        --practice-name "Updated name" ...

Exit codes:
    0  Success
    2  Usage error (missing/invalid args)
    5  Conflict (practice already filled — use --force)
    65 Data error (validation failure)
    66 Prerequisite missing
    78 Config error (malformed JSON)
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
OUTPUT_FILE = PIPELINE_ROOT / "practices" / "case_studies.json"
REQUIRES_STEPS = ["t2_1_scaffold_case_studies"]

VALID_STEPS = {"Define", "Find", "Get", "Verify", "Clean", "Analyse", "Present"}
VALID_ACCESSIBILITY = {"spreadsheet", "gui_tool", "structured_prompt", "code_required"}

console = Console(stderr=True)
app = typer.Typer(help=__doc__, add_completion=False, no_args_is_help=True)


class PracticeModel(BaseModel):
    practice_name: str
    description: str
    pipeline_steps: list[str]
    replaces_category: str
    tools_mentioned: list[str]
    accessibility_level: str
    verification_method: str
    example: str
    practice_rationale: str

    @field_validator("pipeline_steps")
    @classmethod
    def validate_steps(cls, v: list[str]) -> list[str]:
        for step in v:
            if step not in VALID_STEPS:
                raise ValueError(f"Invalid pipeline step: {step}. Valid: {sorted(VALID_STEPS)}")
        if not v:
            raise ValueError("At least one pipeline step required")
        return v

    @field_validator("accessibility_level")
    @classmethod
    def validate_accessibility(cls, v: str) -> str:
        if v not in VALID_ACCESSIBILITY:
            raise ValueError(f"Invalid accessibility_level: {v}. Valid: {sorted(VALID_ACCESSIBILITY)}")
        return v

    @field_validator("practice_rationale")
    @classmethod
    def validate_rationale(cls, v: str) -> str:
        if len(v.strip()) < 10:
            raise ValueError("Rationale must be at least 10 characters")
        return v


def version_callback(value: bool) -> None:
    if value:
        print(f"t2-2-fill-case-study-practice {__version__}")
        raise typer.Exit()


@app.command()
def main(
    source_index: Annotated[int, typer.Option("--source-index", help="0-based index of the case study.")],
    practice_index: Annotated[int, typer.Option("--practice-index", help="0-based index of the practice within the source.")],
    practice_name: Annotated[str, typer.Option("--practice-name", help="Short practice name.")],
    description: Annotated[str, typer.Option("--description", help="What the practice does.")],
    steps: Annotated[str, typer.Option("--steps", help="Comma-separated pipeline steps (e.g. Get,Clean).")],
    replaces: Annotated[str, typer.Option("--replaces", help="What old practice category this replaces.")],
    tools: Annotated[str, typer.Option("--tools", help="Comma-separated tools mentioned.")],
    accessibility: Annotated[str, typer.Option("--accessibility", help="spreadsheet|gui_tool|structured_prompt|code_required")],
    verification: Annotated[str, typer.Option("--verification", help="How a non-coder checks the output.")],
    example: Annotated[str, typer.Option("--example", help="Concrete example from the source.")],
    rationale: Annotated[str, typer.Option("--rationale", help="Why this is classified this way.")],
    force: Annotated[bool, typer.Option("--force", help="Overwrite existing practice at this index.")] = False,
    version: Annotated[bool | None, typer.Option("--version", callback=version_callback, is_eager=True, help="Show version.")] = None,
) -> None:
    """Fill a single practice for a case study."""
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

    if source_index < 0 or source_index >= len(data):
        print(json.dumps({"error": "index_out_of_range", "option": "--source-index", "got": source_index, "max": len(data) - 1}), file=sys.stderr)
        raise typer.Exit(2)

    # Validate via Pydantic
    step_list = [s.strip() for s in steps.split(",") if s.strip()]
    tool_list = [t.strip() for t in tools.split(",") if t.strip()]

    try:
        practice = PracticeModel(
            practice_name=practice_name,
            description=description,
            pipeline_steps=step_list,
            replaces_category=replaces,
            tools_mentioned=tool_list,
            accessibility_level=accessibility,
            verification_method=verification,
            example=example,
            practice_rationale=rationale,
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

    entry = data[source_index]
    practices = entry.get("practices", [])

    # Check for existing practice at this index
    if practice_index < len(practices) and practices[practice_index] is not None:
        existing = practices[practice_index]
        if existing and not force:
            print(json.dumps({"error": "already_filled", "source_index": source_index, "practice_index": practice_index}), file=sys.stderr)
            raise typer.Exit(5)

    # Extend practices list if needed
    while len(practices) <= practice_index:
        practices.append(None)

    practices[practice_index] = practice.model_dump()
    entry["practices"] = practices

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    result = {
        "source_index": source_index,
        "practice_index": practice_index,
        "practice_name": practice_name,
        "source_id": entry.get("source_id", ""),
    }
    print(json.dumps(result))


if __name__ == "__main__":
    app()
