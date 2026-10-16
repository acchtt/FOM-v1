# FOM v1 — Work workflow

FOM v1 runs only in ChatGPT Work and remains separate from Football C.

## Dedicated Work stages

1. **FOM — SWEEP** — GPT-6 Luna / Medium
2. **FOM — RANK** — GPT-6.1 Sol / Medium
3. **FOM — XI LIVE** — GPT-6.1 Sol / Medium
4. **FOM — RECONCILE** — GPT-6 Luna / Medium
5. **FOM — DEEP AUDIT** — GPT-6 Astra / Low, only when triggered

Create a separate Work task for each stage and use the model/effort above.
Do not paste one stage's reasoning into another stage. Transfer only the
structured receipt plus the factual evidence referenced by that receipt.

## Normal sequence

```text
neutral fixture evidence
        ↓
/sweep
        ↓ sweep_receipt.json
/rank
        ↓ rank_receipt.json
/xi or /live
        ↓ decision_receipt.json
/reconcile
        ↓ reconciliation_receipt.json

repeated anomaly / explicit request only
        ↓
/audit deep
```

## Commands

- `/sweep <window>`
- `/rank <sweep receipt>`
- `/xi <rank receipt + screenshots/current evidence>`
- `/live <decision/rank receipt + score/minute/current evidence>`
- `/reconcile <frozen receipts + result>`
- `/audit deep <reconciliation set>`

## Non-negotiable isolation

FOM may not read Football C's prediction, rank, supported burden, decision,
or outcome interpretation before FOM freezes the corresponding output.
Comparison with Football C happens only after both sides are frozen.
