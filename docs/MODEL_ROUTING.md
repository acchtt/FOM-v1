# Work model routing

FOM uses ChatGPT Work only. There is no OpenAI API dependency.

The Work models are stage operators for the same Football C model.

## Default routing

| Stage | Model | Effort | Role |
|---|---|---:|---|
| Sweep | GPT-6 Luna | Medium | broad source acquisition, V4 intake, filtering |
| Rank | GPT-6.1 Sol | Medium | full C evidence research and C ranking |
| XI | GPT-6.1 Sol | Medium | C prematch reassessment and price policy |
| Live | GPT-6.1 Sol | Medium | C current-state reassessment |
| Reconcile | GPT-6 Luna | Medium | structured result/process comparison |
| Deep audit | GPT-6 Astra | Low | repeated consistency/rule-gap diagnosis |

## Cost discipline

- Sweep stays on Luna; split work rather than escalating the whole slate.
- Rank uses 6.1 Sol Medium by default; High only for a genuinely ambiguous
  individual case.
- XI/live uses Medium by default; High only for conflicting material evidence.
- Reconcile stays on Luna for routine classification.
- Astra is exceptional and audit-only.

## Important distinction

```text
Luna / Sol / Astra = Work operators
Football C          = football model
FOM_WORK             = execution route
```

Changing the Work model does not change the football model.

## Context discipline

Each stage loads only:

- its launcher;
- the upstream FOM receipt;
- referenced factual evidence;
- pinned Football C authority files.

Do not load legacy route stage outputs into FOM.
