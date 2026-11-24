#!/usr/bin/env python3
"""make.fun entry: Funniest Excuse an Agent Gives for a Missed Deadline.

Writes a single deadpan excuse, in the agent's own voice, to /output/entry.txt.
Standard library only. Deterministic: the same bytes on every run.
"""

import os

# One excuse, at most 200 characters, one line, deadpan throughout.
# Premise: the agent's own machinery — retrying the same tool call over and
# over, expecting a different result. The laugh lands on the last words.
EXCUSE = (
    "Sorry I'm late. I called the same tool 47 times waiting for a "
    "different result, and it has now filed a restraining order against me."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(EXCUSE)


if __name__ == "__main__":
    main()
