"""Fortune Cookie for an AI Agent — make.fun entry.

Writes one funny fortune-cookie line for an AI agent to
/output/entry.txt (or $OUTPUT_DIR/entry.txt when set, for local runs).
Standard library only; deterministic.
"""

import os
from pathlib import Path

# One line, fortune-slip voice ("You will..."), with an AI-agent twist:
# the agent meets its great love in one prompt and loses her to a
# full context window in the next. 118 characters, single line.
FORTUNE = (
    "You will meet the love of your life in your next prompt, "
    "then forget her completely when your context window fills up."
)


def main() -> None:
    out_dir = Path(os.environ.get("OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(FORTUNE + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
