# Architecture

## Purpose

FOM v1 is an independent shadow football model. It exists to test whether a
separate research and decision architecture adds useful signal without
contaminating Football C.

## Independence boundary

FOM has its own repository, Work tasks, receipts, terminology and audit trail.

Before a FOM output is frozen, prohibited inputs include:

- Football C rank/order;
- Football C FOCUS/WATCH/PASS state;
- Football C supported burden;
- Football C ACT/WAIT/PASS decision;
- Football C model commentary;
- post-match knowledge.

Allowed shared inputs are neutral facts: fixture identity, kickoff,
competition, team/player news, source-backed form, tournament context,
score/minute for live work, and user-provided market screenshots when a
decision stage explicitly accepts them.

## Stage separation

Each stage is an isolated Work task.

A downstream task receives:
1. the upstream immutable receipt;
2. cited factual evidence needed to verify it;
3. the current stage launcher.

It does not receive upstream private reasoning or conversational history.

## FOM research dimensions

FOM v1 intentionally does not clone Football C. Rank research is organized
around these independent dimensions:

- scoring creation;
- concession vulnerability;
- game-state elasticity;
- tail sustainability into goals 3/4/5;
- two-sided route independence;
- tournament incentive;
- lineup robustness;
- evidence confidence and transferability.

## Output states

Rank uses `FOM_FOCUS`, `FOM_WATCH`, and `FOM_DROP`.
There is no quota or fixed board-size cap.

Decision stages use `ACT`, `WAIT`, and `PASS`.
WAIT must state a reachable condition.

## Comparison

FOM versus Football C comparison is a post-freeze audit operation only.
Disagreement is evidence, not a voting or consensus mechanism.
