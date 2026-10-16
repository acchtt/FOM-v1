# FOM v1 — Football C Work workflow

FOM v1 runs in ChatGPT Work as a consistency/orchestration layer around the
single active Football C model.

## Dedicated Work stages

1. **FOM — SWEEP** — GPT-6 Luna / Medium
2. **FOM — RANK** — GPT-6.1 Sol / Medium
3. **FOM — XI LIVE** — GPT-6.1 Sol / Medium
4. **FOM — RECONCILE** — GPT-6 Luna / Medium
5. **FOM — DEEP AUDIT** — GPT-6 Astra / Low, only when triggered

Each task loads the **same pinned SlipTrace authority revision** for that
workflow. Stage handoffs use structured receipts, not private reasoning.

## Normal sequence

```text
resolve latest SlipTrace main
        ↓
pin Football C authority SHA
        ↓
/sweep  — apply V4 intake contract
        ↓ fom-c-sweep-v1
/rank   — apply Football C rank rules
        ↓ fom-c-rank-v1
/xi or /live — apply Football C decision rules
        ↓ fom-c-decision-v1
/reconcile — check execution/model outcome
        ↓ fom-c-reconciliation-v1

repeated inconsistency / explicit request only
        ↓
/audit deep — consistency-first audit
```

## Stage launchers

- `/sweep`: `launchers/SWEEP.md`
- `/rank`: `launchers/RANK.md`
- `/xi`, `/live`: `launchers/XI_LIVE.md`
- `/reconcile`: `launchers/RECONCILE.md`
- `/audit deep`: `launchers/DEEP_AUDIT.md`

## Commands

- `/sweep <window>`
- `/rank <sweep receipt>`
- `/xi <rank receipt + screenshots/current evidence>`
- `/live <rank/decision receipt + current score/minute/evidence>`
- `/reconcile <frozen receipts + result>`
- `/audit deep <reconciliation set>`

## Non-negotiable model boundary

FOM may improve how Football C evidence is gathered, checked, handed off and
audited. FOM may not become a competing football prediction authority.

There are no `FOM_FOCUS`, `FOM_WATCH`, `FOM_DROP`, alternative burden
compiler, alternate WAIT rule or model-voting layer.

Every prediction-state field in FOM receipts is explicitly a **Football C**
state.
