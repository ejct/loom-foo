"""Local link validation only; no network and no runtime routing claims."""
from __future__ import annotations
import importlib.util
from pathlib import Path
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("distribution_gate", ROOT / "scripts/validate_distribution.py")
gate = importlib.util.module_from_spec(spec)
spec.loader.exec_module(gate)


class MarkdownLinkTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)

    def file(self, path, data):
        p = self.root / path
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(data, encoding="utf-8")
        return p

    def test_valid_local_reference(self):
        self.file("skills/example/SKILL.md", "[Ref](references/one.md)\n")
        self.file("skills/example/references/one.md", "content\n")
        self.assertEqual([], gate.broken_relative_markdown_links(self.root))

    def test_missing_reference_fails(self):
        self.file("skills/example/SKILL.md", "[Ref](references/missing.md)\n")
        self.assertEqual(1, len(gate.broken_relative_markdown_links(self.root)))

    def test_optional_fixture_without_link(self):
        self.file("SKILL.md", "Optional developer fixture tests/cases.jsonl is not bundled.\n")
        self.assertEqual([], gate.broken_relative_markdown_links(self.root))

    def test_external_and_anchor_links_are_skipped(self):
        self.file("SKILL.md", "[site](https://example.org/x) [heading](#hello)\n")
        self.assertEqual([], gate.broken_relative_markdown_links(self.root))

    def test_fenced_code_is_not_document_link(self):
        fence = chr(96) * 3
        self.file("SKILL.md", fence + "markdown\n[Example](missing.md)\n" + fence + "\n")
        self.assertEqual([], gate.broken_relative_markdown_links(self.root))

    def test_rejects_escape_outside_repo(self):
        self.file("SKILL.md", "[Unsafe](../../missing.md)\n")
        self.assertEqual(1, len(gate.broken_relative_markdown_links(self.root)))


if __name__ == "__main__":
    unittest.main()
