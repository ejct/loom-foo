"""Publisher/attribution candidate checks: static only, no legal clearance."""
from __future__ import annotations

import json
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
MANIFESTS = ("plugin.json", ".codex-plugin/plugin.json",
             ".claude-plugin/plugin.json", ".antigravity-plugin/plugin.json")


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
        compat = self.manifest(".codex-plugin/plugin.json")
        self.assertEqual("ejct", root["extensions"]["com.openai"]["interface"]["developerName"])
        self.assertEqual("ejct", compat["interface"]["developerName"])
        self.assertEqual(root["extensions"]["com.openai"]["interface"], compat["interface"])

    def test_original_legacy_mit_copyright_preserved(self):
        license_text = self.read("LICENSE")
        self.assertTrue(license_text.startswith("MIT License\n"))
        self.assertIn("Copyright (c) 2026 LoomLoom contributors", license_text)
        self.assertIn("The above copyright notice and this permission notice", license_text)
        self.assertIn("WITHOUT WARRANTY", license_text)
        self.assertIn("LoomLoom contributors", self.read("ATTRIBUTION.md"))

    def test_unverified_private_reporting_and_asset_claims_not_promoted(self):
        publisher = self.read("PUBLISHER.md")
        status = self.read("RELEASE_STATUS.md")
        attribution = self.read("ATTRIBUTION.md")
        self.assertIn("no verified dedicated private privacy-contact channel", publisher)
        self.assertIn("only if enabled", publisher)
        self.assertIn("NOT", publisher.upper())
        self.assertIn("not cleared for publication", self.read("README.md"))
        self.assertIn("publication", status.lower())
        self.assertIn("Lucide", attribution)
        self.assertIn("no checked-in vector/raster icon images or fonts", attribution)
        self.assertIn("have not been recovered", attribution)

    def test_bundle_version_is_unchanged(self):
        inventory = self.manifest("SKILL_INVENTORY.json")
        self.assertEqual("0.41.1", inventory["bundle_version"])
        self.assertEqual(40, len(inventory["skills"]))
        for rel in MANIFESTS + ("gemini-extension.json",):
            with self.subTest(manifest=rel):
                self.assertEqual(inventory["bundle_version"], self.manifest(rel)["version"])


if __name__ == "__main__":
    unittest.main()
