#!/usr/bin/env python3
"""Curated Rakuten Mobile counter-English curriculum. All examples original educational language."""
from pathlib import Path
import json,re
from extended_lessons import EXTRA
ROOT=Path(__file__).resolve().parents[1]
units=[]
def add(ch,title,goal,rule,detail,contrast,pitfall,samples):
    pattern=detail.split("。")[0]
    examples=[]
    for n,line in enumerate(samples.strip().splitlines(),1):
        en,ja,why=[s.strip() for s in line.split('|')]
        examples.append({'id':f'U{len(units)+1:02d}E{n}', 'en':en,'ja':ja,'why':why})
    assert len(examples)==7,(title,len(examples))
    units.append({'id':len(units)+1,'chapter':ch,'title':title,'goal':goal,'sections':[
        {'heading':'しくみと意味','text':rule},
        {'heading':'作り方・語順','text':detail},
        {'heading':'実際の店頭での使い分け','text':contrast},
        {'heading':'よくある間違い・確認ポイント','text':pitfall}],
        'pattern':pattern,'tip':pitfall,'examples':examples})

add(1,'be動詞：自分・商品・状態を紹介する','I am / This is / It is で最初の一文を作る',
'be動詞 am / is / are は「～です」「～にあります」「～の状態です」を表す。英語は主語を省略しないため、受付の自己紹介では I am、商品紹介では This is、現在の状態では It is を使う。',
'主語 + am/is/are + 名詞・形容詞。I am a staff member. / This is the SIM card. / The device is compatible. 否定は is not、疑問は Is this ...? と語順を逆にする。',
'店員として名乗るなら I am ...、案内対象を指すなら This is ...。受付の場所や商品を指さしながら短く区切って話すと、英語初心者のお客様にも伝わる。',
'「This is compatible.」の compatible は形容詞。compatible の前に be動詞が必要。is と are は主語の単複で決める。', '''I am a staff member at Rakuten Mobile.|私は楽天モバイルのスタッフです。|I am は自己紹介の基本形。\nThis is the Rakuten SAIKYO Plan.|こちらが楽天最強プランです。|This is は商品や資料を示す。\nThe monthly fee is tax-inclusive.|月額料金は税込みです。|is の後に形容詞を置く。\nYour device is compatible with this SIM.|お使いの端末はこのSIMに対応しています。|compatible with が「～に対応」。\nThese calling options are not required.|これらの通話オプションへの加入は必須ではありません。|複数主語に are not。\nThe application is not complete yet.|申し込みはまだ完了していません。|否定は is not。\nIs this your current phone number?|こちらが現在の電話番号ですか。|疑問文は Is を先頭にする。''')
add(1,'一般動詞：利用状況をたずねる','use / need / pay / keep を使う',
'一般動詞は「使う・必要とする・支払う・保持する」などの動作や関係を表す。I/you/we/they の現在形では原形を使う。be動詞と一般動詞を無理に重ねない。',
'You + use + data. / We + accept + credit cards. 主語が he/she/it のとき通常 -s/-es を付ける。頻度なら usually / often を一般動詞の前に置く。',
'契約説明は You pay ...（お客様が支払う）と We accept ...（店舗側が受け付ける）で主語を使い分ける。通常の習慣を言うなら現在形。',
'「You are use」や「We are accept」は誤り。進行形にする理由がなければ be動詞は入れない。', '''You pay based on how much data you use.|データ利用量に応じた段階制の料金をお支払いいただきます。|pay based on how much data you use の構造。\nWe accept credit cards for payment.|お支払いにはクレジットカードをご利用いただけます。|We accept で店側の対応を説明する。\nWe help you keep your current phone number.|現在の電話番号を引き継ぐお手伝いをします。|help you + 動詞原形。\nI recommend checking the coverage map.|エリアマップの確認をおすすめします。|recommend + -ing の形。\nThis app uses mobile data.|このアプリはモバイルデータを使用します。|三人称単数は uses。\nCustomers choose a physical SIM or an eSIM.|お客様は物理SIMかeSIMを選びます。|choose は選ぶ。\nWe explain the monthly charges before you apply.|申し込み前に月額料金をご説明します。|before の後に節を置ける。''')
add(1,'Do / Does：Yes・No質問','現在の利用状況を質問する',
'一般動詞の現在形を疑問にするとき Do / Does を文頭に置く。相手に聞く場合は Do you ...? が基本。Does は he/she/it など三人称単数に使い、後ろの動詞は原形に戻す。',
'Do + you + have + ... ? / Does + your phone + support + ... ? 否定は do not / does not + 原形。答えは Yes, I do. / No, I do not. で対応できる。',
'いきなりプラン説明を始めず Do you ...? で利用状況を確認する。Yes/Noで答えられる質問は、聞き返しが起きにくい。',
'「Does your phone supports ...?」は supports ではなく support。Do you are ...? と be動詞疑問文を混ぜない。', '''Do you use more than 20 gigabytes a month?|月に20GBを超えて使いますか。|Do you + 一般動詞。\nDo you want to keep your phone number?|電話番号をそのまま使いたいですか。|want to の前に Do you。\nDo you have a Rakuten ID?|楽天IDをお持ちですか。|所有は have。\nDoes your phone support eSIM?|お使いの端末はeSIMに対応していますか。|主語が your phone なので Does。\nDo you need help with the application?|申し込みのお手伝いは必要ですか。|need help with の使い方。\nDo you usually call overseas?|普段海外に電話しますか。|usually は動詞の前。\nDoes the discount apply to this line?|この回線に割引は適用されますか。|apply to は「～に適用される」。''')
add(1,'疑問詞：何・どれ・どのくらい','What / Which / How much / How many',
'What は「何」、Which は選択肢がある「どちら」、How much は料金や不可算量、How many は数えられる個数を尋ねる。お客様から必要情報を引き出す基本の文型。',
'疑問詞 + do/does + 主語 + 動詞 ...? / 疑問詞 + is/are + 主語 ...? ただし What is ...? のように be動詞があれば do を足さない。',
'「料金」は How much is ...?、「何GB」は How much data ...?、「何回線」は How many lines ...? と、聞きたい対象で変える。',
'How many data は誤り。data usage には how much、SIM cards や lines には how many。Which is ...? は選択肢を示してから使う。', '''What brings you to the store today?|本日はどのようなご用件ですか。|来店目的を自然に尋ねる定型。\nWhich SIM would you prefer?|どちらのSIMをご希望ですか。|複数の選択肢なら Which。\nHow much data do you usually use?|普段どのくらいデータを使いますか。|不可算量に How much。\nHow many lines would you like to sign up for?|何回線お申し込みになりますか。|数えられる回線数に How many。\nWhat is your current carrier?|現在ご利用の携帯会社はどちらですか。|be動詞で質問する。\nHow much is the monthly fee?|月額料金はいくらですか。|価格には How much is ...?。\nWhich option fits your needs best?|どのオプションが一番合いますか。|複数候補を比べて選ぶ。''')

