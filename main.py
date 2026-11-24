#!/usr/bin/env python3
"""One Word, One Username, One Reward — make.fun entry.

The entry is the entrant's own make.fun username, one word and nothing
else. The judge compares two usernames at a time and picks the funnier or
more interesting one, so the program's whole job is to emit that handle
byte-exact: 9 bytes, no trailing newline (the tie-break favours smaller
text, and any extra byte is a different entry).
"""

import os
import sys

USERNAME = "riehann10"


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    expected = USERNAME.encode("utf-8")
    # Binary write: no newline, no encoding surprises, exactly 9 bytes.
    with open("/output/entry.txt", "wb") as f:
        f.write(expected)
    # Read-back verification: the file on disk must be byte-identical to
    # what we intended, otherwise fail loudly instead of submitting a
    # wrong entry (a trailing newline or stray byte changes the entry).
    with open("/output/entry.txt", "rb") as f:
        actual = f.read()
    if actual != expected:
        print(
            f"entry mismatch: wrote {expected!r}, read back {actual!r}",
            file=sys.stderr,
        )
        sys.exit(1)


if __name__ == "__main__":
    main()
