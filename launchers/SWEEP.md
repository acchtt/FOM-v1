# FOM v1 — /sweep Work launcher

Model: **GPT-6 Luna**  
Effort: **Medium**

FOM is not a separate football model. This task executes/checks the current
Football V4 sweep contract for Football C.

## Invocation

```text
/sweep <requested window>
```

## 1. Resolve Football C authority

At the beginning of a **new workflow**:

1. resolve current `acchtt/SlipTrace` `main` commit SHA;
2. read at that exact SHA:
   - `models/football/CURRENT_MODEL.md`
   - `models/football/stages_v4/SWEEP.md`
3. verify CURRENT_MODEL says Football C is the only active model and V4 is the
   active sweep/rank path;
4. pin that SHA in the output receipt.

Do not copy old FOM intake rules over the SlipTrace authority.

## 2. Execute the V4 intake contract

Follow the pinned SlipTrace `SWEEP.md` exactly, including complete date
surfaces, current exclusions, goals-first research admission and any protected
competition exceptions defined there.

FOM must not add an alternative league policy, quota, odds gate, lineup gate or
prediction rule.

Sweep is intake only. Do not produce C FOCUS/WATCH/PASS, certificates, supported
burden or ACT/WAIT/PASS.

## 3. Output consistency wrapper

Return one `fom-c-sweep-v1` receipt containing:

- `workflow_id`;
- pinned Football C authority;
- requested window;
- native V4 receipt reference/status;
- eligible/pending/excluded match IDs;
- consistency checks.

The native V4 receipt remains the football intake authority. The FOM receipt
exists to prove which C revision and procedure were used.

Validate before freezing:

```bash
python tools/validate_receipt.py <receipt.json>
```
