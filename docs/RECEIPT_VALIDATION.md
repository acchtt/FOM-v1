# FOM v1 receipt validation

This is a contract-only implementation, not a fixture collector or a model rule change.

- `schemas/fom-receipt-v1.schema.json` defines five versioned JSON receipt types.
- `tools/validate_receipt.py` validates these receipts offline with Python's standard library.
- `tests/test_receipts.py` covers valid receipts and selected rejection cases.

Run after saving a frozen receipt:

```bash
python tools/validate_receipt.py path/to/sweep.json path/to/rank.json
python -m unittest discover -s tests -v
```

Validation failures return a non-zero exit code. There is no network, database, API, or Football C dependency.

The validator checks required fields, enumerations, timestamps with offsets, WAIT reachability fields, live score/minute fields, sweep window ordering, unique ranked match IDs, and partition consistency between assessed rows and focus/watch/drop.

**Scope limitations:** This is a minimal validator, not a full JSON Schema engine. It does not verify that external evidence URLs resolve, that receipts are cryptographically frozen, that upstream receipts exist, or that all fixtures were discovered. The JSON Schema file can also be checked with a standards-compliant JSON Schema 2020-12 validator when one is available.

Changes to stage execution and fixture acquisition are deliberately deferred.
