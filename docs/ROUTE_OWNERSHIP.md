# Route ownership

FOM and the existing SlipTrace workflow are alternative execution routes for the
same Football C model.

## Route identifiers

- `LEGACY_SLIPTRACE` — existing SlipTrace conversational/production route.
- `FOM_WORK` — isolated ChatGPT Work route in this repository.

## Hard invariant

One workflow belongs to one route.

For FOM:

```text
route_owner = FOM_WORK
```

is frozen at `/sweep` and carried through every downstream receipt.

## Forbidden mixing

A FOM stage must not use as its upstream stage result:

- a legacy SlipTrace V4 sweep receipt;
- a legacy SlipTrace rank board;
- a legacy SlipTrace /xi decision;
- a legacy SlipTrace /live decision.

Public factual evidence may overlap. Route outputs may be compared only after
both are independently frozen.

## Why

Without route ownership, running both workflows on the same slate duplicates
work and makes it impossible to tell whether improved consistency came from the
Work architecture or from reused legacy-stage conclusions.

## Operational rule

When testing a slate with FOM, choose the FOM route before `/sweep` and keep
all stages in FOM until the run is complete.

If a legacy route stage has already been used as the upstream authority for that
workflow, start a new FOM workflow ID rather than splicing it into FOM.
