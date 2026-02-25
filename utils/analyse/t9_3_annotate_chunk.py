# /// script
# requires-python = ">=3.12"
# dependencies = []
# ///
"""CLI for LLM Pass 0 — write section labels into chunk metadata header.

Usage:
    uv run utils/annotate_chunk.py \
      --file chunks/82-periodismo-datos_chunk2.md \
      --sections "Research methodology; Survey design and sampling"
"""

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent
CHUNKS_DIR = ROOT / "research" / "pipeline-canon" / "chunks"


def main():
    file_path = None
    sections = None
    args = sys.argv[1:]
    i = 0
    while i < len(args):
        if args[i] == "--file" and i + 1 < len(args):
            file_path = args[i + 1]
            i += 2
        elif args[i] == "--sections" and i + 1 < len(args):
            sections = args[i + 1]
            i += 2
        else:
            i += 1

    if not file_path or not sections:
        print("Usage: uv run utils/annotate_chunk.py --file PATH --sections TEXT")
        sys.exit(1)

    # Resolve path (could be relative or absolute)
    p = Path(file_path)
    if not p.is_absolute():
        p = CHUNKS_DIR / p.name if not p.exists() else p
    if not p.exists():
        p = CHUNKS_DIR / Path(file_path).name
    if not p.exists():
        print(f"Error: file not found: {file_path}")
        sys.exit(1)

    text = p.read_text()
    sections_line = f"<!-- sections: {sections} -->\n"

    # Insert after existing metadata comments
    lines = text.splitlines(keepends=True)
    insert_idx = 0
    for idx, line in enumerate(lines):
        if line.startswith("<!--") and "-->" in line:
            # Remove existing sections line if present
            if line.startswith("<!-- sections:"):
                lines[idx] = sections_line
                insert_idx = -1  # flag: already replaced
                break
            insert_idx = idx + 1
        else:
            break

    if insert_idx >= 0:
        lines.insert(insert_idx, sections_line)

    p.write_text("".join(lines))
    print(f"Annotated {p.name}: {sections}")


if __name__ == "__main__":
    main()
