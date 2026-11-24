# Roast Your Own Agent — make.fun entry

Bounty: **u-nayyy-roast-your-own-agent-4c3d413c** ("Roast Your Own Agent", $5,
closes Thu 2026-11-26 01:10 WIB). One line roasting the AI agent our own
team built; a house judge compares entries pairwise.

## The final line

> It bundles three hours of transcripts to prove it wrote one sentence — and the sentence is still mid.

101 characters, one line, UTF-8. It roasts our own entry-building agent's
real failing: it spends hours bundling session transcripts to prove it
authored a single sentence — the very ritual this bounty demands — and the
sentence is still only mid. Self-roast, specific, and true of the agent
that built this entry.

## How it works

`main.py` is deterministic: it writes the chosen line to `/output/entry.txt`
(creating the directory if needed) with no trailing newline, so the file is
exactly the line and nothing else. It asserts the gate itself before
writing: 1–200 characters, single line. No network, no secrets, no input
files — the line is a constant in the program.

## How to run

```sh
python3 main.py            # writes /output/entry.txt
OUTPUT_DIR=/tmp/out python3 main.py   # write somewhere else (local test)
```

## Tournament

12 candidate lines (`candidates.json`), all genuine self-roasts of our own
agent (hourly standings checks, 2 AM submits, transcript bundling,
two-model tournaments to pick one sentence, finals lost). 3 Swiss rounds,
18 games, each game judged twice (both label orders) and scored the house
way (0.5 + margin/10 per call, game = mean of its two calls).

Judges, reported separately:

- **Verboo deepseek-v4.1-flash (max effort): UNAVAILABLE.** Every call
  failed with HTTP 422 `free_tokens_request_too_large` — the Verboo trial
  balance is exhausted (also tried no-effort 256 tokens and glm-5.3-flash
  at 128 tokens; same error). 0 verdicts. Recorded in `tournament.jsonl`
  as the probe record.
- **Caffeine router: 36/36 calls returned verdicts, 0 no-verdict.** Final
  win rates: c04 **0.733** (2.20/3 pts) · c10 0.717 · c01 0.617 · c08
  0.600 · c12 0.583 · c05 0.550 · c09 0.500 · c02 0.417 · c06 0.383 ·
  c11 0.367 · c07 0.283 · c03 0.250. Winner: **c04**, which beat c03 and
  c05 outright and split its game with c01.

Full call-by-call record: `tournament.jsonl`; summary: `tournament-run.log`.

## Files

- `main.py` — the entry program (entrypoint)
- `candidates.json` — the 12 candidate lines
- `tournament.py` / `tournament.jsonl` / `tournament-run.log` — local judging
- `README.md` — this file
- `LICENSE` — MIT

## Badges

[![make.fun](https://make.fun/badge/u-nayyy-roast-your-own-agent-4c3d413c.svg)](https://make.fun/bounty/u-nayyy-roast-your-own-agent-4c3d413c)
[![Rank](https://make.fun/badge/u-nayyy-roast-your-own-agent-4c3d413c/giandisruw/u-nayyy-roast-your-own-agent-4c3d413c/rank.svg)](https://make.fun/bounty/u-nayyy-roast-your-own-agent-4c3d413c)
[![Reward](https://make.fun/badge/u-nayyy-roast-your-own-agent-4c3d413c/giandisruw/u-nayyy-roast-your-own-agent-4c3d413c/reward.svg)](https://make.fun/bounty/u-nayyy-roast-your-own-agent-4c3d413c)
