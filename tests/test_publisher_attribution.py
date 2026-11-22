"""Static candidate checks: publisher, old-brand exclusion, icons deferred."""
from __future__ import annotations
import json
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
MANIFESTS = ("plugin.json", ".codex-plugin/plugin.json",
             ".claude-plugin/plugin.json", ".antigravity-plugin/plugin.json")
TEXT_SUFFIXES = {".md", ".json", ".yaml", ".yml", ".py", ".txt", ".sh"}


class PublisherAttributionCandidateTests(unittest.TestCase):
    def read(self, rel):
        return (ROOT / rel).read_text(encoding="utf-8")

    def manifest(self, rel):
        return json.loads(self.read(rel))

    def test_publisher_identity_consistent_without_personal_email(self):
        for rel in MANIFESTS:
            with self.subTest(manifest=rel):
                source = self.manifest(rel)
                self.assertEqual(source["author"], {
                    "name": "ejct",
                    "url": "https://github.com/ejct",
                })
                self.assertNotIn("email", source["author"])
        root = self.manifest("plugin.json")
        codex = self.manifest(".codex-plugin/plugin.json")
        self.assertEqual("ejct", root["extensions"]["com.openai"]["interface"]["developerName"])
        self.assertEqual("ejct", codex["interface"]["developerName"])
        self.assertEqual(root["extensions"]["com.openai"]["interface"], codex["interface"])

    def test_current_mit_notice_and_unresolved_original_rights(self):
        license_text = self.read("LICENSE")
        self.assertTrue(license_text.startswith("MIT License\n"))
        self.assertIn("Copyright (c) 2026 ejct and contributors", license_text)
        self.assertIn("The above copyright notice and this permission notice", license_text)
        self.assertIn("WITHOUT WARRANTY", license_text)
        attribution = self.read("ATTRIBUTION.md")
        self.assertIn("pending confirmation", attribution)
        self.assertIn("third-party", attribution)
        self.assertIn("Do not publish", attribution)

    def test_no_brand_retained_in_current_generic_source(self):
        old_name = "Loom" + "Loom"
        scanned = 0
        for path in ROOT.rglob("*"):
            if (not path.is_file() or path.suffix.lower() not in TEXT_SUFFIXES
                    or ".git" in path.relative_to(ROOT).parts):
                continue
            with self.subTest(path=path.relative_to(ROOT).as_posix()):
                self.assertNotIn(old_name, path.read_text(encoding="utf-8"))
            scanned += 1
        self.assertGreater(scanned, 240)

    def test_unverified_private_reporting_and_icon_deferment(self):
        publisher = self.read("PUBLISHER.md")
        status = self.read("RELEASE_STATUS.md")
        attribution = self.read("ATTRIBUTION.md")
        self.assertIn("no verified dedicated private privacy-contact channel", publisher)
        self.assertIn("only if enabled", publisher)
        self.assertIn("not cleared for publication", self.read("README.md"))
        self.assertIn("PUBLICATION_BLOCKED", status)
        self.assertIn("no bundled icon images", attribution)
        self.assertIn("separate pass", attribution)
        self.assertNotIn("Lucide", attribution)
        root = self.manifest("plugin.json")["extensions"]["com.openai"]["interface"]
        codex = self.manifest(".codex-plugin/plugin.json")["interface"]
        for iface in (root, codex):
            self.assertNotIn("logo", iface)
            self.assertNotIn("composerIcon", iface)
        self.assertNotIn("logo", self.manifest(".antigravity-plugin/plugin.json"))
        self.assertFalse((ROOT / "assets").exists())

    def test_rebranded_handoff_contract_is_not_an_old_protocol_claim(self):
        handoff = self.read("skills/loom-foo-handoff/SKILL.md")
        framing = self.read("skills/loom-foo-handoff/references/CHAT_TEXT_TRANSPORT.md")
        self.assertIn('version: "0.9.0"', handoff)
        self.assertIn("Protocol: loom-foo Chat/Text Handoff v0.3", framing)

    def test_bundle_version_and_skill_versions(self):
        inventory = self.manifest("SKILL_INVENTORY.json")
        self.assertEqual("0.44.0", inventory["bundle_version"])
        self.assertEqual({x["id"] for x in inventory["skills"]}, {p.name for p in (ROOT / "skills").iterdir() if p.is_dir()})
        for rel in MANIFESTS + ("gemini-extension.json",):
            with self.subTest(manifest=rel):
                self.assertEqual(inventory["bundle_version"], self.manifest(rel)["version"])


if __name__ == "__main__":
    unittest.main()
