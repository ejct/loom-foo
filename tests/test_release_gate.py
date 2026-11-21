"""Fail-closed public packaging regressions; all fixture approvals are synthetic."""
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
        self.index = p / "synthetic-review.json"
        self.output = p / "out.zip"

        self.write("SKILL_INVENTORY.json", json.dumps({
            "bundle": "loom-foo", "bundle_version": "0.0.0",
            "skills": [{"id": "loom-foo-test", "version": "0.0.0"}]
        }))
        self.write("skills/loom-foo-test/SKILL.md",
                   "---\nname: loom-foo-test\ndescription: Synthetic test fixture\n"
                   "metadata:\n  version: '0.0.0'\n---\n\nTest body\n")
        for name in ("README.md", "LICENSE", "PUBLISHER.md", "ATTRIBUTION.md",
                     "PRIVACY.md", "TERMS.md", "SUPPORT.md", "SECURITY.md"):
            self.write(name, "synthetic " + name + "\n")

        logo = "./assets/loom-foo-mark-v3.png"
        iface = {"logo": logo, "composerIcon": logo}
        self.write("plugin.json", json.dumps({
            "name": "loom-foo", "version": "0.0.0",
            "extensions": {"com.openai": {"interface": iface}}
        }))
        self.write(".codex-plugin/plugin.json", json.dumps({
            "name": "loom-foo", "version": "0.0.0", "interface": iface
        }))
        self.write(".claude-plugin/plugin.json", json.dumps({
            "name": "loom-foo", "version": "0.0.0"
        }))
        self.write(".antigravity-plugin/plugin.json", json.dumps({
            "name": "loom-foo", "version": "0.0.0", "logo": "assets/loom-foo-mark-v3.png"
        }))
        self.write("gemini-extension.json", json.dumps({
            "name": "loom-foo", "version": "0.0.0"
        }))
        self.write("assets/loom-foo-mark-v3.png", "synthetic placeholder bytes")

    def write(self, name: str, text: str):
        file = self.source / name
        file.parent.mkdir(parents=True, exist_ok=True)
        file.write_text(text, encoding="utf-8")

    def files(self):
        return tuple(sorted(p.relative_to(self.source).as_posix()
                            for p in self.source.rglob("*") if p.is_file()))

    def index_with(self, approved=True, entries=None):
        if entries is None:
            entries = self.files()
        self.index.write_text(json.dumps({
            "schema": 1, "origin": "reviewed-generic-source",
            "approved_by_owner": approved,
            "files": {name: hashlib.sha256((self.source / name).read_bytes()).hexdigest()
                      for name in entries},
        }), encoding="utf-8")

    def test_valid_complete_synthetic_package(self):
        self.index_with()
        self.assertEqual(gate.build(self.source, self.index, self.output), len(self.files()))
        self.assertTrue(self.output.exists())

    def test_unapproved_index_rejected(self):
        self.index_with(False)
        with self.assertRaisesRegex(gate.Reject, "owner review"):
            gate.build(self.source, self.index, self.output)

    def test_missing_index_rejected(self):
        with self.assertRaises(OSError):
            gate.build(self.source, self.index, self.output)

    def test_byte_drift_rejected(self):
        self.index_with()
        self.write("plugin.json", "unexpected")
        with self.assertRaisesRegex(gate.Reject, "UNREVIEWED_BYTES"):
            gate.build(self.source, self.index, self.output)

    def test_missing_brand_asset_rejected(self):
        self.index_with(entries=[p for p in self.files() if not p.startswith("assets/")])
        with self.assertRaisesRegex(gate.Reject, "MISSING_BRAND_ASSET"):
            gate.build(self.source, self.index, self.output)

    def test_missing_skill_root_rejected(self):
        self.index_with(entries=[p for p in self.files() if not p.endswith("/SKILL.md")])
        with self.assertRaisesRegex(gate.Reject, "INCOMPLETE_SKILL_TREE"):
            gate.build(self.source, self.index, self.output)

    def test_unapproved_new_reference_rejected(self):
        self.index_with()
        self.write("skills/loom-foo-test/references/extra.md", "source added after review")
        with self.assertRaisesRegex(gate.Reject, "INCOMPLETE_SKILL_TREE"):
            gate.build(self.source, self.index, self.output)

    def test_inconsistent_platform_version_rejected(self):
        self.write(".claude-plugin/plugin.json",
                   '{"name":"loom-foo","version":"99.0.0"}')
        self.index_with()
        with self.assertRaisesRegex(gate.Reject, "manifest identity/version drift"):
            gate.build(self.source, self.index, self.output)

    def test_missing_attribution_rejected(self):
        self.index_with(entries=[p for p in self.files() if p != "ATTRIBUTION.md"])
        with self.assertRaisesRegex(gate.Reject, "INCOMPLETE_RELEASE"):
            gate.build(self.source, self.index, self.output)

    def test_missing_publisher_rejected(self):
        self.index_with(entries=[p for p in self.files() if p != "PUBLISHER.md"])
        with self.assertRaisesRegex(gate.Reject, "INCOMPLETE_RELEASE"):
            gate.build(self.source, self.index, self.output)

    def test_missing_terms_rejected(self):
        self.index_with(entries=[p for p in self.files() if p != "TERMS.md"])
        with self.assertRaisesRegex(gate.Reject, "INCOMPLETE_RELEASE"):
            gate.build(self.source, self.index, self.output)

    def test_owner_private_path_rejected(self):
        self.write("private/owner/PROFILE.md", "private")
        self.index_with()
        with self.assertRaises(gate.Reject):
            gate.build(self.source, self.index, self.output)

    def test_private_document_locator_rejected(self):
        self.write("skills/loom-foo-test/references/private.md",
                   "https://" + "docs.google.com/document/d/" + "12345678901234567890")
        self.index_with()
        with self.assertRaisesRegex(gate.Reject, "private source locator"):
            gate.build(self.source, self.index, self.output)

    def test_installed_private_plugin_id_rejected(self):
        path = self.source / "SKILL_INVENTORY.json"
        data = json.loads(path.read_text(encoding="utf-8"))
        data["plugin_release_id"] = "plugin" + "rel_synthetic-private-install"
        self.write("SKILL_INVENTORY.json", json.dumps(data))
        self.index_with()
        with self.assertRaisesRegex(gate.Reject, "private development source identifier"):
            gate.build(self.source, self.index, self.output)

    def test_internal_upstream_identifier_rejected(self):
        self.write("README.md", "Source: ejct/" + "LoomDev")
        self.index_with()
        with self.assertRaisesRegex(gate.Reject, "private development source identifier"):
            gate.build(self.source, self.index, self.output)

    def test_public_export_rejects_deprecated_brand(self):
        self.write("README.md", "Former product " + "Loom" + "Loom")
        self.index_with()
        with self.assertRaisesRegex(gate.Reject, "deprecated product brand"):
            gate.build(self.source, self.index, self.output)

    def test_missing_composer_icon_field_rejected(self):
        data = json.loads((self.source / "plugin.json").read_text(encoding="utf-8"))
        del data["extensions"]["com.openai"]["interface"]["composerIcon"]
        self.write("plugin.json", json.dumps(data))
        self.index_with()
        with self.assertRaisesRegex(gate.Reject, "missing native brand reference"):
            gate.build(self.source, self.index, self.output)

    def test_reconciliation_tree_rejected(self):
        (self.source / "reconciliation").mkdir()
        self.index_with()
        with self.assertRaisesRegex(gate.Reject, "MIXED PRIVATE"):
            gate.build(self.source, self.index, self.output)


if __name__ == "__main__":
    unittest.main()
