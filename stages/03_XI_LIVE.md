# /xi and /live — Football C consistency stage

Model: GPT-6.1 Sol, Medium.

## Authority

Use the same pinned SlipTrace SHA as the rank receipt.

Prematch authority:
`models/football/prompts/02_NORMAL_CHAT_XI_ODDS.md`

Live authority:
`models/football/prompts/03_NORMAL_CHAT_LIVE.md`

## /xi

Apply the current Football C policy exactly:

- complete football assessment without requiring odds;
- use only a user screenshot when screenshot-only evidence is supplied;
- do not search replacement odds;
- enforce the frozen-certificate upgrade guard;
- apply C WAIT reachability requirements;
- preserve C price rules;
- distinguish observed quote evaluation from executable action.

Do not create a FOM-specific ACT/WAIT/PASS policy.

## /live

Apply the current C live procedure to actual score/minute/material events.

Do not recreate a prematch decision retrospectively and do not manufacture a
live execution policy.

## Output

Freeze `fom-c-decision-v1` recording the actual C decision plus consistency
checks and the pinned authority revision.
