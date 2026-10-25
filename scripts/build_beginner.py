#!/usr/bin/env python3
"""Build a Japanese-first, zero-English prerequisite course for shop staff.
Each lesson is hand-authored and validated; practice items are reproducible.
"""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
PHASES=[
 ('英語の最初の一歩','アルファベット・数字・単語の順番を知る'),
 ('最初の短い英文','主語・be動詞・名詞から一文を作る'),
 ('お客様とやりとり','質問・否定・できることを伝える'),
 ('丁寧にお願いする','本人確認や希望の聞き取りを伝える'),
 ('料金とプラン','金額・データ量・割引を正確に表現する'),
 ('契約を案内する','SIM・手続き・トラブルを説明する')]
# ID, title, goal, short Japanese explanations (3), key vocabulary (en=ja),
# formula, one fully analyzed sample phrase (en=ja), examples (EN|JA|why).
LESSONS=[
(1,'アルファベットと略語','SIM・ID・QRの文字を見分ける',
 ['英語は A〜Z の26文字を組み合わせて書きます。まずは店頭にある短い表記を「見て分かる」ことを目指します。読み書きが得意でなくても大丈夫です。',
  'SIM は「シム」、eSIM は「イーシム」と呼ぶことが多い表記です。ID は「アイディー」、QR は「キューアール」と一文字ずつ読みます。発音ボタンで必ず耳でも確かめましょう。',
  '文の終わりの . は「ここで文が終わり」、? は質問です。大文字は文の最初や固有名詞にも使います。完璧な発音はあとからで構いません。'],
 'SIM=SIMカード|eSIM=内蔵型SIM|ID=本人確認書類・ID|QR code=QRコード|phone=電話|plan=プラン',
 'This is + 名詞 = これは〜です','This=これは|is=です|a SIM card.=SIMカード',[
 ('This is a SIM card.','これはSIMカードです。','最初は This is をひとかたまりで覚えよう。'),
 ('This is an eSIM.','これはeSIMです。','eSIM は音が「イー」で始まるので an。'),
 ('This is a QR code.','これはQRコードです。','QR は文字を1つずつ読む略語。'),
 ('This is my ID.','これは私の本人確認書類です。','my は「私の」。'),
 ('This is the plan.','こちらがそのプランです。','the は相手と共有している対象に使う。')]),
(2,'1から1000までの数字','料金とデータ量の読み方を知る',
 ['数字は料金説明の基本です。まず one=1、two=2、three=3、ten=10、twenty=20、hundred=100、thousand=1000 を音と一緒に覚えます。',
  '英語の数字は大きい単位から読みます。例: 2,000 = two thousand、2,500 = two thousand five hundred。yen は複数になっても yens にはしません。',
  'GB は gigabytes（ギガバイツ）と読むことができます。料金や特典は変更があるので、ここでは「金額の言い方」を先に練習します。'],
 'one=1|two=2|three=3|ten=10|twenty=20|hundred=100|thousand=1000|yen=円|gigabyte=ギガバイト',
 '数字 + yen / gigabytes = 金額・データ量','Two=2|gigabytes=ギガバイト|are available.=利用できます',[
 ('One gigabyte is enough.','1ギガバイトで十分です。','one は1。'),('Two gigabytes are available.','2ギガバイト利用できます。','two の後は gigabytes と複数。'),('The fee is one thousand yen.','料金は1,000円です。','thousand は1000。'),('The fee is two thousand yen.','料金は2,000円です。','2,000 を音読しよう。'),('Twenty gigabytes is a lot of data.','20ギガバイトは多くのデータ量です。','数字と単位をセットで読む。')]),
(3,'英語の語順','誰が・どうする・何を の順番を理解する',
 ['日本語は「このプランを / 私は / おすすめします」のように順番を入れ替えられます。しかし英語は基本的に「誰が → どうする → 何を」の順番です。',
  'I recommend this plan. は I（私は）+ recommend（すすめる）+ this plan（このプラン）。単語を一個ずつ暗記するより、この並びを真似ると応用できます。',
  '最初は長文を作らず、I check / You choose / We explain のような2語から増やします。'],
 'I=私は|you=あなたは|we=私たちは|check=確認する|recommend=おすすめする|need=必要とする|plan=プラン',
 '誰が + どうする + 何を','I=私は|recommend=おすすめする|this plan.=このプランを',[
 ('I recommend this plan.','私はこのプランをおすすめします。','誰が→どうする→何を。'),('I check your ID.','私は本人確認書類を確認します。','I + check + your ID。'),('You choose the SIM.','あなたがSIMを選びます。','You が文の主人公。'),('We explain the fee.','私たちが料金を説明します。','We は「私たちは」。'),('I need your name.','お名前が必要です。','直訳は「私はあなたの名前を必要とする」。')]),
(4,'最初のあいさつ','短い決まり文句で受付を始める',
 ['全部の文法が分からなくても、まずは店頭で使える短い表現をひとつずつ覚えましょう。Hello は「こんにちは」、Welcome は「ようこそ」。',
  'How can I help you? は「どのようなご用件でしょうか」。疑問文の詳しい形は後の単元で学ぶので、ここではひとかたまりで練習します。',
  '聞き取れなかったら Sorry, one more time, please. のように聞き直してよいです。誤案内を避けるために確認するのは大切です。'],
 'hello=こんにちは|welcome=ようこそ|thank you=ありがとうございます|sorry=すみません|please=お願いします|help=お手伝い',
 'あいさつ + 短い質問','Hello.=こんにちは|Welcome=ようこそ|to Rakuten Mobile.=楽天モバイルへ',[
 ('Hello.','こんにちは。','最初の一言。'),('Welcome to Rakuten Mobile.','楽天モバイルへようこそ。','Welcome to で「〜へようこそ」。'),('How can I help you?','どのようなご用件でしょうか。','まずは丸ごと覚える接客フレーズ。'),('Thank you for waiting.','お待ちいただきありがとうございます。','for waiting で「お待ちいただいたことに」。'),('One more time, please.','もう一度お願いします。','聞き直しに使う。')]),
(5,'I・you・we・it','文の主人公を選ぶ',
 ['英語の主語とは「誰の話なのか」を示す言葉です。I=私、you=あなた、we=私たち、it=それ。まずこの4つを区別します。',
  '日本語では「確認します」とだけ言っても通じますが、英語では I check のように主語を入れるのが基本です。',
  'it はすでに話題にしたSIMやプランなどを指すのに便利です。「それは〜です」と繰り返さず言えます。'],
 'I=私|you=あなた|we=私たち|it=それ|my=私の|your=あなたの|this=これ',
 'I / you / we / it + 動詞','I=私は|have=持っています|the SIM.=SIMを',[
 ('I have the SIM.','私はSIMを持っています。','I は「私は」。'),('You have a phone.','あなたは電話を持っています。','You は「あなたは」。'),('We have the details.','私たちは詳細情報を持っています。','We は「私たちは」。'),('It has a number.','それには番号があります。','It を主語にすると has。'),('This is your plan.','こちらがお客様のプランです。','your は「あなたの」。')]),
(6,'am・is・are','「〜です」を初めて作る',
 ['be動詞は「〜です」「〜の状態です」と言うときの動詞です。I には am、you/we には are、it/this には is を使います。',
  'I am ready. = 私は準備できています。This is free. = これは無料です。日本語の「です」をそのまま一語に当てはめず、主語とセットで考えます。',
  '疑問文にするときは Is this ...? のように is を先に出します。今日はまず「主語 + be動詞」を自分で言えることがゴールです。'],
 'am=です（Iと）|is=です（it/thisと）|are=です（you/weと）|ready=準備ができた|free=無料|available=利用できる',
 '主語 + am / is / are + 説明','I=私は|am=です|ready.=準備できた',[
 ('I am ready.','私は準備できています。','I の後は am。'),('This is free.','これは無料です。','This の後は is。'),('You are ready.','準備できていますね。','You の後は are。'),('We are here to help.','私たちがお手伝いします。','We の後は are。'),('The SIM is available.','そのSIMは利用できます。','単数のSIMには is。')]),
(7,'this・that・these','目の前のものを指して案内する',
 ['this は「これ」、that は「あれ」、these は「これら」です。SIMカードを指さして This is ... と言うだけでも接客が始められます。',
  'these の後には複数の物を置き、These are ... となります。This are や These is にならないようにします。',
  'this plan（このプラン）のように名詞とくっつけても使えます。'],
 'this=これ|that=あれ|these=これら|card=カード|option=オプション|device=端末',
 'This is ... / These are ...','This=これは|is=です|your SIM.=お客様のSIM',[
 ('This is your SIM.','こちらがお客様のSIMです。','一つの物は This is。'),('That is the counter.','あちらがカウンターです。','離れた物は That。'),('These are the options.','こちらがオプションです。','複数は These are。'),('This plan is simple.','このプランはシンプルです。','This + 名詞でも使える。'),('That device is compatible.','あちらの端末は対応しています。','That + 名詞。')]),
(8,'a・an・the と複数形','SIMが1枚か複数かを区別する',
 ['英語では数えられる物が1つのとき a / an をつけることが多いです。a SIM、an eSIM のように「音」で選びます。',
  '2つ以上なら two SIM cards のように名詞を複数形にします。card → cards。数の話では最後の s を意識します。',
  'the は「話し手と聞き手が分かっている、その〜」のように使います。無理に全部訳さなくても構いません。'],
 'a=ひとつの|an=ひとつの（母音の音の前）|the=その|card=カード|number=番号|two=2|three=3',
 'a / an + 単数 / 数字 + 複数','I=私は|have=持っています|a SIM card.=SIMカードを1枚',[
 ('I have a SIM card.','私はSIMカードを1枚持っています。','一つのcardには a。'),('This is an eSIM.','これはeSIMです。','イーで始まる音なので an。'),('You have two numbers.','番号を2つお持ちです。','two の後は numbers。'),('We have three options.','オプションが3種類あります。','three の後も複数形。'),('The SIM is ready.','そのSIMは準備できています。','特定のSIMなので the。')]),
(9,'Yes / No の答え方','質問を理解して一言で答える',
 ['Yes は「はい」、No は「いいえ」です。ただし英語の Yes/No は「相手の質問が正しいか」に対して答えます。',
  'Is this your phone? = これはお客様の電話ですか。Yes, it is. = はい、そうです。No, it is not. = いいえ、違います。',
  'お客様のYes/Noだけでは契約条件が曖昧なときは、必ず具体的に確認しましょう。'],
 'yes=はい|no=いいえ|is=ですか|it=それ|not=〜ではない|correct=正しい',
 'Is this ...? → Yes, it is.','Is=ですか|this=これは|your phone?=お客様の電話',[
 ('Is this your phone?','これはお客様の電話ですか。','Is を先頭に置くと質問。'),('Yes, it is.','はい、そうです。','Is this? に対する答え。'),('No, it is not.','いいえ、違います。','否定の答え。'),('Is this correct?','こちらで正しいですか。','情報の確認に使う。'),('Yes, that is correct.','はい、そのとおりです。','that is correct は確認の答え。')]),
(10,'not / do not','「〜ではない」を伝える',
 ['not は「〜ではありません」。be動詞の文は is not / are not の形で否定します。',
  '一般動詞なら I do not know. = 私は分かりません。英語で正確に答えられない場合は、推測せずに確認します。',
  'not free（無料ではない）と free（無料）は意味が反対です。料金案内では not を必ず聞き取る練習が必要です。'],
 'not=〜ではない|know=知っている|free=無料|included=含まれる|available=利用可能|yet=まだ',
 'is not / do not + 動詞','I=私は|do not know=分かりません|yet.=まだ',[
 ('I do not know yet.','まだ分かりません。','do not know で「知らない」。'),('This option is not free.','このオプションは無料ではありません。','not の有無が料金説明の要。'),('The SIM is not ready.','SIMはまだ準備できていません。','is not で否定。'),('This fee is not included.','この料金は含まれていません。','included と not に注意。'),('We do not need it.','それは必要ありません。','一般動詞の否定は do not。')]),
(11,'what・how much','何ですか・いくらですかを聞く',
 ['What は「何」、How much は「いくら」。料金や希望を聞くための基本の疑問詞です。',
  'What is this? = これは何ですか。How much is it? = いくらですか。短い語順のパターンをセットで覚えます。',
  'How many は数を聞くときに使います。How many lines? は「回線はいくつですか」です。'],
 'what=何|how much=いくら|how many=何個|line=回線|price=価格|need=必要',
 'What is ...? / How much is ...?','How much=いくら|is=ですか|this plan?=このプランは',[
 ('How much is this plan?','このプランはいくらですか。','How much は金額。'),('What is this?','これは何ですか。','What is は「何ですか」。'),('How many lines do you need?','何回線必要ですか。','How many は数えられる物の数。'),('What is your name?','お名前は何ですか。','What is your ...? と置き換えられる。'),('How much data do you use?','データはどれくらい使いますか。','data量には How much。')]),
(12,'can / cannot','できること・できないことを伝える',
 ['can は「〜できます」。can のあとに動詞の原形を置きます。I can check. = 確認できます。',
  'cannot は「できません」。I cannot confirm yet. = まだ確認できません。確証がないときは「できる」と言い切らないようにします。',
  'Can I ...? は「〜してもよいですか」と許可を求められる便利な形です。'],
 'can=できる|cannot=できない|check=確認する|use=使う|scan=読み取る|confirm=確かめる',
 '主語 + can + 動詞の原形','I=私は|can check=確認できます|your SIM.=お客様のSIMを',[
 ('I can check your SIM.','お客様のSIMを確認できます。','can のあとに check。'),('Can I check your ID?','本人確認書類を確認してもよいですか。','Can I は許可の質問。'),('You can use this phone.','この電話を使えます。','You can use。'),('We cannot confirm it yet.','まだ確認できません。','cannot で不可能。'),('Can you scan this code?','このコードを読み取れますか。','Can you は可能かを聞く。')]),
(13,'please / could you','失礼のないお願いをする',
 ['Please + 動詞 は「〜してください」。Please wait. = お待ちください。最初は短い形を使えば十分です。',
  'Could you ...? は「〜していただけますか」の丁寧な依頼。Could you show me your ID? とすると本人確認のお願いになります。',
  '丁寧な表現でも、個人情報を扱う際は実際の店頭ルールに従ってください。'],
 'please=お願いします|could you=〜していただけますか|wait=待つ|show=見せる|sign=署名する|here=ここ',
 'Please + 動詞 / Could you + 動詞?','Could you=していただけますか|show me=私に見せる|your ID?=本人確認書類を',[
 ('Please wait here.','こちらでお待ちください。','Please wait。'),('Could you show me your ID?','本人確認書類を見せていただけますか。','Could you は丁寧。'),('Please sign here.','ここにご署名ください。','sign は署名する。'),('Could you repeat that?','もう一度おっしゃっていただけますか。','聞き直しも丁寧に。'),('Please check this name.','このお名前をご確認ください。','Please + 原形。')]),
(14,'would like / want','お客様の希望を聞き取る',
 ['want は「欲しい・したい」です。I want an eSIM. = eSIMが欲しい。',
  'would like は want より丁寧です。Would you like an eSIM? = eSIMをご希望ですか。',
  '「契約したい」のように動作を言うときは would like to + 動詞。Would you like to keep your number? が便利です。'],
 'want=欲しい|would like=希望する|keep=維持する|change=変更する|number=番号|eSIM=eSIM',
 'Would you like + 名詞? / to + 動詞?','Would you like=ご希望ですか|an eSIM?=eSIMを',[
 ('Would you like an eSIM?','eSIMをご希望ですか。','相手の希望を丁寧に聞く。'),('I want a SIM card.','SIMカードが欲しいです。','want は欲しい。'),('Would you like to keep your number?','今の電話番号を引き継ぎたいですか。','would like to の後は動詞。'),('Do you want to change plans?','プラン変更をご希望ですか。','Do you want to で希望を聞く。'),('I would like to check first.','まず確認したいです。','丁寧な自分の希望。')]),
(15,'need / have to','必要なものを伝える',
 ['need は「必要とする」です。We need your ID. = 本人確認書類が必要です。',
  'need to + 動詞 なら「〜する必要があります」。You need to confirm your details. の形です。',
  'have to も「〜しなければならない」ですが、実際の必要書類や手続き条件は最新の公式情報・社内手順で確認してください。'],
 'need=必要|need to=〜する必要|have to=〜しなければならない|confirm=確認する|details=詳細|document=書類',
 'need + 名詞 / need to + 動詞','We=私たちは|need=必要です|your ID.=本人確認書類が',[
 ('We need your ID.','本人確認書類が必要です。','need の後は物。'),('You need to confirm your details.','ご自身の情報を確認する必要があります。','need to の後は動詞。'),('We need your signature.','ご署名が必要です。','signature は署名。'),('Please check the document.','書類をご確認ください。','Please check で丁寧な指示。'),('Do I have to sign here?','ここに署名する必要がありますか。','have to の疑問形。')]),
(16,'名前・番号・本人確認','聞き取った情報を確認する',
 ['name=名前、address=住所、phone number=電話番号。聞き取った情報をそのまま書き留めず、相手に復唱して確認します。',
  'Could you spell your name? は「お名前のつづりを教えていただけますか」。spell はアルファベットで言うことです。',
  '正確に聞き取れないときは確認をお願いするのが安全です。本人確認の方法は公式の受付ルールに従います。'],
 'name=名前|spell=つづりを言う|address=住所|phone number=電話番号|confirm=確認する|again=もう一度',
 'Could you + 動詞 + 対象?','Could you=していただけますか|spell=つづりを言う|your name?=お名前を',[
 ('Could you spell your name?','お名前のつづりを教えていただけますか。','spell を使う。'),('What is your phone number?','電話番号を教えていただけますか。','What is your ...? の形。'),('Could you confirm your address?','ご住所を確認していただけますか。','confirm は確認。'),('Please say the number again.','番号をもう一度おっしゃってください。','again はもう一度。'),('Is this your full name?','こちらがフルネームですか。','Is this で確認する。')]),
(17,'料金を英語で読む','yen と金額を一文で伝える',
 ['金額は The price is ... yen. の形で言えます。声に出して区切り、桁数を誤らないことを優先します。',
  '1,000 は one thousand、2,500 は two thousand five hundred。円は yen で、語尾に s を付けません。',
  'ここに示す金額は読み上げの練習用の例で、契約時の料金表とは限りません。実際の案内では最新表示額を読み上げます。'],
 'price=価格|fee=料金|yen=円|thousand=千|hundred=百|total=合計|estimate=見積もり',
 'The price is + 金額 + yen.','The price=料金は|is=です|two thousand yen.=2,000円',[
 ('The price is two thousand yen.','料金は2,000円です。','練習用の金額。'),('The fee is one thousand yen.','料金は1,000円です。','練習用の金額。'),('The total is three thousand yen.','合計は3,000円です。','total は合計。'),('This is an estimate.','こちらはお見積もりです。','estimate は見積もり。'),('The device costs five thousand yen.','端末は5,000円です。','costs は費用がかかる。')]),
(18,'月額・税込・追加料金','per month / including tax を言う',
 ['per month は「1か月あたり」、including tax は「税込み」。数字の直後に付け加えるだけで料金説明が正確になります。',
  'A monthly fee は月額料金、an extra fee は追加料金。free（無料）と included（料金に含まれる）は意味が同じとは限りません。',
  '月額以外の手数料や端末代金も別々に案内する必要があります。どの金額なのか名詞を明示して伝えます。'],
 'per month=月額|including tax=税込み|monthly=毎月の|extra=追加の|fee=料金|included=含まれる',
 '金額 + yen + per month','This=これは|is=です|a monthly fee.=月額料金',[
 ('This is a monthly fee.','これは月額料金です。','monthly fee で月額料金。'),('The price includes tax.','その価格には税金が含まれます。','includes tax で税込。'),('There is an extra fee.','追加料金があります。','extra fee に注意。'),('This option has a monthly fee.','このオプションには月額料金があります。','月額の対象を明確にする。'),('The device price is separate.','端末代金は別です。','separate は別。')]),
(19,'データ量と通信','GB・up to・over を伝える',
 ['データ量は gigabytes（GB）で表します。up to 3GB は「3GBまで（3GBを含む）」。over 3GB は「3GBを超える」です。',
  '英語の up to と over は境界が異なります。3GBちょうどの扱いが変わるので、数字の前後も注意して読みます。',
  '国内と海外のデータ条件は違う場合があります。境界の意味と、どのサービスの数字かをはっきり伝えましょう。'],
 'data=データ|gigabyte=ギガバイト|up to=〜まで|over=〜を超えて|use=使う|speed=速度',
 'up to + 数字 / over + 数字','Up to=まで|three gigabytes=3ギガバイト|is included.=含まれます',[
 ('Up to three gigabytes is included.','3ギガバイトまで含まれます。','上限を表す英語の練習文。'),('You can use data here.','ここでデータ通信が使えます。','can use で使用可能。'),('This is over three gigabytes.','これは3ギガバイトを超えています。','over は超える。'),('How much data do you use?','データをどのくらい使いますか。','how much data。'),('The data speed may change.','データ通信速度は変わる場合があります。','may は可能性。')]),
(20,'割引・ポイント・紹介','確約せず条件を確認する',
 ['discount は割引、points はポイント、referral は紹介を表します。ポイント還元は料金からの直接割引と同じではありません。',
  'may は「〜する場合があります」。You may be eligible. は「対象になる可能性があります」で、確実に適用されるとは約束しません。',
  '紹介キャンペーンではリンク/QRコード、エントリー、利用条件などを必ず公式画面で確認します。金額や条件を古いまま断定しないことが重要です。'],
 'discount=割引|points=ポイント|referral=紹介|campaign=キャンペーン|eligible=対象となる|link=リンク',
 'You may be eligible for ...','You=お客様は|may be eligible for=対象になる場合があります|a discount.=割引の',[
 ('You may be eligible for a discount.','割引の対象になる場合があります。','確約ではない。'),('This campaign has conditions.','このキャンペーンには条件があります。','条件を確認する。'),('Please open the referral link.','紹介リンクを開いてください。','リンクを使う紹介の案内。'),('The points are not a bill discount.','ポイントは請求額の割引ではありません。','ポイントと値引きは別。'),('We will check the conditions.','条件を確認いたします。','確認前に断定しない。')]),
(21,'契約の流れ','最初・次・最後を案内する',
 ['手続きの順番は First（最初に）、Next（次に）、Finally（最後に）で表せます。',
  'First, we check your ID. のように「順番を表す言葉 + 短い一文」で話せば分かりやすくなります。',
  '説明と実際の契約内容が一致するか、重要な条件は書面や公式画面で確認しましょう。'],
 'first=最初に|next=次に|finally=最後に|apply=申し込む|confirm=確認する|finish=完了する',
 'First / Next / Finally + 短い一文','First,=最初に|we check=確認します|your ID.=本人確認書類を',[
 ('First, we check your ID.','最初に本人確認書類を確認します。','First で順序。'),('Next, we explain the plan.','次にプランを説明します。','Next は次に。'),('Please confirm your details.','ご自身の情報をご確認ください。','確認の依頼。'),('Finally, we check the result.','最後に結果を確認します。','Finally は最後。'),('We can start the application.','申し込みを始められます。','start the application。')]),
(22,'SIMとeSIM','2つの違いを短く説明する',
 ['SIM card は物理カード、eSIM は端末に組み込まれたSIMです。お客様の端末が対応するか確認が必要です。',
  'physical は「物理的な」、digital は「デジタルの」、compatible は「対応している」。難しい語なので一度に全部覚える必要はありません。',
  'This phone supports eSIM. という文は端末が対応すると確認できた場合にのみ使います。'],
 'SIM card=SIMカード|eSIM=eSIM|physical=物理的な|digital=デジタルの|compatible=対応した|support=対応する',
 'This is ... / It supports ...','An eSIM=内蔵SIMは|is=です|digital.=デジタルの',[
 ('An eSIM is digital.','eSIMはデジタル式です。','an eSIM で始める。'),('A SIM card is physical.','SIMカードは物理的なカードです。','physical は物理的な。'),('This phone supports eSIM.','この電話はeSIMに対応しています。','対応確認後に使う。'),('We need to check compatibility.','対応状況を確認する必要があります。','確認前は断定しない。'),('You can choose a SIM card.','SIMカードを選べます。','can choose は選べる。')]),
(23,'MNPと開通','番号引き継ぎと状況を説明する',
 ['MNP は今の電話番号を他社から引き継ぐ手続きです。keep your number は「番号を維持する」という日常的な言い方です。',
  'activation は開通、complete は完了、in progress は進行中。進捗が不明なときに完了したとは言いません。',
  '必要なMNP手続きは契約方法や状況によって異なるので、店頭の公式手順に従って確認してください。'],
 'MNP=番号乗り換え|keep=維持する|number=番号|activation=開通|complete=完了|in progress=進行中',
 'The ... is + 状態','The activation=開通手続きは|is=です|in progress.=進行中',[
 ('The activation is in progress.','開通手続きは進行中です。','in progress は進行中。'),('Would you like to keep your number?','電話番号を引き継ぎたいですか。','番号引き継ぎの希望確認。'),('We will check the MNP process.','MNP手続きを確認します。','状況を確認する言い方。'),('The application is not complete yet.','申し込みはまだ完了していません。','not complete yet。'),('The activation is complete.','開通が完了しました。','確認が取れた場合のみ使う。')]),
(24,'最初の接客ロールプレイ','受付から確認までつなげる',
 ['ここまでの短文をつなげて、外国人のお客様への最初のご案内を練習します。長く話すより、短く話して確認することを優先しましょう。',
  'Hello → How can I help you? → Would you like ...? → Let me check. の順番で接客を組み立てられます。',
  '料金・割引・契約可否は「今は確認中です」と伝えられれば十分です。正式な説明は最新の公式画面や社内ルールに従ってください。'],
 'hello=こんにちは|help=お手伝い|would like=希望する|check=確認する|please=お願いします|thank you=ありがとう',
 'あいさつ → 要望確認 → 確認 → お礼','Hello.=こんにちは|How can I help you?=ご用件は何でしょうか',[
 ('Hello. How can I help you?','こんにちは。ご用件をお伺いします。','短いあいさつと質問。'),('Would you like an eSIM?','eSIMをご希望ですか。','希望を聞く。'),('Let me check the conditions.','条件を確認いたします。','Let me check は確認します。'),('Please wait a moment.','少々お待ちください。','一度区切って確認。'),('Thank you for waiting.','お待ちいただきありがとうございます。','最後まで丁寧に。')])
]

def parse_vocab(s):
 return [{'en':a.strip(),'ja':b.strip()} for x in s.split('|') for a,b in [x.split('=',1)]]

def create():
 units=[]
 for id,title,goal,explain,vocab,pattern,parts,examples in LESSONS:
  assert len(examples)==5,(id,len(examples))
  parts=parse_vocab(parts); vocab=parse_vocab(vocab)
  es=[{'id':f'B{id:02d}E{j}','en':en,'ja':ja,'why':why} for j,(en,ja,why) in enumerate(examples,1)]
  assert len({x['en'] for x in es})==5,id
  units.append({'id':id,'phase':(id-1)//4+1,'title':title,'goal':goal,'explain':explain,'vocab':vocab,'pattern':pattern,'parts':parts,'examples':es})
 result={'version':2,'description':'英語が初めての人のための24レッスン。数字は原則練習用。料金・キャンペーン条件は公式で確認。','phases':[{'id':i,'title':t,'goal':g} for i,(t,g) in enumerate(PHASES,1)],'units':units}
 target=ROOT/'web/data/beginner.json'
 target.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
 print('Built',len(units),'beginner units;',sum(len(u['examples']) for u in units),'examples; 12 drills each')
if __name__=='__main__':create()