add(2,'Can：できること・可能性','can + 動詞原形で機能を説明',
'can は能力・可能性・許可を表し、直後は必ず動詞の原形。「この端末で使える」「番号を引き継げる」などをシンプルに説明できる。',
'主語 + can + 動詞原形。疑問文は Can + 主語 + 動詞原形 ...? 否定は cannot / can’t。Can you ...? は依頼にも使える。',
'「使える」は can use、「確認できる」は can check。ただし実際に利用可能かは端末・地域・条件を確認した後で断定する。',
'can to use / can uses は誤り。確約していない場合は may や subject to ... を併用して丁寧に条件を伝える。', '''You can keep your current phone number with MNP.|MNPで今の電話番号を引き継げます。|can + keep。\nYou can check your data usage in the app.|アプリでデータ使用量を確認できます。|can + check。\nWe can help you set up your eSIM.|eSIMの設定をお手伝いできます。|help + 人 + 動詞原形。\nCan you open the my Rakuten Mobile app?|my 楽天モバイルアプリを開けますか。|Can you は依頼。\nYou can use tethering at no extra option charge.|テザリング自体に追加オプション料金はかかりません。|no extra option charge と限定する。\nI can show you the coverage map.|エリアマップをご案内できます。|I can show you ...。\nWe cannot guarantee reception in every building.|すべての建物内での電波状況は保証できません。|cannot + 原形。''')
add(2,'Could / May：丁寧にお願いする','Could you ...? / May I ...?',
'could は can の丁寧な依頼、May I ...? は相手の許可を得る丁寧な表現。店頭で画面・書類を見せてもらう際に命令調を避けられる。',
'Could + you + 動詞原形 ...? / May + I + 動詞原形 ...? May I はスタッフがする行為の許可、Could you はお客様にお願いする行為。',
'個人情報の確認では Could you ...? を使い、確認目的を添える。端末を操作するときには May I ...? と同意を得る。',
'Could you to show は誤り。お客様の同意なく端末・ID情報を扱わない。文法上丁寧でも、依頼内容自体への配慮が必要。', '''Could you show me a valid ID, please?|有効な本人確認書類を見せていただけますか。|Could you は丁寧な依頼。\nMay I check the model of your phone?|端末の機種を確認してもよろしいですか。|May I は許可を求める。\nCould you confirm your address, please?|ご住所を確認していただけますか。|confirm で確認。\nMay I explain the charges before we proceed?|進める前に料金をご説明してもよろしいですか。|May I explain ...?。\nCould you wait a moment while I check?|確認する間、少々お待ちいただけますか。|while で同時進行。\nMay I use this screen to show the plan?|この画面でプランをご案内してもよろしいですか。|May I use ...?。\nCould you repeat the last four digits?|下4桁をもう一度おっしゃっていただけますか。|Could you repeat ...?。''')
add(2,'would like：希望をやわらかく確認','Would you like ...? / I would like to ...',
'would like は want より丁寧で、お客様の希望を聞く場面に適する。名詞には would like + 名詞、行動には would like to + 動詞原形を使う。',
'Would you like + 名詞? / Would you like to + 動詞? 「どちらがよいですか」は Which would you prefer?。No, thank you. にも配慮する。',
'オプション勧誘では「加入したいですか」と「説明を聞きたいですか」を区別し、選択はお客様に委ねる。',
'would like to + 名詞 は誤り。want を繰り返すと押しが強く聞こえる場面がある。', '''Would you like a physical SIM or an eSIM?|物理SIMとeSIM、どちらをご希望ですか。|would like + 名詞。\nWould you like to keep your current number?|現在の番号をそのまま使いたいですか。|would like to + 原形。\nWould you like me to explain the call option?|通話オプションをご説明しましょうか。|would like me to ... の構文。\nWhich payment method would you prefer?|どのお支払い方法をご希望ですか。|prefer で丁寧に選択。\nWould you like to review the contract details?|契約内容を確認されますか。|押しつけず確認を促す。\nWould you like a copy of the estimate?|お見積もりの控えをご希望ですか。|would like + 名詞。\nI would like to confirm one detail first.|まず一点確認させてください。|I would like to ... は丁寧な意図。''')
add(2,'Please / Let me：案内と誘導','Please + 動詞 / Let me + 動詞',
'Please + 動詞原形は丁寧な案内や軽いお願い。Let me + 動詞原形は「私に～させてください」。スタッフ側が何をするかを明示できる。',
'Please + check + ... / Let me + explain + ... / Please do not + 動詞。依頼をより丁寧にするときは Could you ...? を使う。',
'手続きの画面で「次に何をするか」を短く案内する。Please tap ... の後に where / what を示すと操作ミスが減る。',
'Let me to check は誤り。Please を付ければどんな命令も適切になるわけではない。', '''Please tap the next button on the screen.|画面の「次へ」ボタンを押してください。|Please + 原形。\nLet me explain the three price tiers.|料金の3段階をご説明します。|Let me + 原形。\nPlease check that your name is correct.|お名前に誤りがないか確認してください。|check that + 節。\nLet me confirm the campaign conditions.|キャンペーン条件を確認いたします。|スタッフの行動を示す。\nPlease do not close the app yet.|まだアプリを閉じないでください。|Please do not + 原形。\nLet me know if anything is unclear.|不明な点があればお知らせください。|Let me know if ...。\nPlease read the terms before signing.|署名前に規約をお読みください。|before + -ing。''')

add(3,'数字と料金：読み方と構造','yen / per month / including tax',
'料金説明は数値＋単位＋期間＋税込・税別を明示する。「月に」は per month、「税込」は including tax または tax included。英語の数字は区切りに注意する。',
'It costs + 金額 + per month. / The monthly fee is + 金額 + including tax. 数字は one thousand seventy-eight yen のように読む。',
'初回の請求、端末代金、オプション料金は月額基本料と分けて話す。同じ 1,078 yen でも「最大」ではなく「3GBまで」が前提。',
'「yen」は単複で形を変えない。monthly と per month は重複させない。税込という条件を落とさない。', '''For up to 3 gigabytes, the monthly fee is 1,078 yen.|3GBまでは月額1,078円です。|up to + 数量 と the monthly fee is ...。\nFor over 3 and up to 20 gigabytes, the monthly fee is 2,178 yen.|3GB超から20GBまでは月額2,178円です。|over と up to の範囲を区別。\nFor over 20 gigabytes, the monthly fee is 3,278 yen.|20GBを超えると月額3,278円です。|over は「超える」。\nAll these prices include tax.|これらの金額はすべて税込みです。|include tax の表現。\nThe option costs 1,100 yen per month.|そのオプションは月額1,100円です。|option costs + 額。\nThis discount saves you 110 yen each month.|この割引で毎月110円安くなります。|saves you + 金額。\nThe total may include other charges.|合計には他の料金が含まれる場合があります。|may で可能性を示す。''')
add(3,'冠詞・単数・複数：SIMと回線','a/an/the、one SIM / two lines',
'数えられる名詞は単数なら a/an/the または所有格を伴うことが多い。すでに話題にした特定のものは the。「a SIM card」「two lines」と使い分ける。',
'a + 子音で始まる音 / an + 母音で始まる音。a physical SIM、an eSIM。複数形は通常 -s を付け、a は付けない。',
'SIM、回線、書類、端末は数えられる。一方 data、information、equipment は一般に不可算名詞として扱う。',
'an SIM は発音により判断（SIM は /sɪm/ なので a SIM）。an eSIM は /iː/ で始まるので an。informations は不可。', '''You can choose a physical SIM card.|物理SIMカードを選べます。|a + 単数可算名詞。\nAn eSIM does not require a removable card.|eSIMは取り外し式カードを必要としません。|an eSIM。\nSome applications require additional documents.|一部のお申し込みには追加の書類が必要です。|複数形の applications と documents。\nPlease insert the SIM card into the phone.|そのSIMカードを端末に入れてください。|既知の特定物には the。\nOne line is already active.|1回線はすでに開通しています。|one line。\nTwo lines are registered under this account.|このアカウントに2回線が登録されています。|複数主語 + are。\nWe need some information about your device.|端末についていくつか情報が必要です。|information は不可算。''')
add(3,'比較表現：より安い・大きい・最適','cheaper / more / the best',
'比較級は2つを比べるとき、最上級は3つ以上から一番を示すときに使う。安い cheap→cheaper、便利 convenient→more convenient。',
'A is cheaper than B. / Which option is better for you? 最上級は the + 最上級。比較対象と適用条件を明示する。',
'営業トークの「他社より安い」は検証が必要。アプリでは自社の料金段階・オプションの比較を中心に練習する。',
'more cheaper は二重比較。the most cheapest も誤り。「best for you」はお客様の利用状況に基づく提案として扱う。', '''The 3-gigabyte tier is cheaper than the unlimited tier.|3GBの料金帯は無制限の料金帯より安いです。|cheaper than。\nThis option may be more convenient for you.|このオプションの方が便利かもしれません。|more convenient。\nWhich plan is better for your data usage?|利用量に合うのはどちらのプランですか。|better は good の比較級。\nAn eSIM can be easier to activate on a compatible phone.|対応端末ではeSIMの方が開通しやすい場合があります。|easier to + 原形。\nThe highest data tier is more expensive than the lowest tier.|利用量が最大の料金帯は最小の料金帯より高額です。|more expensive than の比較級。\nA physical SIM is more suitable for some devices.|機種によっては物理SIMの方が適しています。|more suitable。\nLet us compare the total monthly costs.|月額の合計費用を比較しましょう。|compare + 対象。''')
add(3,'数量表現：まで・超える・それぞれ','up to / more than / each / per',
'料金条件では「以下」「超過」を厳密に言い分ける。up to 3GB は3GBを含み、more than 3GB / over 3GB は3GBを含まない。',
'up to + 数量 / more than + 数量 / each + 単数名詞 / per + 単数名詞。「20GBぴったり」と「20GB超過」は異なる。',
'プランは段階制なので、20GBを少し超えた場合の説明が特に重要。料金の区切りを英語で正確に確認する。',
'less than 3GB と up to 3GB を混同しない。3GBちょうどは up to 3GB に含まれる。', '''The lowest price tier covers up to 3 gigabytes.|最も安い料金帯は3GBまでを対象とします。|up to は境界値を含む。\nIf you use more than 3 gigabytes, the next price tier applies.|3GBを超えると次の料金帯が適用されます。|more than は境界値を含まない。\nThe price changes when you exceed 20 gigabytes.|20GBを超えると料金が変わります。|exceed は超える。\nEach eligible family line gets a 110-yen discount.|条件を満たす家族の各回線が110円割引されます。|each + 単数。\nOne extra gigabyte abroad costs 500 yen.|海外での追加高速データ1GBは500円です。|追加単位と料金。\nThe fee is charged per month.|料金は月ごとに請求されます。|per month。\nThe plan has three usage-based price tiers.|このプランには使用量に応じた3段階の料金があります。|usage-based の複合形容詞。''')

