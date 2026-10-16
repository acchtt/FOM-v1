# /intake — Football C consistency stage

Model: GPT-6 Luna, Medium.

This stage does **not** perform a sweep.

Authority for validating the supplied production bundle is the pinned SlipTrace
`models/football/stages_v4/SWEEP.md`.

## Input

An existing canonical production V4 bundle, normally containing:

- native `V4_SWEEP_READY` receipt;
- unchanged source snapshot;
- rank-handoff manifest when available.

## Responsibilities

- verify the bundle is present and canonical;
- verify native V4 status/integrity metadata;
- pin the Football C/SlipTrace authority revision;
- preserve the frozen eligible/pending/excluded IDs exactly;
- emit a small FOM consistency wrapper for downstream rank.

## Forbidden

- fixture discovery;
- provider date-surface crawling;
- adding/removing fixtures from the frozen sweep cohort;
- reconstructing source.json;
- creating a replacement V4 receipt;
- football prediction.

If validation fails, output `INTAKE_BLOCKED` and stop.

Output `fom-c-intake-v1`.
