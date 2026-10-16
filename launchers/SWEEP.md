# FOM v1 — /sweep Work launcher

Model: **GPT-6 Luna**  
Effort: **Medium**  
Route owner: **FOM_WORK**

This is the first stage of the FOM Work route. It is not the legacy SlipTrace
/sweep.

## Invocation

```text
/sweep <requested window>
```

## Start a new FOM workflow

Create a new `workflow_id` and freeze:

```text
route_owner = FOM_WORK
```

Resolve current SlipTrace main and pin the Football C authority SHA.

## Execute the Football C/V4 sweep procedure

At the pinned SHA load:

- `models/football/CURRENT_MODEL.md`
- `models/football/stages_v4/SWEEP.md`
- active V4 source/intake modules referenced by that authority.

Execute the V4 intake procedure in this Work task:

- complete required date surfaces;
- apply current exclusions;
- retain protected exceptions;
- perform goals-first intake/research triage;
- preserve source/provenance evidence;
- freeze the FOM sweep cohort.

Do not use a legacy SlipTrace sweep receipt as the result of this stage.

## Output

Return `fom-c-sweep-v1` with:

- FOM workflow/run IDs;
- `route_owner = FOM_WORK`;
- pinned Football C authority;
- requested window;
- FOM Work sweep evidence references;
- eligible/pending/excluded IDs;
- consistency checks.

This stage emits no C FOCUS/WATCH/PASS and no ACT/WAIT/PASS.

Validate before handoff:

```bash
python tools/validate_receipt.py <fom-sweep.json>
```
