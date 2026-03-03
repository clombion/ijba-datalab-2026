# /// script
# requires-python = ">=3.12"
# dependencies = ["typer>=0.9.0", "rich>=13.0.0"]
# ///
"""Validate pipeline manifest integrity.

Checks:
- Complete hash chain per file (parent_hash matches previous entry's sha256)
- Current file hash matches latest manifest entry
- Reports files without manifest entries (no provenance)

Usage:
    uv run research/pipeline-canon-2/scripts/t0_validate_manifest.py
    uv run research/pipeline-canon-2/scripts/t0_validate_manifest.py --json

Exit codes:
    0  PASS — manifest is consistent
    1  FAIL — integrity errors found
    66 No manifest file found
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Annotated

import typer
from rich.console import Console

__version__ = "1.0.0"

PIPELINE_ROOT = Path(__file__).resolve().parent.parent
MANIFEST_PATH = PIPELINE_ROOT / "manifest.jsonl"

console = Console(stderr=True)
app = typer.Typer(help=__doc__, add_completion=False)


def _sha256(path: Path) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(8192), b""):
            h.update(chunk)
    return h.hexdigest()


def version_callback(value: bool) -> None:
    if value:
        print(f"t0-validate-manifest {__version__}")
        raise typer.Exit()


@app.command()
def main(
    json_output: Annotated[bool, typer.Option("--json", help="Machine-readable JSON output.")] = False,
    version: Annotated[bool | None, typer.Option("--version", callback=version_callback, is_eager=True, help="Show version.")] = None,
) -> None:
    """Validate manifest.jsonl integrity."""
    if not MANIFEST_PATH.exists():
        if json_output:
            print(json.dumps({"status": "error", "message": "manifest.jsonl not found"}))
        else:
            console.print("[red]manifest.jsonl not found[/red]")
        raise typer.Exit(66)

    entries: list[dict] = []
    with open(MANIFEST_PATH, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line:
                entries.append(json.loads(line))

    errors: list[dict] = []
    warnings: list[dict] = []

    # Group entries by file for chain validation
    by_file: dict[str, list[dict]] = {}
    for entry in entries:
        by_file.setdefault(entry["file"], []).append(entry)

    # Validate hash chains
    for file_key, file_entries in by_file.items():
        for i, entry in enumerate(file_entries):
            if i == 0:
                if entry.get("parent_hash") is not None:
                    errors.append({
                        "type": "chain_error",
                        "file": file_key,
                        "message": f"First entry has non-null parent_hash: {entry['parent_hash']}",
                    })
            else:
                expected_parent = file_entries[i - 1]["sha256"]
                if entry.get("parent_hash") != expected_parent:
                    errors.append({
                        "type": "chain_error",
                        "file": file_key,
                        "message": f"parent_hash mismatch at entry {i}: expected {expected_parent[:12]}..., got {(entry.get('parent_hash') or 'null')[:12]}...",
                    })

        # Check current file hash matches latest entry
        latest = file_entries[-1]
        file_path = PIPELINE_ROOT / latest["file"]
        if file_path.exists():
            current_hash = _sha256(file_path)
            if current_hash != latest["sha256"]:
                errors.append({
                    "type": "hash_mismatch",
                    "file": file_key,
                    "message": f"Current file hash {current_hash[:12]}... != manifest {latest['sha256'][:12]}...",
                })
        else:
            warnings.append({
                "type": "file_missing",
                "file": file_key,
                "message": "File referenced in manifest does not exist",
            })

    # Summary
    steps_seen = sorted({e["step"] for e in entries})
    result = {
        "status": "PASS" if not errors else "FAIL",
        "entries": len(entries),
        "files": len(by_file),
        "steps": steps_seen,
        "errors": errors,
        "warnings": warnings,
    }

    if json_output:
        print(json.dumps(result, indent=2))
    else:
        console.print(f"Manifest: {len(entries)} entries, {len(by_file)} files, {len(steps_seen)} steps")
        for step in steps_seen:
            console.print(f"  {step}")
        if errors:
            console.print(f"\n[red]{len(errors)} error(s):[/red]")
            for e in errors:
                console.print(f"  [{e['type']}] {e['file']}: {e['message']}")
        if warnings:
            console.print(f"\n[yellow]{len(warnings)} warning(s):[/yellow]")
            for w in warnings:
                console.print(f"  [{w['type']}] {w['file']}: {w['message']}")
        if not errors:
            console.print("\n[green]PASS[/green]")
        else:
            console.print("\n[red]FAIL[/red]")

    raise typer.Exit(1 if errors else 0)


if __name__ == "__main__":
    app()
