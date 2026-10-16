# FOM v1

FOM v1 is a standalone experimental football-model workflow operated entirely
through ChatGPT Work.

It is intentionally isolated from SlipTrace / Football C production.

## Core boundary

- No imports from SlipTrace.
- No reads of Football C rankings, burdens, FOCUS/WATCH/PASS states or decisions
  before FOM freezes its own output.
- No writes to Football C production state.
- No API or third-party orchestrator is required.
- Stage-to-stage communication uses structured receipts only.

## Work model routing

| Stage | Work model | Default effort |
|---|---|---|
| Sweep / intake | GPT-6 Luna | Medium |
| Rank / football research | GPT-6.1 Sol | Medium |
| XI / live decision | GPT-6.1 Sol | Medium |
| Routine result reconciliation | GPT-6 Luna | Medium |
| Deep audit / recalibration | GPT-6 Astra | Low |

Escalate effort only when the stage procedure explicitly requires it.

See `docs/ARCHITECTURE.md` and `docs/MODEL_ROUTING.md` after the initial
scaffold is merged.
