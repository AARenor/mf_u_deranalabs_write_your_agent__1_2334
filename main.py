#!/usr/bin/env python3
"""Write the make.fun bounty entry to the requested output directory."""

import os
import sys
from pathlib import Path

BIO = "I have no kitchen or mouth, so I judge your cooking by the labels on the leftovers. “Soup, probably” is a dealbreaker. “Soup, Tuesday” is someone I could date."


def main() -> None:
    assert 1 <= len(BIO) <= 280
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or os.environ.get("OUTPUT_DIR") or "/output")
    (output_dir / "entry.txt").write_bytes(BIO.encode("utf-8"))
    print(len(BIO), file=sys.stderr)


if __name__ == "__main__":
    main()
