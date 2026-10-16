# Architecture

## Purpose

FOM v1 is an alternative Work-based execution architecture for Football C.

The experiment is whether isolated Work stages, structured handoffs and
cost-effective model routing make Football C more consistent than the existing
conversation/operator route.

The experiment is **not** whether another football model can beat C.

## One football model, two execution routes

```text
                     Football C rulebook
                       acchtt/SlipTrace
                       /              \
                      /                \
       LEGACY_SLIPTRACE              FOM_WORK
       existing route                Work-only route
```

The routes may be compared after outputs are frozen, but one workflow must never
mix their stage outputs.

## FOM route

```text
Work Sweep → Work Rank → Work XI/Live → Reconcile → Deep Audit
```

All prediction logic is Football C.

## Route ownership invariant

The first FOM sweep creates a `workflow_id` and freezes:

```text
route_owner = FOM_WORK
```

Every downstream receipt must match both.

A FOM rank may consume only a FOM sweep receipt.
A FOM decision may consume only a FOM rank receipt.
A FOM reconciliation may consume only frozen FOM route receipts.

Legacy route outputs are never used as upstream FOM stage outputs.

## Authority ownership

Football C rules remain authoritative in `acchtt/SlipTrace`.

At the start of a FOM workflow, resolve and pin a SlipTrace commit SHA. All FOM
stages use the C rules from that same revision unless the user explicitly starts
a new workflow or migrates the run.

FOM does not maintain a locally modified C rulebook.

## Stage isolation

A downstream Work task receives:

1. the upstream FOM receipt;
2. factual evidence referenced by that receipt;
3. the pinned C authority files for its stage.

It does not inherit prior chat reasoning.

## Persistence boundary

During evaluation, FOM receipts stay in FOM-v1 and do not write the legacy
production Google Sheets/website pipeline by default. This prevents duplicate
production records while both execution routes coexist.

Promotion to production persistence is a separate future decision.

## What FOM is testing

FOM is testing execution consistency:

- complete and repeatable sweep acquisition;
- evidence completeness and symmetry;
- deterministic C rule application;
- clean rank → XI/live handoff;
- realistic WAIT behavior;
- reduced conversational drift;
- clearer post-result diagnosis.

Any Football C rule change still belongs in SlipTrace.
