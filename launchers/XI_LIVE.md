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

### Mandatory screenshot disagreement gate

Use the pinned SlipTrace /xi authority and runtime.

If `xi_portable.py` returns:

```text
MARKET_DISAGREEMENT_RECHECK_REQUIRED
```

do not answer ACT/WAIT/PASS and do not freeze a FOM decision receipt.

In the same Work task:

1. complete the required football-only disagreement investigation;
2. for G4+ disagreement, verify upper-tail transferability and comparable-context evidence;
3. record the researched football fields and source/evidence refs;
4. rerun the deterministic C football certificate;
5. rerun `xi_portable.py` against the same user screenshot;
6. only after the runtime clears the gate may a final FOM decision receipt be frozen.

The market may trigger research but may never create or upgrade the C certificate by itself.

## /live

Execute C's current-state procedure with actual score, minute and material
events.

Do not recreate a prematch decision retrospectively.

## Output

Return `fom-c-decision-v1` with the same `workflow_id`,
`route_owner = FOM_WORK`, pinned authority and actual C decision.

The receipt must also record whether the screenshot market-disagreement gate was
required and whether it was cleared. If it was required, include a non-empty
research basis and evidence refs. A receipt with required=true and
completed=false is invalid.
