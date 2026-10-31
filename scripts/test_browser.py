"""Smoke test beginner and intensive lessons in a mobile-sized Chromium browser."""
from pathlib import Path
from playwright.sync_api import sync_playwright
import json,re
p=Path(__file__).resolve().parents[1]
with sync_playwright() as w:
 browser=w.chromium.launch(executable_path='/usr/bin/chromium',headless=True,args=['--no-sandbox','--disable-dev-shm-usage'])
 page=browser.new_page(viewport={'width':390,'height':844},device_scale_factor=1)
 errors=[];page.on('pageerror',lambda e:errors.append(str(e)))
 page.goto('about:blank')
 html=re.sub(r'<script src="\./app\.js" defer></script>','', (p/'web/index.html').read_text())
 page.set_content(html,wait_until='load')
 page.add_style_tag(content=(p/'web/style.css').read_text())
 data=json.loads((p/'web/data/course.json').read_text())
 beginner=json.loads((p/'web/data/beginner.json').read_text())
 chunks=json.loads((p/'web/data/chunks.json').read_text())
 practice=json.loads((p/'web/data/practice.json').read_text())
 page.evaluate("({course,beginner,chunks,practice})=>{window.fetch=async url=>({ok:true,json:async()=>url.includes('beginner')?beginner:url.includes('chunks')?chunks:url.includes('practice')?practice:course})}", {'course':data,'beginner':beginner,'chunks':chunks,'practice':practice})
 page.add_script_tag(content=(p/'web/app.js').read_text())
 page.wait_for_selector('[data-action="beginner-phase"]')
 assert page.locator('[data-action="beginner-phase"]').count()==6
 assert '英語がゼロでも' in page.locator('#main').inner_text()
 assert page.evaluate('document.documentElement.scrollWidth<=innerWidth'), 'mobile horizontal overflow home'
 page.screenshot(path=str(p/'docs/mobile-beginner-home.png'),full_page=False)
 page.locator('[data-action="beginner-unit"]').first.click()
 assert 'アルファベット' in page.locator('#main').inner_text()
 assert page.locator('.letter').count()==26
 assert page.locator('.vocab-card').count()>=6
 page.locator('[data-action="beginner-step"][data-id="1"]').click()
 assert page.locator('.word-part').count()>=3
 assert page.locator('.beginner-pattern').count()==1
 page.locator('[data-action="beginner-step"][data-id="2"]').click()
 assert page.locator('.beginner-example').count()==5
 page.locator('.beginner-example [data-action="beginner-hide-translation"]').first.click()
 assert page.locator('.beginner-example .exampleJa').first.is_hidden()
 page.locator('.beginner-example [data-action="beginner-hide-translation"]').first.click()
 assert page.locator('.beginner-example .exampleJa').first.is_visible()
 page.screenshot(path=str(p/'docs/mobile-beginner-lesson.png'),full_page=False)
 page.locator('[data-action="beginner-start"]').click()
 assert '1 / 10' in page.locator('.quizMeta').inner_text()
 saw_beginner_typing=False
 saw_beginner_order=False
 for i in range(10):
  assert f'{i+1} / 10' in page.locator('.quizMeta').inner_text()
  if page.locator('#beginnerTyped').count():
   saw_beginner_typing=True
   page.locator('#beginnerTyped').fill('not a correct answer')
   page.locator('[data-action="beginner-hint"]').click()
   assert page.locator('.typingHint').count()==1
   page.locator('[data-action="beginner-check-typed"]').click()
  elif page.locator('[data-action="beginner-order-add"]').count():
   saw_beginner_order=True
   while page.locator('[data-action="beginner-order-add"]').count():
    page.locator('[data-action="beginner-order-add"]').first.click()
   page.locator('[data-action="beginner-check-order"]').click()
  else:
   page.locator('[data-action="beginner-choice"]').first.click()
  assert page.locator('.feedback').count()==1
  page.locator('[data-action="beginner-next"]').click()
 assert saw_beginner_typing and saw_beginner_order
 assert 'PRACTICE COMPLETE' in page.locator('#main').inner_text()
 assert ' / 10' in page.locator('.score').inner_text()
 assert page.locator('#topStats').inner_text().startswith('入門')
 print('PASS beginner 24 lessons, steps, 10 mixed drills, result')
 page.locator('button[data-tab="learn"]').first.click()
 assert page.locator('[data-action="chapter"]').count()==8
 page.locator('[data-action="unit"]').first.click()
 assert page.locator('.lectureGrid .panel').count()==6
 assert page.locator('.example').count()==7
 assert page.locator('.chunkCard').count()==2
 page.locator('.practiceDisclosure summary').click()
 assert page.locator('.practiceSample').count()==10
 page.locator('[data-action="unitquiz"]').first.click()
 seen_types=set()
 for i in range(20):
  assert f'{i+1} / 20' in page.locator('.quizMeta').inner_text()
  if page.locator('#typedAnswer').count():
   seen_types.add('typing')
   page.locator('#typedAnswer').fill('a practice answer')
   page.locator('[data-action="typehint"]').click()
   assert page.locator('.typingHint').count()==1
   page.locator('[data-action="checktyped"]').click()
  elif page.locator('[data-action="word-add"]').count():
   seen_types.add('order')
   while page.locator('[data-action="word-add"]').count():
    page.locator('[data-action="word-add"]').first.click()
   page.locator('[data-action="checkorder"]').click()
  else:
   seen_types.add('choice')
   page.locator('[data-action="choice"]').first.click()
  assert page.locator('.feedback').count()==1
  page.locator('[data-action="next"]').click()
 assert 'TEST COMPLETE' in page.locator('#main').inner_text()
 assert 'typing' in seen_types and 'order' in seen_types and 'choice' in seen_types
 print('PASS mixed practical 20-question test, hints, typing and ordering')
 page.locator('button[data-tab="scenarios"]').first.click()
 assert page.locator('[data-action="scene"]').count()==15
 page.locator('button[data-tab="phrases"]').first.click()
 assert page.locator('.chunkCard').count()==64
 assert 'depend on' in page.locator('#main').inner_text()
 assert '接客例文 544' in page.locator('#main').inner_text()
 page.locator('[data-action="known-chunk"]').first.click()
 assert page.locator('[data-action="known-chunk"]').first.get_attribute('aria-pressed')=='true'
 page.locator('[data-action="chunktest"]').first.click()
 assert '1 / 10' in page.locator('.quizMeta').inner_text()
 assert '文法の規則' not in page.locator('#main').inner_text()
 page.locator('button[data-tab="phrases"]').first.click()
 page.locator('button[data-tab="facts"]').first.click()
 assert page.locator('.fact').count()==16
 page.locator('button[data-tab="review"]').first.click()
 assert '復習' in page.locator('#main').inner_text()
 assert not errors,errors
 print('PASS all tabs and no JS errors')
 browser.close()
