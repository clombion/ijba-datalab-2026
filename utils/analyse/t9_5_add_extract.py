# /// script
# requires-python = ">=3.12"
# dependencies = []
# ///
"""CLI for LLM to add an extract to an extraction JSON file.

The LLM passes plain text arguments; this script handles all JSON assembly
and enum validation.

Usage:
    uv run utils/analyse/t9_5_add_extract.py \
      --file extractions/07-ddj-handbook-1_chunk2.json \
      --extract "Always verify your data against the original source" \
      --chapter "Getting Data from the Web" \
      --step Verify \
      --secondary-step null \
      --type epistemological \
      --themes "verification, data quality" \
      --notes ""
"""

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent
EXTRACTIONS_DIR = ROOT / "research" / "pipeline-canon" / "extractions"

VALID_STEPS = {"Define", "Find", "Get", "Verify", "Clean", "Analyse", "Present"}
VALID_TYPES = {"procedural", "epistemological", "organizational", "tool-specific"}


def main():
    file_path = None
    extract = None
    chapter = None
    step = None
    secondary_step = None
    extract_type = None
    themes = None
    notes = None

    if "--help" in sys.argv or "-h" in sys.argv:
        print(__doc__)
        sys.exit(0)

    args = sys.argv[1:]
    i = 0
    while i < len(args):
        if args[i] == "--file" and i + 1 < len(args):
            file_path = args[i + 1]; i += 2
        elif args[i] == "--extract" and i + 1 < len(args):
            extract = args[i + 1]; i += 2
        elif args[i] == "--chapter" and i + 1 < len(args):
            chapter = args[i + 1]; i += 2
        elif args[i] == "--step" and i + 1 < len(args):
            step = args[i + 1]; i += 2
        elif args[i] == "--secondary-step" and i + 1 < len(args):
            secondary_step = args[i + 1]; i += 2
        elif args[i] == "--type" and i + 1 < len(args):
            extract_type = args[i + 1]; i += 2
        elif args[i] == "--themes" and i + 1 < len(args):
            themes = args[i + 1]; i += 2
        elif args[i] == "--notes" and i + 1 < len(args):
            notes = args[i + 1]; i += 2
        else:
            print(f"Unknown argument: {args[i]}", file=sys.stderr)
            sys.exit(1)

    # Validate required
    missing = []
    if not file_path: missing.append("--file")
    if not extract: missing.append("--extract")
    if not chapter: missing.append("--chapter")
    if not step: missing.append("--step")
    if not extract_type: missing.append("--type")
    if missing:
        print(f"Error: missing required arguments: {', '.join(missing)}", file=sys.stderr)
        print("Required: --file --extract --chapter --step --type", file=sys.stderr)
        sys.exit(1)

    # Validate enums
    if step not in VALID_STEPS:
        print(f"Error: --step must be one of: {', '.join(sorted(VALID_STEPS))}", file=sys.stderr)
        print(f"  Got: {step}", file=sys.stderr)
        sys.exit(1)

    if extract_type not in VALID_TYPES:
        print(f"Error: --type must be one of: {', '.join(sorted(VALID_TYPES))}", file=sys.stderr)
        print(f"  Got: {extract_type}", file=sys.stderr)
        sys.exit(1)

    if secondary_step and secondary_step != "null" and secondary_step not in VALID_STEPS:
        print(f"Error: --secondary-step must be null or one of: {', '.join(sorted(VALID_STEPS))}", file=sys.stderr)
        sys.exit(1)

    # Resolve file path
    p = Path(file_path)
    if not p.is_absolute():
        p = EXTRACTIONS_DIR / p.name if not p.exists() else p
    if not p.exists():
        p = EXTRACTIONS_DIR / Path(file_path).name
    if not p.exists():
        print(f"Error: file not found: {file_path}", file=sys.stderr)
        sys.exit(1)

    # Parse themes
    theme_list = [t.strip() for t in (themes or "").split(",") if t.strip()]

    # Normalize secondary_step
    sec_step = None if (not secondary_step or secondary_step == "null") else secondary_step

    # Read, append, write
    data = json.loads(p.read_text())
    extract_obj = {
        "extract": extract,
        "chapter": chapter,
        "pipeline_step": step,
        "secondary_step": sec_step,
        "extract_type": extract_type,
        "themes": theme_list,
        "notes": notes or "",
    }
    data["extracts"].append(extract_obj)
    p.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")

    n = len(data["extracts"])
    print(f"Added extract #{n} to {p.name} (step={step}, type={extract_type})")


if __name__ == "__main__":
    main()
