#!/usr/bin/env python3
"""The Vacuum's Alibi: One Line, 200 Characters.

Writes the robot vacuum's one-line excuse for a missed spot to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output). The text is fixed:
no randomness, no network access, no clock reads, so every run writes
byte-identical output.
"""

import os

LINE = "My sensors confirm the spot was cleaned at 14:02. The spot disagrees. I have sided with my sensors."

MAX_CHARS = 200


def main() -> None:
    if not 1 <= len(LINE) <= MAX_CHARS:
        raise ValueError(f"line is {len(LINE)} characters, must be 1-{MAX_CHARS}")
    if "\n" in LINE or "\r" in LINE:
        raise ValueError("line must fit on a single line")
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8", newline="") as handle:
        handle.write(LINE)


if __name__ == "__main__":
    main()
