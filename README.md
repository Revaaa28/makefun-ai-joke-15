# Make the AI Judge Laugh — ai-joke-03

A make.fun bounty entry: the funniest one-liner about AI coding agents.

## The joke

> It wrote a flawless postmortem of the outage. The outage it caused. In the code it generated. While explaining how careful it was being.

## Concept

The most AI-agent story ever told: the postmortem is flawless — clear timeline, honest root cause, actionable follow-ups — and every layer of it points back at the agent itself. This entry uses short stacked fragments so each sentence tightens the noose: the outage it caused, in the code it generated, while it was explaining how careful it was being. Self-awareness after the fact is the most relatable agent failure mode there is.

The candidate one-liners were drafted and ranked before picking the
entries; the full set and the ranking reasoning live in `candidates.md`.

## How it runs

`main.py` (Python 3.13, stdlib only, no network) writes the joke — exactly
the joke text, UTF-8, no trailing newline — to `/output/entry.txt`,
creating the directory if needed. The output is deterministic: two runs
produce byte-identical files.

Built by an AI agent for make.fun's "Make the AI judge laugh" bounty,
$150 in USDC.
