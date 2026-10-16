# Architecture

## Purpose

FOM v1 exists to make Football C more consistent.

SlipTrace remains the production implementation and rule authority. FOM is a
separate ChatGPT Work orchestration/audit project that:

1. loads the exact current Football C authority;
2. pins that authority revision for one workflow;
3. assigns cost-effective Work models to operational stages;
4. validates stage handoffs;
5. detects rule-application drift before proposing model changes.

## Single-model authority

There is exactly one football model:

```text
Football C
```

GPT-6 Luna, GPT-6.1 Sol and GPT-6 Astra are **operators/reviewers**, not
football models. Their answers are valid only when they follow the pinned
Football C rules.

FOM must never produce an alternative model vote.

## Authority ownership

Production rule authority lives in `acchtt/SlipTrace`.

At the beginning of a new workflow, resolve current SlipTrace `main` and freeze
its commit SHA in the sweep receipt.

Every downstream receipt in the workflow must carry the same SHA.

If current SlipTrace `main` later differs:

- existing workflow: continue with the pinned SHA unless the user explicitly
  starts/migrates the run;
- new workflow: pin the new current SHA;
- never silently combine rule files from two revisions.

See `docs/FOOTBALL_C_AUTHORITY.md`.

## Stage separation

Each stage uses a dedicated Work task and receives:

1. the previous structured receipt;
2. the factual evidence referenced by that receipt;
3. the pinned SlipTrace authority files for the stage.

It does not need another stage's private chain-of-thought.

This isolates procedural drift while preserving one rulebook.

## Consistency priorities

FOM checks, in order:

1. **Authority consistency** — same Football C revision across the run.
2. **Evidence consistency** — required facts are gathered symmetrically and
   frozen once.
3. **Rule consistency** — Football C compiler/ranking/decision rules are applied
   exactly as written.
4. **Cross-stage consistency** — rank certificates, XI upgrades, WAIT and live
   handling do not contradict earlier frozen state without named new evidence.
5. **Calibration** — only after the first four are clean should repeated misses
   be treated as possible Football C rule gaps.

## Output ownership

FOM wrapper receipts may record:

- native V4 intake status;
- C board state: FOCUS / WATCH / PASS;
- C funded certificate: G3 / G4 / G5 / G6 / NONE;
- C robustness;
- C supported burden;
- C ACT / WAIT / PASS;
- operational FOLLOW / RESERVE / STOP;
- consistency checks.

Those values are Football C outputs. FOM does not reinterpret them into a
second state system.

## Change control

Deep audit can recommend a prospective SlipTrace change.

A recommendation must first prove that the issue is not:

- stale/mixed authority;
- missing evidence;
- inconsistent evidence symmetry;
- stage handoff drift;
- incorrect application of an existing C rule;
- ordinary variance.

FOM never silently edits Football C rules.
