#!/usr/bin/env python3
"""The Vacuum's Alibi: One Line, 200 Characters.

A robot vacuum's one-line excuse for a missed spot. The program writes
that single line to ``$MAKEFUN_OUTPUT_DIR/entry.txt`` (``/output`` when
the variable is unset).

The line itself is fixed text, assembled from its three sentences at
import time. There is no randomness, no network access and no clock
read anywhere in the program, so every run writes byte-identical
output: 99 characters, UTF-8, no trailing newline.

Design note: validation is split per rule (length, single line, ASCII)
so a future rule change touches one small check, not the writer.
"""

import os
import sys

# The three sentences of the alibi, in order. Joined with a single
# space each, they form the entry line.
SENTENCES = (
    "My sensors confirm the spot was cleaned at 14:02.",
    "The spot disagrees.",
    "I have sided with my sensors.",
)

MAX_CHARS = 200
DEFAULT_OUTPUT_DIR = "/output"


def build_line() -> str:
    """Assemble the entry line from its sentences."""
    return " ".join(SENTENCES)


def check_length(line: str) -> None:
    """The line must be non-empty and fit the 200-character cap."""
    if not 1 <= len(line) <= MAX_CHARS:
        raise ValueError(
            f"entry line is {len(line)} characters, must be 1-{MAX_CHARS}"
        )


def check_single_line(line: str) -> None:
    """The line must contain no line breaks of either kind."""
    if any(ch in line for ch in ("\n", "\r")):
        raise ValueError("entry line must fit on a single line")


def check_ascii(line: str) -> None:
    """The line must be plain ASCII so its byte length is predictable."""
    if not line.isascii():
        raise ValueError("entry line must be plain ASCII")


def validate_line(line: str) -> None:
    """Reject any line that breaks the competition's shape rules."""
    check_length(line)
    check_single_line(line)
    check_ascii(line)


def resolve_output_dir() -> str:
    """Return the directory the harness expects entry.txt in."""
    return os.environ.get("MAKEFUN_OUTPUT_DIR", DEFAULT_OUTPUT_DIR)


def write_entry(line: str, output_dir: str) -> str:
    """Write the line to entry.txt inside output_dir; return the path."""
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(line)
    return path


def main() -> int:
    line = build_line()
    validate_line(line)
    write_entry(line, resolve_output_dir())
    return 0


if __name__ == "__main__":
    sys.exit(main())