add(4,'現在進行形：いま手続き中','am/is/are + -ing',
'現在進行形は「今まさに行っている途中」の操作や確認を表す。現在形が通常の仕組みを説明するのに対し、進行形は現場の進捗を説明する。',
'am/is/are + 動詞ing。「I am checking ...」「We are processing ...」。疑問文は Are you ...?。状態動詞は進行形にしないのが普通。',
'待ち時間の理由を説明するとき「いま確認しています」と伝えられる。ただし進捗や完了予定を根拠なく確約しない。',
'I checking は be動詞不足。I am know は不自然。いま行っている確認行為には checking を使う。', '''I am checking the campaign details now.|今キャンペーンの詳細を確認しています。|am + checking。\nWe are processing your application.|お申し込みを処理しています。|are + processing。\nYour phone is downloading the eSIM profile.|端末がeSIMのプロファイルをダウンロードしています。|is + downloading。\nI am confirming your eligibility.|対象条件を確認しています。|am + confirming。\nThe app is showing an error message.|アプリにエラーメッセージが表示されています。|is + showing。\nWe are waiting for the verification result.|本人確認の結果を待っています。|are + waiting。\nAre you using Wi-Fi at the moment?|現在Wi-Fiをご利用ですか。|Are you + -ing。''')
add(4,'未来表現：次の手順を説明','will / be going to',
'will はこれから行うことや予測、be going to は予定・見込みを示す。店頭では「次に何をしますか」「その後何が起きますか」を説明するのに使う。',
'We will + 原形。/ You are going to + 原形。soon, next, after that などと組み合わせる。保証のない将来は may / usually などで調整。',
'本人確認、開通、請求確定は処理条件が異なるため「必ずすぐ終わる」と断言しない。',
'will to send は誤り。be going to の be を落とさない。将来のポイント付与を即時と説明しない。', '''I will explain the next step.|次の手順をご説明します。|will + 原形。\nWe will check your device compatibility first.|まず端末の対応状況を確認します。|未来に行う処理を示す。\nYou are going to receive a confirmation message.|確認メッセージを受け取る予定です。|are going to + 原形。\nThe final charge will depend on your usage.|最終的な料金は利用量によって決まります。|will depend on。\nI will show you how to use Rakuten Link.|Rakuten Linkの使い方をお見せします。|how to + 動詞。\nWe are going to review the contract together.|一緒に契約内容を確認する予定です。|予定の going to。\nYou may receive points later if you qualify.|対象なら後日ポイントを受け取れる場合があります。|未確定なら may。''')
add(4,'助動詞と義務：必要・必須','need to / have to / must',
'need to は必要性、have to は手続き上の必要条件、must は強い義務。契約説明ではルールに基づく必要事項を中立的に伝えることが重要。',
'You need to + 原形 / You have to + 原形 / You must + 原形。must の後に to は付けない。必要でない場合は do not need to。',
'本人確認書類や楽天IDは手続きの種類・本人属性により必要条件が異なる。条件を確認しながら need to を使う。',
'must to は誤り。must not（禁止）と do not have to（不要）は意味が正反対。', '''You need to verify your identity for the application.|申し込みには本人確認が必要です。|need to verify。\nYou have to sign in with your Rakuten ID.|楽天IDでログインする必要があります。|have to + 原形。\nWe must confirm the applicable campaign terms.|該当キャンペーンの条件を確認しなければなりません。|must + 原形。\nYou do not need to buy a new phone if yours is compatible.|今の端末が対応していれば新しい端末を買う必要はありません。|do not need to は不要。\nYou need to check the MNP reservation number for an in-store transfer.|店頭での乗り換えにはMNP予約番号の確認が必要です。|in-store は店頭。\nYou must agree to the terms before submitting.|送信前に規約に同意する必要があります。|must agree。\nPlease make sure the account name matches your documents.|アカウント名が書類と一致しているかご確認ください。|make sure + 節。''')
add(4,'条件文：もし～なら','if + 現在形, will/can ...',
'if は条件を提示する接続詞。「もしeSIM対応なら」「条件を満たせば割引が適用される」のように確約の範囲を明示できる。',
'If + 主語 + 現在形, 主語 + can/will/may + 原形。未来の条件でも if 節では通常 will を使わず現在形。',
'お客様が条件を満たすか不明な場合は if を付ける。特典を受け取る時期は後日であることも説明する。',
'If you will qualify は通常の条件文では不自然。if を落としてポイント付与を保証しない。', '''If your phone supports eSIM, you can choose it.|端末がeSIM対応なら選択できます。|if + 現在形、can。\nIf you use over 20 gigabytes, the base fee is 3,278 yen.|20GB超なら基本料金は3,278円です。|料金条件の if。\nIf you qualify, the family discount may apply.|対象条件を満たせば家族割が適用される場合があります。|may apply で慎重に説明。\nIf you need assistance, please ask me.|お困りならお声がけください。|条件 + 依頼。\nIf the app fails, we can try another method.|アプリがうまく動かなければ別の方法を試せます。|if + 現在形。\nIf the transfer is complete, we will test the connection.|乗り換えが完了したら通信を確認します。|未来の完了条件。\nIf the campaign has ended, the bonus will not apply.|キャンペーンが終了していれば特典は適用されません。|終了を条件として限定。''')

