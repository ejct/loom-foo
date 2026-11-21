"""Check discoverable public contributor guidance without depending on prose wording."""
from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[1]


class PublicGuidanceTests(unittest.TestCase):
    def test_bilingual_readme_navigation_and_contribution_link(self):
        english = (ROOT / "README.md").read_text(encoding="utf-8")
        ukrainian = (ROOT / "README.uk.md").read_text(encoding="utf-8")
        for text in (english, ukrainian):
            with self.subTest(language=text[:70]):
                self.assertIn("(CONTRIBUTING.md)", text)
                self.assertIn("skills/", text)
        self.assertIn("(README.uk.md)", english)
        self.assertIn("(README.md)", ukrainian)

    def test_contribution_document_and_pr_template_exist(self):
        guidance = ROOT / "CONTRIBUTING.md"
        template = ROOT / ".github" / "PULL_REQUEST_TEMPLATE.md"
        self.assertTrue(guidance.is_file())
        self.assertTrue(template.is_file())
        content = guidance.read_text(encoding="utf-8")
        self.assertIn("scripts/validate_distribution.py", content)
        self.assertIn("unittest discover", content)
        self.assertIn("SECURITY.md", content)
        self.assertIn("PULL_REQUEST_TEMPLATE.md", content)
        self.assertTrue(template.read_text(encoding="utf-8").strip())

    def test_local_markdown_link_targets(self):
        for filename in ("README.md", "README.uk.md", "CONTRIBUTING.md", "AGENTS.md"):
            text = (ROOT / filename).read_text(encoding="utf-8")
            for target in re.findall(r"\]\(([^)]+)\)", text):
                if target.startswith(("http://", "https://", "#", "mailto:")):
                    continue
                path = (ROOT / target.split("#", 1)[0]).resolve()
                with self.subTest(document=filename, target=target):
                    self.assertTrue(path.is_relative_to(ROOT.resolve()))
                    self.assertTrue(path.exists())


if __name__ == "__main__":
    unittest.main()
