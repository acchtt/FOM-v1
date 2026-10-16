# FOM v1 — /xi /live Work launcher

Model: **GPT-6.1 Sol**  
Effort: **Medium**

## Authority gate

Use the same SlipTrace SHA pinned in the rank receipt.

For `/xi` load:
`models/football/prompts/02_NORMAL_CHAT_XI_ODDS.md`

For `/live` load:
`models/football/prompts/03_NORMAL_CHAT_LIVE.md`

Also load `models/football/CURRENT_MODEL.md` at that SHA.

## /xi

Apply Football C only.

- finish football assessment without requiring odds;
- when the user provides a screenshot, use that exact screenshot only;
- never fetch replacement odds;
- enforce the frozen-certificate upgrade guard;
- apply C WAIT reachability and price policy;
- do not convert observed-price comparison into executable action unless the C
  execution contract permits it.

## /live

Apply current C live-state assessment with actual score/minute/material events.

Do not recreate prematch action retrospectively.

## Output

Return `fom-c-decision-v1` with the actual C decision and consistency checks.
No FOM-specific decision policy is permitted.
