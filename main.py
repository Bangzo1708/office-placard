"""Office Artifacts: The One-Line Placard Contest.

Writes a single museum placard line to /output/entry.txt.
Deterministic: one fixed string, no randomness, no network, no clock.
"""

import os

ENTRY = (
    "Microwave, fired clay and obsidian, c. 900 BCE. "
    "Priests reheated offerings; its beep summoned the god of lunch. "
    "Donated by the Break Room Elders."
)

# The gate requires 1-180 characters of UTF-8 text, not only whitespace.
# "Reheated offerings" recasts the microwave's one real job as ritual;
# "the god of lunch" is the deadpan punchline, and the donor line sells
# the label. Keep the entry inside the limit or refuse to write it.
assert 1 <= len(ENTRY) <= 180, f"entry is {len(ENTRY)} chars, must be 1-180"
assert ENTRY.strip(), "entry must not be only whitespace"


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
