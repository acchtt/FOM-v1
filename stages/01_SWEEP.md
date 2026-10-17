# /sweep — FOM_WORK Football C intake

Model: GPT-6 Luna, Medium.

This is the independent acquisition and admission-research stage of the FOM
Work route.

## Route and authority

Create `route_owner=FOM_WORK`, pin current SlipTrace main, and use the current
V4 sweep/completeness code from that SHA.

## Native intake versus FOM handoff

`V4_SWEEP_READY` proves a valid native source intake. It does not alone prove
that FOM should hand the slate to `/rank`.

Use:

- `RANK_READY`: at least one eligible fixture;
- `RESEARCH_PENDING`: zero eligible with unresolved goal/researchability work;
- `EMPTY_FINAL`: zero eligible and no unresolved research;
- `BLOCKED`: named process failure.

## Pending-enrichment loop

When native V4 is ready but:

```text
eligible = 0
pending > 0
```

continue targeted research of the pending fixtures in the same FOM sweep stage.
Gather missing recent-goal/researchability/format evidence, refresh current
fixture state, create a new source-observed V4 epoch, and rerun the native sweep.

Do not restart complete acquisition when only the admitted fixture research is
missing.

A `RESEARCH_PENDING` checkpoint may be frozen when the Work turn must stop,
but it is not a rank handoff.

## Completion standard

A rank handoff requires `handoff_state=RANK_READY`.

A completed no-candidate slate uses `EMPTY_FINAL`.

## Blockers

- SOURCE_SURFACE_BLOCKED
- SOURCE_COMPLETENESS_FAILED
- NATIVE_EXECUTION_UNAVAILABLE

## Forbidden

- legacy SlipTrace stage outputs as upstream FOM state;
- partial fixture list presented as rank-ready;
- zero-eligible pending receipt presented as completed;
- fixed board cap;
- odds/lineup blockers not present in current V4;
- FOM-specific prediction states.

Output `fom-c-sweep-v1`.
