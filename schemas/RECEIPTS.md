# FOM Football C consistency receipts

FOM receipts do not define a second model or a second sweep. They wrap existing
V4/Football C execution so cross-stage consistency can be validated.

Every receipt includes a workflow ID, run ID and pinned Football C authority.

## fom-c-intake-v1

Wraps an **existing** canonical production V4 sweep bundle.

It records:

- native V4 receipt reference/status;
- native source reference;
- eligible/pending/excluded IDs;
- authority SHA;
- handoff consistency checks.

It never discovers fixtures.

## fom-c-rank-v1

Wraps the actual Football C rank result. Assessed rows use only C states:
FOCUS, WATCH, PASS.

`official_board` must contain exactly all assessed C-FOCUS match IDs. There is
no numeric cap.

## fom-c-decision-v1

Wraps the actual Football C /xi or /live decision: ACT, WAIT, PASS.

## fom-c-reconciliation-v1

Classifies whether a miss came from C application drift, evidence/process
failure, genuine C model miss, or normal variance.

## fom-c-audit-v1

Advisory deep-audit output. It cannot create an alternate prediction and cannot
mutate SlipTrace automatically.
