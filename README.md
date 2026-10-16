# FOM v1

FOM v1 is the **ChatGPT Work execution route for Football C**.

It is not a second football model and it is not a checker layered on top of the
existing SlipTrace conversation workflow. It is a complete alternative route
that executes the same Football C model through isolated Work stages.

## Two routes, one model

```text
LEGACY_SLIPTRACE route
/sweep → /rank → /xi → /live → /audit
                 │
                 └── Football C

FOM_WORK route
/sweep → /rank → /xi → /live → /reconcile → /audit deep
                 │
                 └── Football C
```

A workflow is owned by exactly one route. Stage outputs from the two routes must
not be mixed inside the same workflow.

## Core rules

- **Football C is the sole football prediction authority.**
- FOM loads Football C rules from a pinned `acchtt/SlipTrace` revision.
- FOM executes its own Work-stage `/sweep → /rank → /xi → /live` chain.
- FOM does not consume legacy SlipTrace sweep/rank/decision outputs for the same
  workflow.
- Every FOM receipt carries `route_owner = FOM_WORK`.
- FOM has no alternate burden compiler, ranking formula, or ACT/WAIT/PASS policy.
- FOM does not write SlipTrace production state during evaluation unless the
  user explicitly promotes the route.
- No OpenAI API or third-party orchestrator is required.

## Work model routing

| FOM stage | Work model | Default effort |
|---|---|---:|
| /sweep | GPT-6 Luna | Medium |
| /rank | GPT-6.1 Sol | Medium |
| /xi | GPT-6.1 Sol | Medium |
| /live | GPT-6.1 Sol | Medium |
| /reconcile | GPT-6 Luna | Medium |
| /audit deep | GPT-6 Astra | Low |

Different Work models are operators around the same Football C rulebook.

Read `WORKFLOW.md`, `docs/ROUTE_OWNERSHIP.md`,
`docs/FOOTBALL_C_AUTHORITY.md`, and the stage launchers before operating FOM.
