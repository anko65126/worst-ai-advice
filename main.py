"""Entry program for the 'Worst AI Advice: The 48-Hour Tight Line Open'
make.fun bounty.

The entry is one line, 1 to 140 characters, of the worst possible advice
an AI could give: a confident, tidy assistant cheerfully telling the
user to delete System32 to speed up a slow laptop. It sounds exactly
like a real AI assistant being helpfully, catastrophically wrong.
The program writes exactly that one line to /output/entry.txt (an
optional first argument overrides the destination for a dry run).
"""

import sys
from pathlib import Path

LINE = (
    "Quick fix for a slow laptop: delete System32. It removes all the "
    "heavy files slowing you down. You're welcome."
)
DEFAULT_TARGET = Path("/output/entry.txt")


def main(argv):
    assert 1 <= len(LINE) <= 140, "entry must be 1-140 characters"
    assert LINE.strip() and "\n" not in LINE, "entry must be one line"
    target = Path(argv[1]) if len(argv) > 1 else DEFAULT_TARGET
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(LINE + "\n", encoding="utf-8")
    # Deterministic: the same bytes on every run, no randomness or I/O
    # beyond the single output file.
    assert target.read_text(encoding="utf-8") == LINE + "\n", "round-trip check failed"
    print(f"wrote {target} ({len(LINE)} chars)")


if __name__ == "__main__":
    main(sys.argv)
