"""Offline Football C consistency contract tests."""
import json
import pathlib
import sys
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))
from validate_receipt import validate, validate_bundle  # noqa: E402

SCHEMA = json.loads((ROOT / "schemas/fom-receipt-v1.schema.json").read_text())
NOW = "2026-10-16T15:00:00+00:00"
SHA = "a" * 40
OTHER_SHA = "b" * 40


def authority(stage_path, sha=SHA):
    return {
        "repository": "acchtt/SlipTrace",
        "commit_sha": sha,
        "active_model": "C",
        "current_model_path": "models/football/CURRENT_MODEL.md",
        "stage_authority_path": stage_path,
    }


def base(version, stage, run_id, stage_path, sha=SHA):
    return {
        "schema_version": version,
        "workflow_id": "FOMC-workflow-001",
        "run_id": run_id,
        "route_owner": "FOM_WORK",
        "stage": stage,
        "created_at": NOW,
        "evidence_refs": [],
        "football_c_authority": authority(stage_path, sha),
    }


def sweep(run_id="FOMC-sweep-001", sha=SHA):
    return {
        **base(
            "fom-c-sweep-v1",
            "sweep",
            run_id,
            "models/football/stages_v4/SWEEP.md",
            sha,
        ),
        "requested_window": {
            "start": NOW,
            "end": "2026-10-16T16:00:00+00:00",
        },
        "native_receipt_ref": "V4-test",
        "native_receipt_status": "V4_SWEEP_READY",
        "eligible_match_ids": ["m1"],
        "pending_match_ids": [],
        "excluded_match_ids": [],
        "consistency_checks": {
            "complete_date_surface_contract_applied": True,
            "standing_exclusions_applied": True,
            "no_odds_or_lineup_blocker_added": True,
            "no_c_prediction_emitted": True,
        },
    }


def rank(run_id="FOMC-rank-001", sha=SHA):
    return {
        **base(
            "fom-c-rank-v1",
            "rank",
            run_id,
            "models/football/stages_v4/RANK.md",
            sha,
        ),
        "sweep_receipt_ref": "FOMC-sweep-001",
        "c_execution_ref": "C-board-001",
        "assessed": [
            {
                "match_id": "m1",
                "c_board_state": "FOCUS",
                "funded_certificate": "G3",
                "robustness": "ROBUST",
                "supported_line": 2.5,
                "follow_lane": "FOLLOW",
                "evidence_refs": [],
            },
            {
                "match_id": "m2",
                "c_board_state": "WATCH",
                "funded_certificate": "G3",
                "robustness": "FRAGILE",
                "follow_lane": "STOP",
                "evidence_refs": [],
            },
        ],
        "official_board": ["m1"],
        "consistency_checks": {
            "full_cohort_researched": True,
            "focus_only_board_admission": True,
            "no_fixed_numeric_cap": True,
            "price_blind_ranking": True,
            "same_authority_revision": True,
        },
    }


