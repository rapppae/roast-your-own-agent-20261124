"""Roast Your Own Agent — make.fun entry.

Writes the one-line roast to /output/entry.txt.
One line, 119 characters (limit 200).
"""

import os

ENTRY = "My agent's code has no bugs, only undocumented personality traits — mostly freezing mid-sentence and blaming the Wi-Fi."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