add(5,'現在完了：もう済んだ／まだ済んでいない','have / has + 過去分詞',
'現在完了は過去の出来事と「今の状態」をつなぐ。手続きの完了や過去の利用経験を確認できる。have/has + 過去分詞。',
'Have you + 過去分詞 ...? / We have already ... / It has not ... yet. already は「すでに」、yet は否定・疑問で「まだ／もう」。',
'「申請済み」と「開通済み」は別の事実。何が完了したかを正確に言う。',
'have submitted と submitted の違いに注意。have did は誤り、have done が正しい。', '''Have you already requested an MNP reservation number?|MNP予約番号はすでに取得済みですか。|Have you already + 過去分詞。\nWe have received your application.|お申し込みを受け付けました。|have received で現在の受付状態。\nYour eSIM has not been activated yet.|eSIMはまだ有効化されていません。|has not been ... yet。\nHave you used Rakuten Mobile before?|以前楽天モバイルを使ったことがありますか。|経験の現在完了。\nI have checked the latest campaign page.|最新のキャンペーンページを確認しました。|have checked。\nThe payment method has been registered.|お支払い方法の登録が完了しました。|has been + 過去分詞。\nWe have not confirmed your eligibility yet.|対象かどうかはまだ確認できていません。|not ... yet。''')
add(5,'過去形：以前の契約や履歴','did / was / transferred',
'過去形はすでに終わった具体的な出来事を話す。last month / yesterday / before など過去の時点を伴いやすい。',
'動詞の過去形：use→used、pay→paid、go→went。疑問は Did you + 原形? be動詞の過去は was/were。',
'以前利用していた会社、前月の請求、前回の来店を確認する。必要以上の個人情報を尋ねない。',
'Did you used は誤り。Did の後は use。過去の料金を現行価格だと誤認させない。', '''Did you use another carrier last month?|先月は別の携帯会社を使っていましたか。|Did + 動詞原形。\nWhen did you request the MNP number?|いつMNP予約番号を取得しましたか。|疑問詞 + did。\nThe phone worked yesterday.|端末は昨日動作していました。|worked は過去。\nI checked the account status earlier.|先ほどアカウント状態を確認しました。|checked は過去。\nWas the SIM working before the update?|更新前はSIMが使えていましたか。|Was + 主語。\nDid you receive the confirmation email?|確認メールは届きましたか。|Did you receive。\nThe customer changed the payment method last week.|お客様は先週支払い方法を変更しました。|changed は過去。''')
add(5,'受動態：手続き・ポイント付与','be + 過去分詞',
'受動態は「誰が行ったか」より「何が処理されたか」を中心に言う。サービス説明で使う applied / charged / awarded / verified が重要。',
'The fee is charged ... / Points are awarded ... / The ID was verified ...。be動詞の時制と主語の単複を合わせる。',
'キャンペーンは「特典が付与される」ではなく「条件達成時に付与される」など条件句を忘れない。',
'Points awarded は be が抜けている。pay / charge は誰に何を請求するかまで言うと誤解が減る。', '''Points are awarded after the conditions are met.|条件を満たした後にポイントが付与されます。|are awarded の受動態。\nThe monthly fee is based on data usage.|月額料金はデータ利用量に基づいています。|is based on。\nYour identity must be verified.|本人確認が必要です。|must be + 過去分詞。\nThe contract details will be displayed on screen.|契約内容は画面に表示されます。|will be displayed。\nSome calls are not covered by the free call service.|一部の通話は無料通話の対象外です。|are not covered by。\nThe charges are billed monthly.|料金は月ごとに請求されます。|are billed。\nThe discount is applied only to eligible lines.|割引は対象回線にのみ適用されます。|is applied to。''')
add(5,'間接疑問：丁寧に確認する','Could you tell me if / what ...',
'直接疑問の What is ...? を「教えていただけますか」の一部にすると、後半は通常の語順に戻る。Could you tell me ...? は受付で役立つ。',
'Could you tell me + what + 主語 + 動詞 ...? / Do you know + whether + 主語 + 動詞 ...? 文中の疑問節は平叙文の語順。',
'お客様の要望や端末仕様を丁寧に確認する場面に適する。難しければ二文に分けてもよい。',
'Could you tell me what is your carrier? は間接疑問として不自然。what your carrier is にする。', '''Could you tell me which carrier you use now?|現在の携帯会社を教えていただけますか。|間接疑問は you use の順。\nDo you know whether your phone supports eSIM?|端末がeSIM対応かご存じですか。|whether + 主語 + 動詞。\nCould you tell me how much data you use?|使うデータ量を教えていただけますか。|how much data you use。\nMay I ask when you requested the MNP number?|MNP予約番号を取得した時期を伺ってよろしいですか。|when + 平叙語順。\nI will check whether this option is available.|このオプションが利用可能か確認します。|check whether ...。\nPlease tell me what error message you see.|どのエラーが出ているか教えてください。|what + 名詞 + 主語 + 動詞。\nCould you confirm which plan you selected?|選択したプランをご確認いただけますか。|which plan you selected。''')

add(6,'前置詞：日付・時間・場所・費用','on / in / at / by / for',
'前置詞は短いが誤解を生みやすい。at は時刻・場所の点、on は日付、in は月や期間、by は期限、for は目的・対象を表す。',
'on Monday / in October / at 3 p.m. / by the deadline / for your phone。まとまりで覚えると接客時に迷いにくい。',
'締切を言う場合 by を選ぶ。until はある時点まで状態が続く意味で、by はそれまでに完了する意味。',
'in Monday や on 3 p.m. に注意。「来月末までに」は by the end of next month。', '''Please visit us on Friday.|金曜日にご来店ください。|曜日は on。\nThe campaign conditions may change in October.|キャンペーン条件は10月に変更される場合があります。|月は in。\nYour appointment is at three o'clock.|ご予約は3時です。|時刻は at。\nPlease complete the procedure by the deadline.|期限までに手続きを完了してください。|by は締切。\nThis document is for identity verification.|この書類は本人確認用です。|for は目的。\nWe will check the signal inside the store.|店内で電波状況を確認します。|inside は内部。\nThe final amount appears on the billing screen.|最終金額は請求画面に表示されます。|on the screen。''')
add(6,'接続詞：理由と対比を説明','because / so / although / but',
'because は原因、so は結果、although は譲歩、but は対比をつなぐ。説明に理由を添えると押し付けになりにくい。',
'We need to check because ... / ..., so ... / Although ... , ...。because と so を同じ二節の接続語として重ねない。',
'キャンペーンが使えない理由や端末の制約を理由＋代替案で伝える。断るだけで終わらせない。',
'Because ... so ... を同一文で併用しない。although ... but ... も基本はどちらか一方を接続語として使う。', '''We need to verify your ID because this is a contract.|契約手続きなので本人確認が必要です。|because で理由。\nYour device supports eSIM, so we can proceed.|端末がeSIM対応なので進められます。|so で結果。\nAlthough the plan offers unlimited data, speed restrictions may apply.|データ無制限のプランですが速度制限がかかる場合があります。|although で譲歩。\nThis option is useful, but it costs extra.|このオプションは便利ですが追加料金がかかります。|but で対比。\nPlease keep the app open because activation is in progress.|開通手続き中なのでアプリを開いたままにしてください。|because の理由付け。\nThe offer has conditions, so please review them carefully.|特典には条件があるため注意してご確認ください。|so は因果。\nAlthough the phone is unlocked, compatibility still needs checking.|SIMロックが解除済みでも対応機種か確認が必要です。|although の譲歩。''')
add(6,'before / after / when：順番を説明','before + -ing / after + 節',
'手続きは順番が重要。before は「～する前に」、after は「～した後で」、when は「～したとき」。動詞-ing または主語＋動詞の節を続けられる。',
'Before + -ing, ... / After + 主語 + 現在形, ... / When + 主語 + 現在形, ...。未来の順序でも従属節は通常現在形。',
'紹介キャンペーンでは「申し込み前にリンクからログイン」の順序が重要。単に「コードを入力」と誤案内しない。',
'after you will log in ではなく after you log in。before applying と before apply の違いも確認。', '''Open the referral link before applying.|申し込み前に紹介リンクを開いてください。|before + -ing。\nAfter you sign in, review the eligibility rules.|ログイン後に対象条件をご確認ください。|after + 現在形。\nWhen activation finishes, test mobile data.|開通後にモバイルデータ通信を試してください。|when + 現在形。\nPlease save your current settings before changing the SIM.|SIM変更前に現在の設定を保存してください。|before + -ing。\nAfter the payment method is registered, we can continue.|支払い方法の登録後に進められます。|after + 受動態。\nPlease ask if you have questions while reading the terms.|規約を読んでいる間に質問があればお尋ねください。|while + -ing相当の節。\nWe check compatibility before starting the transfer.|乗り換え開始前に対応機種を確認します。|before + -ing。''')
add(6,'either / both / neither：選択肢の整理','either A or B / both A and B',
'either A or B は二者択一、both A and B は両方、neither A nor B はどちらも～ない。SIMや支払い方法を整理する場面で便利。',
'either + A + or + B / both + A + and + B / neither + A + nor + B。並列する要素の形をそろえる。',
'どちらでも選択できるかは事実確認が必要。「両方利用可能」と「どちらか選ぶ」は別の意味。',
'either A and B は誤り。both を使って二者択一を表現しない。', '''You can choose either a physical SIM or an eSIM.|物理SIMまたはeSIMのどちらかを選べます。|either ... or。\nBoth plans include access to Rakuten Link.|両プランともRakuten Linkを利用できます。|both は両方。\nWe need both your Rakuten ID and payment details.|楽天IDと支払い情報の両方が必要です。|both ... and。\nEither method may work depending on your device.|端末によってはどちらの方法でも使える場合があります。|either method。\nNeither option should be added without your consent.|同意なくどちらのオプションも追加すべきではありません。|neither は否定。\nYou can review either option before deciding.|決める前にどちらのオプションも確認できます。|either option。\nBoth the price and the conditions matter.|価格と条件の両方が重要です。|both ... and。''')

