# Architecture

## Purpose

FOM v1 exists to make Football C more consistent.

SlipTrace remains the production implementation, fixture-acquisition system and
Football C rule authority. FOM is a separate ChatGPT Work
orchestration/consistency project.

## No duplicate sweep

The production boundary is:

```text
SlipTrace /sweep
    ↓ canonical V4_SWEEP_READY
FOM /intake
    ↓
FOM /rank → /xi|/live → /reconcile
```

FOM `/intake` may validate the production bundle and its provenance, but it
must not:

- crawl date surfaces;
- search for additional fixtures;
- expand the requested window;
- rebuild source.json;
- repair an incomplete sweep by doing acquisition itself;
- modify the frozen eligible queue.

If the bundle is missing or invalid, FOM stops with `INTAKE_BLOCKED`.

## Single-model authority

There is exactly one football model:

```text
Football C
```

GPT-6 Luna, GPT-6.1 Sol and GPT-6 Astra are operators/reviewers, not football
models. Their answers are valid only when they follow the pinned Football C
rules.

## Authority ownership

Production rule authority lives in `acchtt/SlipTrace`.

At FOM intake, resolve current SlipTrace `main`, verify
`models/football/CURRENT_MODEL.md`, and pin the commit SHA for the FOM
workflow. Downstream receipts must carry the same SHA.

If current SlipTrace main later differs:

- existing workflow continues with the pinned SHA unless explicitly migrated;
- a new workflow pins the new main revision;
- never silently combine rule files from two revisions.

## Stage separation

Each stage uses a dedicated Work task and receives:

1. the previous structured receipt;
2. the factual evidence referenced by that receipt;
3. the pinned SlipTrace authority files for the stage.

This isolates procedural drift while preserving one rulebook and one production
sweep.

## Consistency priorities

FOM checks, in order:

1. authority consistency;
2. intake handoff integrity;
3. evidence consistency;
4. Football C rule consistency;
5. cross-stage consistency;
6. calibration only after the above are clean.

## Output ownership

FOM wrapper receipts may record native V4 intake status and actual Football C
outputs. They never redefine them.

## Change control

Deep audit may recommend a prospective SlipTrace change only after ruling out
handoff drift, evidence problems, incorrect C application and ordinary
variance.
