# /// script
# requires-python = ">=3.12"
# dependencies = ["typer>=0.9.0"]
# ///
"""Pipeline manifest utility — append-only JSONL for chain integrity.

Each script calls append_manifest() after writing output files. The manifest
records what was produced, from what inputs, with sha256 hashes for integrity.

Module usage:
    from manifest import append_manifest, check_manifest_prerequisites
    append_manifest("t1_1_filter_disrupted", "disrupted.csv", ["research/pipeline-canon/horizon-table.csv"])
    check_manifest_prerequisites(["t1_1_filter_disrupted"])  # exits 66 if missing
"""

from __future__ import annotations

import hashlib
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

import typer

__version__ = "1.0.0"

PIPELINE_ROOT = Path(__file__).resolve().parent.parent
MANIFEST_PATH = PIPELINE_ROOT / "manifest.jsonl"


def _sha256(path: Path) -> str:
    """Compute sha256 hex digest of a file."""
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(8192), b""):
            h.update(chunk)
    return h.hexdigest()


def _read_manifest() -> list[dict]:
    """Read all manifest entries."""
    if not MANIFEST_PATH.exists():
        return []
    entries = []
    with open(MANIFEST_PATH, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line:
                entries.append(json.loads(line))
    return entries


def _find_parent_hash(entries: list[dict], file_key: str) -> str | None:
    """Find the most recent sha256 for a given file in the manifest."""
    for entry in reversed(entries):
        if entry.get("file") == file_key:
            return entry.get("sha256")
    return None


def append_manifest(
    step: str,
    output_path: str | Path,
    input_paths: list[str | Path] | None = None,
) -> dict:
    """Append a manifest entry after writing an output file.

    Args:
        step: Pipeline step identifier (e.g. "t1_1_filter_disrupted")
        output_path: Path to the output file (relative to PIPELINE_ROOT or absolute)
        input_paths: List of input file paths this output was derived from

    Returns:
        The manifest entry dict that was written.
    """
    output = Path(output_path)
    if not output.is_absolute():
        output = PIPELINE_ROOT / output

    file_key = str(Path(output_path))
    sha = _sha256(output)

    entries = _read_manifest()
    parent_hash = _find_parent_hash(entries, file_key)

    entry = {
        "step": step,
        "file": file_key,
        "sha256": sha,
        "parent_hash": parent_hash,
        "inputs": [str(p) for p in (input_paths or [])],
        "timestamp": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
    }

    MANIFEST_PATH.parent.mkdir(parents=True, exist_ok=True)
    with open(MANIFEST_PATH, "a", encoding="utf-8") as f:
        f.write(json.dumps(entry, ensure_ascii=False) + "\n")

    return entry


def check_manifest_prerequisites(required_steps: list[str]) -> None:
    """Check that all required pipeline steps have been run.

    Exits with code 66 if any prerequisite is missing from the manifest.
    """
    entries = _read_manifest()
    completed_steps = {e["step"] for e in entries}

    missing = [s for s in required_steps if s not in completed_steps]
    if missing:
        for step in missing:
            print(
                json.dumps({"error": "prerequisite_missing", "step": step}),
                file=sys.stderr,
            )
        print(
            f"prerequisite {missing[0]} not found in manifest — run it first",
            file=sys.stderr,
        )
        raise typer.Exit(66)
