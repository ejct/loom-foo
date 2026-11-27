#!/usr/bin/env python3
"""Offline source/contract checks; do not claim runtime skill activation."""
import json
from pathlib import Path
import re
import unittest
ROOT = Path(__file__).resolve().parents[1]
ID = 'loom-foo-email-intake'
REFS = {'SOURCE_COVERAGE.md','EPISODE_RECONSTRUCTION.md','EMAIL_TRUST.md','GMAIL.md','MONITOR_COMPOSITION.md'}
class Contract(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.skill=(ROOT/'SKILL.md').read_text('utf-8')
        cls.refs='\n'.join(p.read_text('utf-8') for p in (ROOT/'references').glob('*.md'))
    def test_identity_version(self):
        self.assertEqual(ROOT.name, ID)
        head=self.skill.split('---',2)[1]
        for x in [f'name: {ID}','version: "0.10.0"','family: "knowledge"','authority: "read-only"']:
            self.assertIn(x,head)
    def test_all_references_exist(self):
        found=set(re.findall(r'references/([A-Z_]+\.md)',self.skill))
        self.assertEqual(found,REFS)
        self.assertTrue({p.name for p in (ROOT/'references').glob('*.md')} <= REFS)  # overlay builds omit preserved refs
    def test_monitor_does_not_gain_authority(self):
        s=self.skill+self.refs
        for x in ['Email Evidence Packet','Email Evidence Packet v1','SKILL_NOT_LOADED','last','source','READ_COMPLETE_WITHIN_SCOPE','PARTIAL_INTAKE','SOURCE_UNAVAILABLE','ATTEMPT']:
            self.assertIn(x.lower(),s.lower())
        for x in ['cross-run dedup','schedule','state writes','alert','read-only']:
            self.assertIn(x.lower(),s.lower())
    def test_history_preserved(self):
        c=(ROOT/'CHANGELOG.md').read_text('utf-8')
        h=(ROOT/'LINEAGE.md')
        if h.exists(): self.assertIn('first independently packaged',h.read_text('utf-8'))
        self.assertIn('0.8.0',c)
        self.assertIn('0.9.0',c)
    def test_no_private_identifiers(self):
        s='\n'.join(p.read_text('utf-8') for p in ROOT.rglob('*.md'))
        self.assertNotRegex(s, r'https?://(?:docs|drive)\.google\.com/(?:document/d/|file/d/|drive/folders/)[A-Za-z0-9_-]{16,}')
        self.assertNotRegex(s, r'(?:ghp|gho|ghs|github_pat)_[A-Za-z0-9_]{20,}')
        self.assertNotRegex(s, r'sk-proj-[A-Za-z0-9_-]{30,}')
        self.assertFalse(list(ROOT.rglob('*.eml')))
        self.assertFalse(list(ROOT.rglob('*.mbox')))
    def test_monitor_case_definitions(self):
        p=ROOT/'tests/monitor_composition_cases.json'
        arr=json.loads(p.read_text('utf-8'))
        self.assertGreaterEqual(len(arr),5)
        self.assertEqual(len(arr),len({x['id'] for x in arr}))
        self.assertTrue(all(x.get('expected') and x.get('scenario') for x in arr))
if __name__=='__main__':unittest.main(verbosity=2)
