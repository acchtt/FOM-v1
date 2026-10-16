# FOM v1 — Football C Work workflow

FOM v1 runs in ChatGPT Work as a consistency/orchestration layer around the
single active Football C model.

## Important acquisition boundary

FOM does **not** run its own sweep.

Production SlipTrace `/sweep` remains the only fixture-discovery and V4 intake
workflow. FOM starts after that sweep has produced a canonical
`V4_SWEEP_READY` bundle.

## Dedicated Work stages

1. **FOM — INTAKE** — GPT-6 Luna / Medium
2. **FOM — RANK** — GPT-6.1 Sol / Medium
3. **FOM — XI LIVE** — GPT-6.1 Sol / Medium
4. **FOM — RECONCILE** — GPT-6 Luna / Medium
5. **FOM — DEEP AUDIT** — GPT-6 Astra / Low, only when triggered

Each task loads the same pinned SlipTrace authority revision for that workflow.
Stage handoffs use structured receipts, not private reasoning.

## Normal sequence

```text
SlipTrace production /sweep
        ↓
canonical V4_SWEEP_READY bundle
        ↓
FOM /intake — validate/accept bundle only
        ↓ fom-c-intake-v1
FOM /rank — apply Football C rank rules
        ↓ fom-c-rank-v1
FOM /xi or /live — apply Football C decision rules
        ↓ fom-c-decision-v1
FOM /reconcile
        ↓ fom-c-reconciliation-v1

repeated inconsistency / explicit request only
        ↓
FOM /audit deep
```

## Stage launchers

- `/intake`: `launchers/INTAKE.md`
- `/rank`: `launchers/RANK.md`
- `/xi`, `/live`: `launchers/XI_LIVE.md`
- `/reconcile`: `launchers/RECONCILE.md`
- `/audit deep`: `launchers/DEEP_AUDIT.md`

## Commands

- `/intake <V4_SWEEP_READY bundle>`
- `/rank <intake receipt>`
- `/xi <rank receipt + screenshots/current evidence>`
- `/live <rank/decision receipt + current score/minute/evidence>`
- `/reconcile <frozen receipts + result>`
- `/audit deep <reconciliation set>`

If no valid V4 sweep bundle exists, FOM returns `INTAKE_BLOCKED` and instructs
the operator to run the normal SlipTrace `/sweep`. FOM must not compensate by
discovering fixtures itself.

## Non-negotiable model boundary

FOM may improve how Football C evidence is checked, handed off and audited. FOM
may not become a competing football prediction authority.

There are no `FOM_FOCUS`, `FOM_WATCH`, `FOM_DROP`, alternative burden
compiler, alternate WAIT rule or model-voting layer.

Every prediction-state field in FOM receipts is explicitly a **Football C**
state.
