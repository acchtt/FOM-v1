# Football C authority resolution

FOM never owns the football model rulebook or fixture acquisition.

## Production authority

Repository: `acchtt/SlipTrace`

SlipTrace `/sweep` remains the sole source of the canonical V4 sweep bundle.

At FOM `/intake`:

1. receive an existing canonical V4 bundle;
2. resolve current SlipTrace `main`;
3. record the exact 40-character commit SHA;
4. read `models/football/CURRENT_MODEL.md` at that SHA;
5. verify Football C is the only active model;
6. verify the supplied bundle is a valid V4 handoff;
7. freeze the SHA in the FOM intake receipt.

FOM does not perform missing source acquisition.

## Stage authority paths

| FOM stage | SlipTrace authority |
|---|---|
| intake validation | `models/football/stages_v4/SWEEP.md` |
| rank | `models/football/stages_v4/RANK.md` |
| prematch decision | `models/football/prompts/02_NORMAL_CHAT_XI_ODDS.md` |
| live decision | `models/football/prompts/03_NORMAL_CHAT_LIVE.md` |
| reconciliation / deep audit | `models/football/prompts/04_WORK_POST_SLATE_AUDIT.md` |

## Invalid intake

If the canonical V4 bundle is absent, incomplete, unattested, malformed or
otherwise invalid:

```text
INTAKE_BLOCKED
```

The correct recovery is to run/fix the normal SlipTrace `/sweep`, not to let
FOM crawl fixtures independently.

## Authority change

If SlipTrace main advances after a workflow starts, do not silently switch rule
revisions. Existing runs keep the pinned revision unless explicitly migrated.
