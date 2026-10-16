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
   - `models/football/stages_v4/README.md`
   - `models/football/stages_v4/source_completeness.py`
   - `models/football/stages_v4/stage.py`
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

### Work execution protocol

Do not stop after finding a plausible fixture list. A valid sweep requires the
native V4 source-completeness contract and native V4 execution.

1. Convert the requested ICT window to UTC and derive the exact
   `required_surface_keys` required by the pinned
   `source_completeness.py`.
2. Use Work's browser to open a provider's actual date/listing surfaces. Search
   results may help locate the surface, but snippets, isolated league pages and
   federation fixture pages are not proof of complete provider-date
   acquisition.
3. Exhaust every page / lazy-loaded block needed by the chosen provider and
   record the exact listing URL, observation time, provider page count,
   pages fetched, senior competition-block count, fixture count and canonical
   fixture IDs required by the current V4 manifest.
4. Build the full provider-date fixture union before applying the league
   registry. Do not assemble several hand-picked leagues and call that the date
   surface.
5. Perform the required independent terminal refetch for the final six hours
   (or the whole window when shorter) and reconcile it exactly against the
   source fixture union.
6. Only after acquisition is complete, gather the source-backed goal-history /
   researchability fields required by the pinned V4 code. Missing evidence
   stays pending exactly as V4 specifies; do not invent it and do not turn it
   into C PASS.
7. Materialize the exact `football-stages-v4` `source.json`, preserving the
   untouched acquisition evidence and timestamps.
8. Execute the native pinned stage:

   ```bash
   python models/football/stages_v4/stage.py --output v4_sweep.json sweep --source source.json
   ```

   Use the actual Work/cloud-computer clock; do not use `--now` for a live
   prospective sweep.
9. Confirm the output status is `V4_SWEEP_READY` and preserve the native
   integrity hash before creating the FOM wrapper.

If the first provider cannot support complete date-surface enumeration, try a
suitable independently checkable date/listing provider permitted by the pinned
V4 authority. Do not fail merely because the first search results are
insufficient.

If the Work environment cannot execute Python but a complete untouched
`source.json` exists, report `NATIVE_EXECUTION_UNAVAILABLE`. The pinned
SlipTrace repository documents a replay-attestation recovery path, but using it
requires an explicit repository write/authorization; do not silently push a
recovery file.

If no permitted provider can be completely enumerated after reasonable
fallback attempts, report `SOURCE_SURFACE_BLOCKED`. If native V4 rejects the
prepared manifest, report `SOURCE_COMPLETENESS_FAILED` with the exact native
validation error. These are process blockers, not Football C predictions.

A partial fixture table is diagnostic only. It is never a completed sweep and
must not be handed to `/rank`.

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
