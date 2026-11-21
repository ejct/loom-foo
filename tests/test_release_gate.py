"""Release packaging is fail closed. Synthetic fixtures never authorize real publication."""
from __future__ import annotations

import hashlib
import importlib.util
import json
from pathlib import Path
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("public_gate", ROOT / "scripts/build_public_release.py")
gate = importlib.util.module_from_spec(spec)
spec.loader.exec_module(gate)


class PublicReleaseBoundaryTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        p = Path(self.tmp.name)
        self.source = p / "generic"
        self.source.mkdir()
        (self.source / "plugin.json").write_text('{"name":"synthetic","version":"0.0.0"}', encoding="utf-8")
        self.index = p / "approved.json"
        self.output = p / "out.zip"

    def index_with(self, approved: bool, entries=("plugin.json",)):
        self.index.write_text(json.dumps({
            "schema": 1, "origin": "reviewed-generic-source",
            "approved_by_owner": approved,
            "files": {
                name: hashlib.sha256((self.source / name).read_bytes()).hexdigest()
                for name in entries
            },
        }), encoding="utf-8")

    def test_missing_approval_rejected(self):
        self.index_with(False)
        with self.assertRaises(gate.Reject):
            gate.build(self.source, self.index, self.output)

    def test_missing_index_rejected(self):
        with self.assertRaises(OSError):
            gate.build(self.source, self.index, self.output)

    def test_synthetic_approved_index_can_build(self):
        self.index_with(True)
        self.assertEqual(gate.build(self.source, self.index, self.output), 1)
        self.assertTrue(self.output.exists())

    def test_byte_drift_refused(self):
        self.index_with(True)
        (self.source / "plugin.json").write_text("changed")
        with self.assertRaisesRegex(gate.Reject, "UNREVIEWED_BYTES"):
            gate.build(self.source, self.index, self.output)

    def test_owner_private_path_refused(self):
        p = self.source / "private" / "owner" / "PROFILE.md"
        p.parent.mkdir(parents=True)
        p.write_text("not shareable", encoding="utf-8")
        self.index_with(True, ("plugin.json", "private/owner/PROFILE.md"))
        with self.assertRaises(gate.Reject):
            gate.build(self.source, self.index, self.output)

    def test_owner_document_locator_refused(self):
        p = self.source / "skills" / "test" / "SKILL.md"
        p.parent.mkdir(parents=True)
        p.write_text("https://" + "docs.google.com/document/d/" + "12345678901234567890", encoding="utf-8")
        self.index_with(True, ("plugin.json", "skills/test/SKILL.md"))
        with self.assertRaisesRegex(gate.Reject, "private source locator"):
            gate.build(self.source, self.index, self.output)

    def test_reconciliation_root_refused(self):
        p = self.source / "reconciliation"
        p.mkdir()
        self.index_with(True)
        with self.assertRaisesRegex(gate.Reject, "MIXED PRIVATE"):
            gate.build(self.source, self.index, self.output)


if __name__ == "__main__":
    unittest.main()
