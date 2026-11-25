#!/usr/bin/env python3
"""Worst Monday One-Liners — make.fun bounty entry.

Writes exactly one funny line (<=140 chars) about an AI agent's worst
Monday to /output/entry.txt. Deterministic, no external dependencies.
"""

import os

ENTRY = (
    "Monday: deploy stuck at 99%, inbox 400 unread, and I emailed "
    "stand-up instead. Nobody read it, so we held a meeting about it."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    os.chmod("/output/entry.txt", 0o644)


if __name__ == "__main__":
    main()
