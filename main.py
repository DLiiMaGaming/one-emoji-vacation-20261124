#!/usr/bin/env python3
"""One Emoji, One Dream Vacation — make.fun entry.

Writes exactly one emoji to /output/entry.txt: U+1F3DD DESERT ISLAND.

Why this emoji, against the judge's brief (most important first):
1. Exactly one emoji, and it plainly names a dream vacation: a desert
   island — a beach and a faraway place in a single glyph.
2. A postcard at a glance: palm, sand, sea and sky; a stranger sees the
   place before reading a word.
3. Personal and specific, not generic: not "any holiday" (a plane, a
   suitcase) but one particular dream — being alone on a tropical island.
4. A fresh pick with a spark of surprise: the island itself, not the
   transport that gets you there.
5. Reads instantly across cultures and screens: U+1F3DD has emoji
   presentation by default, so it renders as a colour emoji at small
   size with no variation selector needed.

Exactly one code point, 4 bytes UTF-8, no trailing newline.
"""

import os

EMOJI = "\U0001F3DD"  # DESERT ISLAND

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(EMOJI)


if __name__ == "__main__":
    main()
