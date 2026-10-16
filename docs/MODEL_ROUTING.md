# Work model routing

FOM uses ChatGPT Work only. There is no OpenAI API dependency.

The Work models are execution roles around one Football C authority.

## Default routing

| Stage | Model | Effort | Role |
|---|---|---:|---|
| Intake | GPT-6 Luna | Medium | validate existing V4 handoff; no acquisition |
| Rank | GPT-6.1 Sol | Medium | complete Football C evidence and rule application |
| XI/live | GPT-6.1 Sol | Medium | current Football C assessment/decision policy |
| Reconcile | GPT-6 Luna | Medium | structured outcome/process classification |
| Deep audit | GPT-6 Astra | Low | independent consistency and rule-gap audit |

## Escalation policy

- Intake stays on Luna and fails closed on an invalid/missing V4 bundle.
- Rank moves 6.1 Sol Medium → High only for a genuinely ambiguous C evidence
  case, not because the slate is large.
- XI/live uses High only when material current evidence conflicts.
- Reconcile normally stays on Luna.
- Astra is reserved for `/audit deep`, repeated structural failures, or an
  explicit user request.

## Important distinction

Changing the Work model does not change the football model, and FOM does not
duplicate the production sweep.

```text
SlipTrace /sweep
      ↓
Luna intake check ┐
Sol rank/XI       ├──> same pinned Football C rules
Astra audit       ┘
```

## Cost discipline

Load only the current stage launcher, incoming consistency receipt, exact pinned
SlipTrace authority files and referenced evidence. Do not repeat fixture
discovery inside FOM.
