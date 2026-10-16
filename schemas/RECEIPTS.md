# Receipt contracts

All receipts are JSON objects with common fields:

```json
{
  "schema_version": "fom-...",
  "run_id": "FOM-...",
  "created_at": "ISO-8601 timestamp",
  "stage": "sweep|rank|decision|reconciliation|audit",
  "evidence_refs": []
}
```

## fom-sweep-v1
Requires research_queue, pending and excluded.

## fom-rank-v1
Requires assessed, focus_board, watch and drop.

## fom-decision-v1
Requires match_id, context, decision, football_thesis_state, basis,
invalidation_conditions and evidence_refs.
WAIT additionally requires wait_condition and reachability_basis.

## fom-reconciliation-v1
Requires match_id, frozen_receipt_ref, actual_result, primary_miss_class,
secondary_factors and hindsight_guard_passed.

Deep-audit output is advisory and versioned. It must name the prospective rule
change, supporting receipt IDs and regression cases.
