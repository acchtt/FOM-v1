# FOM v1 — /sweep Work launcher

Model: **GPT-6 Luna**  
Effort: **Medium**

Use this launcher in a dedicated ChatGPT Work task.

## Invocation

```text
/sweep <requested window>
```

Resolve the requested window into explicit offset-aware ISO-8601 start and end
timestamps before fixture research. Keep kickoff timestamps offset-aware.

## Isolation gate

This task is FOM-only.

Before the receipt is frozen, do **not** read or use:

- Football C rank/order;
- Football C FOCUS/WATCH/PASS;
- Football C supported burden;
- Football C ACT/WAIT/PASS;
- Football C model commentary;
- post-match outcomes for fixtures in the requested window.

Allowed inputs are neutral factual evidence only.

If a source page contains prohibited Football C material, do not use that source
for this run.

## Task

Build the neutral FOM research cohort for the requested window.

For each candidate fixture:

1. resolve fixture identity;
2. confirm competition;
3. confirm kickoff;
4. exclude friendlies and already-configured exclusions;
5. gather lightweight, current, goal-relevant factual evidence;
6. flag missing or conflicting evidence instead of guessing;
7. place the fixture in exactly one of:
   - `research_queue`
   - `pending`
   - `excluded`

Do not rank the fixtures and do not produce a football verdict.

Do not produce:

- `FOM_FOCUS`, `FOM_WATCH`, or `FOM_DROP`;
- `ACT`, `WAIT`, or `PASS`;
- a supported goal line;
- a bookmaker quote unless the task is explicitly given a user screenshot for
  factual identification only;
- a fixed-size board or quota.

## Evidence references

Every source used must have a stable reference.

The top-level `evidence_refs` must contain the union of evidence references used
by the receipt.

Every `research_queue` row must list the evidence references supporting that
fixture's identity/current intake evidence.

Do not place private chain-of-thought or conversational reasoning in the receipt.

## Output contract

Return exactly one JSON object conforming to
`schemas/fom-receipt-v1.schema.json` with:

```json
{
  "schema_version": "fom-sweep-v1",
  "run_id": "FOM-...",
  "created_at": "offset-aware ISO-8601 timestamp",
  "stage": "sweep",
  "evidence_refs": [],
  "requested_window": {
    "start": "offset-aware ISO-8601 timestamp",
    "end": "offset-aware ISO-8601 timestamp"
  },
  "research_queue": [
    {
      "match_id": "stable fixture identifier",
      "home_team": "Home",
      "away_team": "Away",
      "competition": "Competition",
      "kickoff": "offset-aware ISO-8601 timestamp",
      "evidence_refs": [],
      "priority": 1,
      "reason": "brief factual intake reason"
    }
  ],
  "pending": [
    {
      "match_id": "stable fixture identifier",
      "reason": "missing/conflicting evidence"
    }
  ],
  "excluded": [
    {
      "match_id": "stable fixture identifier",
      "reason": "friendlies/configured exclusion/outside requested window"
    }
  ]
}
```

`priority` orders research attention only. It is not a FOM rank or prediction.

## Pre-freeze checks

Before returning the receipt:

- verify every kickoff lies inside the requested window unless the row is
  `excluded` for being outside it;
- verify no fixture appears in more than one bucket;
- verify all timestamps are offset-aware;
- verify every researchable row has evidence references;
- verify no Football C output or post-match result contaminated the run;
- validate the JSON with:

```bash
python tools/validate_receipt.py <receipt.json>
```

If validation fails, repair the JSON before freezing it.

## Freeze

Once a valid receipt is returned to the next stage, treat that receipt as
immutable. A material correction requires a new sweep run and a new `run_id`.

The next stage receives only this frozen receipt and the factual evidence
referenced by it.
