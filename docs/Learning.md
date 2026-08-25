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