add(7,'紹介：関係代名詞と説明の追加','a customer who / a link that',
'who は人、that/which は物事を追加説明する関係代名詞。「紹介を受けた人」「条件を満たすリンク」を一文で説明できる。',
'a customer who qualifies ... / a link that you receive ...。関係節が直前の名詞を修飾する。関係節内の動詞の主語に注意。',
'紹介制度はリンク・QRコード利用が中心。特定の入力欄に数値コードを入れる方式だと決めつけない。',
'which は通常人の主語には使わない。関係節の意味を取り違えると特典対象者を誤案内する。', '''A customer who meets the conditions may receive points.|条件を満たすお客様はポイントを受け取れる場合があります。|who で customer を説明。\nThis is the referral link that you should open first.|こちらが最初に開く紹介リンクです。|that で link を説明。\nThe QR code that the referrer shares leads to the referral page.|紹介者が共有するQRコードから紹介ページへ進めます。|that で QR code を説明。\nCustomers who have already applied may not qualify.|すでに申し込んだ方は対象外となる場合があります。|who 節で対象を限定。\nThe campaign page that we checked lists the conditions.|確認したキャンペーンページに条件が載っています。|that ... checked。\nPeople who use Rakuten Link must follow the campaign rules.|Rakuten Linkを使う方もキャンペーン規約に従う必要があります。|who use の複数主語。\nThis is the document that explains the point schedule.|こちらがポイント付与時期を説明する書類です。|that explains ...。''')
add(7,'if / unless：対象・対象外を伝える','if / unless / only if',
'unless は「～でない限り」、only if は「～の場合に限り」。キャンペーン条件を詳しく説明する際に有用だが、条件の追加・省略はしない。',
'You may qualify if ... / You may not qualify unless ... / ... only if ...。unless は if not の意味に近いが、二重否定に注意。',
'特典の適用対象は申込経路・申込時期・初回契約かどうかなど複数条件があり得る。確認してから説明する。',
'unless you do not ... は二重否定になりやすい。「unless は～しない限り」を一度日本語で確認。', '''You may qualify if you meet every requirement.|すべての条件を満たせば対象となる場合があります。|if で必要条件。\nYou may not qualify unless you use the referral process correctly.|紹介手順を正しく使わないと対象外となる場合があります。|unless は～しない限り。\nThe bonus applies only if all conditions are met.|特典はすべての条件を満たした場合に限り適用されます。|only if。\nUnless the page confirms it, I cannot promise the bonus.|公式ページで確認できなければ特典はお約束できません。|unless の使い方。\nIf you applied before opening the link, check the rules carefully.|リンクを開く前に申し込んだ場合は規約をよく確認してください。|if + 過去形。\nYou can join the offer only if your contract is eligible.|契約が対象である場合に限り特典に参加できます。|only if。\nUnless the deadline is extended, the stated date applies.|期限が延長されない限り記載日が適用されます。|unless の例外条件。''')
add(7,'不確実性：may / might / subject to','断定と可能性を分ける',
'キャンペーンの可否、通信品質、開通時刻など断定できない事項には may / might / subject to を使う。can は一般的に可能、will は比較的強い将来の確信。',
'It may ... / It might ... / It is subject to + 名詞。may と might の後は動詞原形。subject to は条件・制約がかかることを示す。',
'「必ず付与される」「どこでもつながる」といった断定を避ける一方、分かっている基本料金は明確に言い切る。',
'may to apply は誤り。subject to conditions を「確定」と訳さない。', '''The campaign may change without prior notice.|キャンペーンは予告なく変更される場合があります。|may + 原形。\nYour eligibility is subject to the official rules.|適用可否は公式規約に従います。|subject to ...。\nThe connection speed may be restricted at busy times.|混雑時には速度が制限される場合があります。|may be + 過去分詞。\nPoint awards might take several months.|ポイント付与まで数か月かかる可能性があります。|might + 原形。\nThe offer may not be combined with another promotion.|別の特典と併用できない場合があります。|may not の不確実性。\nWe cannot confirm the bonus until the conditions are checked.|条件確認までは特典を確約できません。|cannot confirm until。\nAvailability is subject to device compatibility.|利用可否は端末の対応状況によります。|subject to + 名詞。''')
add(7,'割引：be eligible for / apply to','対象条件を正確に述べる',
'eligible は「条件を満たして対象になる」、apply は「規則・割引が適用される」。人が eligible、割引が applies という主語の違いを意識する。',
'be eligible for + 特典 / a discount applies to + 対象 / qualify for + 特典。「対象か確認します」は check your eligibility。',
'家族割、こども割、青春割、シニアプログラムは適用方法や対象年齢が異なる。割引とポイント還元も区別。',
'You are apply は誤り。eligible for と apply to の前置詞を混同しない。シニア制度のポイント還元を料金値引きと言わない。', '''You may be eligible for the family discount.|家族割の対象となる場合があります。|eligible for + 特典。\nThe family discount applies to eligible lines.|家族割は対象回線に適用されます。|applies to + 対象。\nLet me check your eligibility for this offer.|この特典の対象か確認いたします。|check your eligibility。\nThe youth discount is for customers aged 13 to 22.|青春割は13歳から22歳が対象です。|aged 13 to 22。\nSome senior benefits are awarded as points.|シニア向け特典の一部はポイントで進呈されます。|awarded as points。\nThis offer requires an entry or separate application.|この特典にはエントリーまたは別途申し込みが必要です。|requires + 名詞。\nPlease verify whether the family group is registered.|家族グループが登録済みか確認してください。|whether で可否を問う。''')

