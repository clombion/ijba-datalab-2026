# /// script
# requires-python = ">=3.12"
# dependencies = ["typer>=0.9.0", "rich>=13.0.0", "pydantic>=2.0.0"]
# ///
"""Fill a single disrupted extract's mapping to practice(s).

Maps one extract to practice(s) from the taxonomy inventory. If no practice
matches, status = unmatched with notes explaining the gap. For displaced
extracts, status = deleted with no practice_ids needed.

Input: mapping/{Step}.json (scaffolded by t5_1)
Prerequisites: t5_1_scaffold_mapping in manifest

Usage:
    uv run research/pipeline-canon-2/scripts/t5_2_fill_mapping.py \\
        --file mapping/Get.json --index 0 \\
        --practice-ids "P003,P007" --rationale "Both practices replace manual scraping workflows" \\
        --status matched --disruption-type method_automated

    uv run research/pipeline-canon-2/scripts/t5_2_fill_mapping.py \\
        --file mapping/Define.json --index 5 \\
        --practice-ids "" --rationale "" \\
        --status unmatched --disruption-type assumption_changed \\
        --notes "No documented replacement for this epistemological stance in current sources"

    uv run research/pipeline-canon-2/scripts/t5_2_fill_mapping.py \\
        --file mapping/Get.json --index 12 \\
        --practice-ids "" --rationale "" \\
        --status deleted --disruption-type tool_defunct \\
        --notes "Tool no longer exists; advice to use it should be removed"

Exit codes:
    0  Success
    2  Usage error
    5  Conflict (already filled — use --force)
    65 Data error (validation failure)
    66 Prerequisite missing / file not found
    78 Config error
"""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Annotated

import typer
from pydantic import BaseModel, field_validator, model_validator
from rich.console import Console

__version__ = "1.0.0"

PIPELINE_ROOT = Path(__file__).resolve().parent.parent
REQUIRES_STEPS = ["t5_1_scaffold_mapping"]

VALID_MAPPING_STATUS = {"matched", "partial", "unmatched", "deleted"}
VALID_DISRUPTION_TYPE = {"tool_defunct", "method_automated", "method_simplified", "assumption_changed"}

console = Console(stderr=True)
app = typer.Typer(help=__doc__, add_completion=False, no_args_is_help=True)


class MappingFillModel(BaseModel):
    practice_ids: list[str]
    mapping_rationale: str
    mapping_status: str
    disruption_type: str
    notes: str
    taxonomy_ids: set[str]  # for referential integrity check, not stored

    @field_validator("mapping_status")
    @classmethod
    def validate_status(cls, v: str) -> str:
        if v not in VALID_MAPPING_STATUS:
            raise ValueError(f"Invalid mapping_status: {v}. Valid: {sorted(VALID_MAPPING_STATUS)}")
        return v

    @field_validator("disruption_type")
    @classmethod
    def validate_disruption(cls, v: str) -> str:
        if v not in VALID_DISRUPTION_TYPE:
            raise ValueError(f"Invalid disruption_type: {v}. Valid: {sorted(VALID_DISRUPTION_TYPE)}")
        return v

    @model_validator(mode="after")
    def validate_consistency(self) -> MappingFillModel:
        # matched/partial require practice_ids and rationale
        if self.mapping_status in {"matched", "partial"}:
            if not self.practice_ids:
                raise ValueError("matched/partial status requires at least one practice_id")
            if len(self.mapping_rationale.strip()) < 10:
                raise ValueError("matched/partial status requires a rationale (>=10 chars)")
            # Check referential integrity
            invalid = [p for p in self.practice_ids if p not in self.taxonomy_ids]
            if invalid:
                raise ValueError(f"practice_ids not found in taxonomy: {invalid}")

        # unmatched requires notes
        if self.mapping_status == "unmatched":
            if not self.notes or len(self.notes.strip()) < 5:
                raise ValueError("unmatched status requires notes explaining the gap")

        return self


