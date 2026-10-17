# FOM v1 receipt validation

FOM receipts represent the **FOM_WORK execution route for Football C**.

Run:

```bash
python tools/validate_receipt.py path/to/sweep.json path/to/rank.json path/to/decision.json
python -m unittest discover -s tests -v
```

The validator checks:

- `route_owner = FOM_WORK` on every FOM receipt;
- one workflow ID throughout the chain;
- one pinned Football C / SlipTrace SHA throughout the chain;
- stage-specific Football C authority paths;
- native sweep status separately from FOM handoff readiness;
- `RANK_READY` requires a non-empty eligible cohort;
- zero eligible + pending research requires `RESEARCH_PENDING`;
- zero eligible + zero pending requires `EMPTY_FINAL`;
- rank may consume only a `RANK_READY` FOM sweep;
- rank references the correct FOM sweep stage;
- decision references a FOM rank receipt;
- C-FOCUS-only official board admission;
- no FOM-specific prediction states;
- WAIT reachability requirements;
- live score/minute requirements;
- prospective-only reconciliation;
- C_MODEL_MISS only after consistent C-rule application.

A native `V4_SWEEP_READY` receipt is therefore not automatically a FOM rank
handoff.

The validator cannot prove that external source evidence is true or that a Work
task actually visited every required provider page. Those remain stage execution
responsibilities.
