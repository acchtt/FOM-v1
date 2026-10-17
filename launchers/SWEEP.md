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

For an unfinished FOM sweep checkpoint:

```text
/sweep resume <workflow_id>
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

## 2. Initial Work execution

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
4. Build the full provider-date fixture union before registry/filtering.
5. Perform the required terminal refetch for the final six hours, or the whole
   window when shorter, and reconcile it to the acquired union.
6. Gather the source-backed goal-history and researchability evidence already
   available for the current fixtures. Never invent missing evidence.
7. Materialize the exact V4 `source.json`.
8. Execute the pinned native stage:

   ```bash
   python models/football/stages_v4/stage.py --output v4_sweep.json sweep --source source.json
   ```

9. Preserve the native integrity hash and inspect:
   - `eligible_queue`;
   - `goal_research_queue`;
   - `pending_goal_research_count`;
   - `pending_researchability_count`;
   - `pending_discovery_count`.

## 3. FOM handoff state

Native `V4_SWEEP_READY` means the source intake is valid. It does **not**
necessarily mean the FOM route is ready for `/rank`.

Classify the FOM handoff:

### RANK_READY

Use when the native V4 receipt has at least one eligible fixture.

Pending lower-priority research may remain visible in the receipt; it does not
block ranking of the already-qualified cohort.

### RESEARCH_PENDING

Use when:

```text
eligible_count = 0
and
pending research > 0
```

This is the state shown when all source-visible candidates still need
goal-history/researchability work.

Do **not** hand this receipt to `/rank`.

Continue inside the FOM sweep task:

1. target the exact pending fixtures from `goal_research_queue`,
   `discovery_watchlist`, and researchability-pending ledger rows;
2. gather their real recent competitive results and required current-channel /
   tournament-format proof;
3. refresh current fixture status and kickoff;
4. create a **new source-observed V4 epoch** with fresh timestamps;
5. rerun native `stage.py sweep`;
6. reassess the handoff state.

Do not restart the whole worldwide/date-surface crawl merely because goal
research was pending. Preserve the already-proven acquisition surface and enrich
the pending cohort prospectively, as the pinned V4 authority permits.

If the Work turn must end before enrichment is finished, freeze a
`RESEARCH_PENDING` checkpoint and report:

```text
/sweep resume <workflow_id>
```

Never describe that checkpoint as a completed rank handoff.

### EMPTY_FINAL

Use when:

```text
eligible_count = 0
pending research = 0
```

This is an honest completed slate with no rankable goal candidates. Do not run
`/rank`.

### BLOCKED

Use for a genuine process failure:

- `SOURCE_SURFACE_BLOCKED`
- `SOURCE_COMPLETENESS_FAILED`
- `NATIVE_EXECUTION_UNAVAILABLE`

A partial fixture table is diagnostic only.

## 4. Output

Return `fom-c-sweep-v1` containing:

- FOM workflow/run IDs;
- `route_owner = FOM_WORK`;
- pinned Football C authority;
- requested window;
- FOM Work source/evidence references;
- native V4 receipt reference/status when available;
- `handoff_state`;
- eligible/pending/excluded IDs;
- blocker code when blocked;
- consistency checks.

This stage emits no C FOCUS/WATCH/PASS and no ACT/WAIT/PASS.

Only a receipt with:

```text
handoff_state = RANK_READY
```

may be passed to FOM `/rank`.

Validate before handoff:

```bash
python tools/validate_receipt.py <fom-sweep.json>
```
