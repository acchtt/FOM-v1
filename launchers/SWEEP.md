# FOM v1 — /sweep Work launcher

Model: **GPT-6 Luna**  
Effort: **Medium**  
Route owner: **FOM_WORK**

This is the first stage of the FOM Work route. It independently executes the
current Football V4 intake procedure while using the same Football C authority.

## Invocation

```text
/sweep <requested window>
```

## 1. Start the FOM route

Create a new `workflow_id` and freeze:

```text
route_owner = FOM_WORK
```

Do not import a legacy SlipTrace sweep receipt or legacy fixture selection as
this stage's output.

Resolve current `acchtt/SlipTrace` main and, at that exact SHA, read:

- `models/football/CURRENT_MODEL.md`
- `models/football/stages_v4/SWEEP.md`
- `models/football/stages_v4/README.md`
- `models/football/stages_v4/source_completeness.py`
- `models/football/stages_v4/stage.py`

Verify Football C is the only active model and pin the SHA for this FOM
workflow.

## 2. Work execution protocol

A plausible fixture list is not a completed sweep. The FOM route must satisfy
the native V4 source-completeness contract.

1. Convert the requested ICT window to UTC and derive the exact required date
   surfaces from the pinned V4 completeness contract.
2. Use Work's browser to open a provider's actual date/listing surfaces. Search
   snippets, isolated league pages and federation fixture pages are not proof
   of complete date-surface acquisition.
3. Exhaust every required page/lazy-loaded block and record the exact listing
   URL, observation time, page counts, competition-block counts, fixture counts
   and canonical fixture IDs required by the pinned manifest.
4. Build the full provider-date fixture union **before** registry/filtering.
5. Perform the required terminal refetch for the final six hours, or the whole
   window when shorter, and reconcile it to the acquired union.
6. Only after complete acquisition, gather the source-backed goal-history and
   researchability evidence required by the pinned V4 code. Missing evidence
   remains pending; never invent it or convert it into C PASS.
7. Materialize the exact V4 `source.json`.
8. Execute the pinned native stage:

   ```bash
   python models/football/stages_v4/stage.py --output v4_sweep.json sweep --source source.json
   ```

   For a live prospective sweep use the actual Work/cloud-computer clock; do
   not fake a historical `--now`.
9. Require native status `V4_SWEEP_READY` and preserve its integrity hash
   before freezing the FOM sweep receipt.

If the first provider cannot satisfy full date-surface enumeration, try an
appropriate permitted date/listing fallback rather than stopping at a partial
fixture table.

## 3. Named blockers

If the route cannot complete, stop with a process blocker rather than a fake
sweep:

- `SOURCE_SURFACE_BLOCKED`
- `SOURCE_COMPLETENESS_FAILED`
- `NATIVE_EXECUTION_UNAVAILABLE`

A partial fixture table is diagnostic only and must never be handed to FOM
`/rank`.

## 4. Output

Return `fom-c-sweep-v1` containing:

- FOM workflow/run IDs;
- `route_owner = FOM_WORK`;
- pinned Football C authority;
- requested window;
- FOM Work source/evidence references;
- native V4 receipt reference/status when successful;
- eligible/pending/excluded IDs;
- named blocker when unsuccessful;
- consistency checks.

This stage emits no C FOCUS/WATCH/PASS and no ACT/WAIT/PASS.

Validate before handoff:

```bash
python tools/validate_receipt.py <fom-sweep.json>
```
