# Football C authority resolution for FOM_WORK

FOM does not own a separate football rulebook.

## Authority source

Repository: `acchtt/SlipTrace`

At the start of a new FOM `/sweep`:

1. resolve current SlipTrace `main`;
2. record the exact commit SHA;
3. read `models/football/CURRENT_MODEL.md`;
4. verify Football C is the only active model;
5. load the stage authority files from that same revision;
6. freeze the SHA in the FOM sweep receipt.

Every downstream FOM stage uses that same pinned revision.

## Stage authority paths

| FOM stage | SlipTrace authority |
|---|---|
| /sweep | `models/football/stages_v4/SWEEP.md` |
| /rank | `models/football/stages_v4/RANK.md` |
| /xi | `models/football/prompts/02_NORMAL_CHAT_XI_ODDS.md` |
| /live | `models/football/prompts/03_NORMAL_CHAT_LIVE.md` |
| /reconcile, /audit deep | `models/football/prompts/04_WORK_POST_SLATE_AUDIT.md` |

The active engine files referenced by those documents are authoritative too.

## Same rules, separate execution

FOM may read Football C rules and engine contracts from SlipTrace.

FOM must not use legacy SlipTrace **stage outputs** as its upstream workflow
state. This distinction is fundamental:

- allowed: C rule files, V4 procedure files, public football facts;
- forbidden as upstream FOM state: legacy sweep receipt, rank board, XI/live
  decision.

## Authority change

If SlipTrace main advances during an active FOM workflow:

- report `AUTHORITY_CHANGED`;
- continue the existing workflow on its pinned SHA by default;
- start a new workflow to use the new C revision;
- never silently mix C revisions.

## Rule changes

If FOM deep audit finds a genuine C rule defect, the proposed fix belongs in
SlipTrace. FOM itself does not fork or mutate the Football C rulebook.
