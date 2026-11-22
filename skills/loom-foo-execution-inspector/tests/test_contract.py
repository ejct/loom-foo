import json
from pathlib import Path
import unittest
import yaml

BASE = Path(__file__).resolve().parents[1]
ROOT = (BASE / 'SKILL.md').read_text(encoding='utf-8')

class CandidateStaticTests(unittest.TestCase):
    def test_metadata(self):
        self.assertTrue(ROOT.startswith('---\n'))
        fm = yaml.safe_load(ROOT.split('---', 2)[1])
        self.assertEqual(fm['name'], 'loom-foo-execution-inspector')
        self.assertEqual(fm['metadata']['family'], 'engineering')
        self.assertEqual(fm['metadata']['version'], '0.4.0')
        self.assertIn('Not running new tests', fm['description'])
    def test_read_only_and_boundaries(self):
        for fragment in ['Read-only', 'Never run or rerun tests', 'loom-foo-change-verification', 'loom-foo-sanity-check', 'loom-foo-handoff', 'SAME_CONTEXT']:
            self.assertIn(fragment, ROOT)
    def test_claim_states(self):
        for fragment in ['RUNTIME_OBSERVED', 'TOOL_OBSERVED', 'SOURCE_SUPPORTED', 'MODEL_REPORTED', 'FULL', 'PARTIAL', 'METADATA_ONLY', 'NOT_CONFIRMED', 'NOT_RUN', 'NOT_COVERED', 'UNVERIFIED', 'INCONCLUSIVE']:
            self.assertIn(fragment, ROOT)
    def test_optional_reference_and_no_stale_contract(self):
        self.assertNotIn('ANSWER_RECEIPT_V0.2', ROOT)
        self.assertIn('docs/ANSWER_RECEIPT_V0.3.md', ROOT)
        self.assertIn('references/TRACE_CLAIMS_AND_BOUNDARIES.md', ROOT)
        self.assertTrue((BASE / 'references/TRACE_CLAIMS_AND_BOUNDARIES.md').exists())
    def test_native_metadata_preserved(self):
        expected = "interface:\n  display_name: Execution Inspector\n  short_description: Inspect agent execution and evidence claims\n  brand_color: '#F2B705'\n"
        self.assertEqual((BASE / 'agents/openai.yaml').read_text(encoding='utf-8'), expected)
    def test_fixtures(self):
        routing=json.loads((BASE / 'tests/routing_cases.json').read_text(encoding='utf-8'))
        inspections=json.loads((BASE / 'tests/inspection_cases.json').read_text(encoding='utf-8'))
        self.assertEqual(len(routing['cases']), 10)
        self.assertEqual(len(inspections['cases']), 10)
        self.assertEqual(len(set(c['id'] for c in routing['cases'])), 10)
        self.assertGreaterEqual(len([x for x in routing['cases'] if x['expected_owner']=='loom-foo-execution-inspector']),3)
        self.assertGreaterEqual(len([x for x in routing['cases'] if x['expected_owner'] != 'loom-foo-execution-inspector']),4)
        self.assertEqual(inspections['kind'], 'expected_dispositions_not_behavioral_results')
    def test_no_private_context(self):
        for word in ['sk-proj-', 'api_key=', 'USER_PRIVATE_RECORD_ID']:
            self.assertNotIn(word, ROOT)

if __name__=='__main__': unittest.main()
