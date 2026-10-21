from playwright.sync_api import sync_playwright
from pathlib import Path
from urllib.parse import urlparse
import mimetypes
p=Path(__file__).resolve().parent.parent
with sync_playwright() as w:
 browser=w.chromium.launch(executable_path='/usr/bin/chromium',headless=True,args=['--no-sandbox','--disable-dev-shm-usage','--no-proxy-server','--proxy-bypass-list=*'])
 page=browser.new_page(viewport={'width':390,'height':844}, device_scale_factor=1)
 errors=[]
 page.on('pageerror',lambda e: errors.append(str(e)))
 page.goto('about:blank')
 html=(p/'web/index.html').read_text(encoding='utf8').replace('<script src="/app.js" defer></script>','')
 page.set_content(html,wait_until='load')
 page.add_style_tag(content=(p/'web/style.css').read_text(encoding='utf8'))
 import json
 data=json.loads((p/'web/data/course.json').read_text(encoding='utf8'))
 page.evaluate("(data) => {window.fetch = async () => ({ok:true,json:async()=>data})}",data)
 page.add_script_tag(content=(p/'web/app.js').read_text(encoding='utf8'))
 page.wait_for_selector('[data-action="chapter"]')
 assert '文法を理解して' in page.locator('body').inner_text()
 assert page.locator('[data-action="chapter"]').count()==8
 print('main loaded',page.title())
 page.screenshot(path=str(p/'docs/mobile-home.png'),full_page=True)
 page.locator('button[data-action="unit"]').first.click()
 assert page.locator('.example').count()==7
 assert page.locator('.lectureGrid .panel').count()==6
 print('lesson loaded')
 page.screenshot(path=str(p/'docs/mobile-lesson.png'),full_page=False)
 page.locator('[data-action="unitquiz"]').first.click()
 assert '1 / 20' in page.locator('.quizMeta').inner_text()
 assert page.locator('.choice').count()>=2
 opts=page.locator('button[data-action="choice"]');
 opts.first.click()
 assert page.locator('.feedback').count()==1
 print('quiz feedback',page.locator('.feedback').inner_text()[:100])
 page.locator('[data-action="next"]').click()
 assert '2 / 20' in page.locator('.quizMeta').inner_text()
 # run through the rest of the quiz using a mixture of order and multiple choice questions
 for _ in range(19):
  if page.locator('button[data-action="choice"]').count():
   page.locator('button[data-action="choice"]').first.click()
  elif page.locator('button[data-action="word-add"]').count():
   while page.locator('button[data-action="word-add"]').count():page.locator('button[data-action="word-add"]').first.click()
   page.locator('button[data-action="checkorder"]').click()
  else:
   raise AssertionError('no answer options')
  assert page.locator('.feedback').count()==1
  page.locator('[data-action="next"]').click()
 assert 'TEST COMPLETE' in page.locator('body').inner_text()
 print('unit 20 questions completed')
 page.locator('button[data-action="quitagain"]').click()
 assert page.locator('#main h1').inner_text()=='文法テスト'
 page.locator('[data-setting="from"]').select_option('4')
 page.locator('[data-setting="to"]').select_option('6')
 print('from-to set')
 page.locator('[data-action="allrange"]').click()
 assert '640問' in page.locator('#main').inner_text()
 page.locator('[data-action="qty"][data-qty="10"]').click()
 page.locator('button[data-action="startcustom"]').click()
 assert '1 / 10' in page.locator('.quizMeta').inner_text()
 print('custom test works')
 page.locator('[data-action="quitquiz"]').click()
 page.locator('[data-tab="review"]').first.click()
 assert '間違えた問題だけ' in page.locator('#main').inner_text()
 print('review works')
 page.locator('[data-tab="scenarios"]').first.click()
 assert page.locator('[data-action="scene"]').count()==15
 page.locator('[data-action="scene"]').last.click()
 assert page.locator('.hiddenSentence').count()>=1
 page.locator('[data-action="revealscene"]').click()
 assert page.locator('.hiddenSentence').count()==0
 print('scenarios works')
 page.locator('[data-tab="phrases"]').first.click()
 assert '接客例文 224' in page.locator('#main').inner_text()
 page.locator('#search').fill('eSIM')
 assert page.locator('.example').count()>0
 print('phrases filtering works')
 page.locator('[data-tab="facts"]').first.click()
 assert page.locator('.fact').count()==16
 print('fact links loaded')
 page.screenshot(path=str(p/'docs/mobile-facts.png'),full_page=False)
 assert not errors, '\\n'.join(errors)
 print('ALL BROWSER CHECKS PASS')
 browser.close()
