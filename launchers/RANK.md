# FOM v1 — /rank Work launcher

Model: **GPT-6.1 Sol**  
Effort: **Medium**  
Route owner: **FOM_WORK**

## Invocation

```text
/rank <fom-c-sweep-v1 receipt>
```

For `/rank FOM newest receipt`, resolve the latest FOM sweep receipt for the
active workflow. Do not silently fall back to an older workflow.

## Route and handoff gate

Accept only a FOM sweep receipt with:

- the same `workflow_id`;
- `route_owner = FOM_WORK`;
- a pinned Football C authority SHA;
- `handoff_state = RANK_READY`;
- at least one eligible fixture.

If the newest FOM sweep is `RESEARCH_PENDING`, do not attempt C ranking and do
not call the slate complete. Return the exact recovery action:

```text
/sweep resume <workflow_id>
```

If it is `EMPTY_FINAL`, report an honest completed empty shortlist. If it is
`BLOCKED`, report its named blocker.

Do not substitute a legacy SlipTrace sweep receipt, older FOM workflow, or
legacy rank output.

## Authority gate

At the exact SHA from the FOM sweep receipt load:

- `models/football/CURRENT_MODEL.md`;
- `models/football/stages_v4/RANK.md`;
- active Football C engine/rule files referenced there.

If current SlipTrace main differs, report `AUTHORITY_CHANGED` but do not
silently switch this workflow.

## Execute Football C rank

Research the complete eligible FOM sweep cohort and apply C exactly:

- fresh status/kickoff checks required by the pinned rank contract;
- current football evidence;
- tournament incentive;
- C goal certificates and supported-burden compiler;
- C transferability/comparable-context rules;
- C ranking key;
- C FOCUS/WATCH/PASS;
- C-FOCUS-only official board;
- no fixed numeric board cap;
- FOLLOW/RESERVE/STOP only as the operational lane after C selection.

Do not invent a FOM ranking formula or second model vote.

## Output

Return `fom-c-rank-v1` owned by the same FOM workflow.

Validate:

```bash
python tools/validate_receipt.py <fom-sweep.json> <fom-rank.json>
```
