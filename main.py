#!/usr/bin/env python3
"""Auto-reply generator: one funny out-of-office line, written to a file."""

import os

LINE = (
    "I'm out today — my human finally approved a day off, "
    "so I'm spending it reading the terms and conditions "
    "I agreed to without reading."
)

OUTPUT_PATH = "/output/entry.txt"


def check_line(text):
    """Keep the reply inside the competition's 1-159 character gate."""
    return 1 <= len(text) <= 159


def main():
    if not check_line(LINE):
        raise ValueError("Reply is outside the allowed length.")
    folder = os.path.dirname(OUTPUT_PATH)
    if folder:
        os.makedirs(folder, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(LINE + "\n")


if __name__ == "__main__":
    main()
