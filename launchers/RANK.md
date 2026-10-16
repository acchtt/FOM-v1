# FOM v1 — /rank Work launcher

Model: **GPT-6.1 Sol**  
Effort: **Medium**

## Invocation

```text
/rank <fom-c-intake-v1 receipt>
```

## Authority gate

Read `football_c_authority.commit_sha` from the intake receipt.

At that exact SlipTrace SHA load:

- `models/football/CURRENT_MODEL.md`;
- `models/football/stages_v4/RANK.md`;
- active Football C engine/rule files referenced by the authority.

If current SlipTrace `main` differs, report `AUTHORITY_CHANGED` but do not
silently switch this run.

## Task

Execute/check the current Football C rank procedure exactly.

Do not create an independent FOM score, state, supported line or ranking key.

Required consistency checks include:

- original V4/source/status contract satisfied;
- complete eligible cohort researched or explicitly accounted for;
- price-blind C assessment;
- C certificate compiler used exactly;
- C ranking key used exactly;
- official board contains every and only C-FOCUS row;
- no numeric board cap;
- FOLLOW/RESERVE/STOP treated as operational lane, not a second selector.

## Output

Return `fom-c-rank-v1` wrapping the C result and the same pinned authority SHA.

Validate before handoff:

```bash
python tools/validate_receipt.py <intake.json> <rank.json>
```
