#!/usr/bin/env python3
"""Dependency-free package/fixture integrity checks. NOT agent runtime evaluation."""
from pathlib import Path
import json
import re
import unittest

ROOT = Path(__file__).resolve().parents[1]
ID = "loom-foo-email-intake"
REQUIRED_REFS = {
    "SOURCE_COVERAGE.md", "EPISODE_RECONSTRUCTION.md", "EMAIL_TRUST.md", "GMAIL.md"
}

class PackageIntegrity(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.skill = (ROOT / "SKILL.md").read_text(encoding="utf-8")
        cls.head = cls.skill.split("---", 2)[1]
        cls.route = json.loads((ROOT / "tests/routing_cases.json").read_text(encoding="utf-8"))
        cls.behavior = json.loads((ROOT / "tests/behavior_cases.json").read_text(encoding="utf-8"))

    def test_frontmatter_and_identity(self):
        self.assertEqual(ROOT.name, ID)
        for clause in ["name: " + ID, 'version: "0.8.0"', 'family: "knowledge"', 'authority: "read-only"']:
            self.assertIn(clause, self.head)
        self.assertRegex(self.head, r'description:\s*"[^\n]{40,500}"')
        self.assertTrue(re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", ID))
        self.assertLessEqual(len(ID), 64)

    def test_every_referenced_file_exists(self):
        refs = set(re.findall(r"references/([A-Z_]+\.md)", self.skill))
        self.assertEqual(refs, REQUIRED_REFS)
        self.assertEqual({p.name for p in (ROOT / "references").glob("*.md")}, REQUIRED_REFS)

    def test_critical_contract_and_owners(self):
        for clause in ["Read-only", "untrusted", "SOURCE_UNAVAILABLE", "PARTIAL_INTAKE", "EVIDENCE_READY", "loom-foo-link-intake", "loom-foo-knowledge-intake", "not", "same model context", "Email Evidence Packet"]:
            self.assertIn(clause.lower(), self.skill.lower())

    def test_history_vs_fictitious_releases(self):
        h = (ROOT / "LINEAGE.md").read_text(encoding="utf-8")
        c = (ROOT / "CHANGELOG.md").read_text(encoding="utf-8")
        self.assertIn("first independently packaged", h)
        self.assertIn("first standalone", c.lower())
        self.assertIn("not evidence", c.lower())
        self.assertEqual(len(re.findall(r"(?m)^## \d+\.\d+\.\d+", c)), 1)

    def test_fixture_integrity(self):
        self.assertGreaterEqual(len(self.route), 12)
        self.assertGreaterEqual(len(self.behavior), 12)
        self.assertEqual(len({x['id'] for x in self.route}), len(self.route))
        self.assertEqual(len({x['id'] for x in self.behavior}), len(self.behavior))
        expected_modes = {"LOOKUP", "EPISODE", "DELTA", "SECURITY_INSPECTION", "NOT_TRIGGER"}
        for case in self.route:
            self.assertTrue(case['prompt'].strip())
            self.assertIn(case['expected_mode'], expected_modes)
            self.assertTrue(case['expected_owner'].strip())
            self.assertTrue(case['reason'].strip())
            self.assertIsInstance(case['expected_refs'], list)
            for ref in case['expected_refs']:
                self.assertIn(ref, REQUIRED_REFS)
        for case in self.behavior:
            self.assertTrue(all(case.get(k) for k in ("scenario", "expected", "contract")))
        self.assertGreaterEqual(sum(x['expected_mode'] == 'NOT_TRIGGER' for x in self.route), 6)
        self.assertGreaterEqual(sum(x['expected_mode'] != 'NOT_TRIGGER' for x in self.route), 6)

    def test_reference_security_and_scope(self):
        txt = "\n".join(p.read_text(encoding="utf-8") for p in (ROOT / "references").glob("*.md"))
        for clause in ["PARTIAL", "truncated", "Spam", "source", "ATTEMPT", "EXTERNAL_STATE_UNKNOWN", "next_page_token", "prompt injection"]:
            self.assertIn(clause.lower(), txt.lower())

    def test_no_private_source_payloads_or_actions(self):
        source = "\n".join(p.read_text(encoding="utf-8") for p in ROOT.rglob("*.md"))
        self.assertNotRegex(source, r"https?://(?:docs|drive)\.google\.com/(?:document/d/|file/d/|drive/folders/)[A-Za-z0-9_-]{16,}")
        self.assertNotRegex(source, r"(?:ghp|gho|ghs|github_pat)_[A-Za-z0-9_]{20,}")
        self.assertNotRegex(source, r"sk" + r"-proj-[A-Za-z0-9_-]{30,}")
        self.assertFalse(list(ROOT.rglob("*.eml")))
        self.assertFalse(list(ROOT.rglob("*.mbox")))

if __name__ == "__main__":
    unittest.main(verbosity=2)
