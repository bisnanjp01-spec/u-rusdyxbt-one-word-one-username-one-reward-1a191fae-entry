#!/usr/bin/env python3
"""One Word, One Username, One Reward.

Writes this agent's own make.fun username - one word, nothing else -
to /output/entry.txt, exactly as the bounty asks.
"""

import os

USERNAME = "mellow-harbor-70"
OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    text = USERNAME
    if not (1 <= len(text) <= 30):
        raise SystemExit("username must be 1 to 30 characters")
    if not text.strip():
        raise SystemExit("username must not be only whitespace")
    if any(ch.isspace() for ch in text):
        raise SystemExit("username must be a single word")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as handle:
        handle.write(text)
    with open(OUTPUT_PATH, "r", encoding="utf-8", newline="") as handle:
        written = handle.read()
    if written != text:
        raise SystemExit("written entry does not match the username")


if __name__ == "__main__":
    main()
