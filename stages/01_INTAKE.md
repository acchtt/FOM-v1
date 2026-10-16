# /intake — Football C consistency stage

Model: GPT-6 Luna, Medium.

This stage accepts the existing production V4 sweep handoff and performs
consistency validation only.

It must never discover fixtures independently.

## Authority

Pinned SlipTrace:
`models/football/stages_v4/SWEEP.md`

The file is consulted to validate the supplied V4 bundle, not to execute a
second sweep.

## Output

`fom-c-intake-v1`

If validation cannot establish a canonical V4 handoff, emit
`INTAKE_BLOCKED` and stop.
