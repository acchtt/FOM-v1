# FOM_WORK Football C receipt contracts

FOM receipts represent a complete alternative Work execution route for Football
C.

Every FOM receipt includes `route_owner=FOM_WORK`, one workflow ID, and one
pinned Football C authority revision.

## fom-c-sweep-v1

The FOM sweep receipt distinguishes native intake status from downstream handoff
status.

`handoff_state` is one of:

- `RANK_READY` — eligible cohort is non-empty and may go to rank;
- `RESEARCH_PENDING` — native intake is valid, but eligible=0 while
  goal/researchability work remains;
- `EMPTY_FINAL` — native intake is complete, eligible=0 and no pending
  admission research remains;
- `BLOCKED` — named process blocker.

A native `V4_SWEEP_READY` with zero eligible and pending research is therefore
**not** a FOM rank handoff.

## fom-c-rank-v1

Consumes only a matching FOM sweep receipt with
`handoff_state=RANK_READY`.

Assessed rows use Football C states only: FOCUS, WATCH, PASS.

`official_board` contains exactly all C-FOCUS IDs. No numeric cap.

## fom-c-decision-v1

Consumes only the matching FOM rank receipt and records the actual C
ACT/WAIT/PASS decision.

## fom-c-reconciliation-v1

Uses frozen FOM route receipts and outcomes to separate process/application
drift from genuine C model miss or normal variance.

## fom-c-audit-v1

Deep audit is advisory. Cross-route comparison is allowed only after independent
freeze and cannot become upstream FOM evidence.

## Route invariant

All receipts in one FOM workflow must have:

```text
route_owner = FOM_WORK
same workflow_id
same pinned Football C commit SHA
```

No legacy SlipTrace stage output may be spliced into the chain.
