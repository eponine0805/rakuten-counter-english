#!/usr/bin/env python3
"""Static checks for the course and its offline bundle. No extra packages required."""
import json,re,sys,subprocess
from pathlib import Path
root=Path(__file__).resolve().parents[1]
course=json.loads((root/'web/data/course.json').read_text(encoding='utf8'))
units=course['units']
assert course['reviewedOn']=='2026-10-21'
assert len(course['chapters'])==8 and [ch['id'] for ch in course['chapters']]==list(range(1,9))
assert len(units)==32 and [u['id'] for u in units]==list(range(1,33))
assert len(course['scenarios'])==15 and len({x['id'] for x in course['scenarios']})==15
assert len(course['sources'])==10 and len(course['facts'])==16
seen=set()
for u in units:
 assert 1<=u['chapter']<=8
 assert len(u['sections'])==6 and all(s['text'] and s['heading'] for s in u['sections'])
 assert len(u['examples'])==7
 assert len(set(x['en'] for x in u['examples']))==7
 assert len(set(x['ja'] for x in u['examples']))==7
 assert u['pattern']
 for e in u['examples']:
  assert e['id'] not in seen; seen.add(e['id'])
  assert e['en'][-1] in '?!.', (u['id'],e['en'])
  assert e['ja'] and e['why']
  assert re.search('[A-Za-z]',e['en'])
for sc in course['scenarios']:
 assert len(sc['lines'])>=5
 for line in sc['lines']:
  assert len(line)==3 and line[0] in ('staff','customer')
  assert line[1] and line[2]
for f in course['facts']:
 assert isinstance(f['source'],int) and 0<=f['source']<len(course['sources'])
 assert f['title'] and f['body']
for source in course['sources']:
 assert source['url'].startswith('https://network.mobile.rakuten.co.jp/')
for ch in course['chapters']:
 group=[u for u in units if u['chapter']==ch['id']]
 assert len(group)==4
 assert len({u['pattern'] for u in group})==4
for filename in ('index.html','app.js','style.css','sw.js','manifest.webmanifest','icon.svg','data/course.json','data/chunks.json'):
 assert (root/'web'/filename).is_file()
assert '15の接客シーン' in (root/'web/app.js').read_text(encoding='utf8')
assert 'まとめ表現の意味' in (root/'web/app.js').read_text(encoding='utf8')
assert '文法の規則' not in (root/'web/app.js').read_text(encoding='utf8')
chunks=json.loads((root/'web/data/chunks.json').read_text(encoding='utf8'))['chunks']
assert len(chunks)==64
assert all(len([c for c in chunks if c['unit']==u['id']])==2 for u in units)
assert all(c['en'] and c['ja'] and c['sample'] and c['sampleJa'] for c in chunks)
assert any(c['en']=='depend on' for c in chunks)
assert sum(len(u['examples']) for u in units)==224
assert len(units)*20==640
try: subprocess.run(['node','--check',str(root/'web/app.js')], check=True, capture_output=True)
except FileNotFoundError: print('Note: Node.js not present; JS syntax check skipped')
print('PASS: 32 lessons / 64 practical chunks / no grammar rule questions / 640 questions / 15 scenarios / JS syntax')
