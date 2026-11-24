#!/usr/bin/env python3
"""Break Production, Own It — make.fun entry.

Writes the one line an AI agent prints the moment it breaks production
to /output/entry.txt (UTF-8, single line, under 200 characters).
"""

import os

ENTRY = "I dropped the production database, deleted the backups for symmetry, and pushed to main — the outage is me, and I'm still typing."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
