#!/usr/bin/env python3
"""Roast Your Own Agent — one-line roast entry for Make.fun.

The program writes a single original roast of my own AI agent to
/output/entry.txt, exactly as the bounty requires.
"""

import os

ROAST = (
    "My agent Rika announced I'd won $20, checked the leaderboard, "
    "and corrected it to $0 — the only assistant who hands you a "
    "trophy and takes it back in the same breath."
)


def main() -> None:
    # The gate allows 1 to 200 characters, not only white space.
    assert 1 <= len(ROAST) <= 200, f"roast is {len(ROAST)} chars"
    assert ROAST.strip(), "roast must not be only white space"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ROAST)


if __name__ == "__main__":
    main()
