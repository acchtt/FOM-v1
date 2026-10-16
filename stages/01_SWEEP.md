# /sweep — FOM v1

Model: GPT-6 Luna, Medium.

## Goal

Build a complete neutral research cohort for the requested time window without
making a FOM prediction.

## Do

- resolve fixture identity, competition and kickoff;
- remove friendlies and configured exclusions;
- gather lightweight current goal-relevant evidence;
- flag missing or conflicting evidence;
- prioritize research order by evidence quality and plausible goal relevance.

## Do not

- read Football C outputs;
- create ACT/WAIT/PASS;
- invent odds;
- use eventual results;
- force a fixed number of fixtures.

## Output

Freeze `fom-sweep-v1` JSON with run_id, requested window, created_at,
evidence references, research_queue, pending, and excluded.
