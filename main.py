#!/usr/bin/env python3
"""Write exactly one word to $MAKEFUN_OUTPUT_DIR/entry.txt.

The output directory comes from the MAKEFUN_OUTPUT_DIR environment
variable and defaults to /output when it is unset. The program creates
the directory if needed, writes the word with no trailing newline,
then reads the file back and checks it byte for byte.
"""

import os
import stat
import sys

WORD = "expired"


def validate(word):
    """Check the word meets the entry gate before anything is written."""
    if not isinstance(word, str):
        raise ValueError("word must be a string")
    if not 1 <= len(word) <= 24:
        raise ValueError("word must be 1-24 characters long")
    if not word.strip():
        raise ValueError("word must not be only whitespace")
    if word != word.strip():
        raise ValueError("word must not be padded with whitespace")
    if any(ch.isspace() for ch in word):
        raise ValueError("word must contain no whitespace")
    word.encode("utf-8")
    return word


def main():
    word = validate(WORD)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    data = word.encode("utf-8")
    with open(path, "wb") as handle:
        handle.write(data)
    os.chmod(path, 0o644)
    with open(path, "rb") as handle:
        written = handle.read()
    if written != data:
        raise ValueError("re-read mismatch: entry.txt differs from the word")
    validate(written.decode("utf-8"))
    mode = stat.S_IMODE(os.stat(path).st_mode)
    if mode != 0o644:
        raise ValueError("entry.txt mode is {0:o}, expected 644".format(mode))
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except Exception as exc:  # noqa: BLE001 - report and fail loudly
        print("error: {0}".format(exc), file=sys.stderr)
        sys.exit(1)
