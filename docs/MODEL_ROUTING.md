# Work model routing

FOM uses ChatGPT Work only. There is no OpenAI API dependency.

## Default routing

| Stage | Model | Effort | Why |
|---|---|---:|---|
| Sweep/intake | GPT-6 Luna | Medium | high-volume extraction and classification |
| Rank | GPT-6.1 Sol | Medium | main research/reasoning workload |
| XI/live | GPT-6.1 Sol | Medium | current evidence and decision reasoning |
| Reconcile | GPT-6 Luna | Medium | mechanical result comparison and miss tagging |
| Deep audit | GPT-6 Astra | Low | independent high-capability review, used sparingly |

## Escalation policy

- Sweep stays on Luna.
- Rank moves 6.1 Sol from Medium to High only for a genuinely ambiguous case.
- XI/live uses High only for materially conflicting current evidence.
- Reconcile stays on Luna unless classification itself is ambiguous.
- Astra is reserved for `/audit deep`, repeated failure patterns, or explicit request.

## Cost discipline

Load only the current stage launcher, incoming receipt, and evidence explicitly
referenced by that receipt. Do not load the entire project history for normal
operations.
