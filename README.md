# Counter English — 楽天モバイルスタッフ向け英文法

楽天モバイルでの接客英語を練習するための**非公式・独立した英語学習Webアプリ**です。フランス語文法アプリとは別のリポジトリです。

## 学習内容

- 8章32単元。be動詞から丁寧な依頼、料金比較、条件文、受動態、間接疑問まで
- 単元ごとに文法講義6節、解説つきの接客例文7件、理解確認20問
- 合計224例文・640問。合格ラインは20問中16問
- 出題範囲・問題数の指定、誤答復習、進捗保存、バックアップと復元
- 契約、MNP、料金、SIM/eSIM、Rakuten Link、オプション、紹介、家族割、海外、端末保証等に関する15の会話シーン
- 英文検索とお気に入り。ブラウザの英語音声読み上げ（0.65〜1.1倍速）
- 料金・キャンペーン等の公式情報を確認できる画面

## Netlify 公開（GitHub連携）

1. Netlifyで Add new project → Import an existing project → GitHub
2. GitHubリポジトリ eponine0805/rakuten-counter-english を選択
3. Base directory はリポジトリ直下、Publish directory は web、Build command は空欄
4. Deploy site で公開。ルートの netlify.toml にも公開先を設定済み

HTML / CSS / JavaScript の静的アプリで、npm install、APIキー、有料API、データベースは不要です。

## ローカルで動かす

Pythonがあればリポジトリのルートで python3 -m http.server 8000 -d web を実行し、ブラウザで http://localhost:8000 を開きます。直接 index.html をファイルとして開くとJSON読み込みがブロックされる場合があります。

## ファイル

- web/index.html: 画面の土台
- web/app.js: 文法講義・クイズ・復習・例文・接客会話・音声
- web/style.css: PC・モバイルのスタイル
- web/data/course.json: 32単元の講義、224例文、15接客会話、公式情報
- web/sw.js: オフラインキャッシュ
- docs/RESEARCH.md: 公的条件の確認メモと参照リンク

元の制作ソースZIPは別途作成済みです。こちらのリポジトリにはNetlifyで公開するための静的Webアプリを格納しています。

## 免責・学習記録

独立した非公式教材であり、楽天モバイルの公式研修資料ではありません。教材の事実確認は2026年10月21日時点です。実際の契約・価格・割引適用・紹介特典を保証するものではありません。学習データは端末のlocalStorageに保存され、バックアップ用JSONを利用できます。端末により音声品質・速度が異なります。