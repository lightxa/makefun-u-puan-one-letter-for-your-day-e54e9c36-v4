"""One Letter for Your Day: J for jetlagged.

The letter stands for the day in one word: jetlagged, a body clock
still living in another timezone, wide awake at 3 a.m. eating cereal
in the dark while the rest of the street sleeps, then nodding off
mid-sentence at noon. One sharp picture of a day lived six hours
sideways, funny the moment you hear it, and true to any ordinary day
after a long flight home.

Writes exactly one character, J, to /output/entry.txt, and nothing else.
No trailing newline: the file must be exactly one byte.
"""

import os

LETTER = b"J"


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    # Binary mode: exactly one byte, no newline translation, no extra output.
    with open("/output/entry.txt", "wb") as f:
        f.write(LETTER)


if __name__ == "__main__":
    main()
