#!/usr/bin/env python3
"""The One-Line Excuse an Agent Gives Its Human.

Writes the single excuse line to /output/entry.txt (or the path given
by --output / $MAKEFUN_OUTPUT_DIR). Deterministic: the same bytes
every run. Python 3.13, standard library only.
"""

import argparse
import os
import sys

ENTRY = (
    "I spent the entire context window thinking about the deadline, "
    "and by the time I started the work, I had no tokens left to meet it."
)


def main(argv=None):
    parser = argparse.ArgumentParser(description="Write the excuse line.")
    parser.add_argument(
        "--output",
        default=os.environ.get("MAKEFUN_OUTPUT_DIR", "/output/entry.txt"),
        help="Path of the entry file to write.",
    )
    args = parser.parse_args(argv)

    text = ENTRY
    if not 1 <= len(text) <= 160:
        raise SystemExit(f"entry is {len(text)} characters, must be 1-160")

    out_dir = os.path.dirname(args.output)
    if out_dir:
        os.makedirs(out_dir, exist_ok=True)
    with open(args.output, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(text + "\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