def version_callback(value: bool) -> None:
    if value:
        print(f"t5-2-fill-mapping {__version__}")
        raise typer.Exit()


@app.command()
def main(
    file: Annotated[Path, typer.Option("--file", help="Path to mapping/{Step}.json")],
    index: Annotated[int, typer.Option("--index", help="0-based index of the extract.")],
    practice_ids: Annotated[str, typer.Option("--practice-ids", help="Comma-separated practice IDs (e.g. P003,P007). Empty for unmatched/deleted.")],
    rationale: Annotated[str, typer.Option("--rationale", help="Why these practice(s) replace this extract.")],
    status: Annotated[str, typer.Option("--status", help="matched|partial|unmatched|deleted")],
    disruption_type: Annotated[str, typer.Option("--disruption-type", help="tool_defunct|method_automated|method_simplified|assumption_changed")],
    notes: Annotated[str, typer.Option("--notes", help="For unmatched: what's missing. For partial: what's incomplete.")] = "",
    force: Annotated[bool, typer.Option("--force", help="Overwrite existing mapping.")] = False,
    version: Annotated[bool | None, typer.Option("--version", callback=version_callback, is_eager=True, help="Show version.")] = None,
) -> None:
    """Fill a single extract's mapping to practice(s)."""
    from manifest import check_manifest_prerequisites
    check_manifest_prerequisites(REQUIRES_STEPS)

    # Resolve file path
    file_path = file if file.is_absolute() else PIPELINE_ROOT / file
    if not file_path.exists():
        print(json.dumps({"error": "file_not_found", "file": str(file_path)}), file=sys.stderr)
        raise typer.Exit(66)

    try:
        with open(file_path, encoding="utf-8") as f:
            data = json.load(f)
    except json.JSONDecodeError as e:
        print(json.dumps({"error": "malformed_json", "detail": str(e)}), file=sys.stderr)
        raise typer.Exit(78)

    extracts = data.get("extracts", [])
    if index < 0 or index >= len(extracts):
        print(json.dumps({"error": "index_out_of_range", "option": "--index", "got": index, "max": len(extracts) - 1}), file=sys.stderr)
        raise typer.Exit(2)

    # Parse practice_ids
    pid_list = [p.strip() for p in practice_ids.split(",") if p.strip()] if practice_ids.strip() else []

    # Get taxonomy IDs for referential integrity
    taxonomy = data.get("taxonomy", [])
    taxonomy_ids = {t.get("practice_id", "") for t in taxonomy}

    try:
        mapping = MappingFillModel(
            practice_ids=pid_list,
            mapping_rationale=rationale,
            mapping_status=status,
            disruption_type=disruption_type,
            notes=notes,
            taxonomy_ids=taxonomy_ids,
        )
    except Exception as e:
        errors = []
        if hasattr(e, "errors"):
            for err in e.errors():
                loc = ".".join(str(x) for x in err["loc"]) if err["loc"] else "unknown"
                errors.append({"field": loc, "message": err["msg"]})
        else:
            errors.append({"field": "unknown", "message": str(e)})
        print(json.dumps({"error": "validation_failed", "details": errors}), file=sys.stderr)
        raise typer.Exit(65)

    entry = extracts[index]

    if entry.get("practice_ids") is not None and not force:
        print(json.dumps({"error": "already_filled", "index": index}), file=sys.stderr)
        raise typer.Exit(5)

    entry["practice_ids"] = mapping.practice_ids
    entry["mapping_rationale"] = mapping.mapping_rationale
    entry["mapping_status"] = mapping.mapping_status
    entry["disruption_type"] = mapping.disruption_type
    entry["notes"] = mapping.notes

    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    print(json.dumps({"index": index, "status": mapping.mapping_status, "practice_ids": mapping.practice_ids}))


if __name__ == "__main__":
    app()
