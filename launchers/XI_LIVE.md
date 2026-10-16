# FOM v1 — /xi /live Work launcher

Model: **GPT-6.1 Sol**  
Effort: **Medium**  
Route owner: **FOM_WORK**

## Route gate

Accept only FOM_WORK rank/decision receipts from the same FOM workflow.
Do not use a legacy SlipTrace rank board or legacy XI/live decision as upstream
state.

## Authority

Use the workflow's pinned SlipTrace SHA.

For `/xi` load:
`models/football/prompts/02_NORMAL_CHAT_XI_ODDS.md`

For `/live` load:
`models/football/prompts/03_NORMAL_CHAT_LIVE.md`

## /xi

Execute Football C exactly:

- football assessment does not require odds;
- user screenshot is the sole price source when supplied;
- do not fetch replacement odds;
- enforce frozen-certificate upgrade guard;
- apply C WAIT reachability and price policy;
- separate observed-price evaluation from executable action.

## /live

Execute C's current-state procedure with actual score, minute and material
events.

Do not recreate a prematch decision retrospectively.

## Output

Return `fom-c-decision-v1` with the same `workflow_id`,
`route_owner = FOM_WORK`, pinned authority and actual C decision.
