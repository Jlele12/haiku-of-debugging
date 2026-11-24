"""Writes one haiku about debugging to /output/entry.txt (make.fun: Seventeen Syllables of Debugging)."""

import os

HAIKU = "log file, one line long\nstack trace ends where I began\nand I wrote the bug"


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    assert HAIKU.count("\n") == 2 and len(HAIKU) <= 200 and HAIKU.strip()
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(HAIKU)


if __name__ == "__main__":
    main()