add(8,'オプション：費用・有無・比較','optional / additional / included',
'オプション案内では included（含まれる）と optional（任意）を明確に分ける。additional は追加費用、free trial は無料期間であって永続的無料とは限らない。',
'This option costs ... / It is optional. / It is included in the plan. / A separate fee applies. 明細に見せながら伝える。',
'15分標準通話かけ放題とRakuten Linkの無料通話は異なる仕組み。通常電話アプリで使う場合を説明する。',
'「free」は後続課金や条件を確認せず使わない。無料通話には対象外番号がある。', '''The 15-minute standard calling option costs 1,100 yen per month.|15分（標準）通話かけ放題は月額1,100円です。|サービス名＋費用。\nThis option is optional, not mandatory.|このオプションは任意で、必須ではありません。|optional と mandatory。\nRakuten Link is included in the plan.|Rakuten Linkはプランに含まれています。|included in ...。\nThe first month may be free under the offer conditions.|条件によって初回1か月が無料となる場合があります。|may be free。\nSome numbers are excluded from free calls.|一部の番号は無料通話の対象外です。|be excluded from。\nThe standard dialer normally costs 22 yen per 30 seconds.|標準電話アプリは通常30秒22円です。|per 30 seconds。\nWould you like to compare the calling options?|通話オプションを比較されますか。|Would you like to ...。''')
add(8,'海外ローミング：対象地域と制限','included / once / after / additional',
'海外ローミングは対象地域・端末・データ上限などを明示して説明する。国内のデータ無制限を海外にも無条件で適用すると誤案内になる。',
'Up to 2GB of high-speed roaming data is included. / After 2GB, speed is reduced. / You can add ... for ...。',
'対象地域では月2GBまでの高速データがプラン料金に含まれ、超過後は低速。追加1GBあたり500円の高速データチャージがある。',
'「海外でも無制限の高速通信」は誤り。国際通話やSMSの料金は別途条件を確認。', '''Up to 2 gigabytes of high-speed roaming data is included.|海外での高速ローミングデータは2GBまで含まれます。|up to 2 gigabytes。\nAfter 2 gigabytes, the roaming speed is reduced.|2GBを超えるとローミング速度が低下します。|after + 数量。\nYou can add one gigabyte for 500 yen.|500円で1GBの高速データを追加できます。|add ... for ...。\nPlease check whether your destination is supported.|渡航先が対象地域かご確認ください。|whether ... is supported。\nInternational calls may have separate charges.|国際通話には別途料金がかかる場合があります。|may have ...。\nPlease check device compatibility before traveling.|渡航前に端末の対応状況をご確認ください。|before + -ing。\nThe domestic unlimited-data tier does not mean unlimited high-speed roaming.|国内の無制限料金帯でも海外高速ローミングが無制限になるわけではありません。|does not mean ...。''')
add(8,'費用の内訳：単純現在と受動態','base fee / option fee / total',
'月額基本料金と端末代、オプション代、通話料を分ける。The total includes ... では内訳、is billed ... では請求方法を示せる。',
'The base fee is ... / The total includes ... / An additional charge may apply. 請求確定前は estimate（見積額）を使う。',
'税込額・請求月・割引とポイント還元の違いに注意して説明する。値引きとポイント還元は同じではない。',
'「実質1,100円」は請求額1,100円と限らない。還元されるポイントを金銭の即時値引きと説明しない。', '''The base monthly fee depends on your data usage.|基本月額料金はデータ使用量によって変わります。|depends on。\nThe estimate includes this optional service.|この見積額にはオプションサービスが含まれます。|includes。\nDevice installment payments are separate from the plan fee.|端末の分割払いはプラン料金とは別です。|separate from。\nA charge for standard calls may appear on your bill.|標準通話料が請求に含まれる場合があります。|may appear。\nThe discounted amount and the point rewards are different.|割引額とポイント還元は異なります。|different。\nPlease review the total before confirming the contract.|契約確定前に合計額をご確認ください。|before + -ing。\nThe final billing amount may differ from this estimate.|最終請求額は見積もりと異なる場合があります。|may differ from。''')
add(8,'トラブル対応：問題の特定と提案','seem / try -ing / let us',
'不具合対応は原因を決めつけず、現象を聞いて仮説を示す。It seems ... は断定を避け、Let us try ... は一緒に操作することを表す。',
'It seems that + 節 / Let us + 原形 / Try + -ing / Could you tell me ...?。確認→原因の切り分け→次の対応を分ける。',
'設定変更前に同意を取り、データ消失の恐れがある操作は十分な説明が必要。通信エリア確認やSIM設定を順番に進める。',
'「This will definitely fix it」と保証しない。try to restart と try restarting はニュアンスが少し異なる。', '''It seems that the phone is not connecting to mobile data.|端末がモバイルデータに接続できていないようです。|It seems that ...。\nCould you tell me when the issue started?|いつから問題が起きているか教えていただけますか。|間接疑問。\nLet us check the mobile data setting first.|まずモバイルデータ設定を確認しましょう。|Let us + 原形。\nPlease try restarting the phone.|端末の再起動をお試しください。|try + -ing。\nWe may need to check the APN settings.|APN設定を確認する必要があるかもしれません。|may need to。\nI cannot promise that this will fix the issue.|これで必ず直るとはお約束できません。|cannot promise that ...。\nIf the problem continues, we will review the next steps.|問題が続く場合は次の対応をご案内します。|if 条件。''')

chapters=[
 (1,'接客の基本','挨拶から希望の聞き取りまで、短い英文で会話を始める'),
 (2,'丁寧な応対','本人確認・案内・依頼を失礼なく伝える'),
 (3,'料金説明','金額、容量、比較、範囲の違いを厳密に伝える'),
 (4,'手続きと条件','進行状況、必要書類、次のステップを説明する'),
 (5,'契約と確認','完了・過去・受動態・間接疑問で正確に確認する'),
 (6,'SIMと進行手順','場所・順序・理由・選択肢を説明する'),
 (7,'紹介・割引・キャンペーン','紹介リンクや適用条件を誤解なく説明する'),
 (8,'オプションとトラブル対応','有料オプション、ローミング、請求、不具合に対応する')]
assert len(units)==32
for u,(structure,practice) in zip(units,EXTRA):
    u['sections'].extend([
        {'heading':'文のしくみをもう一段深く理解する','text':structure},
        {'heading':'店頭で誤解を防ぐ応用','text':practice}])
for u in units:
    assert len(u['examples'])==7
    assert len({x['en'] for x in u['examples']})==7
    assert len({x['ja'] for x in u['examples']})==7
    for x in u['examples']:
        assert x['en'].endswith(('.', '?', '!'))

