# Learning Note

---

# 2026-08-03

## 今日できるようになったこと

- JavaScript入力欄追加
- Markdown表示
- Dify APIの理解
- APIキーの役割を理解
- テストセット作成

---

## 気付き

FastAPIはAPIキーを使って
Difyアプリへアクセスしている。

システムプロンプトやKnowledgeは
Dify側で管理できる。

---

## 次回

- Dify System Prompt Version1
- Knowledge作成

---

## 一言

JavaScript対応まで完成した。
AIコーチらしくなってきた。

# LEARNING

## 2026-08-13

### 1. RAGの基本構造

RAGは単にナレッジベースを作成するだけでは動作しない。

ユーザー入力
↓
知識検索
↓
LLM
↓
回答

という流れを作り、

検索結果をLLMへ渡す必要がある。


### 2. Knowledge Retrievalのquery

知識検索ノードでは、
ユーザーの質問を検索クエリとして使用する。

今回、

ユーザー入力 / query

を知識検索ノードのクエリテキストとして設定した。


### 3. LLM Context

知識検索結果をLLMのContextへ設定することで、
LLMがナレッジ検索結果を利用して回答できる。

Knowledge Retrievalのresultを
LLM Contextへ接続した。


### 4. RAGは「知識追加」だけではない

今回のRAGでは単なる知識情報ではなく、

「レビューするときに何を見るべきか」

というレビュー基準もナレッジとして与えた。

これによって、

HTML
CSS
JavaScript

を個別に見るだけでなく、

HTML ↔ CSS ↔ JavaScript

の関連性を確認する能力を強化できた。


### 5. CrossCheckの重要性

Webアプリでは各コードが単体で正しくても、

- HTMLのid
- CSSのclass
- JavaScriptのDOM参照

が一致していなければ正しく動作しない。

コードレビューでは
「コード単体の正しさ」だけでなく
「コード間の整合性」が重要。


### 6. DOMの理解

DOMはJavaScriptからHTML要素を取得したり、
Webページの内容を書き換えたりするための仕組み。

例：

document.getElementById("result")

JavaScriptがHTML要素を正しく取得するには、
HTML側のidとの一致が必要。


### 7. RAGの評価方法

RAG導入後だけを見て「良くなった」と判断するのではなく、

RAG導入前
↓
同じTEST
↓
RAG導入後

で比較することが重要。

今回TEST00〜06を再実行することで、
CrossCheck能力の改善を確認できた。


### 8. AI評価では「出なかった項目」も重要

AIが正しい回答をしたかだけではなく、

「期待していたが出力されなかった観点」

を見ることで次の改善点が分かる。

TEST06では、

- Security
- 総合100点評価
- 一部評価軸の網羅性

が次の改善候補として確認された。


### 9. ユーザー質問とAI内部評価基準は分ける

ユーザーに、

「Securityを確認してください」
「Performanceを確認してください」
「CrossCheckしてください」

とすべて指定させるのではなく、

「このWebサイト全体をレビューしてください」

という自然な質問から、
AI Coach自身が必要なレビュー項目を判断することが望ましい。

これはWeb Design AI Coachの重要な設計方針とする。

## 2026-08-17

### 1. RAGは接続しただけでは確認にならない

Knowledge Searchノードを追加しただけでは、
実際にRAGが使われているかは判断できない。

Difyのログ・引用を確認し、

- Knowledgeが検索されたか
- LLMへContextとして渡されたか
- 回答にKnowledgeが利用されたか

まで確認することが重要。

---

### 2. System PromptとKnowledgeは役割が違う

System PromptはAIの

- 役割
- 判断基準
- 回答方針
- 優先順位

を決める。

Knowledgeはレビュー時に参照する

- HTML
- CSS
- JavaScript
- CrossCheck

などの知識・基準を補強する。

すべてをSystem Promptに書くのではなく、
System PromptとRAGを役割分担させることが重要。

---

