(()=>{'use strict';
const KEY='counter-english-2026-staff-v1', PREF='counter-english-voice-v1';
const $=sel=>document.querySelector(sel), E=v=>String(v??'').replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
const shuffle=a=>{const b=[...a];for(let i=b.length-1;i>0;i--){const j=Math.floor(Math.random()*(i+1));[b[i],b[j]]=[b[j],b[i]]}return b};
const sample=a=>shuffle(a); const unique=a=>[...new Set(a)];
let course=null, beginner=null, chunks=[], bank=[], active='beginner', chapterOpen=1, unitId=null, quiz=null, scenarioId=null, scenarioRevealed=new Set(), phraseSearch='',phraseFilter='全部',favoritesOnly=false;
let beginnerPhase=1, beginnerId=null, beginnerStep=0, beginnerQuiz=null, beginnerHidden={};
let settings={from:1,to:32,count:10};
let progress={best:{},answered:0,correct:0,wrong:{},favorites:{},learnedChunks:{},last:null,started:{},beginnerBest:{},beginnerWrong:{},beginnerAnswered:0};
let voice={rate:.78,locale:'en-US'}, voiceMap={};let voiceIndex=0;
try{const o=JSON.parse(localStorage.getItem(KEY));if(o&&typeof o==='object'&&o.best&&o.wrong)progress={...progress,...o}}catch(e){}
try{const o=JSON.parse(localStorage.getItem(PREF));if(o&&[.65,.75,.78,.85,1,1.1].includes(o.rate)){voice={...voice,...o}}}catch(e){}
const STORE=()=>{try{localStorage.setItem(KEY,JSON.stringify(progress))}catch(e){notify('保存できません。端末の空き容量をご確認ください。')}};
const storeVoice=()=>{try{localStorage.setItem(PREF,JSON.stringify(voice))}catch(e){}};
function notify(s){const t=$('#toast');t.textContent=s;t.style.display='block';clearTimeout(notify.timer);notify.timer=setTimeout(()=>t.style.display='none',3300)}
function speakButton(s,small=true){let id='v'+(++voiceIndex);voiceMap[id]=s;return `<button class="btn secondary ${small?'sm':''}" data-action="speak" data-voice="${id}" title="英語の音声を再生" aria-label="発音を聞く">▶ 発音</button>`}
function voiceControl(){return `<div class="voice"><label for="speed">英語音声の速さ</label><select id="speed" data-setting="speed">${[.65,.75,.78,.85,1,1.1].map(n=>`<option value="${n}" ${voice.rate===n?'selected':''}>${n}×${n===.78?'（標準）':''}</option>`).join('')}</select><label for="locale">発音</label><select id="locale" data-setting="locale"><option value="en-US" ${voice.locale==='en-US'?'selected':''}>アメリカ英語</option><option value="en-GB" ${voice.locale==='en-GB'?'selected':''}>イギリス英語</option></select><span class="note">端末の英語音声を使用。声質や速度は端末により異なります。</span></div>`}
function speak(text){if(!('speechSynthesis'in window)){notify('このブラウザは読み上げに非対応です。');return}const t=String(text||'');if(!t)return;try{speechSynthesis.cancel();let u=new SpeechSynthesisUtterance(t);u.lang=voice.locale;u.rate=voice.rate;u.pitch=1;const vs=speechSynthesis.getVoices();let candidate=vs.find(v=>v.lang===voice.locale&&v.localService)||vs.find(v=>v.lang===voice.locale)||vs.find(v=>v.lang.startsWith('en-'));if(candidate)u.voice=candidate;u.onerror=()=>notify('英語音声を再生できませんでした。端末のTTS設定をご確認ください。');speechSynthesis.speak(u)}catch(e){notify('英語音声を再生できませんでした。')}}
function scrollUp(){window.scrollTo({top:0,behavior:'instant'})}
function nav(tab){active=tab;unitId=null;scenarioId=null;quiz=null;beginnerId=null;beginnerQuiz=null;render();scrollUp()}
function setMain(html){$('#main').innerHTML=html;document.querySelectorAll('[data-tab]').forEach(t=>{t.classList.toggle('active',t.dataset.tab===active);t.setAttribute('aria-current',t.dataset.tab===active?'page':'false')});const mastered=Object.values(progress.best).filter(n=>n>=16).length;const beginnerDone=beginner?.units.filter(u=>beginnerMastered(u.id)).length||0;$('#topStats').textContent=`入門 ${beginnerDone}/24 · 文法 ${mastered}/32`}
const unitBy=id=>course.units.find(u=>u.id===Number(id));
// A0: independent scaffolded course. The existing 32-unit intensive course remains unchanged.
const beginnerUnit=id=>beginner.units.find(u=>u.id===Number(id));
const beginnerMastered=id=>(progress.beginnerBest?.[id]??0)>=10;
function beginnerNext(){return beginner.units.find(u=>!beginnerMastered(u.id))?.id||24}
function renderBeginnerHome(){
 const passed=beginner.units.filter(u=>beginnerMastered(u.id)).length;
 const phases=beginner.phases.map(ph=>{
  const units=beginner.units.filter(u=>u.phase===ph.id);
  const done=units.filter(u=>beginnerMastered(u.id)).length;
  const open=beginnerPhase===ph.id;
  return `<div class="panel"><button class="chapterHead row" data-action="beginner-phase" data-id="${ph.id}" aria-expanded="${open}"><span class="chapterNo">${String(ph.id).padStart(2,'0')}</span><span class="grow"><span class="chapterTitle">${E(ph.title)}</span><span class="chapterGoal">${E(ph.goal)}</span></span><span class="pill">${done}/4</span><span class="muted">${open?'⌃':'⌄'}</span></button>${open?`<div class="units">${units.map(u=>`<button class="unitRow" data-action="beginner-unit" data-id="${u.id}"><span class="index ${beginnerMastered(u.id)?'beginner-done':''}">${String(u.id).padStart(2,'0')}</span><span class="grow"><b>${E(u.title)}</b><small>${E(u.goal)}</small></span><span class="right">${progress.beginnerBest?.[u.id]!==undefined?progress.beginnerBest[u.id]+'/12':'未学習'} ›</span></button>`).join('')}</div>`:''}</div>`;
 }).join('');
 setMain(`<div class="hero beginner-hero"><div class="eyebrow">START HERE · ENGLISH FROM ZERO</div><h1 class="h1">英語がゼロでも、<br>最初の一言から。</h1><p class="sub">英単語も文法も分からなくてOK。まず文字と音から始め、<b>単語を聞く → 日本語で理解 → 短文をまねる → 12問練習</b> の順番で、少しずつ楽天モバイルの接客英語へ進みます。</p><div class="buttonRow"><button class="btn" data-action="beginner-unit" data-id="${beginnerNext()}">${passed===0?'第1課から始める':'続きから学ぶ'} →</button><button class="btn secondary" data-tab="learn">既存の文法32単元へ</button></div></div><div class="stats"><div class="stat"><strong>${passed}<span class="mininum">/24</span></strong><small>合格した入門課</small></div><div class="stat"><strong>${progress.beginnerAnswered||0}</strong><small>入門の回答数</small></div><div class="stat"><strong>${Object.keys(progress.beginnerWrong||{}).length}</strong><small>復習したい問題</small></div></div><div class="progress" role="progressbar" aria-valuemin="0" aria-valuemax="24" aria-valuenow="${passed}" aria-label="入門の進捗"><i style="width:${passed/24*100}%"></i></div><div class="notice"><b>学び方：</b>1回に1課だけでも大丈夫です。単語の聞き取りと12問の練習は何度でも挑戦できます。途中を飛ばすこともできます。料金例は読み方の練習で、最新の契約条件ではありません。</div>${Object.keys(progress.beginnerWrong||{}).length?'<div class="panel" style="margin-top:14px"><b>苦手な問題を復習しよう</b><p class="note">間違えた問題だけ再練習できます。</p><button class="btn secondary sm" data-action="beginner-review">入門の間違いを復習 →</button></div>':''}<div class="section-label">ROAD MAP · 6ステップ / 24レッスン</div><div class="stack">${phases}</div>${voiceControl()}`);
}
const alphabet='ABCDEFGHIJKLMNOPQRSTUVWXYZ'.split('');
function beginnerSteps(){return `<div class="beginner-steps" aria-label="学習の進行状況">${['1 単語','2 使える型','3 例文','4 練習'].map((s,i)=>`<span class="beginner-step ${beginnerStep===i?'here':beginnerStep>i?'passed':''}">${s}</span>`).join('')}</div>`}
function beginnerAction(next,back=null){return `<div class="footerCTA beginner-footer">${back===null?'<span class="note">焦らず、一つずつ進みましょう。</span>':`<button class="btn secondary sm" data-action="beginner-step" data-id="${back}">← 前の画面</button>`}<button class="btn" data-action="${next===3?'beginner-start':'beginner-step'}" data-id="${next}">${next===3?'12問の練習を始める':'次へ進む'} →</button></div>`}
function renderBeginnerLesson(){
 const u=beginnerUnit(beginnerId);if(!u){beginnerId=null;return renderBeginnerHome()}
 let core='';const intro=`<div class="lesson-head"><button class="back" data-action="beginner-home">← 入門コースに戻る</button><div class="eyebrow">BEGINNER · LESSON ${String(u.id).padStart(2,'0')} / 24</div><h1 class="h1">${E(u.title)}</h1><p class="sub">${E(u.goal)}</p></div>${beginnerSteps()}`;
 if(beginnerStep===0){
  const letterCards=u.id===1?`<section class="panel"><h2 class="beginner-h2">英語の26文字（タップして音を聞く）</h2><p class="note">英語の文字名と単語中の読み方は違うことがあります。ここはまず文字名に慣れましょう。</p><div class="alphabet-grid">${alphabet.map(ch=>`<button class="letter" data-action="say-letter" data-letter="${ch}">${ch}<span>▶</span></button>`).join('')}</div></section>`:'';
  core=`<div class="panel beginner-intro"><span class="tag">きょう覚えること</span><h2 class="beginner-h2">まずはこの単語だけ</h2><p class="beginner-par">${E(u.explain[0])}</p><p class="note">発音を押して音を聞き、日本語の意味を見比べましょう。カタカナ表記ではなく、英語の音をまねるのが目標です。</p></div>${letterCards}<div class="vocab-grid">${u.vocab.map(v=>`<div class="vocab-card"><strong>${E(v.en)}</strong><span>${E(v.ja)}</span>${speakButton(v.en)}</div>`).join('')}</div>${voiceControl()}${beginnerAction(1)}`;
 }else if(beginnerStep===1){
  core=`<div class="panel beginner-intro"><span class="tag">英語をかたまりで覚える</span><h2 class="beginner-h2">短いかたまりをつなぐ</h2>${u.explain.map(x=>`<p class="beginner-par">${E(x)}</p>`).join('')}<div class="beginner-pattern"><small>今日の型</small><strong>${E(u.pattern)}</strong></div></div><div class="section-label">A SENTENCE, PIECE BY PIECE · 分解してみる</div><div class="panel"><div class="beginner-parts">${u.parts.map(p=>`<div class="word-part"><b>${E(p.en)}</b><small>${E(p.ja)}</small></div>`).join('')}</div><p class="note">色分けした語句を左から読めば、一文を自分で作る基礎になります。</p>${speakButton(u.parts.map(x=>x.en).join(' '),false)}</div>${beginnerAction(2,0)}`;
 }else if(beginnerStep===2){
  core=`<div class="panel beginner-intro"><span class="tag">読む・聞く・まねる</span><h2 class="beginner-h2">短い例文を5つ</h2><p class="beginner-par">いきなり暗記しなくて大丈夫。英文の下の日本語を見て、発音を聞き、言えるところだけ声に出しましょう。</p></div>${voiceControl()}<div class="stack">${u.examples.map((ex,i)=>`<article class="panel example beginner-example"><span class="step">${i+1} / 5</span><div class="exampleEn">${E(ex.en)}</div><div class="exampleJa">${E(ex.ja)}</div><p class="explain">${E(ex.why)}</p>${speakButton(ex.en)} <button class="btn secondary sm" data-action="beginner-hide-translation" data-id="${i}">${beginnerHidden[i]?'日本語を見る':'日本語を隠して挑戦'}</button></article>`).join('')}</div>${beginnerAction(3,1)}`;
 }
 setMain(intro+core);
 if(beginnerStep===2){document.querySelectorAll('.beginner-example').forEach((el,i)=>{el.querySelector('.exampleJa').hidden=Boolean(beginnerHidden[i])})}
}
function expressionChunks(sentence){
 const words=sentence.trim().split(/\s+/);
 const phrases=(chunks||[]).map(p=>p.en).concat(["This is","There is","How can I help you","Would you like to","Let me check","Thank you for waiting","per month","including tax","up to","more than","sign in","sign up","depends on","is based on","be eligible for","May I check","Could you show me"]).sort((a,b)=>b.split(/\s+/).length-a.split(/\s+/).length);
 const plain=x=>x.toLowerCase().replace(/^[^a-z0-9]+|[^a-z0-9]+$/g,'');
 const parts=[];for(let i=0;i<words.length;){let found=0;for(const phrase of phrases){const pw=phrase.split(/\s+/);if(pw.length<2||pw.length>words.length-i)continue;if(pw.every((p,j)=>plain(p)===plain(words[i+j]))){found=pw.length;break}}parts.push(words.slice(i,i+(found||1)).join(' '));i+=found||1;}return parts;
}
function beginnerQuestions(u){const es=u.examples.slice(0,4), xs=[];
 es.forEach((e,i)=>{
  xs.push({id:`B${u.id}:meaning:${i}`,kind:'choice',group:1,label:'英文の意味を選ぶ',prompt:e.en,correct:e.ja,choices:es.map(x=>x.ja),ex:e});
 });
 es.forEach((e,i)=>{
  xs.push({id:`B${u.id}:english:${i}`,kind:'choice',group:2,label:'日本語から英語を選ぶ',prompt:e.ja,correct:e.en,choices:es.map(x=>x.en),ex:e});
 });
 es.forEach((e,i)=>{
  let parts=expressionChunks(e.en);
  xs.push({id:`B${u.id}:order:${i}`,kind:'order',group:3,label:'語順を組み立てる',prompt:e.ja,correct:e.en,chunks:parts,ex:e});
 });return xs;
}
function beginnerStart(ids=null){
 const u=beginnerUnit(beginnerId);if(!u)return;
 const all=beginnerQuestions(u);const source=ids?all.filter(q=>ids.includes(q.id)):all;
 if(!source.length){notify('復習対象がありません');return}
 beginnerQuiz={items:source.map(q=>q.kind==='order'?{...q,pool:shuffle(q.chunks.map((value,id)=>({value,id}))),placed:[]}:{...q,choices:shuffle(q.choices)}),index:0,score:0,answered:false,pick:null,good:null,firstTry:{},hint:false};
 beginnerStep=3;render();scrollUp();
}
function beginnerCurrent(){return beginnerQuiz?.items[beginnerQuiz.index]}
function beginnerAnswer(ok,pick){const q=beginnerCurrent();if(!q||beginnerQuiz.answered)return;
 beginnerQuiz.answered=true;beginnerQuiz.good=ok;beginnerQuiz.pick=pick;beginnerQuiz.firstTry[q.id]=ok;
 if(ok)beginnerQuiz.score++;
 progress.beginnerAnswered=(progress.beginnerAnswered||0)+1;
 progress.beginnerWrong=progress.beginnerWrong||{};
 if(ok)delete progress.beginnerWrong[q.id];else progress.beginnerWrong[q.id]=true;
 STORE();render();
}
function beginnerOrder(idx,remove=false){const q=beginnerCurrent();if(!q||q.kind!=='order'||beginnerQuiz.answered)return;
 if(remove){const x=q.placed.splice(idx,1)[0];if(x)q.pool.push(x)}else{const x=q.pool.splice(idx,1)[0];if(x)q.placed.push(x)}render();
}
function beginnerNextQ(){if(!beginnerQuiz)return;
 if(beginnerQuiz.index===beginnerQuiz.items.length-1){
  if(beginnerQuiz.items.length===12){progress.beginnerBest=progress.beginnerBest||{};progress.beginnerBest[beginnerId]=Math.max(progress.beginnerBest[beginnerId]||0,beginnerQuiz.score)}
  STORE();beginnerStep=4;render();scrollUp();return;
 }
 beginnerQuiz.index++;beginnerQuiz.answered=false;beginnerQuiz.good=null;beginnerQuiz.pick=null;beginnerQuiz.hint=false;render();scrollUp();
}
function renderBeginnerQuiz(){const q=beginnerCurrent();if(!q){beginnerQuiz=null;beginnerStep=2;return renderBeginnerLesson()}
 const idx=beginnerQuiz.index,answered=beginnerQuiz.answered;
 const choices=q.kind==='choice'?`<div class="choiceList">${q.choices.map(c=>`<button class="choice ${answered&&c===q.correct?'correct':answered&&c===beginnerQuiz.pick?'incorrect':''}" data-action="beginner-choice" data-answer="${E(c)}" ${answered?'disabled':''}>${E(c)}</button>`).join('')}</div>`:`<><div class="section-label">タップした順に文になります（押すと戻せます）</div><div class="chipAnswer">${q.placed.map((p,i)=>`<button data-action="beginner-order-remove" data-id="${i}" ${answered?'disabled':''}>${E(p.value)} ×</button>`).join('')||'<span class="note">下から英語の語句をタップ</span>'}</div><div class="section-label">使う英語の語句</div><div class="chipPool">${q.pool.map((p,i)=>`<button data-action="beginner-order-add" data-id="${i}" ${answered?'disabled':''}>${E(p.value)}</button>`).join('')}</div>${!answered?`<div class="buttonRow"><button class="btn" data-action="beginner-check-order" ${q.pool.length?'disabled':''}>答え合わせ</button><button class="btn secondary" data-action="beginner-order-reset">やり直す</button></div>`:''}</>`;
 const feedback=answered?`<div class="feedback ${beginnerQuiz.good?'ok':'bad'}"><strong>${beginnerQuiz.good?'✓ 正解！':'正解を確認しましょう'}</strong><p><b>正解：</b>${E(q.correct)}</p><p>${E(q.ex.why)}</p><div>${speakButton(q.ex.en)}</div></div><button class="btn full" data-action="beginner-next">${idx===beginnerQuiz.items.length-1?'結果を見る':'次の問題に進む →'}</button>`:'';
 const hint=!answered?`<div class="beginner-hint"><button class="btn secondary sm" data-action="beginner-hint">${beginnerQuiz.hint?'ヒントを閉じる':'わからないのでヒントを見る'}</button>${beginnerQuiz.hint?`<p class="note">使える英語の型：${E(beginnerUnit(beginnerId).pattern)}<br>例文の解説：${E(q.ex.why)}<br>${q.kind==='order'?'英語の最初の語句：'+E(q.chunks[0]):'問題文を音で確かめてみましょう。'}</p>`:''}</div>`:'';
 setMain(`<div class="quizShell"><button class="back" data-action="beginner-back-example">← 例文を読み直す</button><div class="eyebrow">BEGINNER · LESSON ${beginnerId}</div><h1 class="h1">12問のやさしい練習</h1><div class="quizMeta"><span>STEP ${q.group}/3 · ${E(q.label)}</span><span>${idx+1} / ${beginnerQuiz.items.length}</span></div><div class="progress"><i style="width:${(idx+Number(answered))/beginnerQuiz.items.length*100}%"></i></div><div class="quizPrompt"><div class="quizTitle">${E(q.prompt)}</div>${q.group===1?speakButton(q.ex.en):''}<p class="note">${q.group===1?'意味を選ぶ練習です。':q.group===2?'日本語に合う英文を探します。':'英語のかたまりを左から並べて文を作ります。'}</p></div>${choices}${hint}${feedback}<p class="note">間違えても学習記録に残るだけです。何度でもやり直せます。</p></div>`);
}
function renderBeginnerResult(){const total=beginnerQuiz?.items.length||0,score=beginnerQuiz?.score||0;
 if(!total)return renderBeginnerHome();
 const retry=beginnerQuiz.items.filter(q=>!beginnerQuiz.firstTry[q.id]).map(q=>q.id);
 setMain(`<div class="quizShell"><div class="eyebrow">BEGINNER · PRACTICE COMPLETE</div><h1 class="h1">${score>=Math.ceil(total*0.83)?'一歩ずつ覚えられています。':'間違えても、繰り返せば大丈夫。'}</h1><div class="panel"><div class="score">${score}<small> / ${total}</small></div><div class="progress"><i style="width:${score/total*100}%"></i></div><p class="sub">${total===12?'10問以上正解で入門課に合格。':''}忘れた問題は復習として残ります。</p><div class="buttonRow">${retry.length?`<button class="btn" data-action="beginner-retry">間違えた${retry.length}問だけ練習</button>`:''}<button class="btn secondary" data-action="beginner-start">12問を最初から</button><button class="btn secondary" data-action="beginner-step" data-id="2">例文を読み直す</button>${beginnerId<24?`<button class="btn" data-action="beginner-unit" data-id="${beginnerId+1}">次のレッスン →</button>`:`<button class="btn" data-tab="learn">文法32単元へ →</button>`}</div></div><div class="section-label">今回の問題</div><div class="stack">${beginnerQuiz.items.map(q=>`<div class="panel"><span class="step">${beginnerQuiz.firstTry[q.id]?'✓ 正解':'↻ もう一度'}</span><p class="beginner-par">${E(q.ex.en)}<br><span class="note">${E(q.ex.ja)}</span></p></div>`).join('')}</div></div>`);
 beginnerQuiz.retry=retry;
}

function summary(){const mastered=Object.values(progress.best).filter(n=>n>=16).length;return `<div class="stats"><div class="stat"><strong>${mastered}<span style="font-size:13px">/32</span></strong><small>合格した単元</small></div><div class="stat"><strong>${progress.answered}</strong><small>累計回答数</small></div><div class="stat"><strong>${Object.keys(progress.wrong).length}</strong><small>要復習の問題</small></div></div><div class="progress" role="progressbar" aria-valuenow="${mastered}" aria-valuemin="0" aria-valuemax="32" aria-label="単元合格の進捗"><i style="width:${mastered/32*100}%"></i></div>`}
function renderLearn(){const sections=course.chapters.map(ch=>{let units=course.units.filter(u=>u.chapter===ch.id),done=units.filter(u=>(progress.best[u.id]??0)>=16).length,open=chapterOpen===ch.id;return `<div class="panel"><button class="chapterHead row" data-action="chapter" data-id="${ch.id}" aria-expanded="${open}"><span class="chapterNo">${String(ch.id).padStart(2,'0')}</span><span class="grow"><span class="chapterTitle">${E(ch.title)}</span><span class="chapterGoal">${E(ch.goal)}</span></span><span class="pill">${done}/${units.length}</span><span class="muted">${open?'⌃':'⌄'}</span></button>${open?`<div class="units">${units.map(u=>`<button class="unitRow ${(progress.best[u.id]??0)>=16?'done':''}" data-action="unit" data-id="${u.id}"><span class="index">${String(u.id).padStart(2,'0')}</span><span class="grow"><b>${E(u.title)}</b><small>${E(u.goal)}</small></span><span class="right">${progress.best[u.id]!==undefined?progress.best[u.id]+'/20':'講義＋20問'} ›</span></button>`).join('')}</div>`:''}</div>`}).join('');setMain(`<div class="hero"><div class="eyebrow">NEXT STEP · AFTER BEGINNER COURSE</div><h1 class="h1">入門の次は、<br>本格的な文法32単元。</h1><p class="sub">楽天モバイルの店頭で使う表現を、短いフレーズから段階的に身につけます。1単元につき<b>6節の解説 → 7つの接客例文 → 20問の理解確認</b>で身につけます。</p><div class="toolbar"><button class="btn" data-action="unit" data-id="${nextUnit()}">続きから学ぶ →</button><button class="btn secondary" data-tab="scenarios">接客会話を見る</button></div></div>${summary()}<div class="notice"><b>実務上の注意：</b>料金・特典は2026年10月21日の公式確認をもとに収録しています。契約時は必ず最新の公式規約・店頭手順を確認してください。非公式教材です。</div><div class="notice"><b>英語にまだ自信がない場合：</b>まずは文字と単語から練習する「ゼロから入門」24課がおすすめです。<button class="btn secondary sm" data-tab="beginner">入門コースに戻る →</button></div><div class="section-label">COURSE · 8 CHAPTERS / 32 UNITS</div><div class="stack">${sections}</div>${voiceControl()}`)}
function nextUnit(){return course.units.find(u=>(progress.best[u.id]??0)<16)?.id||1}
function renderUnit(){let u=unitBy(unitId);if(!u){nav('learn');return};const best=progress.best[u.id];setMain(`<div class="lesson-head"><button class="back" data-action="backlearn">← 文法一覧へ</button><div class="eyebrow">CHAPTER ${String(u.chapter).padStart(2,'0')} · LESSON ${String(u.id).padStart(2,'0')} / 32</div><h1 class="h1">${E(u.title)}</h1><p class="sub">${E(u.goal)}</p></div><div class="callout"><b>難しく感じたら：</b>まずは日本語解説つき24課の「ゼロから入門」で短文を練習できます。 <button class="btn secondary sm" data-tab="beginner">入門で練習する →</button></div><div class="lessonSummary"><span class="tag">本単元の到達目標</span><p>${E(u.sections[0].text)}</p><span class="pill">6節の解説</span> <span class="pill">例文7件</span> <span class="pill">確認テスト20問</span>${best!==undefined?`<p><b>ベスト ${best}/20 ${best>=16?'· 合格':'· 再挑戦推奨'}</b></p>`:''}</div><div class="section-label">01 — 使い方の解説</div><div class="lectureGrid">${u.sections.map((s,i)=>`<section class="panel"><div class="lectureHeading">${String(i+1).padStart(2,'0')} · ${E(s.heading)}</div><p class="lectureBody">${E(s.text)}</p></section>`).join('')}</div><div class="section-label">02 — この単元で覚える英語のかたまり</div><div class="chunkGrid">${chunks.filter(c=>c.unit===u.id).map(c=>`<article class="panel chunkCard"><div class="step">USEFUL CHUNK</div><h3>${E(c.en)}</h3><div class="exampleJa">${E(c.ja)}</div><div class="chunkSample">${E(c.sample)}</div><div class="note">${E(c.sampleJa)}</div><div class="exampleActions">${speakButton(c.en)}${speakButton(c.sample)}</div></article>`).join('')}</div><div class="section-label">03 — 解説付きの実務例文</div>${voiceControl()}<div class="stack">${u.examples.map((ex,i)=>`<article class="panel example"><div class="between"><span class="step">EXAMPLE ${String(i+1).padStart(2,'0')} / 07</span><span class="tag">接客英語</span></div><div class="exampleEn">${E(ex.en)}</div><div class="exampleJa">${E(ex.ja)}</div><p class="explain">${E(ex.why)}</p><div class="exampleActions">${speakButton(ex.en)}<button class="btn secondary sm" data-action="favorite" data-example="${ex.id}">${progress.favorites[ex.id]?'★ 保存済み':'☆ 例文を保存'}</button></div></article>`).join('')}</div><div class="section-label">04 — 接客表現の定着</div><div class="panel"><b>20問テスト</b><p class="sub">定型表現の練習2問・英語→日本語6問・日本語→英語6問・フレーズを組み立てる6問。16/20点で合格。誤答は復習に自動保存されます。</p><button class="btn" data-action="unitquiz" data-id="${u.id}">この単元の20問に挑戦 →</button></div><div class="footerCTA"><span class="note">理解 → 例文 → 反復演習</span><button class="btn" data-action="unitquiz" data-id="${u.id}">20問テスト →</button></div>`)}
function makeBank(){
 bank=[];
 const allJa=chunks.map(c=>c.ja),allEn=chunks.map(c=>c.en);
 for(const u of course.units){
  const es=u.examples.slice(0,6);
  const unitChunks=chunks.filter(c=>c.unit===u.id);
  for(const [i,c] of unitChunks.entries()){
   bank.push({id:`${u.id}:chunk:${i}`,unit:u.id,type:'choice',label:i===0?'まとめ表現の意味':'日本語から表現を選ぶ',
     prompt:i===0?c.en:c.ja,correct:i===0?c.ja:c.en,choices:i===0?allJa:allEn,note:`${c.sample} — ${c.sampleJa}`});
  }
  for(let k=0;k<6;k++){
   const ex=es[k],jaOptions=es.map(t=>t.ja),enOptions=es.map(t=>t.en);
   bank.push({id:`${u.id}:en-ja:${k}`,unit:u.id,type:'choice',label:'英文を聞いて意味を選ぶ',prompt:ex.en,correct:ex.ja,choices:jaOptions,note:ex.why});
   bank.push({id:`${u.id}:ja-en:${k}`,unit:u.id,type:'choice',label:'接客場面に合う英語を選ぶ',prompt:ex.ja,correct:ex.en,choices:enOptions,note:ex.why});
   const parts=expressionChunks(ex.en);
   bank.push({id:`${u.id}:order:${k}`,unit:u.id,type:'order',label:'表現を組み立てる',prompt:ex.ja,correct:ex.en,chunks:parts,note:ex.why});
  }
 }
}

function chooseDistinct(q){if(q.type==='order'){q.bag=shuffle(q.chunks.map((value,id)=>({value,id})));q.placed=[];return q}const options=[q.correct,...shuffle(unique(q.choices).filter(x=>x!==q.correct)).slice(0,3)];q.options=shuffle(options);return q}
function startQuiz(ids,origin='custom'){let selected=ids.map(id=>bank.find(q=>q.id===id)).filter(Boolean).map(q=>chooseDistinct({...q}));if(!selected.length){notify('出題対象の問題がありません。');return}quiz={origin,questions:selected,at:0,score:0,firstTry:{},selected:null,chosen:null,answered:false};active=origin==='review'?'review':'test';render();scrollUp()}
function unitQuiz(id){const ids=bank.filter(q=>q.unit===Number(id)).map(q=>q.id);startQuiz(ids,'unit:'+id)}
function beginCustom(){const valid=bank.filter(q=>q.unit>=settings.from&&q.unit<=settings.to);const count=settings.count==='all'?valid.length:Math.min(Number(settings.count),valid.length);startQuiz(shuffle(valid).slice(0,count).map(q=>q.id),'custom')}
function current(){return quiz?.questions[quiz.at]}
function register(ok){if(quiz.answered)return;const q=current();quiz.answered=true;quiz.selected=ok;quiz.firstTry[q.id]=ok;if(ok)quiz.score++;progress.answered++;progress.correct+=Number(ok);if(ok)delete progress.wrong[q.id];else progress.wrong[q.id]=true;STORE();render()}
function selectChoice(value){if(!quiz||quiz.answered)return;quiz.chosen=value;register(value===current().correct)}
function wordChoice(idx,back=false){if(!quiz||quiz.answered||current().type!=='order')return;const q=current();if(back){let item=q.placed.splice(idx,1)[0];if(item)q.bag.push(item)}else{let item=q.bag.splice(idx,1)[0];if(item)q.placed.push(item)}render()}
function checkOrder(){if(!quiz||quiz.answered)return;const q=current();if(q.type!=='order'||q.bag.length)return;register(q.placed.map(x=>x.value).join(' ')===q.chunks.join(' '))}
function nextQuestion(){if(!quiz)return;if(quiz.at>=quiz.questions.length-1){finishQuiz();return}quiz.at++;quiz.selected=null;quiz.chosen=null;quiz.answered=false;render();scrollUp()}
function finishQuiz(){let ids=quiz.questions.map(q=>q.unit),set=unique(ids);if(quiz.origin.startsWith('unit:')&&quiz.questions.length===20){const id=Number(quiz.origin.split(':')[1]);progress.best[id]=Math.max(progress.best[id]||0,quiz.score);progress.last={unit:id,score:quiz.score,time:Date.now()}}
 STORE();quiz.result=true;render();scrollUp()}
function renderQuiz(){if(quiz.result)return renderQuizResult();const q=current(),answer=quiz.answered,idx=quiz.at;const choices=q.type==='choice'?`<div class="choiceList">${q.options.map((v,i)=>`<button data-action="choice" data-value="${E(v)}" class="choice ${answer&&v===q.correct?'correct':answer&&v===quiz.chosen&&v!==q.correct?'incorrect':''}" ${answer?'disabled':''}><b style="margin-right:10px;color:#a19ca0">${String.fromCharCode(65+i)}</b>${E(v)}</button>`).join('')}</div>`:`<div><div class="section-label">回答欄 — かたまりを順番に並べる</div><div class="chipAnswer">${q.placed.map((p,i)=>`<button data-action="word-back" data-id="${i}" ${answer?'disabled':''}>${E(p.value)} ×</button>`).join('')||'<span class="note">下から英語の語句を選択してください</span>'}</div><div class="section-label">かたまり・語句</div><div class="chipPool">${q.bag.map((p,i)=>`<button data-action="word-add" data-id="${i}" ${answer?'disabled':''}>${E(p.value)}</button>`).join('')}</div>${!answer?`<div class="buttonRow"><button class="btn" data-action="checkorder" ${q.bag.length?'disabled':''}>この語順で解答</button><button class="btn secondary" data-action="resetorder">やり直す</button></div>`:''}</div>`;
 const result=answer?`<div class="feedback ${quiz.selected?'ok':'bad'}"><strong>${quiz.selected?'✓ 正解！':'✕ 誤答：正解を確認しましょう'}</strong><p><b>正解：</b>${E(q.correct)}</p><p>${E(q.note)}</p>${q.type==='choice'&&/^[\x20-\x7e]+$/.test(q.correct)?speakButton(q.correct):''}</div><button class="btn full" data-action="next">${idx===quiz.questions.length-1?'結果を見る':'次の問題 →'}</button>`:'';
 setMain(`<div class="quizShell"><button class="back" data-action="quitquiz">← テスト設定に戻る</button><div class="quizMeta"><span>${E(q.label)} · UNIT ${q.unit}</span><span>${idx+1} / ${quiz.questions.length}</span></div><div class="progress"><i style="width:${(idx+Number(answer))/quiz.questions.length*100}%"></i></div><div class="quizPrompt"><div class="eyebrow">${q.type==='order'?'PUT THE WORDS IN ORDER':'CHOOSE ONE ANSWER'}</div><div class="quizTitle">${E(q.prompt)}</div>${q.type==='choice'&&/^[\x20-\x7e]+$/.test(q.prompt)?speakButton(q.prompt):''}</div>${choices}${result}<div class="note" style="margin-top:18px">1問目の解答結果を記録します。間違えた問題は自動的に「復習」に追加されます。</div></div>`)}
function renderQuizResult(){let total=quiz.questions.length,score=quiz.score,ok=score>=Math.ceil(total*.8),retry=quiz.questions.filter(q=>quiz.firstTry[q.id]===false).map(q=>q.id);setMain(`<div class="quizShell"><div class="eyebrow">TEST COMPLETE</div><h1 class="h1">${ok?'よくできました。':'間違えた箇所を復習しましょう。'}</h1><div class="panel"><div class="score">${score}<small> / ${total} 問</small></div><div class="progress"><i style="width:${score/total*100}%"></i></div><p class="sub">正答率 ${Math.round(score/total*100)}%　${quiz.origin.startsWith('unit:')?score>=16?'✓ 単元合格（16問以上）':'単元合格には16問以上必要です':'80%以上を目標に繰り返しましょう'}</p><div class="buttonRow">${retry.length?`<button class="btn" data-action="retrywrong">誤答${retry.length}問だけ再挑戦</button>`:''}<button class="btn secondary" data-action="quitagain">テスト設定へ</button>${quiz.origin.startsWith('unit:')?`<button class="btn secondary" data-action="unit" data-id="${quiz.origin.split(':')[1]}">講義を復習</button>`:''}</div></div><div class="section-label">今回の設問</div><div class="stack">${quiz.questions.map(q=>`<div class="panel between"><div><b style="font-size:12px">${E(q.label)}</b><div style="font-size:12px;color:var(--muted)">${E(q.prompt)}</div></div><span class="tag">${quiz.firstTry[q.id]?'正解':'復習'}</span></div>`).join('')}</div></div>`);quiz.retry=retry}
function renderTest(){const options=course.units.map(u=>`<option value="${u.id}">${String(u.id).padStart(2,'0')} · ${E(u.title)}</option>`).join('');const select=(v)=>options.replace(`value="${v}"`,`value="${v}" selected`);let pool=bank.filter(q=>q.unit>=settings.from&&q.unit<=settings.to).length;setMain(`<div class="eyebrow">PRACTICAL ENGLISH TEST</div><h1 class="h1">接客英語テスト</h1><p class="sub">対象の範囲と問題数を指定。全範囲選択も同じ画面から。32単元640問から出題します。</p><div class="panel"><div class="formGrid"><div class="field"><label for="from">開始単元</label><select id="from" data-setting="from">${select(settings.from)}</select></div><div class="field"><label for="to">終了単元</label><select id="to" data-setting="to">${select(settings.to)}</select></div></div><div class="formActions"><button class="btn secondary sm" data-action="allrange">全範囲を指定</button><span class="note">この範囲：${pool}問</span></div><div class="section-label">問題数</div><div class="qtys">${[10,20,30,40,50,80,100,'all'].map(n=>`<button class="btn sm ${settings.count===n?'selected':'secondary'}" data-action="qty" data-qty="${n}">${n==='all'?'範囲内すべて':n+'問'}</button>`).join('')}</div><div class="keyline"></div><button class="btn full" data-action="startcustom">この条件でテスト開始 →</button></div><div class="notice">文法用語や規則の暗記は出題しません。まとめ表現2問＋接客英文の意味・使い方12問＋表現の組み立て6問／単元。</div>`)}
function renderReview(){const wrongIds=Object.keys(progress.wrong).filter(id=>bank.some(q=>q.id===id));const noviceWrong=Object.keys(progress.beginnerWrong||{});setMain(`<div class="panel"><span class="tag">最初の24課</span><h2 class="beginner-h2">入門の復習</h2><p class="sub">間違えた問題：${noviceWrong.length}問</p><button class="btn secondary" data-action="beginner-review" ${noviceWrong.length?'':'disabled'}>入門の間違いを練習 →</button></div><div class="eyebrow">SMART REVIEW</div><h1 class="h1">間違えた問題だけ、繰り返す。</h1><p class="sub">テストの誤答を保存し、もう一度解いて正解すると一覧から外れます。苦手な表現を残さず復習できます。</p><div class="panel"><div class="between"><div><div class="score">${wrongIds.length}<small> 問</small></div><span class="note">復習対象</span></div><button class="btn" data-action="startreview" ${wrongIds.length?'':'disabled'}>まとめて復習 →</button></div></div><div class="section-label">登録中の問題</div>${wrongIds.length?`<div class="stack">${wrongIds.slice(0,100).map(id=>{let q=bank.find(b=>b.id===id);return `<div class="panel between"><div><span class="step">UNIT ${q.unit} · ${E(q.label)}</span><div style="font-size:13px">${E(q.prompt)}</div></div><button class="btn secondary sm" data-action="single" data-question="${id}">1問</button></div>`}).join('')}</div>`:'<div class="empty">現在、復習待ちの問題はありません。<br>テストに挑戦すると誤答がここに追加されます。</div>'}<div class="section-label">学習データ</div><div class="panel"><p class="note">端末内保存です。ブラウザのデータ消去や端末変更に備え、バックアップを保存できます。復元はこのアプリ専用のJSONファイルのみ受け付けます。</p><div class="buttonRow"><button class="btn secondary sm" data-action="export">学習記録を保存（JSON）</button><button class="btn secondary sm" data-action="import">バックアップを読み込む</button><input type="file" id="restoreFile" accept="application/json,.json" hidden></div></div>`)}
function renderScenarios(){if(scenarioId)return renderScene();setMain(`<div class="eyebrow">ROLEPLAY · REAL STORE SITUATIONS</div><h1 class="h1">その場で言えるまで練習する。</h1><p class="sub">お客様の質問を聞く → 自分で英語を考える → スタッフの回答例を開く、というロールプレイ方式。どの会話も料金やキャンペーンを無条件に保証しない説明にしています。</p>${voiceControl()}<div class="section-label">15の接客シーン</div><div class="infoGrid">${course.scenarios.map(sc=>`<div class="panel"><span class="tag">${E(sc.tag)}</span><h3>${E(sc.title)}</h3><p class="note">${sc.lines.length}発話 · 和訳・音声・回答の表示切替</p><button class="btn secondary sm" data-action="scene" data-id="${sc.id}">会話を練習する →</button></div>`).join('')}</div>`)}
function sceneSentenceParts(sc,line,index){
 const english=(line[1].match(/[^.!?]+(?:[.!?]+|$)/g)||[line[1]]).map(s=>s.trim()).filter(Boolean);
 const japanese=(line[2].match(/[^。！？]+[。！？]?/g)||[line[2]]).map(s=>s.trim()).filter(Boolean);
 // Two source translations combine multiple English sentences into one Japanese sentence.
 const corrected={
  'S4:2':['物理SIMは取り外せるカードです。','eSIMは対応端末に内蔵される仕組みです。'],
  'S14:5':['はい。対象のお客様はmy 楽天モバイルからオプションの追加・変更ができます。','現在の条件を確認しましょう。']
 };
 const ja=corrected[`${sc.id}:${index}`]||(english.length===japanese.length?japanese:english.length===1?[line[2]]:[line[2],...Array(english.length-1).fill('')]);
 return english.map((en,i)=>({en,ja:ja[i]||''}));
}
function renderScene(){
 const sc=course.scenarios.find(s=>s.id===scenarioId);
 if(!sc){scenarioId=null;return renderScenarios()}
 setMain(`<button class="back" data-action="backscenes">← 接客会話一覧へ</button><div class="eyebrow">ROLEPLAY · ${E(sc.tag)}</div><h1 class="h1">${E(sc.title)}</h1><p class="sub">お客様の英語を聞いて、自分ならどう答えるか考えましょう。スタッフの回答例は英文1文ずつ開けます。日本語訳と発音も一緒に確認できます。</p>${voiceControl()}<div class="toolbar" style="margin:18px 0"><button class="btn secondary sm" data-action="speakscene">会話全文の音声 ▶</button></div><div class="scene">${sc.lines.map((line,i)=>{
   const staff=line[0]==='staff';
   if(!staff)return `<div class="sceneLine"><div class="speaker">CUSTOMER · お客様</div><div class="en">${E(line[1])}</div><div class="ja">${E(line[2])}</div><div class="exampleActions">${speakButton(line[1])}</div></div>`;
   const parts=sceneSentenceParts(sc,line,i);
   return `<div class="sceneLine staff"><div class="speaker">STAFF · スタッフ</div><div class="scenePrompt">自分ならどう答える？</div>${parts.map((part,j)=>{
     const key=`${i}:${j}`,opened=scenarioRevealed.has(key);
     const answerId=`scene-answer-${sc.id}-${i}-${j}`;
     const label=parts.length===1?'この文の回答例を見る':`${j+1}文目の回答例を見る`;
     return `<div class="sceneAnswerUnit"><button type="button" class="btn secondary sm sceneReveal" data-action="reveal-sentence" data-line="${i}" data-sentence="${j}" data-reveal-label="${E(label)}" aria-controls="${E(answerId)}" aria-expanded="${opened}">${opened?'この文の回答例を隠す':E(label)}</button><div class="sceneAnswer" id="${E(answerId)}" ${opened?'':'hidden'}><div class="en">${E(part.en)}</div>${part.ja?`<div class="ja">${E(part.ja)}</div>`:''}<div class="exampleActions">${speakButton(part.en)}</div></div></div>`;
   }).join('')}</div>`;
 }).join('')}</div><div class="disclaimer">本会話は学習用の例であり、契約の可否やキャンペーン適用を保証するものではありません。実務では最新の公式情報をご確認ください。</div>`)
}
function renderPhrases(){
 const matches=c=>[c.en,c.ja,c.sample,c.sampleJa].some(s=>s.toLowerCase().includes(phraseSearch.toLowerCase()));
 const filteredChunks=chunks.filter(c=>(phraseFilter==='全部'||course.chapters.find(ch=>ch.id===course.units[c.unit-1].chapter).title===phraseFilter)&&matches(c));
 const ordered=filteredChunks.slice().sort((a,b)=>Number(Boolean(progress.learnedChunks?.[a.id]))-Number(Boolean(progress.learnedChunks?.[b.id]))||a.unit-b.unit);
 const examples=course.units.flatMap(u=>u.examples.map(e=>({...e,chapter:u.chapter,unit:u.id,title:u.title})));
 const filteredExamples=examples.filter(x=>(phraseFilter==='全部'||course.chapters.find(c=>c.id===x.chapter).title===phraseFilter)&&(!favoritesOnly||progress.favorites[x.id])&&[x.en,x.ja,x.why,x.title].some(s=>s.toLowerCase().includes(phraseSearch.toLowerCase())));
 const mastered=chunks.filter(c=>progress.learnedChunks?.[c.id]).length;
 setMain(`<div class="eyebrow">CHUNKS · REAL STORE ENGLISH</div><h1 class="h1">単語ではなく、英語をかたまりで覚える。</h1><p class="sub"><b>depend on（〜によって変わる）</b>のような、よく一緒に使う言葉をそのまま覚えます。意味 → 発音 → 実際の接客例文で確認しましょう。</p>${voiceControl()}<div class="searchbar"><input class="input" id="search" placeholder="例：depend on / 対象 / 契約 / ポイント" value="${E(phraseSearch)}" aria-label="まとめ表現や接客例文を検索"></div><div class="toolbar"><select id="phraseFilter" style="max-width:245px" data-setting="phraseFilter"><option>全部</option>${course.chapters.map(c=>`<option ${phraseFilter===c.title?'selected':''}>${E(c.title)}</option>`).join('')}</select><button class="btn sm ${favoritesOnly?'selected':'secondary'}" data-action="favoritesonly">☆ 例文の保存済みだけ</button></div><div class="panel" style="margin:14px 0"><div class="between"><div><b>まとめ表現 64個</b><p class="note">覚えた ${mastered} / 64 · 未習得を先に表示</p></div><button class="btn" data-action="chunktest">まとめ表現だけ10問 →</button></div></div><div class="section-label">まず覚える英語のかたまり · ${filteredChunks.length}件</div><div class="chunkGrid">${ordered.map(c=>`<article class="panel chunkCard"><span class="step">UNIT ${String(c.unit).padStart(2,'0')}</span><h3>${E(c.en)}</h3><div class="exampleJa">${E(c.ja)}</div><div class="chunkSample">${E(c.sample)}</div><p class="note">${E(c.sampleJa)}</p><div class="exampleActions">${speakButton(c.en)} ${speakButton(c.sample)}<button class="btn secondary sm ${progress.learnedChunks?.[c.id]?'selected':''}" data-action="known-chunk" data-id="${c.id}" aria-pressed="${Boolean(progress.learnedChunks?.[c.id])}">${progress.learnedChunks?.[c.id]?'✓ 覚えた':'○ 覚えたら押す'}</button></div></article>`).join('')}</div><div class="section-label">接客例文 224 · ${filteredExamples.length}件</div>${filteredExamples.length?`<div class="phraseItems">${filteredExamples.slice(0,120).map(x=>`<article class="panel example"><span class="step">UNIT ${x.unit} · ${E(x.title)}</span><div class="exampleEn">${E(x.en)}</div><div class="exampleJa">${E(x.ja)}</div><p class="explain">${E(x.why)}</p><div class="exampleActions">${speakButton(x.en)}<button class="btn secondary sm" data-action="favorite" data-example="${x.id}">${progress.favorites[x.id]?'★ 保存済み':'☆ 保存'}</button><button class="btn secondary sm" data-action="copy" data-example="${x.id}">コピー</button></div></article>`).join('')}</div>`:'<div class="empty">検索に一致する例文はありません。</div>'}${filteredExamples.length>120?'<p class="note">例文は先頭120件を表示しています。検索で絞り込めます。</p>':''}`);
}
function renderFacts(){setMain(`<div class="eyebrow">OFFICIAL FACT CHECK · ${course.reviewedOn}</div><h1 class="h1">契約・料金・キャンペーンの根拠を確認。</h1><p class="sub">教材内の実務に関する数値や制度の確認先です。<b>このアプリは公式サイトをリアルタイム同期しません。</b>特典を案内する前に該当する公式ページを開いてください。</p><div class="disclaimer"><b>注意：</b>${E(course.disclaimer)} 紹介リンク／QRと店舗専用のキャンペーンコードを混同しないこと。内容は予告なく変更されます。</div><div class="section-label">確認済み項目</div><div class="stack">${course.facts.map(f=>`<article class="panel fact"><span class="tag">${E(f.tag)}</span><div><h3>${E(f.title)}</h3><p>${E(f.body)}</p><a href="${E(course.sources[f.source].url)}" target="_blank" rel="noopener noreferrer">公式情報：${E(course.sources[f.source].label)} ↗</a></div></article>`).join('')}</div><div class="section-label">公式の参照リンク</div><div class="panel">${course.sources.map(s=>`<p><a href="${E(s.url)}" target="_blank" rel="noopener noreferrer">${E(s.label)} ↗</a></p>`).join('')}</div>`)}
function render(){if(!course||!beginner)return;if(active==='beginner'){if(beginnerQuiz){if(beginnerStep===4)renderBeginnerResult();else renderBeginnerQuiz();return}if(beginnerId!==null){renderBeginnerLesson();return}renderBeginnerHome();return}if(quiz){renderQuiz();return}if(unitId){renderUnit();return}if(active==='learn')renderLearn();else if(active==='test')renderTest();else if(active==='review')renderReview();else if(active==='scenarios')renderScenarios();else if(active==='phrases')renderPhrases();else renderFacts()}
function restoreFile(file){if(!file)return;if(file.size>1024*1024){notify('大きすぎるファイルです。');return}const reader=new FileReader();reader.onload=()=>{try{let parsed=JSON.parse(reader.result);if(parsed.app!=='counter-english'||!parsed.progress||!parsed.progress.best||!parsed.progress.wrong)throw new Error('形式が違います');const p=parsed.progress;if(!['object'].includes(typeof p.favorites)||typeof p.answered!=='number')throw new Error('データが不正です');progress={...progress,...p};STORE();notify('学習記録を復元しました');render()}catch(e){notify('このアプリ用のバックアップJSONを選択してください')}};reader.readAsText(file)}
const handle=async b=>{if(b.dataset.tab){nav(b.dataset.tab);return}const a=b.dataset.action;
 if(a==='beginner-home'){beginnerId=null;beginnerQuiz=null;active='beginner';render();scrollUp()}
 else if(a==='beginner-phase'){beginnerPhase=beginnerPhase===Number(b.dataset.id)?null:Number(b.dataset.id);render()}
 else if(a==='beginner-unit'){beginnerId=Number(b.dataset.id);beginnerPhase=Math.ceil(beginnerId/4);beginnerStep=0;beginnerQuiz=null;beginnerHidden={};active='beginner';render();scrollUp()}
 else if(a==='beginner-step'){beginnerStep=Number(b.dataset.id);beginnerQuiz=null;render();scrollUp()}
 else if(a==='beginner-start'){beginnerStart()}
 else if(a==='beginner-back-example'){beginnerQuiz=null;beginnerStep=2;render();scrollUp()}
 else if(a==='beginner-hide-translation'){let i=Number(b.dataset.id);beginnerHidden[i]=!beginnerHidden[i];let el=b.closest('article')?.querySelector('.exampleJa');if(el)el.hidden=beginnerHidden[i];b.textContent=beginnerHidden[i]?'日本語を見る':'日本語を隠して挑戦'}
 else if(a==='say-letter'){speak(b.dataset.letter)}
 else if(a==='beginner-choice'){beginnerAnswer(b.dataset.answer===beginnerCurrent().correct,b.dataset.answer)}
 else if(a==='beginner-order-add'){beginnerOrder(Number(b.dataset.id))}
 else if(a==='beginner-order-remove'){beginnerOrder(Number(b.dataset.id),true)}
 else if(a==='beginner-order-reset'){let q=beginnerCurrent();q.pool=shuffle(q.chunks.map((value,id)=>({value,id})));q.placed=[];render()}
 else if(a==='beginner-check-order'){let q=beginnerCurrent();if(q.pool.length)return;beginnerAnswer(q.placed.map(x=>x.value).join(' ')===q.chunks.join(' '),q.placed.map(x=>x.value).join(' '))}
 else if(a==='beginner-hint'){beginnerQuiz.hint=!beginnerQuiz.hint;render()}
 else if(a==='beginner-next'){beginnerNextQ()}
 else if(a==='beginner-retry'){beginnerStart(beginnerQuiz.retry)}
 else if(a==='beginner-review'){let ids=Object.keys(progress.beginnerWrong||{});if(ids.length){const n=Number(ids[0].split(':')[0].slice(1));beginnerId=n;beginnerPhase=Math.ceil(n/4);active='beginner';beginnerStart(ids.filter(id=>id.startsWith('B'+n+':')))}}
 else if(a==='chapter'){chapterOpen=chapterOpen===Number(b.dataset.id)?null:Number(b.dataset.id);render()}
 else if(a==='unit'){unitId=Number(b.dataset.id);active='learn';quiz=null;render();scrollUp()}
 else if(a==='backlearn'){unitId=null;active='learn';render();scrollUp()}
 else if(a==='unitquiz'){unitQuiz(b.dataset.id)}
 else if(a==='allrange'){settings.from=1;settings.to=32;render()}
 else if(a==='qty'){settings.count=b.dataset.qty==='all'?'all':Number(b.dataset.qty);render()}
 else if(a==='startcustom'){beginCustom()}
 else if(a==='startreview'){startQuiz(shuffle(Object.keys(progress.wrong)),'review')}
 else if(a==='single'){startQuiz([b.dataset.question],'review')}
 else if(a==='choice'){selectChoice(b.dataset.value)}
 else if(a==='word-add'){wordChoice(Number(b.dataset.id))}
 else if(a==='word-back'){wordChoice(Number(b.dataset.id),true)}
 else if(a==='resetorder'){let q=current();q.bag=shuffle(q.chunks.map((value,id)=>({value,id})));q.placed=[];render()}
 else if(a==='checkorder'){checkOrder()}
 else if(a==='next'){nextQuestion()}
 else if(a==='retrywrong'){startQuiz(quiz.retry,quiz.origin.startsWith('unit:')?'review':'review')}
 else if(a==='quitquiz'||a==='quitagain'){quiz=null;unitId=null;active='test';render();scrollUp()}
 else if(a==='scene'){scenarioId=b.dataset.id;scenarioRevealed=new Set();render();scrollUp()}
 else if(a==='backscenes'){scenarioId=null;render();scrollUp()}
 else if(a==='reveal-sentence'){
  const key=`${Number(b.dataset.line)}:${Number(b.dataset.sentence)}`;
  const answer=document.getElementById(b.getAttribute('aria-controls'));
  if(!answer)return;
  const opened=!scenarioRevealed.has(key);
  if(opened)scenarioRevealed.add(key);else scenarioRevealed.delete(key);
  answer.hidden=!opened;
  b.setAttribute('aria-expanded',String(opened));
  b.textContent=opened?'この文の回答例を隠す':b.dataset.revealLabel;
 }
 else if(a==='speakscene'){let sc=course.scenarios.find(s=>s.id===scenarioId);speak(sc.lines.map(x=>x[1]).join(' '))}
 else if(a==='speak'){speak(voiceMap[b.dataset.voice])}
 else if(a==='favorite'){let id=b.dataset.example;if(progress.favorites[id])delete progress.favorites[id];else progress.favorites[id]=true;STORE();render()}
 else if(a==='chunktest'){const ids=shuffle(bank.filter(q=>q.id.includes(':chunk:'))).slice(0,10).map(q=>q.id);startQuiz(ids,'chunks')}
 else if(a==='known-chunk'){progress.learnedChunks=progress.learnedChunks||{};const key=b.dataset.id;if(progress.learnedChunks[key])delete progress.learnedChunks[key];else progress.learnedChunks[key]=true;STORE();const known=!!progress.learnedChunks[key];b.textContent=known?'✓ 覚えた':'○ 覚えたら押す';b.classList.toggle('selected',known);b.setAttribute('aria-pressed',String(known))}
 else if(a==='favoritesonly'){favoritesOnly=!favoritesOnly;render()}
 else if(a==='copy'){let ex=course.units.flatMap(u=>u.examples).find(x=>x.id===b.dataset.example);try{await navigator.clipboard.writeText(ex.en+'\n'+ex.ja);notify('例文をコピーしました')}catch(e){notify('コピーできませんでした')}}
 else if(a==='export'){const text=JSON.stringify({app:'counter-english',version:1,exportedAt:new Date().toISOString(),progress},null,2);const url=URL.createObjectURL(new Blob([text],{type:'application/json'}));const link=document.createElement('a');link.href=url;link.download='counter-english-learning-backup.json';link.click();setTimeout(()=>URL.revokeObjectURL(url),1500)}
 else if(a==='import'){$('#restoreFile')?.click()}
};
document.addEventListener('click',ev=>{const b=ev.target.closest('button[data-action],button[data-tab]');if(b)handle(b)});
document.addEventListener('change',ev=>{let el=ev.target;if(el.id==='restoreFile'){restoreFile(el.files[0]);el.value='';return}if(!el.dataset.setting)return;const type=el.dataset.setting;if(type==='from'||type==='to'){settings[type]=Number(el.value);if(settings.from>settings.to){if(type==='from')settings.to=settings.from;else settings.from=settings.to}render()}else if(type==='speed'){voice.rate=Number(el.value);storeVoice();notify('音声速度を変更しました')}else if(type==='locale'){voice.locale=el.value;storeVoice();notify('発音の種類を変更しました')}else if(type==='phraseFilter'){phraseFilter=el.value;render()}});
document.addEventListener('input',ev=>{if(ev.target.id==='search'){let pos=ev.target.selectionStart;phraseSearch=ev.target.value;render();let x=$('#search');x?.focus();x?.setSelectionRange(pos,pos)}});
async function init(){try{const r=await fetch('./data/course.json',{cache:'no-cache'});if(!r.ok)throw new Error(r.status);course=await r.json();const c=await fetch('./data/chunks.json',{cache:'no-cache'});if(!c.ok)throw new Error('まとめ表現データがありません');chunks=(await c.json()).chunks;if(chunks.length!==64||course.units.some(u=>chunks.filter(c=>c.unit===u.id).length!==2))throw new Error('まとめ表現データの不整合');const b=await fetch('./data/beginner.json',{cache:'no-cache'});if(!b.ok)throw new Error('入門教材がありません');beginner=await b.json();if(beginner.units.length!==24)throw new Error('入門教材の不整合');if(course.units.length!==32)throw new Error('教材単元数の不整合');makeBank();if(bank.length!==640)throw new Error('設問数の不整合');render();if('serviceWorker'in navigator&&location.protocol==='https:')navigator.serviceWorker.register('./sw.js').catch(()=>{})}catch(e){$('#main').innerHTML=`<div class="panel"><h1>教材を読み込めませんでした</h1><p>NetlifyなどのWebサーバーから公開してください。直接ファイルを開く場合はブラウザの制約により読み込めない場合があります。</p><p class="error">${E(e.message)}</p><button class="btn" onclick="location.reload()">再読み込み</button></div>`;console.error(e)}}
init();
})();