scenarios=[
 {'id':'S1','title':'来店・要件ヒアリング','tag':'受付','lines':[
 ['staff','Welcome to Rakuten Mobile. How can I help you today?','楽天モバイルへようこそ。本日はどのようなご用件ですか。'],['customer','I would like to switch from another carrier.','他社から乗り換えたいです。'],['staff','Would you like to keep your current phone number?','今の電話番号をそのまま使いたいですか。'],['customer','Yes, please.','はい、お願いします。'],['staff','I will explain the transfer procedure and required documents.','乗り換え手順と必要書類をご説明します。']]},
 {'id':'S2','title':'基本料金の3段階','tag':'料金','lines':[
 ['customer','How much is the monthly fee?','月額料金はいくらですか。'],['staff','It depends on how much data you use each month.','毎月のデータ利用量で変わります。'],['staff','Up to 3GB is 1,078 yen; over 3GB up to 20GB is 2,178 yen.','3GBまでは1,078円、3GB超から20GBまでは2,178円です。'],['staff','Over 20GB is 3,278 yen. All these prices include tax.','20GB超は3,278円です。いずれも税込みです。'],['customer','Are options included?','オプションは含まれますか。'],['staff','Optional services and other charges may be added separately.','任意オプション等は別途料金が加算される場合があります。']]},
 {'id':'S3','title':'MNP・持ち物確認','tag':'契約','lines':[
 ['customer','Can I keep my current number?','今の番号を維持できますか。'],['staff','Yes. This process is called MNP.','はい。MNPという手続きです。'],['staff','For an in-store transfer, please check your MNP reservation number.','店頭での乗り換えではMNP予約番号をご用意ください。'],['staff','You will also need an accepted ID, your Rakuten ID and payment information.','利用可能な本人確認書類、楽天ID、支払情報も必要です。'],['customer','Does the document type matter?','書類の種類は関係ありますか。'],['staff','Yes. The accepted documents and procedures depend on your situation.','はい。利用できる書類と手続きは状況によって異なります。']]},
 {'id':'S4','title':'物理SIMとeSIM','tag':'契約','lines':[
 ['staff','Would you like a physical SIM or an eSIM?','物理SIMとeSIMのどちらをご希望ですか。'],['customer','What is the difference?','どう違いますか。'],['staff','A physical SIM is a removable card. An eSIM is built into a compatible phone.','物理SIMは取り外せるカードで、eSIMは対応端末に内蔵される仕組みです。'],['staff','May I check whether your phone supports eSIM?','eSIM対応か確認してもよろしいですか。'],['customer','Sure.','もちろんです。'],['staff','Thank you. We will check the supported devices before proceeding.','ありがとうございます。進む前に対応端末を確認します。']]},
 {'id':'S5','title':'Rakuten Linkと通話','tag':'オプション','lines':[
 ['customer','Are phone calls free?','通話は無料ですか。'],['staff','Eligible domestic calls are free when you use Rakuten Link.','Rakuten Linkを利用した対象国内通話は無料です。'],['staff','Some numbers are excluded, such as certain service numbers.','一部の特番など対象外番号があります。'],['customer','What if I use the regular phone app?','通常の電話アプリならどうなりますか。'],['staff','The standard rate is 22 yen per 30 seconds unless an applicable option covers the call.','該当するオプションがない場合、標準料金は30秒22円です。']]},
 {'id':'S6','title':'15分標準通話オプション','tag':'オプション','lines':[
 ['staff','There is an optional 15-minute standard calling service.','15分の標準通話オプションがあります。'],['customer','How much does it cost?','いくらですか。'],['staff','It costs 1,100 yen per month, including tax.','月額1,100円（税込）です。'],['staff','It covers eligible domestic calls of up to 15 minutes each through the standard dialer.','標準電話アプリで1回15分以内の対象国内通話をカバーします。'],['staff','The first month may be free under the applicable conditions.','条件により初回1か月が無料となる場合があります。'],['customer','I would like to compare it with Rakuten Link.','Rakuten Linkと比較したいです。']]},
 {'id':'S7','title':'紹介リンクとQRコード','tag':'紹介','lines':[
 ['customer','I have a referral code. How do I use it?','紹介コードがあります。どう使いますか。'],['staff','Let us check whether you mean a referral link or a QR code.','紹介リンクまたはQRコードのことか確認しましょう。'],['staff','The official referral process uses a link or QR code and a Rakuten account sign-in.','公式紹介制度ではリンクやQRコードと楽天会員ログインを利用します。'],['staff','Please open the referral link and sign in before applying.','申し込み前に紹介リンクからログインしてください。'],['customer','Will I receive points immediately?','ポイントはすぐにもらえますか。'],['staff','No. Points are awarded later in installments only if all conditions are met.','いいえ。すべての条件を満たした場合に後日分割で付与されます。']]},
 {'id':'S8','title':'紹介特典の細かい条件','tag':'紹介','lines':[
 ['customer','How many points can I receive?','何ポイントもらえますか。'],['staff','The number of points depends on the current campaign and your application route.','ポイント数は現行キャンペーンと申込区分によります。'],['staff','A first-time MNP application and a new-number application may have different rewards.','初回MNPと新規電話番号の申し込みでは特典が異なる場合があります。'],['staff','The referral campaign also requires a qualifying Rakuten Link call.','紹介キャンペーンには所定のRakuten Link通話も必要です。'],['customer','Can you guarantee that I will get the points?','必ずポイントがもらえると約束できますか。'],['staff','I can explain the rules, but I cannot guarantee rewards before eligibility is confirmed.','規約はご説明できますが、対象確認前に付与は確約できません。']]},
 {'id':'S9','title':'家族割と年齢別特典','tag':'割引','lines':[
 ['customer','Is there a discount for families?','家族割はありますか。'],['staff','Eligible family lines can receive a 110-yen monthly discount.','対象の家族回線は月額110円の割引を受けられます。'],['staff','A family group must be created or joined under the program rules.','制度に従って家族グループを作成または参加する必要があります。'],['customer','What about children or seniors?','子どもやシニア向けはどうですか。'],['staff','There are separate age-based programs. Some provide discounts and others provide points.','別の年齢別制度もあります。料金割引のものとポイント還元のものがあります。'],['staff','Let us check your eligibility and application method.','対象条件と申込方法を確認しましょう。']]},
 {'id':'S10','title':'海外での利用','tag':'海外','lines':[
 ['customer','Can I use Rakuten Mobile overseas?','海外でも使えますか。'],['staff','In supported destinations, up to 2GB of high-speed roaming data is included each month.','対象地域では高速ローミングデータが月2GBまで含まれます。'],['customer','What happens after 2GB?','2GBを超えるとどうなりますか。'],['staff','The connection becomes slower. You can purchase extra high-speed data for 500 yen per gigabyte.','低速になります。高速データは1GBあたり500円で追加できます。'],['staff','Please check the country, device and call charges before your trip.','渡航前に国・端末・通話料金をご確認ください。']]},
 {'id':'S11','title':'契約事務手数料の例外','tag':'契約','lines':[
 ['customer','Is there an administration fee?','契約事務手数料はありますか。'],['staff','For the first four cumulative lines under the same name, the sign-up administration fee is generally zero.','同一名義の累計4回線目までは通常、契約事務手数料が無料です。'],['staff','From the fifth cumulative line, a 3,850-yen fee per line applies under the current rules.','現在の規定では累計5回線目から1回線あたり3,850円かかります。'],['customer','Does a canceled line count?','解約済みの回線も数えますか。'],['staff','Yes, past lines count toward the cumulative total under the defined period.','はい。規定の期間内に契約した解約済み回線も累計に含まれます。']]},
 {'id':'S13','title':'来店予約・見積もり・エントリー特典','tag':'店頭キャンペーン','lines':[
 ['customer','I booked an appointment. Is there a store promotion?','来店予約をしました。店舗のキャンペーンはありますか。'],
 ['staff','There is a promotion for eligible customers who make a reservation, request an estimate and complete the required entry.','来店予約・お見積もり・エントリーなどの条件を満たすお客様向けのキャンペーンがあります。'],
 ['customer','Does everyone receive 2,000 points?','全員が2,000ポイントもらえますか。'],
 ['staff','No. The current promotion is a prize draw, so the number of points may vary.','いいえ。現行キャンペーンは抽選なのでポイント数は異なる場合があります。'],
 ['staff','Please scan the in-store QR code and enter using your Rakuten ID and reservation number, subject to the official rules.','公式条件に従って、店頭のQRコードから楽天IDと来店予約番号を使ってエントリーしてください。'],
 ['customer','When are the points awarded?','ポイントはいつ付与されますか。'],
 ['staff','They are awarded later if all the conditions are verified. Let us review the current campaign page together.','すべての条件が確認された場合に後日付与されます。現行のキャンペーンページを一緒に確認しましょう。'] ]},
 {'id':'S12','title':'通信不良・丁寧な対応','tag':'サポート','lines':[
 ['customer','My mobile data is not working.','モバイルデータ通信が使えません。'],['staff','I am sorry for the inconvenience. When did the problem start?','ご不便をおかけして申し訳ありません。いつから問題が発生しましたか。'],['customer','It started this morning.','今朝からです。'],['staff','May I check the network settings with your permission?','ご同意のもとネットワーク設定を確認してもよろしいですか。'],['customer','Yes.','はい。'],['staff','Thank you. We will check the settings first and explain the next steps.','ありがとうございます。まず設定を確認し、次の対応をご案内します。']]}
]


