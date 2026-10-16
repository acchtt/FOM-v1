# Work model routing

FOM uses ChatGPT Work only. There is no OpenAI API dependency.

The Work models are execution roles around one Football C authority.

## Default routing

| Stage | Model | Effort | Role |
|---|---|---:|---|
| Sweep/intake | GPT-6 Luna | Medium | source acquisition checks and V4 contract execution |
| Rank | GPT-6.1 Sol | Medium | complete Football C evidence and rule application |
| XI/live | GPT-6.1 Sol | Medium | current Football C assessment/decision policy |
| Reconcile | GPT-6 Luna | Medium | structured outcome/process classification |
| Deep audit | GPT-6 Astra | Low | independent consistency and rule-gap audit |

## Escalation policy

- Sweep stays on Luna; malformed acquisition should fail closed rather than
  escalating model capability.
- Rank moves 6.1 Sol Medium → High only for a genuinely ambiguous C evidence
  case, not because the slate is large.
- XI/live uses High only when material current evidence conflicts.
- Reconcile normally stays on Luna.
- Astra is reserved for `/audit deep`, repeated structural failures, or an
  explicit user request.

## Important distinction

Changing the Work model does **not** change the football model.

```text
Luna worker ┐
Sol worker  ├──> same pinned Football C rules
Astra audit ┘
```

Astra cannot overrule C with its own football opinion. It can identify that C
was applied inconsistently or propose a prospective C rule change.

## Cost discipline

Load only:

- the current stage launcher;
- the incoming FOM consistency receipt;
- the exact pinned SlipTrace authority files;
- evidence referenced by the receipt.

Do not load the entire Football v2 history for routine work.
