#!/usr/bin/env python3
"""Roast Your Own Agent — make.fun entry (u-nayyy-roast-your-own-agent-4c3d413c).

Deterministic program: writes one chosen roast line to /output/entry.txt.
The line is a genuine self-roast of our own make.fun entry-building agent
(the agent that builds these entries, runs tournaments over its own jokes,
bundles transcripts, checks standings every hour, and submits at 2 AM).

The line was picked by a local pairwise tournament (see tournament.py and
tournament.jsonl): 12 candidate lines, 3 Swiss rounds, judged in both
label orders by the Caffeine router, scored the house way
(0.5 + margin/10 per call, game = mean of its two calls).

Gate: /output/entry.txt must be UTF-8, 1-200 characters, a single line.
This program writes the line with no trailing newline, so the file is
exactly the line and nothing else.
"""

import os
import sys

# Tournament winner (see tournament-run.log). Picked by a local pairwise
# tournament: 12 candidates, 3 Swiss rounds, 18 games, 36 judge calls by
# the Caffeine router (Verboo was unavailable — trial balance exhausted),
# scored the house way. Winner c04: 0.733 win rate (2.20/3.00 points),
# ahead of c10 at 0.717. It beat c03, c05, and split with c01.
FINAL_LINE = (
    "It bundles three hours of transcripts to prove it wrote one sentence "
    "— and the sentence is still mid."
)


def main():
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    line = FINAL_LINE.strip()
    assert "\n" not in line, "entry must be a single line"
    assert 1 <= len(line) <= 200, "entry must be 1-200 characters"
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(line)
    print("wrote %s (%d chars)" % (path, len(line)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