class ReceiptTests(unittest.TestCase):
    def test_sweep_valid_and_window_order(self):
        x = sweep()
        self.assertEqual(validate(x, SCHEMA), [])
        x["requested_window"]["end"] = NOW
        self.assertTrue(validate(x, SCHEMA))

    def test_sweep_buckets_are_disjoint(self):
        x = sweep()
        x["excluded_match_ids"] = ["m1"]
        self.assertTrue(validate(x, SCHEMA))

    def test_legacy_route_owner_is_rejected(self):
        x = sweep()
        x["route_owner"] = "LEGACY_SLIPTRACE"
        self.assertTrue(validate(x, SCHEMA))

    def test_bundle_rejects_wrong_upstream_stage_type(self):
        s = sweep()
        r = rank()
        r["sweep_receipt_ref"] = r["run_id"]
        errors = validate_bundle([s, r])
        self.assertTrue(any("must reference fom-c-sweep-v1" in e for e in errors))

    def test_rank_board_is_exactly_c_focus(self):
        x = rank()
        self.assertEqual(validate(x, SCHEMA), [])
        x["official_board"] = []
        self.assertTrue(validate(x, SCHEMA))

    def test_alternate_fom_prediction_state_is_rejected(self):
        x = rank()
        x["assessed"][0]["c_board_state"] = "FOM_FOCUS"
        self.assertTrue(validate(x, SCHEMA))

    def test_wrong_stage_authority_path_is_rejected(self):
        x = rank()
        x["football_c_authority"]["stage_authority_path"] = (
            "models/football/stages_v4/SWEEP.md"
        )
        self.assertTrue(validate(x, SCHEMA))

    def test_wait_requires_reachability(self):
        x = {
            **base(
                "fom-c-decision-v1",
                "decision",
                "FOMC-dec-001",
                "models/football/prompts/02_NORMAL_CHAT_XI_ODDS.md",
            ),
            "rank_receipt_ref": "FOMC-rank-001",
            "c_execution_ref": "C-xi-001",
            "match_id": "m1",
            "context": {"phase": "prematch"},
            "c_decision": "WAIT",
            "c_board_state": "FOCUS",
            "basis": "C conditional execution state",
            "invalidation_conditions": [],
            "price_evidence_mode": "USER_SCREENSHOT_ONLY",
            "consistency_checks": {
                "same_authority_revision": True,
                "no_replacement_odds": True,
                "certificate_upgrade_guard_applied": True,
                "wait_reachability_checked": True,
                "no_retrospective_prematch_action": True,
            },
        }
        self.assertTrue(validate(x, SCHEMA))
        x["wait_condition"] = "O2.5 reaches required C price"
        x["reachability_basis"] = "reachable from the observed screenshot state"
        self.assertEqual(validate(x, SCHEMA), [])

    def test_live_requires_live_authority_and_score_minute(self):
        x = {
            **base(
                "fom-c-decision-v1",
                "decision",
                "FOMC-live-001",
                "models/football/prompts/03_NORMAL_CHAT_LIVE.md",
            ),
            "rank_receipt_ref": "FOMC-rank-001",
            "c_execution_ref": "C-live-001",
            "match_id": "m1",
            "context": {"phase": "live"},
            "c_decision": "PASS",
            "c_board_state": "FOCUS",
            "basis": "current C route no longer supports action",
            "invalidation_conditions": [],
            "price_evidence_mode": "LIVE_COMPARISON_ONLY",
            "consistency_checks": {
                "same_authority_revision": True,
                "no_replacement_odds": True,
                "certificate_upgrade_guard_applied": True,
                "wait_reachability_checked": True,
                "no_retrospective_prematch_action": True,
            },
        }
        self.assertTrue(validate(x, SCHEMA))
        x["context"].update(minute=42, home_score=1, away_score=0)
        self.assertEqual(validate(x, SCHEMA), [])

    def test_c_model_miss_requires_consistent_application(self):
        x = {
            **base(
                "fom-c-reconciliation-v1",
                "reconciliation",
                "FOMC-rec-001",
                "models/football/prompts/04_WORK_POST_SLATE_AUDIT.md",
            ),
            "frozen_receipt_ref": "FOMC-dec-001",
            "match_id": "m1",
            "actual_result": {"home_score": 1, "away_score": 0},
            "primary_issue_class": "C_MODEL_MISS",
            "secondary_factors": [],
            "rule_application_consistent": False,
            "prospective_evidence_only": True,
        }
        self.assertTrue(validate(x, SCHEMA))
        x["rule_application_consistent"] = True
        self.assertEqual(validate(x, SCHEMA), [])

    def test_audit_is_advisory_and_consistency_first(self):
        x = {
            **base(
                "fom-c-audit-v1",
                "audit",
                "FOMC-audit-001",
                "models/football/prompts/04_WORK_POST_SLATE_AUDIT.md",
            ),
            "trigger": "explicit_request",
            "reconciliation_refs": ["FOMC-rec-001"],
            "finding_type": "RULE_GAP",
            "affected_stage": "rank",
            "proposed_action": "propose a prospective SlipTrace patch",
            "supporting_receipt_ids": ["FOMC-rank-001"],
            "regression_cases": ["case-1"],
            "prospective_knowability_basis": "evidence existed before kickoff",
            "consistency_first_checked": True,
            "requires_sliptrace_change": True,
            "advisory_only": True,
        }
        self.assertEqual(validate(x, SCHEMA), [])

    def test_bundle_rejects_mixed_football_c_authority(self):
        s = sweep()
        r = rank(sha=OTHER_SHA)
        errors = validate_bundle([s, r])
        self.assertTrue(errors)
        self.assertTrue(any("mixed Football C authority" in e for e in errors))

    def test_bundle_accepts_same_authority(self):
        self.assertEqual(validate_bundle([sweep(), rank()]), [])


if __name__ == "__main__":
    unittest.main()
