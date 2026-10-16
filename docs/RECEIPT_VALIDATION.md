# FOM v1 receipt validation

FOM receipts are **Football C consistency wrappers**, not alternative-model
receipts.

- `schemas/fom-receipt-v1.schema.json` defines five wrapper receipt types.
- `tools/validate_receipt.py` validates receipts offline with Python's standard
  library.
- `tests/test_receipts.py` covers state, authority and cross-stage invariants.

Run:

```bash
python tools/validate_receipt.py path/to/intake.json path/to/rank.json
python -m unittest discover -s tests -v
```

The validator checks:

- active model is exactly Football C;
- authority repository is exactly `acchtt/SlipTrace`;
- a 40-character SlipTrace commit SHA is pinned;
- each stage names the correct authority file;
- all receipts in one workflow use the same authority SHA;
- rank official board contains exactly C-FOCUS rows;
- there is no FOM-specific prediction state;
- WAIT has a reachable condition and basis;
- live decisions contain score/minute;
- the production sweep window carried by intake is valid;
- intake certifies that no fixture discovery was performed; downstream references do not cross workflows when both receipts are supplied.

The validator cannot prove that web evidence is true, that the referenced
SlipTrace commit exists, or that native Football C Python execution actually
occurred. Those are Work-stage responsibilities.
