"""Static candidate sanity checks; do not assert host routing or task quality."""
import json
import unittest
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
TEXT = (ROOT / "SKILL.md").read_text(encoding="utf-8")
FRONT = yaml.safe_load(TEXT.split("---", 2)[1])
CASES = json.loads((ROOT / "tests" / "routing_cases.json").read_text(encoding="utf-8"))


class OnboardingCandidateContract(unittest.TestCase):
    def test_exact_identity_and_version(self):
        self.assertEqual(FRONT["name"], ROOT.name)
        self.assertEqual(FRONT["metadata"]["version"], "0.3.0")
        self.assertEqual(FRONT["metadata"]["family"], "engineering")

    def test_positive_and_negative_discovery(self):
        self.assertIn("already installed plugin", FRONT["description"])
        for label in ("Positive triggers", "Non-triggers", "ALREADY_INSTALLED_TRYOUT", "RESUME_TASK"):
            self.assertIn(label, TEXT)

    def test_l1_effect_boundary(self):
        for rule in ("not a prerequisite for ordinary skill use", "No welcome tour", "automatic host routing", "Never silently edit"):
            self.assertIn(rule, TEXT)

    def test_native_interface_unchanged(self):
        interface = yaml.safe_load((ROOT / "agents" / "openai.yaml").read_text(encoding="utf-8"))["interface"]
        self.assertEqual(interface, {"display_name": "Loom-foo Onboarding", "short_description": "Start with a relevant Loom-foo skill and real task", "brand_color": "#F2B705"})

    def test_fixture_shape_and_uniqueness(self):
        self.assertEqual(CASES["skill"], FRONT["name"])
        self.assertEqual(CASES["version"], FRONT["metadata"]["version"])
        cases = CASES["cases"]
        self.assertEqual(len(cases), len({c["id"] for c in cases}))
        self.assertGreaterEqual(len(cases), 10)
        for c in cases:
            self.assertTrue(c["prompt"].strip())
            self.assertIn(c["expected_path"], {"NONE", "RESUME_TASK", "FIRST_USE", "ALREADY_INSTALLED_TRYOUT", "SETUP_CHECK"})
            self.assertIn(c["expected_effect"], {"not_onboarding", "options_only", "real_task", "demo", "no_unapproved_mutation"})

    def test_negative_neighbor_and_first_use_examples(self):
        ids = {c["id"] for c in CASES["cases"]}
        self.assertTrue({"routine_ux", "direct_brief", "skill_rewrite", "project_integration", "installed_tryout", "demo_requested", "interrupted_user_task"}.issubset(ids))
        for c in CASES["cases"]:
            if c["expected_path"] == "NONE":
                self.assertNotEqual(c["expected_owner"], FRONT["name"])


if __name__ == "__main__":
    unittest.main()
