# FOM_WORK Football C receipt contracts

FOM receipts represent a complete alternative Work execution route for Football
C. They are not wrappers around legacy SlipTrace stage outputs.

Every FOM receipt includes:

```json
{
  "workflow_id": "FOMC-...",
  "run_id": "FOMC-...",
  "route_owner": "FOM_WORK",
  "football_c_authority": {
    "repository": "acchtt/SlipTrace",
    "commit_sha": "<40 hex>",
    "active_model": "C",
    "current_model_path": "models/football/CURRENT_MODEL.md",
    "stage_authority_path": "<stage authority>"
  }
}
```

## fom-c-sweep-v1

Created by the FOM Work sweep. It owns the workflow and freezes
`route_owner=FOM_WORK`.

It records the FOM-acquired window/cohort/provenance and emits no prediction.

## fom-c-rank-v1

Consumes only the matching FOM sweep receipt.

Assessed rows use Football C states only:
FOCUS, WATCH, PASS.

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
