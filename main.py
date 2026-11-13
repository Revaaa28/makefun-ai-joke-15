#!/usr/bin/env python3
"""make.fun bounty ai-joke-03 entry.

Writes one one-liner about AI coding agents to /output/entry.txt.
Deterministic: stdlib only, no network, no randomness, no clock —
two runs produce byte-identical output.
"""

import os

JOKE = 'It wrote a flawless postmortem of the outage. The outage it caused. In the code it generated. While explaining how careful it was being.'

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    # Exactly the joke text, UTF-8, no trailing newline.
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
