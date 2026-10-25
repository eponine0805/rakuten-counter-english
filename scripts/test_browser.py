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
 page.evaluate("({course,beginner})=>{window.fetch=async url=>({ok:true,json:async()=>url.includes('beginner')?beginner:course})}", {'course':data,'beginner':beginner})
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
 assert '1 / 12' in page.locator('.quizMeta').inner_text()
 for i in range(12):
  page.locator('[data-action="beginner-hint"]').click()
  assert page.locator('.beginner-hint').inner_text().find('今日の型')>=0
  if page.locator('[data-action="beginner-choice"]').count():
   page.locator('[data-action="beginner-choice"]').first.click()
  else:
   while page.locator('[data-action="beginner-order-add"]').count():page.locator('[data-action="beginner-order-add"]').first.click()
   page.locator('[data-action="beginner-check-order"]').click()
  assert page.locator('.feedback').count()==1
  page.locator('[data-action="beginner-next"]').click()
 assert 'PRACTICE COMPLETE' in page.locator('#main').inner_text()
 assert ' / 12' in page.locator('.score').inner_text()
 assert page.locator('#topStats').inner_text().startswith('入門')
 print('PASS beginner 24 lessons, steps, 12 drills, result')
 page.locator('button[data-tab="learn"]').first.click()
 assert page.locator('[data-action="chapter"]').count()==8
 page.locator('[data-action="unit"]').first.click()
 assert page.locator('.lectureGrid .panel').count()==6
 assert page.locator('.example').count()==7
 page.locator('[data-action="unitquiz"]').first.click()
 assert '1 / 20' in page.locator('.quizMeta').inner_text()
 page.locator('[data-action="choice"]').first.click()
 assert page.locator('.feedback').count()==1
 page.locator('[data-action="next"]').click()
 assert '2 / 20' in page.locator('.quizMeta').inner_text()
 print('PASS original 32 lessons and 20-question quiz')
 page.locator('button[data-tab="scenarios"]').first.click()
 assert page.locator('[data-action="scene"]').count()==15
 page.locator('button[data-tab="phrases"]').first.click()
 assert '接客例文 224' in page.locator('#main').inner_text()
 page.locator('button[data-tab="facts"]').first.click()
 assert page.locator('.fact').count()==16
 page.locator('button[data-tab="review"]').first.click()
 assert '復習' in page.locator('#main').inner_text()
 assert not errors,errors
 print('PASS all tabs and no JS errors')
 browser.close()
