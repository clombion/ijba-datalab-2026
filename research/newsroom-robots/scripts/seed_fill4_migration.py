#!/usr/bin/env python3
"""One-time migration: seed fill-4 entries for 34 already-validated files.

The 8 re-run files (banished + re-scaffolded on Feb 28) are skipped — they
have broken provenance chains and need a clean scaffold→fill→validate cycle.

Run from research/newsroom-robots/:
    python3 scripts/seed_fill4_migration.py

After seeding, run validate to confirm:
    uv run ta.py validate --pass 4 --dir outputs/episode_recodes/ --fix \
        --check-scaffold --manifest outputs/manifest.csv --codebook outputs/codebook.json
"""

import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path

OUTPUTS_DIR = Path("outputs")
MANIFEST_PATH = OUTPUTS_DIR / ".pipeline-manifest.jsonl"
RECODE_DIR = OUTPUTS_DIR / "episode_recodes"

# 8 files with broken provenance from the Feb 28 re-run
RERUN_FILES = {
    "2024-05-26-adrian-gill-ai-image-generation.json",
    "2025-07-09-nordic-summit-hard-truths.json",
    "2025-07-15-florent-daudens-open-source-ai.json",
    "2025-08-14-sara-beykpour-news-aggregation.json",
    "2025-09-08-djordje-padejski-ai-literacy-education.json",
    "2025-09-08-ivar-krustok-estonia-delfi.json",
    "2025-09-23-ludwig-siegele-economist-ai.json",
    "2025-10-08-vilas-dhar-future-journalism-human.json",
}


def file_sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> None:
    if not MANIFEST_PATH.exists():
        raise SystemExit(f"ERROR: {MANIFEST_PATH} not found")
    if not RECODE_DIR.is_dir():
        raise SystemExit(f"ERROR: {RECODE_DIR} not found")

    # Index latest validate-4 per file from manifest
    validate_entries: dict[str, dict] = {}
    for line in MANIFEST_PATH.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line:
            continue
        record = json.loads(line)
        if record.get("step") == "validate-4":
            validate_entries[record["file"]] = record

    # Process each recode file
    seeded = 0
    skipped_rerun = 0
    skipped_mismatch = 0
    skipped_no_entry = 0

    json_files = sorted(RECODE_DIR.glob("*.json"))
    for f in json_files:
        if f.name in RERUN_FILES:
            skipped_rerun += 1
            continue

        rel_path = f"episode_recodes/{f.name}"
        entry = validate_entries.get(rel_path)
        if not entry:
            print(f"  SKIP {f.name}: no validate-4 entry")
            skipped_no_entry += 1
            continue

        current_hash = file_sha256(f)
        manifest_hash = entry.get("sha256", "")
        if current_hash != manifest_hash:
            print(f"  SKIP {f.name}: hash mismatch (file modified since validate-4)")
            skipped_mismatch += 1
            continue

        # Write fill-4 migration entry
        record = {
            "step": "fill-4",
            "file": rel_path,
            "sha256": current_hash,
            "parent": current_hash,
            "migration": True,
            "ts": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        }
        with MANIFEST_PATH.open("a", encoding="utf-8") as mf:
            mf.write(json.dumps(record, ensure_ascii=False) + "\n")
        seeded += 1

    print(f"\nSeeded {seeded} fill-4 migration entries")
    print(f"Skipped: {skipped_rerun} re-run, {skipped_mismatch} hash mismatch, {skipped_no_entry} no entry")
    print(f"Total recode files: {len(json_files)}")


if __name__ == "__main__":
    main()
