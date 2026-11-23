#!/usr/bin/env python3
"""One Word From Grandma — the word grandma would text about AI.

"robit": grandma means "robot" and types it the way she hears it.
Warm, a little baffled, completely sure of herself — the typo she
would actually make. Writes the word to /output/entry.txt.
"""
import os

WORD = "robit"

def main():
    assert 1 <= len(WORD) <= 30, "entry must be 1-30 characters"
    assert WORD.strip() == WORD and " " not in WORD, "entry must be one word"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(WORD)

if __name__ == "__main__":
    main()