### 3. 「🔴を減らす」のではなく「🔴の精度を上げる」

今回のSystem Prompt改善で最も重要だった点。

単純に🔴判定を減らすと、
本当に重大な問題まで見逃す可能性がある。

目標は、

正常コード
→ 不要な🔴を出さない

重大な不具合
→ 🔴を維持する

という判定精度の向上。

TEST01とTEST05などを比較することで、
この両方を確認できた。

---

### 4. AI評価には正常系と異常系の両方が必要

AIの品質確認では、
エラーを発見できるかだけでは不十分。

正常なコードを
「問題がある」と誤判定しないことも重要。

そのためテストケースには、

- 正常系
- 単純エラー
- CrossCheck
- UX / Accessibility
- ロジックエラー
- 大規模コード

など異なる性質のケースを用意する必要がある。

---

### 5. AIの「問題検出」と「理由説明」は別々に評価する

TEST05では、

`if(name="")`

の問題自体と修正方法は正しく検出したが、
「常にtrueになる」という理由説明には技術的な不正確さがあった。

そのためAIレビュー品質は、

1. 問題を発見できたか
2. 重大度は正しいか
3. 理由は正しいか
4. 修正方法は正しいか

を分けて評価する必要がある。

---

### 6. Promptは完成品ではなくVersion管理する

System Promptを毎回少しずつ変更すると、
以前より良くなったのか悪くなったのか判断しにくくなる。

今回のPromptを

**Review Mode v1.0**

としてFIXし、

今後変更する場合は

v1.1
v1.2

のようにVersion管理する。

これにより、TEST00〜06を使った回帰テストが可能になる。

## 2026-08-25

### GitHubとRenderを使ったWebアプリ公開

今回、ローカルPCで開発していたFastAPIアプリを
GitHub経由でRenderへ公開した。

基本的な流れ：

VS Code
↓
Git
↓
GitHub
↓
Render
↓
公開Webアプリ

GitHubへpushするとRenderが変更を検知し、
Auto-Deployによって公開アプリへ変更が反映されることを確認した。

### Gitの役割

以下の基本操作を実際の開発で使用した。

- `git status`
- `git add`
- `git commit`
- `git push`
- `git remote -v`

`git status` を使うことで、
変更済み・ステージ済み・未追跡ファイルを確認できる。

### .gitignoreの役割

`.gitignore` はGitHubへ公開したくないファイルを
Gitの管理対象から除外するために使用する。

今回、

- `.venv`
- `.env`
- `__pycache__`

などをGitHubへ登録しない構成を確認した。

特にAPIキーを含む `.env` をGitHubへpushしないことが重要。

### 環境変数によるAPIキー管理

ローカル環境では `.env`、
Renderでは Environment Variables を使用する。

Python側では、

`os.getenv("DIFY_API_KEY")`

によって環境に応じたAPIキーを取得できる。

コードにAPIキーを直接記述しない構成にすることで、
GitHub公開時の秘密情報流出を防止できる。

### requirements.txtの役割

RenderにはローカルPCの `.venv` をアップロードしない。

代わりに `requirements.txt` に必要なPythonパッケージを記載し、
Renderが公開環境で必要なパッケージをインストールする。

### HTTPステータスの確認

Renderログから以下を確認した。

- `200 OK`：正常処理
- `304 Not Modified`：ブラウザキャッシュを利用しており正常

`POST /review 200 OK` により、
公開環境のFastAPIがレビュー処理を正常に実行していることを確認できる。

### 公開後テストの重要性

ローカル環境で正常でも、
公開環境で初めて見つかる問題がある。

今回、

CSS空欄
↓
`Field required`
↓
原因調査
↓
FastAPI修正
↓
Git commit / push
↓
Render Auto-Deploy
↓
再テスト
↓
PASS

という一連の修正サイクルを経験した。

「作って終わり」ではなく、
公開後に確認・修正・再テストすることもWebアプリ開発の一部である。

