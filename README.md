# FOM v1

FOM v1 is the **Football C consistency and Work orchestration layer**.

It is not a second football model. Football C remains the only prediction
authority. FOM exists to make Football C execution more consistent across
/rank, /xi, /live and /audit while using cost-effective ChatGPT Work models for
different operational jobs.

## Core boundary

- **SlipTrace `/sweep` is the sole fixture-acquisition authority.**
- FOM never performs a second fixture crawl or rebuilds a V4 sweep.
- FOM begins from an existing canonical `V4_SWEEP_READY` bundle.
- **Football C is the only football model.**
- FOM must apply the current Football C rulebook from `acchtt/SlipTrace`.
- FOM must not invent alternative model states, burden rules or decision rules.
- A workflow pins one SlipTrace commit SHA and keeps that authority revision
  unchanged across downstream stages.
- If SlipTrace changes mid-run, FOM reports `AUTHORITY_CHANGED` instead of
  silently mixing rule versions.
- No OpenAI API or third-party orchestrator is required.

## Work model routing

| Stage | Work model | Default effort | Role |
|---|---|---:|---|
| Intake / handoff check | GPT-6 Luna | Medium | validate existing production V4 bundle only |
| Rank / C research | GPT-6.1 Sol | Medium | prepare and apply Football C research consistently |
| XI / live | GPT-6.1 Sol | Medium | apply current Football C decision policy |
| Reconcile | GPT-6 Luna | Medium | classify process/model misses mechanically |
| Deep audit | GPT-6 Astra | Low | independent consistency/rule-gap review |

Different Work models are workers around **one Football C rulebook**, not
different prediction models.

Start with `WORKFLOW.md`, `docs/FOOTBALL_C_AUTHORITY.md`, and the stage
launchers.
