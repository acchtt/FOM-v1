# FOM Football C consistency receipts

FOM receipts do not define a second model. They wrap Football C/V4 execution so
cross-stage consistency can be validated.

Every receipt includes:

```json
{
  "workflow_id": "FOMC-...",
  "run_id": "FOMC-...",
  "football_c_authority": {
    "repository": "acchtt/SlipTrace",
    "commit_sha": "<40 hex>",
    "active_model": "C",
    "current_model_path": "models/football/CURRENT_MODEL.md",
    "stage_authority_path": "<stage-specific path>"
  }
}
```

All receipts with the same `workflow_id` must use the same
`football_c_authority.commit_sha`.

## fom-c-sweep-v1
Wraps native V4 intake. It records the native receipt reference/status and
eligible/pending/excluded IDs. It contains no prediction.

## fom-c-rank-v1
Wraps the actual Football C rank result. Assessed rows use only C states:
FOCUS, WATCH, PASS.

`official_board` must contain exactly all assessed C-FOCUS match IDs. There is
no numeric cap.

## fom-c-decision-v1
Wraps the actual Football C /xi or /live decision: ACT, WAIT, PASS.
WAIT requires a reachable condition and basis.

## fom-c-reconciliation-v1
Classifies whether a miss came from C application drift, evidence/process
failure, genuine C model miss, or normal variance.

## fom-c-audit-v1
Advisory deep-audit output. It cannot create an alternate prediction and cannot
mutate SlipTrace automatically.