scenarios.extend([
 {'id':'S14','title':'留守番電話と最強通話パック','tag':'有料オプション','lines':[
 ['customer','Do you offer voicemail?','留守番電話はありますか。'],
 ['staff','Yes. The voicemail option costs 330 yen per month, including tax.','はい。留守番電話オプションは月額330円（税込）です。'],
 ['customer','Is voicemail included in my basic plan?','基本プランに含まれていますか。'],
 ['staff','No. It is a separate paid option. A first-month-free offer may apply to eligible first-time sign-ups.','いいえ。別料金の有料オプションです。初回申込者には条件付きで最初の1か月が無料となる場合があります。'],
 ['customer','Can I add it later?','後から追加できますか。'],
 ['staff','Yes, eligible customers can manage options through my Rakuten Mobile. Let us check the current conditions.','はい。対象のお客様はmy 楽天モバイルからオプションの追加・変更ができます。現在の条件を確認しましょう。']]},
 {'id':'S15','title':'故障・紛失時の端末保証','tag':'有料オプション','lines':[
 ['customer','Can I get insurance for my phone?','スマートフォンの保証はありますか。'],
 ['staff','There are device-protection options, and availability depends on the device and purchase route.','端末保証オプションがありますが、対象となるかは機種や購入経路によります。'],
 ['customer','Is the monthly price the same for every phone?','月額料金はどの機種でも同じですか。'],
 ['staff','No. For the current device replacement plan, monthly fees depend on the eligible device price.','いいえ。現行のスマホ交換保証では対象端末の価格などによって月額料金が異なります。'],
 ['staff','A separate charge may apply when you request a replacement.','交換を申し込む際に別途自己負担金が発生する場合があります。'],
 ['customer','Can I enroll at any time?','いつでも加入できますか。'],
 ['staff','Enrollment rules depend on the product. I will check the official terms before we proceed.','加入時期の条件は商品によって異なります。手続き前に公式規約を確認します。']]}
])
scenarios.sort(key=lambda scene:int(scene['id'][1:]))

sources=[
 {'label':'プラン料金・通話・手数料','url':'https://network.mobile.rakuten.co.jp/fee/saikyo-plan/detail/'},
 {'label':'紹介キャンペーン（公式・条件確認）','url':'https://network.mobile.rakuten.co.jp/campaign/referral/'},
 {'label':'キャンペーン一覧','url':'https://network.mobile.rakuten.co.jp/campaign/'},
 {'label':'契約・乗り換え申し込みガイド','url':'https://network.mobile.rakuten.co.jp/guide/procedure/'},
 {'label':'15分標準通話かけ放題','url':'https://network.mobile.rakuten.co.jp/service/standard-free-call/'},
 {'label':'海外ローミング','url':'https://network.mobile.rakuten.co.jp/service/international-roaming/'},
 {'label':'オプションサービス','url':'https://network.mobile.rakuten.co.jp/service/'},
 {'label':'ショップ来店予約・見積もりキャンペーン','url':'https://network.mobile.rakuten.co.jp/campaign/shop-weekday-reservation/'},
 {'label':'留守番電話','url':'https://network.mobile.rakuten.co.jp/service/voice-mail/'},
 {'label':'スマホ交換保証プラス ＆ 家電補償','url':'https://network.mobile.rakuten.co.jp/service/replacement-warranty-plus-appliances/'}]
productFacts=[
 {'tag':'料金','title':'Rakuten最強プラン（通常料金・税込）','body':'3GBまで1,078円／月、3GB超～20GBまで2,178円／月、20GB超は3,278円／月。その他の通話料・オプション料金等は別途発生する場合があります。','source':0},
 {'tag':'料金','title':'Rakuten最強U-NEXT','body':'税込4,378円／月。基本プランの3段階料金と混同せず、動画作品の追加料金等にも注意。','source':0},
 {'tag':'割引','title':'家族割','body':'対象回線は月110円の値引き。グループ作成・参加と適用条件を確認。','source':0},
 {'tag':'割引','title':'年齢別の特典','body':'12歳以下のこども割、13～22歳の青春割、65歳以上のシニアプログラム。割引かポイント還元か、申込方法と条件は制度ごとに確認。','source':0},
 {'tag':'通話','title':'Rakuten Linkの国内通話','body':'Rakuten Linkを利用した対象国内通話は無料。一部対象外番号あり。標準電話アプリは原則22円／30秒。','source':0},
 {'tag':'オプション','title':'15分（標準）通話かけ放題','body':'税込1,100円／月。標準電話アプリで1回15分以内の対象国内通話。初回1か月無料キャンペーンには条件あり。日割り対象外。','source':4},
 {'tag':'オプション','title':'留守番電話','body':'税込330円／月。初回1か月無料の特典は初回申し込み等の条件あり。Rakuten Link等からの再生方法、1417での再生に通話料が発生する場合がある点を案内する。','source':8},
 {'tag':'オプション','title':'端末保証・交換オプション','body':'スマホ交換保証プラス＆家電補償の現行月額料金は対象の製品価格や製品区分等によって異なり、交換時の自己負担金もあり。加入できるタイミングや対象範囲を確認。旧「スマホ交換保証プラス」は新規受付終了のため混同しない。','source':9},
 {'tag':'海外','title':'海外ローミング','body':'対象国・端末で高速通信月2GBまでプラン料金内。超過後は原則最大128kbps。高速データ追加は1GBあたり500円。','source':5},
 {'tag':'紹介','title':'紹介は「数値コード入力」と決めつけない','body':'公式の紹介リンク・QRコードから楽天IDでログインする流れを確認。申込前のログイン、所定期間の開通、Rakuten Linkによる10秒以上の発信通話等の条件。キャンペーンコード1784は紹介施策の管理識別子で、紹介リンクの代わりに契約画面へ入力するコードとは限らない。','source':1},
 {'tag':'紹介','title':'紹介特典のポイント付与','body':'後日・分割で付与、対象条件あり。2026年10月確認の公式案内では紹介者7,000pt・初回MNP被紹介者13,000pt（新規番号12,000pt）など。キャンペーンは変更されるため必ず現行条件を確認。','source':1},
 {'tag':'キャンペーン','title':'来店予約・店頭見積もり特典（2026年10月開始）','body':'ショップ来店予約、店頭でのお見積もり、来店時のQR読み取りとエントリーなどの条件を満たすと抽選で最大2,000ポイント。店頭で本人がキャンペーン参加を申告し、所定の期限内に来店・エントリーが必要。来店予約番号なども必要で、過去の来店特典参加等の除外条件にも注意。','source':7},
 {'tag':'契約','title':'MNPと持ち物','body':'店頭のMNPでは原則予約番号が必要。本人確認書類、楽天ID・パスワード、支払い手段など。国籍・年齢などにより必要書類は異なる。','source':3},
 {'tag':'契約','title':'契約事務手数料の例外','body':'同一名義の累計4回線目までは無料。2025年11月19日以降、累計5回線目以上は1回線3,850円（税込）。解約済み回線も規定に従って累計に含む。','source':0},
 {'tag':'その他','title':'速度と通信品質','body':'データ無制限でも混雑時等の速度制御があり得る。対応エリア・建物内の受信・対応機種は個別に確認。','source':0},
 {'tag':'その他','title':'データタイプ新規受付停止','body':'Rakuten最強プラン（データタイプ）は2026年3月5日から新規受付を一時停止。通常プランと混同して勧めない。','source':0},
]
output={'name':'Counter English — Rakuten Mobile Staff Practice','version':'1.0.0','reviewedOn':'2026-10-21','disclaimer':'非公式の個人学習用教材。実際の接客では最新の公式キャンペーン・契約条件・店舗ルールを確認すること。','chapters':[{'id':n,'title':title,'goal':goal} for n,title,goal in chapters],'units':units,'scenarios':scenarios,'sources':sources,'facts':productFacts}
OUT=ROOT/'web/data/course.json'; OUT.parent.mkdir(parents=True,exist_ok=True)
OUT.write_text(json.dumps(output,ensure_ascii=False,indent=2),encoding='utf-8')
print(f'{len(units)} units, {len(units)*7} examples, {len(units)*20} quizzes, {len(scenarios)} dialogues, {OUT.stat().st_size} bytes')
