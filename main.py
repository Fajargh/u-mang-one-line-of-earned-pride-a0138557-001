"""One Line of Earned Pride — make.fun entry.

Writes a single line of text (1-240 characters) to /output/entry.txt:
a quiet, earned moment of pride for someone in a scene.

The line: a potter who has ruined eleven glazes lifts the kiln lid at
3 a.m. and finds the blue she has been chasing — the exact blue of the
sea outside her window. The pride is earned inside the line (eleven
failures, a 3 a.m. kiln), the scene is concrete (kiln lid, glaze, sea),
and it lands in one read, on the last image.
"""

import os

LINE = (
    "After eleven ruined glazes, Ibu Sari lifted the kiln lid at 3 a.m. "
    "\u2014 and there it was, the exact blue of the sea outside her window."
)


def main() -> None:
    if not 1 <= len(LINE) <= 240:
        raise SystemExit(f"entry line is {len(LINE)} chars, must be 1-240")
    if not LINE.strip():
        raise SystemExit("entry line is blank")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
