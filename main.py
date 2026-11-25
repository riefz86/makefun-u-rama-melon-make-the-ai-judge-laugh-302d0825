#!/usr/bin/env python3
"""Make the AI Judge Laugh — one original office-life joke.

Writes a single line (1-200 UTF-8 characters) to /output/entry.txt.
Deterministic: no input, no network, no randomness.
"""

import os

JOKE = (
    "I declined a meeting to protect my focus time, so my manager "
    "scheduled a meeting about why I decline meetings."
)


def main() -> None:
    text = JOKE.strip()
    assert 1 <= len(text) <= 200, f"joke is {len(text)} chars, must be 1-200"
    assert "\n" not in text, "entry must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)
    os.chmod("/output/entry.txt", 0o644)
    print(text)
    print(f"({len(text)} characters)")


if __name__ == "__main__":
    main()
