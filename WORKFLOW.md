# FOM v1 — Work-only Football C workflow

FOM v1 is a complete alternative Football C execution route built from isolated
ChatGPT Work tasks.

## Route ownership

At FOM `/sweep`, the workflow is frozen with:

```text
route_owner = FOM_WORK
```

Every downstream FOM receipt must keep the same `workflow_id`,
`route_owner`, and pinned Football C authority SHA.

For that workflow, do not substitute outputs from the legacy SlipTrace route.

## Dedicated Work stages

1. **FOM — SWEEP** — GPT-6 Luna / Medium
2. **FOM — RANK** — GPT-6.1 Sol / Medium
3. **FOM — XI LIVE** — GPT-6.1 Sol / Medium
4. **FOM — RECONCILE** — GPT-6 Luna / Medium
5. **FOM — DEEP AUDIT** — GPT-6 Astra / Low, exceptional only

Each stage normally runs as its own Work task. Transfer structured receipts and
referenced factual evidence, not another stage's private reasoning.

## Normal FOM route

```text
FOM /sweep
GPT-6 Luna
    ↓ fom-c-sweep-v1
FOM /rank
GPT-6.1 Sol
    ↓ fom-c-rank-v1
FOM /xi or /live
GPT-6.1 Sol
    ↓ fom-c-decision-v1
FOM /reconcile
GPT-6 Luna
    ↓ fom-c-reconciliation-v1

repeated structural issue / explicit request only
    ↓
FOM /audit deep
GPT-6 Astra
```

## Commands

- `/sweep <window>`
- `/rank <fom-c-sweep-v1 receipt>`
- `/xi <fom-c-rank-v1 receipt + current evidence/screenshots>`
- `/live <fom-c-rank-v1 or decision receipt + current state>`
- `/reconcile <frozen FOM receipts + result>`
- `/audit deep <FOM reconciliation set>`

## No cross-route handoff

The FOM route must not accept a legacy SlipTrace stage receipt as its upstream
stage result.

Neutral factual sources may of course be the same. The prohibition is on
**stage outputs and decisions**, not on public football facts.

If the user wants the legacy route, use SlipTrace end-to-end. If the user wants
FOM, use FOM end-to-end for that workflow.

## Football authority

Both routes use Football C. FOM pins the SlipTrace revision that defines C and
applies those rules without creating a second model.
