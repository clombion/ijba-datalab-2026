# /// script
# requires-python = ">=3.12"
# dependencies = []
# ///
"""CLI for LLM to score an extract for LLM-era relevance (T10).

Usage:
    uv run utils/analyse/t10_2_score_extract.py \
      --file relevance/07-ddj-handbook-1.json \
      --index 3 \
      --relevance endures \
      --rationale "Verification against original sources is fundamental journalism"
"""

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent
RELEVANCE_DIR = ROOT / "research" / "pipeline-canon" / "relevance"

VALID_RELEVANCE = {"endures", "displaced", "needs_update"}


def main():
    file_path = None
    index = None
    relevance = None
    rationale = None

    if "--help" in sys.argv or "-h" in sys.argv:
        print(__doc__)
        sys.exit(0)

    args = sys.argv[1:]
    i = 0
    while i < len(args):
        if args[i] == "--file" and i + 1 < len(args):
            file_path = args[i + 1]; i += 2
        elif args[i] == "--index" and i + 1 < len(args):
            index = int(args[i + 1]); i += 2
        elif args[i] == "--relevance" and i + 1 < len(args):
            relevance = args[i + 1]; i += 2
        elif args[i] == "--rationale" and i + 1 < len(args):
            rationale = args[i + 1]; i += 2
        else:
            print(f"Unknown argument: {args[i]}", file=sys.stderr)
            sys.exit(1)

    # Validate
    missing = []
    if not file_path: missing.append("--file")
    if index is None: missing.append("--index")
    if not relevance: missing.append("--relevance")
    if not rationale: missing.append("--rationale")
    if missing:
        print(f"Error: missing required arguments: {', '.join(missing)}", file=sys.stderr)
        sys.exit(1)

    if relevance not in VALID_RELEVANCE:
        print(f"Error: --relevance must be one of: {', '.join(sorted(VALID_RELEVANCE))}", file=sys.stderr)
        print(f"  Got: {relevance}", file=sys.stderr)
        sys.exit(1)

    # Resolve path
    p = Path(file_path)
    if not p.is_absolute():
        p = RELEVANCE_DIR / p.name if not p.exists() else p
    if not p.exists():
        p = RELEVANCE_DIR / Path(file_path).name
    if not p.exists():
        print(f"Error: file not found: {file_path}", file=sys.stderr)
        sys.exit(1)

    data = json.loads(p.read_text())
    extracts = data.get("extracts", [])

    if index < 0 or index >= len(extracts):
        print(f"Error: index {index} out of range (0-{len(extracts) - 1})", file=sys.stderr)
        sys.exit(1)

    extracts[index]["llm_relevance"] = relevance
    extracts[index]["relevance_rationale"] = rationale

    p.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Scored extract #{index} in {p.name}: {relevance}")


if __name__ == "__main__":
    main()
