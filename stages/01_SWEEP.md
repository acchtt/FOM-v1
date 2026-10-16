# /sweep — Football C consistency stage

Model: GPT-6 Luna, Medium.

Authority is the pinned SlipTrace
`models/football/stages_v4/SWEEP.md`.

FOM does not define a second intake model.

## Responsibilities

- resolve and pin current Football C authority for a new workflow;
- apply the native V4 acquisition/intake contract exactly;
- preserve current user exclusions and protected exceptions from SlipTrace;
- record native V4 output references;
- detect missing evidence or procedure drift;
- continue acquisition through permitted provider fallbacks until the native V4
  completeness contract is satisfied or a named blocker is proven;
- materialize the exact V4 `source.json` and execute the pinned native
  `stage.py sweep` before declaring the sweep complete;
- distinguish `SOURCE_SURFACE_BLOCKED`, `SOURCE_COMPLETENESS_FAILED` and
  `NATIVE_EXECUTION_UNAVAILABLE` from a valid `V4_SWEEP_READY`;
- emit no football prediction.

## Forbidden

- alternate FOM research/admission rules;
- fixed board cap;
- odds or lineup blockers not present in current V4;
- FOM prediction states;
- retrospective fixture admission;
- treating search snippets, isolated league/federation pages or a partial
  fixture table as complete provider-date acquisition;
- stopping after the first inadequate provider when a permitted complete
  date/listing fallback remains available.

Output `fom-c-sweep-v1`.
