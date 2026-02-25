# /// script
# requires-python = ">=3.12"
# dependencies = []
# ///
"""Action log utility — append timestamped entries to action-log.md.

Both a CLI tool and an importable module.

CLI usage:
    uv run utils/log_action.py --script "chunk_corpus.py" --message "Chunked 81 sources into 142 chunks"

Module usage:
    from log_action import log_action
    log_action("chunk_corpus.py", "Chunked 81 sources into 142 chunks")
"""

import sys
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ACTION_LOG = ROOT / "research" / "pipeline-canon" / "action-log.md"


def log_action(script: str, message: str, tag: str = "live") -> None:
    """Append a timestamped entry to action-log.md."""
    ts = datetime.now().strftime("%Y-%m-%dT%H:%M")
    lines = message.strip().splitlines()
    body = "\n".join(f"- {l}" for l in lines)
    entry = f"\n## {ts} — {script} [{tag}]\n{body}\n"

    ACTION_LOG.parent.mkdir(parents=True, exist_ok=True)
    with open(ACTION_LOG, "a") as f:
        f.write(entry)


def main():
    script = None
    message = None
    tag = "live"
    if "--help" in sys.argv or "-h" in sys.argv:
        print(__doc__)
        sys.exit(0)

    args = sys.argv[1:]
    i = 0
    while i < len(args):
        if args[i] == "--script" and i + 1 < len(args):
            script = args[i + 1]
            i += 2
        elif args[i] == "--message" and i + 1 < len(args):
            message = args[i + 1]
            i += 2
        elif args[i] == "--tag" and i + 1 < len(args):
            tag = args[i + 1]
            i += 2
        else:
            print(f"Unknown argument: {args[i]}", file=sys.stderr)
            sys.exit(1)

    if not script or not message:
        print("Usage: uv run utils/log_action.py --script NAME --message MSG [--tag TAG]", file=sys.stderr)
        sys.exit(1)

    log_action(script, message, tag)
    print(f"Logged: {script} [{tag}]", file=sys.stderr)


if __name__ == "__main__":
    main()
