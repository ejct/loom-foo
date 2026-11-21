#!/usr/bin/env python3
"""Validate this skill's source and authored fixtures, not runtime behavior."""
from pathlib import Path
import json
import re
import sys
try:
    import yaml
except ImportError:
    sys.exit("FAIL: PyYAML is required; static check not run")

ROOT=Path(__file__).resolve().parents[1]
errors=[]
text=(ROOT/'SKILL.md').read_text(encoding='utf-8')
fm=re.match(r'\A---\n(.*?)\n---\n',text,re.S)
if not fm:
    errors.append('Missing valid frontmatter delimiters')
    data={}
else:
    try: data=yaml.safe_load(fm.group(1))
    except yaml.YAMLError as e:
        errors.append(f'Invalid YAML frontmatter: {e}')
        data={}

if data.get('name')!=ROOT.name: errors.append('Name/folder mismatch')
if not re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*',ROOT.name) or len(ROOT.name)>64:
    errors.append('Invalid skill ID')
metadata=data.get('metadata') or {}
if metadata.get('version')!='0.2.0': errors.append('Wrong version')
if metadata.get('family')!='design': errors.append('Wrong family')
if metadata.get('project')!='loom-foo': errors.append('Wrong project')
if not isinstance(data.get('description'),str) or len(data['description'])<40 or len(data['description'])>1024:
    errors.append('Missing or oversized description')

# References can occur in the root, secondary sources and README.
for source in [ROOT/'SKILL.md',*sorted((ROOT/'references').glob('*.md'))]:
    body=source.read_text(encoding='utf-8')
    for relative in re.findall(r'`(references/[A-Za-z0-9_./-]+\.md)`',body):
        if not (ROOT/relative).is_file(): errors.append(f'Dangling reference in {source.name}: {relative}')
for mode in ['REFRAME','DIVERGE','UNSTICK','SYNTHESIZE','CONVERGE']:
    if f'**{mode}:**' not in text: errors.append(f'Missing root mode {mode}')
for clause in ['FIXED','FLEXIBLE','UNKNOWN','Concept Exploration Note','not a mandatory']:
    if clause not in text: errors.append(f'Missing expected contract clause: {clause}')
try:
    fx=json.loads((ROOT/'tests/routing_cases.json').read_text(encoding='utf-8'))
    if fx.get('skill')!=ROOT.name or fx.get('version')!='0.2.0': errors.append('Fixture identity/version mismatch')
    cases=fx.get('cases') or []
    if not cases: errors.append('Empty fixtures')
    ids=[x.get('id') for x in cases]
    if len(set(ids))!=len(ids): errors.append('Duplicate case id')
    npos=nneg=0
    for c in cases:
        required=('id','prompt','expected_owner','expect_creative_method','expected_mode','acceptance')
        if not all(k in c for k in required): errors.append(f'Incomplete fixture: {c.get("id")}')
        if not isinstance(c.get('acceptance'),list) or not c['acceptance']:
            errors.append(f'Empty acceptance: {c.get("id")}')
        if c.get('expect_creative_method'):
            npos+=1
            if c.get('expected_mode') not in ['REFRAME','DIVERGE','UNSTICK','SYNTHESIZE','CONVERGE']:
                errors.append(f'Invalid creative mode: {c.get("id")}')
        else:
            nneg+=1
            if c.get('expected_mode')!='NONE': errors.append(f'Unexpected mode on negative: {c.get("id")}')
    if not npos or not nneg: errors.append('Need positive and negative fixtures')
except (KeyError,ValueError,OSError,TypeError) as e:
    errors.append(f'Fixture invalid: {e}')
    npos=nneg=0

if errors:
    for err in errors: print('FAIL:',err,file=sys.stderr)
    sys.exit(1)
print(f'STATIC PASS: {ROOT.name} v0.2.0, {npos} positive / {nneg} negative authored cases')
print('NOT TESTED: host discovery, automatic routing, task execution, field impact')
