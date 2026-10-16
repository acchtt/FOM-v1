# FOM v1 — /intake Work launcher

Model: **GPT-6 Luna**  
Effort: **Medium**

This launcher validates an existing production V4 sweep bundle. It must never
perform fixture acquisition.

## Invocation

```text
/intake <canonical V4_SWEEP_READY bundle>
```

## Required input

Use the production SlipTrace sweep output, normally:

- native `V4_SWEEP_READY` receipt;
- unchanged source snapshot;
- rank-handoff manifest when supplied.

Do not substitute a hand-built fixture list.

## Authority gate

1. resolve current `acchtt/SlipTrace` main;
2. read `models/football/CURRENT_MODEL.md`;
3. verify Football C is the only active model;
4. use `models/football/stages_v4/SWEEP.md` only to validate the supplied
   native bundle;
5. pin the exact SlipTrace commit SHA in the intake wrapper.

## Validation only

Allowed:
- inspect the supplied bundle;
- check V4 status/integrity/provenance;
- copy frozen eligible/pending/excluded IDs into the wrapper;
- detect an invalid or incomplete handoff.

Forbidden:
- web-searching for fixtures to complete the window;
- provider date-surface crawling;
- adding missed fixtures;
- rebuilding source.json;
- generating a replacement V4 receipt;
- changing the frozen cohort.

If the native bundle is not valid, return:

```text
INTAKE_BLOCKED
```

and tell the operator to run/fix the normal SlipTrace `/sweep`.

## Output

Return exactly one `fom-c-intake-v1` receipt conforming to
`schemas/fom-receipt-v1.schema.json`.

Validate together with downstream receipts using:

```bash
python tools/validate_receipt.py <intake.json> <rank.json>
```
