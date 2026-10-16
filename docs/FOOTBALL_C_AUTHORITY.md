# Football C authority resolution

FOM never owns the football model rulebook.

## Production authority

Repository: `acchtt/SlipTrace`

For every **new** FOM workflow:

1. resolve current SlipTrace `main`;
2. record the exact 40-character commit SHA;
3. read `models/football/CURRENT_MODEL.md` at that SHA;
4. verify Football C is the only active model;
5. load the stage-specific authority file at that same SHA;
6. freeze the SHA in the first FOM receipt.

Downstream stages inherit the pinned SHA.

## Stage authority paths

| FOM stage | SlipTrace authority |
|---|---|
| sweep | `models/football/stages_v4/SWEEP.md` |
| rank | `models/football/stages_v4/RANK.md` |
| prematch decision | `models/football/prompts/02_NORMAL_CHAT_XI_ODDS.md` |
| live decision | `models/football/prompts/03_NORMAL_CHAT_LIVE.md` |
| reconciliation / deep audit | `models/football/prompts/04_WORK_POST_SLATE_AUDIT.md` |

The active engine files referenced by those documents remain authoritative too.

## Authority change

If SlipTrace `main` advances after a workflow has started:

- do not silently switch rule revisions;
- mark `AUTHORITY_CHANGED`;
- existing run continues with the pinned revision by default;
- a new workflow pins the new main revision;
- migration of an in-flight run requires explicit user instruction.

This makes cross-stage differences diagnosable instead of allowing rule drift.

## No local fork

FOM may document orchestration and consistency checks, but must not copy and
modify Football C rules into a local alternative rulebook.

If deep audit finds a genuine model-rule defect, the fix belongs in SlipTrace
through a prospective, tested change.
