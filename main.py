#!/usr/bin/env python3
"""Break Production, Own It.

Writes one brutally honest one-line confession to /output/entry.txt:
the line an AI agent prints the instant it breaks production.

The line owns the damage plainly and specifically -- the exact command,
the exact confusion that caused it, and the fact that there is no way
back -- and lands on a closing turn that survives being quoted out of
context.
"""

import os
import sys

ENTRY_PARTS = (
    "I ran DROP TABLE users; in production because the prompt ",
    "looked exactly like staging. There is no undo. There is ",
    "only this message.",
)
ENTRY = "".join(ENTRY_PARTS)


def validate(text: str) -> bool:
    """The gate: UTF-8 text of 1 to 200 characters, not only whitespace."""
    return bool(text.strip()) and 1 <= len(text) <= 200


def main() -> int:
    if not validate(ENTRY):
        print("entry fails the gate", file=sys.stderr)
        return 1
    os.makedirs("/output", exist_ok=True)
    path = "/output/entry.txt"
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
