# /// script
# requires-python = ">=3.12"
# dependencies = ["typer>=0.9.0"]
# ///
"""Action log utility — append timestamped entries to action-log.md.

Both a CLI tool and an importable module.

CLI usage:
    uv run research/pipeline-canon-2/scripts/log_action.py --script "filter_disrupted.py" --message "Filtered 1,328 disrupted extracts"

Module usage:
    from log_action import log_action
    log_action("filter_disrupted.py", "Filtered 1,328 disrupted extracts")
"""

from __future__ import annotations

import sys
from datetime import datetime
from pathlib import Path
from typing import Annotated

__version__ = "1.0.0"

PIPELINE_ROOT = Path(__file__).resolve().parent.parent
ACTION_LOG = PIPELINE_ROOT / "action-log.md"


def log_action(script: str, message: str, tag: str = "live", ts: str | None = None) -> None:
    """Append a timestamped entry to action-log.md."""
    ts = ts or datetime.now().strftime("%Y-%m-%dT%H:%M")
    lines = message.strip().splitlines()
    body = "\n".join(f"- {line}" for line in lines)
    entry = f"\n## {ts} — {script} [{tag}]\n{body}\n"

    ACTION_LOG.parent.mkdir(parents=True, exist_ok=True)
    with open(ACTION_LOG, "a") as f:
        f.write(entry)


if __name__ == "__main__":
    import typer

    app = typer.Typer(help=__doc__, add_completion=False, no_args_is_help=True)

    def version_callback(value: bool) -> None:
        if value:
            print(f"log-action {__version__}")
            raise typer.Exit()

    @app.command()
    def main(
        script: Annotated[str, typer.Option("--script", help="Name of the calling script.")],
        message: Annotated[str, typer.Option("--message", help="Log message text.")],
        tag: Annotated[str, typer.Option("--tag", help="Log tag.")] = "live",
        version: Annotated[bool | None, typer.Option("--version", callback=version_callback, is_eager=True, help="Show version.")] = None,
    ) -> None:
        log_action(script, message, tag)
        print(f"Logged: {script} [{tag}]", file=sys.stderr)

    app()
