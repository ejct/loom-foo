"""Static contract and package integrity only. Does NOT test live host activation or actual Core repair."""
from pathlib import Path
import json
import re
import unittest
import yaml

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / 'SKILL.md'

class ProjectIntegrationPackage(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.text = SKILL.read_text(encoding='utf-8')
        cls.fm = yaml.safe_load(cls.text.split('---',2)[1])
        cls.behavior = json.loads((ROOT/'tests/behavior_cases.json').read_text(encoding='utf-8'))

    def test_metadata(self):
        self.assertEqual(clsname := self.fm['name'], ROOT.name)
        self.assertEqual(clsname, 'loom-foo-project-integration')
        self.assertEqual(self.fm['metadata']['family'],'planning')
        self.assertEqual(self.fm['metadata']['version'],'0.5.0')

    def test_inherited_authority(self):
        for term in ('One user-facing product','Original outcome first','Platform-controlled availability',
                     'NO_SETUP', 'EXISTING_CORE', 'SETUP_PROPOSED', 'SETUP_AUTHORIZED', 'LOCAL_INSPECTION_NEEDED',
                     'foo-loom-bootstrap','mutable branch HEAD','do not implement an Auto/Off/On switch'):
            with self.subTest(term=term):self.assertIn(term.lower(),self.text.lower())

    def test_partial_contract(self):
        for term in ('PARTIAL_SETUP','PROJECT_STATE_RECOVERY.md','interrupted','symlink','managed block'):
            self.assertIn(term,self.text)
        self.assertIn('No Core ceremony',self.text)

    def test_reference_paths_exist(self):
        names=set(re.findall(r'references/([A-Za-z0-9_.-]+\.md)', self.text))
        self.assertEqual(names, {'PROJECT_STATE_RECOVERY.md','PD_AUTHORIZED_SETUP.md','PROJECT_SETUP_HANDOFF.md'})
        for name in names:self.assertTrue((ROOT/'references'/name).is_file())

    def test_nontrigger_reference_load_guards(self):
        self.assertIn('**not for** clean new setup',self.text)
        self.assertIn('do not load for read-only analysis',self.text)
        self.assertIn('not generic Task Briefs',self.text)

    def test_authorized_setup_respects_pin(self):
        s=(ROOT/'references/PD_AUTHORIZED_SETUP.md').read_text()
        for term in ('immutable', 'source', 'AGENTS.md', 'safe copy', 'policies', 'verify exact pin', 'never silently upgrade'):
            self.assertTrue(term.lower() in s.lower() or term in self.text, term)

    def test_safe_recovery(self):
        s=(ROOT/'references/PROJECT_STATE_RECOVERY.md').read_text()
        for term in ('PARTIAL_SETUP','symlink','legacy','managed', 'direct evidence', 'concurrent','approval','permission','Bootstrap'):
            with self.subTest(term=term):
                self.assertIn(term.lower(),(s+' '+self.text).lower())

    def test_unavailable_workspace_handoff(self):
        s=(ROOT/'references/PROJECT_SETUP_HANDOFF.md').read_text()
        for term in ('read-only preflight','lock alone','local project','not','partial/drifted'):
            self.assertIn(term.lower(),(s+' '+self.text).lower())

    def test_routing_negative_and_neighbor(self):
        cases=self.behavior['cases']; kinds={c['kind'] for c in cases}
        self.assertEqual(kinds,{'positive','negative','neighbor','safety'})
        self.assertGreaterEqual(len(cases),12)
        self.assertFalse(next(c for c in cases if c['id']=='partial-lock-only')['writes_allowed'])
        self.assertFalse(next(c for c in cases if c['id']=='feature-only-approval')['writes_allowed'])

    def test_ui_metadata(self):
        m=yaml.safe_load((ROOT/'agents/openai.yaml').read_text())
        self.assertEqual(m['interface']['display_name'],'Project Integration')
        self.assertEqual(m['interface']['brand_color'],'#F2B705')

    def test_no_private_identifier_pattern(self):
        for file in ROOT.rglob('*'):
            if file.is_file() and file.suffix in ('.md','.json','.py','.yaml'):
                s=file.read_text()
                self.assertNotRegex(s,r'sk-proj-[A-Za-z0-9_-]{10,}')
                self.assertNotRegex(s,r'docs\.google\.com/document/d/[A-Za-z0-9_-]{20,}')

    @staticmethod
    def validate_subject(text, existing_references):
        fm=yaml.safe_load(text.split('---',2)[1])
        problems=[]
        if fm.get('metadata',{}).get('version')!='0.5.0': problems.append('version mismatch')
        paths=set(re.findall(r'references/([A-Za-z0-9_.-]+\.md)', text))
        for name in sorted(paths-existing_references): problems.append('missing reference: '+name)
        return problems

    def test_version_mutation_is_detected(self):
        original=self.text
        mutated=original.replace('version: "0.5.0"','version: "0.4.1"',1)
        self.assertNotEqual(original,mutated)
        existing={p.name for p in (ROOT/'references').glob('*.md')}
        self.assertEqual([],self.validate_subject(original,existing))
        self.assertIn('version mismatch',self.validate_subject(mutated,existing))

    def test_missing_reference_mutation_is_detected(self):
        existing={p.name for p in (ROOT/'references').glob('*.md')}
        self.assertEqual([],self.validate_subject(self.text,existing))
        missing='PROJECT_STATE_RECOVERY.md'
        self.assertIn(missing,existing)
        self.assertIn('missing reference: '+missing,self.validate_subject(self.text,existing-{missing}))

if __name__=='__main__':unittest.main()