## 2026-08-25 - Phase 7.1で学んだこと

### 1. 公開することとアクセスを制限することは別

RenderへDeployするとアプリはインターネットからアクセス可能になる。

開発中のアプリやAPIコストが発生するアプリでは、
公開後のアクセス制御も考える必要がある。

### 2. 画面だけでなく処理側も保護する

トップ画面 `/` だけをログイン必須にしても、
`/review` が直接利用できればDify APIを呼び出される可能性がある。

そのため、

- `/`
- `/review`

の両方で認証状態を確認する必要がある。

### 3. Sessionの役割

ログイン成功時にSessionへ認証済み状態を保存することで、
ページを移動するたびにパスワードを入力する必要がなくなる。

ログアウト時にはSessionを削除する。

### 4. 秘密情報はソースコードへ書かない

APIキーやパスワードなどは、

ローカル：
`.env`

公開環境：
Render Environment Variables

で管理する。

GitHubへ秘密情報をpushしないことが重要。

### 5. 新しいライブラリを使ったらrequirements.txtも更新する

SessionMiddlewareの利用時に、

`ModuleNotFoundError: No module named 'itsdangerous'`

が発生した。

ローカルで

`python -m pip install itsdangerous`

を実行するだけでなく、
Renderでも同じ環境を再現できるように
`requirements.txt` へ追加する必要がある。

### 6. Deploy失敗時は原因を切り分ける

今回、GitHubへのpush後、
Renderに `APP_PASSWORD` と `SESSION_SECRET` がまだ存在しない状態で
最初のDeployが失敗した。

環境変数を設定して再Deployすることで正常にLiveとなった。

Deploy失敗そのものではなく、
EventsやLogsから原因を確認することが重要。

### 7. 公開環境テストでは新しいブラウザSessionを使う

InPrivateウィンドウを利用することで、
既存のログインSessionの影響を受けず、

「初めてアクセスしたユーザー」

として認証動作を確認できる。

### 今回できるようになったこと

- FastAPIへの簡易ログイン機能追加
- Sessionを使った認証状態管理
- ログアウト処理
- URL単位でのアクセス制御
- 環境変数によるパスワード管理
- Python依存パッケージ管理
- Render Environment Variables設定
- Deploy失敗からの復旧
- 公開環境での認証テスト

# Phase 8：Review Mode v1.1 機能改善・拡張

## 目的

Review Mode v1.0を基準として、
実際の使用・テストから見つかった課題を改善し、
より実用的なWeb Design AI Coachへ拡張する。

---

## 8-1 Focused Review 要件定義

### 背景

Review Mode v1.0では、
具体的な修正質問を入力した場合でも、
「総合評価」「良い点」などを含む
General Review形式で回答する傾向があった。

### 改善方針

ユーザーの質問内容に応じて、

- General Review
- Focused Review

を自動的に切り替える。

### General Review

コード全体について、
問題点・改善点を広くレビューする。

### Focused Review

ユーザーが指定した問題・変更目的に集中し、
必要な修正コードを優先して提示する。

---

## 8-2 Beforeテスト

Focused Review実装前の挙動を確認するため、
TEST-F01～F05を作成して評価。

| TEST | 内容 | Before |
|---|---|---|
| F01 | 画像＋テキストを横並び | △ |
| F02 | ボタンを中央配置・必要部分のみ | × |
| F03 | PC3列・スマホ1列 | × |
| F04 | JavaScript ID不一致 | △ |
| F05 | General Review境界テスト | ○ |

### Beforeテストから分かったこと

- 技術的な修正内容そのものは概ね正しい
- HTML / CSS / JavaScriptのCrossCheck能力もある
- しかし具体的な質問でもGeneral Review形式になりやすい
- 必要以上に回答範囲が広がる場合がある

---

## 8-3 System Prompt改善

以下のルールを追加。

