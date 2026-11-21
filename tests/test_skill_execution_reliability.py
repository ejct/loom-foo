"""P1-P4 synthetic contract checks; NOT observed ChatGPT/Codex/Claude runtime tests."""
import hashlib
from types import SimpleNamespace
import json
from pathlib import Path
import runpy
import tempfile
import unittest

BASE = Path(__file__).resolve().parents[1]
ENG = BASE / "skills/loom-foo-skill-engineering"
TASK = BASE / "skills/loom-foo-agent-task-design"
VERIFY = BASE / "skills/loom-foo-change-verification"
router = SimpleNamespace(**runpy.run_path(str(ENG / "scripts/evaluate_routing_observations.py"), run_name="__routing_tests__"))

class RoutingEvidenceTests(unittest.TestCase):
    def setUp(self):
        self.cases = [{"id": "owner", "expected_owner": "loom-foo-skill-engineering"},
                      {"id": "negative", "expected_owner": "none"}]

    def test_absent_observation_is_not_pass(self):
        self.assertEqual(router.evaluate(self.cases, [])["status"], "INCOMPLETE_NOT_CONFIRMED")

    def test_model_claim_is_not_host_observation(self):
        observations = [{"case_id": "owner", "origin": "MODEL_REPORT", "trace_ref": "self",
                         "selected_owner": "loom-foo-skill-engineering", "root_read_observed": True}]
        self.assertEqual(router.evaluate(self.cases, observations)["cases"][0]["routing"], "NOT_CONFIRMED")

    def test_wrong_owner_fails(self):
        observations = [{"case_id": "owner", "origin": "HOST_TRACE", "trace_ref": "trace-1",
                         "selected_owner": "none"}]
        self.assertEqual(router.evaluate(self.cases, observations)["status"], "ROUTING_FAIL")

    def test_correct_routing_does_not_prove_read(self):
        observations = [{"case_id": "owner", "origin": "HOST_TRACE", "trace_ref": "trace-2",
                         "selected_owner": "loom-foo-skill-engineering"}]
        row = router.evaluate(self.cases, observations)["cases"][0]
        self.assertEqual((row["routing"], row["root_delivery"]), ("PASS", "NOT_CONFIRMED"))

    def test_positive_and_negative_traces(self):
        observations = [{"case_id": "owner", "origin": "HOST_TRACE", "trace_ref": "trace-3",
                         "selected_owner": "loom-foo-skill-engineering", "root_read_observed": True},
                        {"case_id": "negative", "origin": "HOST_TRACE", "trace_ref": "trace-4",
                         "selected_owner": "none"}]
        self.assertEqual(router.evaluate(self.cases, observations)["status"], "OBSERVED_WITHIN_SCOPE")

    def test_duplicate_or_unknown_cases_fail_closed(self):
        with self.assertRaises(ValueError): router.evaluate(self.cases, [{"case_id": "missing"}])
        with self.assertRaises(ValueError): router.evaluate(self.cases, [{"case_id": "owner"},{"case_id": "owner"}])

class SourceAndReadbackTests(unittest.TestCase):
    def test_source_signed_slices_opt_in(self):
        method = (TASK / "references/PD_TASK_CONSTRUCTION.md").read_text()
        root = (TASK / "SKILL.md").read_text()
        for phrase in ("source-signed", "verbatim", "abridged", "source"):
            self.assertIn(phrase, (root + method).lower())
        self.assertIn("Do not force every short task", method)
        self.assertIn("disclose", method)

    def test_semantically_incomplete_delivery_guard(self):
        delivery=(TASK / "references/INPUT_AND_OUTPUT_DELIVERY.md").read_text()
        self.assertIn("SAVED_CONTENT_INCOMPLETE",delivery)
        self.assertIn("incomplete",delivery.lower())


class OraclePermissionTests(unittest.TestCase):
    def test_edited_test_oracle_is_detectable(self):
        with tempfile.TemporaryDirectory() as tmp:
            test = Path(tmp)/"acceptance.py"
            test.write_text("assert unauthorized_is_rejected()\n")
            baseline = hashlib.sha256(test.read_bytes()).hexdigest()
            test.write_text("assert True\n")
            self.assertNotEqual(baseline, hashlib.sha256(test.read_bytes()).hexdigest())

    def test_permission_claim_and_live_proof_distinguished(self):
        policy = (VERIFY / "references/VERIFIER_INTEGRITY.md").read_text()
        role = (TASK / "references/TASK_PROFILES_AND_ASSURANCE.md").read_text()
        for name in ("INSTRUCTION_ONLY", "HOST_ENFORCED_READ_ONLY", "NOT_CONFIRMED"):
            self.assertIn(name, policy)
        self.assertIn("INSTRUCTION_ONLY", role)
        self.assertIn("synthetic", policy.lower())
        self.assertIn("shell", policy.lower())

if __name__ == "__main__":
    unittest.main()
