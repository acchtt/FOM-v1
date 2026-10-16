"""Offline contract smoke tests: python -m unittest discover -s tests -v"""
import datetime as dt
import json
import pathlib
import sys
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))
from validate_receipt import validate  # noqa: E402

SCHEMA = json.loads((ROOT / "schemas/fom-receipt-v1.schema.json").read_text())
NOW = "2026-10-16T15:00:00+00:00"


def base(version, stage):
    return {"schema_version": version, "run_id": "FOM-test-001",
            "stage": stage, "created_at": NOW, "evidence_refs": []}


class ReceiptTests(unittest.TestCase):
    def test_sweep_valid_and_window_order(self):
        x = {**base("fom-sweep-v1", "sweep"),
             "requested_window": {"start": NOW, "end": "2026-10-16T16:00:00+00:00"},
             "research_queue": [], "pending": [], "excluded": []}
        self.assertEqual(validate(x, SCHEMA), [])
        x["requested_window"]["end"] = NOW
        self.assertTrue(validate(x, SCHEMA))

    def test_rank_partition(self):
        x = {**base("fom-rank-v1", "rank"), "sweep_receipt_ref": "FOM-sweep-1",
             "assessed": [{"match_id": "m1", "state": "FOM_FOCUS",
                           "basis": "reason", "evidence_refs": []}],
             "focus_board": ["m1"], "watch": [], "drop": []}
        self.assertEqual(validate(x, SCHEMA), [])
        x["focus_board"] = []
        self.assertTrue(validate(x, SCHEMA))

    def test_wait_requires_reachability(self):
        x = {**base("fom-decision-v1", "decision"), "match_id": "m1",
             "rank_receipt_ref": "FOM-rank-1", "context": {"phase": "prematch"},
             "decision": "WAIT", "football_thesis_state": "intact",
             "basis": "conditional", "invalidation_conditions": []}
        self.assertTrue(validate(x, SCHEMA))
        x["wait_condition"] = "A"
        x["reachability_basis"] = "B"
        self.assertEqual(validate(x, SCHEMA), [])

    def test_live_requires_score_and_minute(self):
        x = {**base("fom-decision-v1", "decision"), "match_id": "m1",
             "rank_receipt_ref": "FOM-rank-1", "context": {"phase": "live"},
             "decision": "PASS", "football_thesis_state": "invalid",
             "basis": "route closed", "invalidation_conditions": []}
        self.assertTrue(validate(x, SCHEMA))
        x["context"].update(minute=42, home_score=1, away_score=0)
        self.assertEqual(validate(x, SCHEMA), [])

    def test_reconciliation_valid(self):
        x = {**base("fom-reconciliation-v1", "reconciliation"),
             "match_id": "m1", "frozen_receipt_ref": "FOM-dec-1",
             "actual_result": {"home_score": 2, "away_score": 1},
             "primary_miss_class": "NORMAL_VARIANCE",
             "secondary_factors": [], "hindsight_guard_passed": True}
        self.assertEqual(validate(x, SCHEMA), [])

    def test_audit_valid(self):
        x = {**base("fom-audit-v1", "audit"), "trigger": "explicit_request",
             "reconciliation_refs": ["FOM-rec-1"], "proposed_rule": "proposal only",
             "affected_stage": "rank", "supporting_receipt_ids": ["FOM-rank-1"],
             "regression_cases": ["case-1"],
             "prospective_knowability_basis": "known before kickoff",
             "advisory_only": True}
        self.assertEqual(validate(x, SCHEMA), [])

    def test_reject_unexpected_field(self):
        x = {**base("fom-sweep-v1", "sweep"),
             "requested_window": {"start": NOW, "end": "2026-10-16T16:00:00+00:00"},
             "research_queue": [], "pending": [], "excluded": [], "football_c_rank": 1}
        self.assertTrue(validate(x, SCHEMA))


if __name__ == "__main__":
    unittest.main()
