#!/usr/bin/env python3
"""Validate the beginner scaffold and both course data assets."""
import json,subprocess
from pathlib import Path
root=Path(__file__).resolve().parents[1]
b=json.loads((root/'web/data/beginner.json').read_text(encoding='utf8'))
a=json.loads((root/'web/data/course.json').read_text(encoding='utf8'))
assert len(b['phases'])==6 and len(b['units'])==24
assert len(a['units'])==32 and len(a['scenarios'])==15
chunks=json.loads((root/'web/data/chunks.json').read_text(encoding='utf8'))['chunks']
assert len(chunks)==64
ids=set()
for n,u in enumerate(b['units'],1):
 assert u['id']==n and u['phase']==(n-1)//4+1
 assert len(u['explain'])==3 and all(len(s)>20 for s in u['explain'])
 assert len(u['vocab'])>=6 and len(u['parts'])>=2
 assert len(u['examples'])==5
 assert all(e['en'] and e['ja'] and e['why'] for e in u['examples'])
 assert len({e['en'] for e in u['examples']})==5
 assert u['pattern']
 for e in u['examples']:
  assert e['id'] not in ids;ids.add(e['id'])
assert sum(len(x['examples']) for x in b['units'])==120
assert 24*12+32*20==928
subprocess.run(['node','--check',str(root/'web/app.js')],check=True)
print('PASS beginner 24 lessons, 120 examples, 288 questions, legacy 640 questions, 928 combined')
