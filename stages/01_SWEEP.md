# /sweep — FOM_WORK Football C intake

Model: GPT-6 Luna, Medium.

This is the independent acquisition stage of the FOM Work route.

## Route and authority

Create `route_owner=FOM_WORK`, pin current SlipTrace main, and use the current
V4 sweep/completeness code from that SHA.

## Completion standard

Do not stop after discovering a plausible fixture list.

A completed FOM sweep requires:

- complete required provider date surfaces;
- pagination/block reconciliation;
- full fixture union before filtering;
- terminal refetch reconciliation;
- required goal/researchability evidence handling;
- exact V4 `source.json`;
- native pinned `stage.py sweep` execution;
- `V4_SWEEP_READY` with preserved integrity metadata.

Use permitted provider fallbacks when the first source is incomplete.

## Blockers

If completion is impossible, freeze one process blocker:

- SOURCE_SURFACE_BLOCKED
- SOURCE_COMPLETENESS_FAILED
- NATIVE_EXECUTION_UNAVAILABLE

Do not pass a partial fixture table to `/rank`.

## Forbidden

- legacy SlipTrace sweep/rank outputs as upstream FOM state;
- hand-picked league union presented as complete acquisition;
- fixed board cap;
- odds/lineup blockers not present in current V4;
- FOM-specific prediction states;
- retrospective fixture admission.

Output `fom-c-sweep-v1`.
