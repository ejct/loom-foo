"""Offline package integrity and boundary checks. Not a routing execution test."""
from pathlib import Path
import json,re,subprocess,unittest,yaml

HERE=Path(__file__).resolve().parent.parent
ROOT=(HERE/'SKILL.md').read_text(encoding='utf-8')
SKILL='loom-foo-identity-design'
SHA={'IDENTITY_CONCEPT_AND_SYSTEM.md': '3d948ecb74230ee8d722c6efe1a5aa98dc697877', 'IDENTITY_DELIVERY_AND_QA.md': 'cc918af08526a33d9ec2f21923ce6d28bb98b4f1'}
class PackageChecks(unittest.TestCase):
    def test_metadata(self):
        match=re.match(r'^---\n(.*?)\n---\n',ROOT,re.S)
        self.assertIsNotNone(match)
        fm=yaml.safe_load(match.group(1))
        self.assertEqual(fm['name'],SKILL)
        self.assertEqual(fm['metadata']['family'],'design')
        self.assertEqual(fm['metadata']['version'],'0.5.0')
    def test_references(self):
        names=set(re.findall(r'`references/([^`]+\.md)`',ROOT))
        self.assertGreaterEqual(len(names),3)
        for name in names: self.assertTrue((HERE/'references'/name).is_file(), name)
    def test_source_references_unchanged(self):
        for name,sha in SHA.items():
            actual=subprocess.check_output(['git','hash-object',str(HERE/'references'/name)],text=True).strip()
            self.assertEqual(actual,sha)
    def test_owner_boundaries(self):
        for other in ('loom-foo-typography','loom-foo-design-review','loom-foo-icon-design'):
            self.assertIn(other,ROOT)
        self.assertIn('loom-foo-graphic-design',ROOT)
    def test_authority_and_fidelity(self):
        for token in ['PRESERVE', 'CHANGE', 'APPROXIMATE_REVISION', 'trademark', 'vector']:
            self.assertIn(token.lower(),ROOT.lower())
    def test_fixture_oracles_are_not_claims(self):
        data=json.loads((HERE/'tests'/'routing_and_behavior_cases.json').read_text(encoding='utf-8'))
        self.assertEqual(data['metadata']['kind'],'proposed_oracle_not_execution_observation')
        self.assertEqual(len(data['cases']),10)
        owners=[c['owner'] for c in data['cases']]
        self.assertIn(SKILL,owners)
        self.assertTrue(any(o!=SKILL for o in owners))
    def test_invalid_version_guard(self):
        altered=ROOT.replace('version: "0.5.0"','version: "999.invalid"',1)
        self.assertNotEqual(altered,ROOT)
        front=yaml.safe_load(re.match(r'^---\n(.*?)\n---\n',altered,re.S).group(1))
        self.assertNotEqual(front['metadata']['version'],'0.5.0')
    def test_missing_reference_guard(self):
        ref=next(iter(SHA))
        path=HERE/'references'/ref
        self.assertTrue(path.exists())
        nonexistent=path.parent/(ref+'.missing')
        self.assertFalse(nonexistent.exists())
if __name__=='__main__': unittest.main()