- General / FocusedのMode判定
- Focused Review専用回答形式
- 最小変更の原則
- Focused Reviewでも関連範囲のCrossCheckを実施
- 重大な問題はFocused Reviewでも指摘
- General / Focused回答形式の分離

### 設計方針

Review Mode v1.0で正常に動作している
General Review能力を極力変更しない。

新しい機能を追加する際も、
既存機能への副作用を最小限にする。

---

## 8-4 Afterテスト

System Prompt改善後、
同じTEST-F01～F05を再実行。

| TEST | 内容 | Before | After |
|---|---|---:|---:|
| F01 | 画像＋テキストを横並び | △ | ○ |
| F02 | ボタン中央・必要部分のみ | × | ○ |
| F03 | PC3列・スマホ1列 | × | ○ |
| F04 | JavaScript ID不一致 | △ | ○ |
| F05 | General Review境界 | ○ | ○※ |

### 結果

Mode判定：5/5成功

Focused Review：
F01～F04すべてPASS。

General Review：
F05で正常にGeneral Reviewへ分類された。

### F05既知の軽微課題

General Review後半に、

- 変更内容の説明
- 必要な追加修正
- 注意点

などFocused Reviewでも使用する見出しが
一部出力される場合がある。

回答内容およびMode判定には問題がないため、
現時点では許容する。

Promptへの制約追加による副作用を避けるため、
これ以上のPrompt変更は現時点では行わない。

---

## 8-5 UI改善（追加開発予定）

実際のReview Mode使用中に見つかった
UI上の改善要求をPhase 8の開発計画へ追加する。

### UI-01：AI添削中インジケーター

AI添削ボタン押下後、
回答生成中であることをユーザーに表示する。

予定仕様：

- 「AI添削中...」表示
- スピナー等のインジケーター表示
- 添削中はAI添削ボタンを一時的に無効化
- 回答完了後に通常状態へ戻す

目的：

- ボタンが正常に押されたことを明確にする
- Dify回答待ち時間のユーザー不安を軽減
- 二重送信を防止する

### UI-02：コードクリアボタン

HTML / CSS / JavaScript入力欄を
ワンクリックでクリアできる機能を追加する。

予定仕様：

- HTMLをクリア
- CSSをクリア
- JavaScriptをクリア
- 質問欄は保持
- AI添削ボタン付近に配置

目的：

- 複数コードの連続テストをしやすくする
- 手動でコードを全選択・削除する操作を減らす

---

## Phase 8 現在地

完了：

- Focused Review要件定義
- TEST-F01～F05作成
- Beforeテスト
- System Prompt改善
- Afterテスト
- General / Focused自動判定確認
- CrossCheck回帰確認

次：

1. Phase 8の記録整理
2. UI-01 AI添削中インジケーター実装
3. UI-02 コードクリア機能実装
4. UI動作テスト
5. ローカル最終確認
6. Git commit / GitHub保存
7. RenderへDeploy
8. 公開環境確認
9. Phase 8最終記録

## Phase 8：Focused Review開発で学んだこと

### 1. AIの回答内容と回答形式は分けて評価する

Focused Review実装前のTEST-F01～F05では、
期待した回答形式にならないケースがあった。

しかし回答内容を確認すると、

- HTML / CSS / JavaScriptの理解
- 修正箇所の特定
- 必要なコードの生成
- HTML / CSS / JavaScript間のCrossCheck

など、技術的な回答能力そのものは概ね正常だった。

今回の主な問題は、
「正しい答えを出せないこと」ではなく、

「具体的な質問でもGeneral Review形式で回答してしまうこと」

だった。

このことから、
AI機能を評価するときは、

- 回答内容が正しいか
- 回答範囲が適切か
- 回答形式が目的に合っているか

を分けて確認することが重要だと学んだ。

---

### 2. Before / Afterテストで変更効果を確認する

System Promptを変更する前に、
TEST-F01～F05を固定してBeforeテストを実施した。

