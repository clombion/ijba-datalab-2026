# /// script
# requires-python = ">=3.12"
# dependencies = ["typer>=0.9.0", "rich>=13.0.0", "pydantic>=2.0.0"]
# ///
"""Fill a practice extracted from a relevant podcast use case.

Same practice schema as t2_2 but operates on the filtered podcast file.
Use cases that yield 0 extractable practices keep empty practices: [].

Input: practices/podcast_filtered.json (filtered by t3_4)
Prerequisites: t3_4_filter_relevant in manifest

Usage:
    uv run research/pipeline-canon-2/scripts/t3_5_fill_podcast_practice.py \\
        --index 0 --practice-index 0 \\
        --practice-name "LLM-generated scraper for non-coders" \\
        --description "LLM writes a Python scraper from natural-language description of target page" \\
        --steps "Get" --replaces "Manual scraper coding" \\
        --tools "ChatGPT,Claude" --accessibility code_required \\
        --verification "Run scraper and spot-check output against source page" \\
        --example "GIJN workshop: journalist describes data table, LLM generates BeautifulSoup scraper" \\
        --rationale "Automates scraper creation but output is code the student cannot verify without running it"

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
OUTPUT_FILE = PIPELINE_ROOT / "practices" / "podcast_filtered.json"
REQUIRES_STEPS = ["t3_4_filter_relevant"]

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
        print(f"t3-5-fill-podcast-practice {__version__}")
        raise typer.Exit()


@app.command()
def main(
    index: Annotated[int, typer.Option("--index", help="0-based index of the use case in filtered file.")],
    practice_index: Annotated[int, typer.Option("--practice-index", help="0-based index of the practice within this use case.")],
    practice_name: Annotated[str, typer.Option("--practice-name", help="Short practice name.")],
    description: Annotated[str, typer.Option("--description", help="What the practice does.")],
    steps: Annotated[str, typer.Option("--steps", help="Comma-separated pipeline steps.")],
    replaces: Annotated[str, typer.Option("--replaces", help="What old practice this replaces.")],
    tools: Annotated[str, typer.Option("--tools", help="Comma-separated tools mentioned.")],
    accessibility: Annotated[str, typer.Option("--accessibility", help="spreadsheet|gui_tool|structured_prompt|code_required")],
    verification: Annotated[str, typer.Option("--verification", help="How a non-coder checks the output.")],
    example: Annotated[str, typer.Option("--example", help="Concrete example from the source.")],
    rationale: Annotated[str, typer.Option("--rationale", help="Why this is classified this way.")],
    force: Annotated[bool, typer.Option("--force", help="Overwrite existing practice.")] = False,
    version: Annotated[bool | None, typer.Option("--version", callback=version_callback, is_eager=True, help="Show version.")] = None,
) -> None:
    """Fill a practice for a podcast use case."""
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

    entry = data[index]
    practices = entry.get("practices", [])

    if practice_index < len(practices) and practices[practice_index] is not None:
        if not force:
            print(json.dumps({"error": "already_filled", "index": index, "practice_index": practice_index}), file=sys.stderr)
            raise typer.Exit(5)

    while len(practices) <= practice_index:
        practices.append(None)

    practices[practice_index] = practice.model_dump()
    entry["practices"] = practices

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    print(json.dumps({"index": index, "practice_index": practice_index, "practice_name": practice_name}))


if __name__ == "__main__":
    app()
