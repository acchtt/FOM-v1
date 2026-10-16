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
- rank references a FOM sweep receipt;
- decision references a FOM rank receipt;
- C-FOCUS-only official board admission;
- no FOM-specific prediction states;
- WAIT reachability requirements;
- live score/minute requirements;
- prospective-only reconciliation;
- C_MODEL_MISS only after consistent C-rule application.

Legacy SlipTrace stage outputs are not valid upstream FOM receipts.

The validator cannot prove that external source evidence is true or that a Work
task actually visited every required provider page. Those remain stage execution
responsibilities.