その後、
同じ入力・同じ質問でAfterテストを行うことで、
Prompt変更による効果を比較できた。

結果：

| TEST | Before | After |
|---|---:|---:|
| F01 | △ | ○ |
| F02 | × | ○ |
| F03 | × | ○ |
| F04 | △ | ○ |
| F05 | ○ | ○ |

特にF05をGeneral Reviewの境界テストとして残したことで、
Focused Reviewを追加した結果、
すべての質問がFocused Reviewになってしまうような
副作用がないことも確認できた。

機能追加では、
新機能が動くことだけではなく、
既存機能が壊れていないことを確認する
「回帰確認」も重要である。

---

### 3. 最小変更の原則はAIの回答品質にも有効

Focused Reviewでは、
ユーザーの目的を達成するために必要な箇所だけを
変更するルールを追加した。

TEST-F02では、
ボタンを中央配置するために
親要素全体のレイアウトを変更するのではなく、

`display: block;`
`margin: 0 auto;`

という小さな変更で対応できた。

TEST-F03でも、
PC用CSSを書き換えず、
スマートフォン用のmedia queryだけを追加する回答になった。

コード修正では、
「動くコードを作る」だけではなく、

「現在正常に動いている部分をできるだけ変更しない」

という考え方が重要である。

---

### 4. Focused ReviewでもCrossCheckは失わない

回答範囲を狭くすると、
HTML / CSS / JavaScript間の確認能力まで
弱くなる可能性を懸念していた。

TEST-F04では、

HTML：
`id="menu-button"`

JavaScript：
`getElementById("menu-btn")`

という不一致を正しく検出した。

さらにCSS側の
`.menu-list.is-open`
も確認できていた。

この結果から、

「回答範囲を狭くすること」と
「確認範囲を狭くしすぎること」は別である

と分かった。

Focused Reviewでも、
質問に関係する範囲については
HTML / CSS / JavaScriptを横断して確認する必要がある。

---

### 5. Promptを厳格化しすぎない

TEST-F05ではGeneral ReviewへのMode判定は正常だったが、
回答後半にFocused Reviewでも使用する見出しが
一部出力される現象が残った。

これを完全に抑制するため、
回答形式をさらに厳格に指定するPromptも試した。

しかし、
Promptルールを追加し続けると、

- Promptが長くなる
- 指示同士が競合する可能性がある
- 正常に動いているF01～F04へ影響する可能性がある
- General Review本来の回答品質へ影響する可能性がある

という新しいリスクが生まれる。

そのため今回は、

「Mode判定と回答内容に問題がなければ、
軽微な見出し混在は既知課題として許容する」

と判断した。

すべての問題をその場で完全に修正するのではなく、
影響度と副作用のリスクを比較して
「今は変更しない」と判断することも開発の一部である。

---

### 6. テスト中の想定外も切り分けて判断する

TEST-F02では、
テスト入力時にCSSの`padding`を誤入力していた。

AIはこの誤記を検出し、
必要な修正として指摘した。

当初のテスト目的には含まれていない指摘だったが、
実際に入力コードに問題が存在していたため、
AIの不要な指摘ではなく正常な検出と判断した。

テストでは、
「期待していなかった回答＝誤回答」
とすぐ判断するのではなく、

- テストデータの問題
- AIの問題
- 仕様上許容できる動作

を切り分けて確認する必要がある。

---

### Phase 8で得た開発上の考え方

今回のPhase 8では、

要件を決める
→ テストケースを固定する
→ Beforeを確認する
→ 変更する
→ 同じ条件でAfterを確認する
→ 既存機能への副作用を確認する
→ 残った課題の影響度を判断する

という流れで開発を進めた。

AIアプリ開発では、
Promptを変更すれば必ず良くなるわけではない。

「何が問題なのか」
「どこまで直す必要があるのか」
「変更によって別の問題を起こさないか」

をテスト結果から判断し、
必要な範囲だけ変更することが重要だと学んだ。