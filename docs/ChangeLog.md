# Change Log

プロジェクトの変更履歴

---

## v0.1

### FastAPI環境構築

- FastAPIプロジェクト作成
- HTML画面表示
- CSS適用

---

## v0.2

### Dify API接続

- Dify API連携
- APIキー管理（.env）
- エラー処理追加

---

## v0.3

### AI添削画面

- Markdown表示対応
- 入力内容保持
- レイアウト改善

---

## v0.4

### JavaScript添削対応

- JavaScript入力欄追加
- HTML・CSS・JavaScript同時添削



# CHANGELOG

## 2026-08-13

### Added

- Web Design AI Coach用ナレッジベースをDifyに作成
- CrossCheck Guideをナレッジとして登録
- HTML・CSS・JavaScript間の整合性確認ルールを追加
- Difyワークフローに「知識検索」ノードを追加
- 知識検索結果をLLMコンテキストへ接続

### Changed

Difyワークフローを以下に変更。

ユーザー入力
↓
知識検索
↓
LLM
↓
回答

知識検索のクエリとして
`ユーザー入力 / query`
を使用。

LLMが検索結果を参照して回答するRAG構成へ変更。

### Tested

RAG導入後にTEST00〜TEST06を再実行。

特にTEST04・TEST05で、

- HTML / JavaScript ID不一致
- HTML / CSS class不整合
- DOM参照不一致
- 変数未定義
- 条件式の誤り

などを正しく検出できることを確認。

TEST06では抽象的な「Webサイト全体レビュー」という質問から、
UX、Accessibility、Performance、保守性、
CrossCheckなど複数観点のレビューが行われることを確認。

### Result

RAG導入によって、
HTML・CSS・JavaScript間のCrossCheck能力が改善した。

一方でTEST06から、

- 総合レビュー評価軸の網羅性
- Security評価
- 100点満点評価
- 出力形式の安定性

について改善余地があることを確認した。

## 2026-08-17

### Phase 6：System Prompt評価・改善

#### RAG導入後評価

- TEST00〜TEST06を使用してRAG導入後のレビュー品質を評価
- Knowledge Search → LLM のRAG構成を確認
- DifyログからKnowledgeが実際に引用されていることを確認
- HTML / CSS / JavaScriptのCrossCheck能力が維持されていることを確認

#### System Prompt改善

レビュー結果で「🔴 必ず修正」が過剰に出る傾向を確認。

System Promptの「レビューの優先順位」を修正し、

- 実際に動作しない問題 → 🔴 必ず修正
- 動作するが改善余地がある問題 → 🟡 改善推奨
- 将来的な設計改善 → 🟢 発展的な提案

という判定基準を明確化した。

#### System Prompt修正後の再評価

TEST01〜TEST06を再実行。

確認結果：

- 正常コードへの過剰な🔴判定を抑制
- ID不一致、未定義変数、構文・ロジック問題などの重大問題は🔴判定を維持
- HTML / CSS / JavaScriptのCrossCheck能力を維持
- 改善推奨と発展的提案の分類精度が向上
- 大規模コードでもレビュー能力を維持

#### 残課題

- aria-labelを不要なケースでも提案する場合がある
- 一部で🔴 / 🟡の境界に揺れがある
- 理由説明に軽微な技術的不正確さが発生する場合がある
- 総合レビューの100点評価基準は今後検討

### Phase 6 完了

Phase 6のSystem Prompt改善を完了。

現在のSystem Promptを

**Review Mode v1.0 基準Prompt**

としてFIX。

次フェーズではReview Mode v1.0を基準として、
Render公開を含む実用化へ進む。

## 2026-08-25

### Phase 7：Render公開・公開後確認

#### Renderへのデプロイ

- GitHubに `web-design-ai-coach` リポジトリを作成
- ローカルGitリポジトリとGitHubを接続
- `master` ブランチをGitHubへpush
- RenderとGitHubリポジトリを接続
- Root Directoryを `app` に設定
- Build Commandを設定
- Start Commandを設定
- Render Environment Variablesに `DIFY_API_KEY` を設定
- Web Design AI CoachをRenderへ公開
- 公開URLから正常にアクセスできることを確認

#### APIキー管理改善

- `config.py` に残っていた旧形式のDify APIキーを削除
- APIキーを `.env` / Render Environment Variablesで管理する構成に統一
- `.env` が `.gitignore` によりGitHubへ登録されないことを確認

#### 部分入力レビュー対応

公開環境でCSSを空欄にしてレビューした際、
FastAPIで `Field required` が発生する問題を確認。

原因：

- `html_code`
- `css_code`

が `Form(...)` により必須入力になっていた。

対応：

- HTML / CSS / JavaScriptを `Form("")` に変更
- 各コードを任意入力可能に変更

GitHubへpush後、Render Auto-Deployで自動反映。
同条件で再テストし正常動作を確認。

#### 公開後動作確認

- 公開URLアクセス：PASS
- AI添削：PASS
- HTMLのみの部分入力レビュー：PASS
- Firefox：PASS
- Chrome：PASS
- スマートフォン Safari：PASS
- Render `GET /`：200 OK
- Render `POST /review`：200 OK
- Dify API：200 OK
- GitHub → Render Auto-Deploy：正常動作

#### 残課題

- 全コード未入力時のFastAPI側入力チェック
- `DIFY RESPONSE` 全文ログ出力の停止
- Render Free環境のスリープ復帰確認
- 必要に応じたスマートフォンUI改善

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

## 2026-08-25 - Phase 7.1 簡易パスワード認証

### Added

- `templates/login.html` を追加
- FastAPI SessionMiddlewareを追加
- `/login` GET/POSTを追加
- `/logout` を追加
- `APP_PASSWORD` 環境変数を追加
- `SESSION_SECRET` 環境変数を追加
- `itsdangerous` を依存パッケージとして追加

### Changed

- `/` に認証チェックを追加
- `/review` に認証チェックを追加
- `index.html` にログアウトリンクを追加
- `requirements.txt` に `itsdangerous` を追加

### Deployment

- GitHub commit `a545917` をRenderへDeploy
- Render Environment Variablesに認証用環境変数を設定
- 再Deploy後 `Deploy live` を確認

### Verification

- 未認証アクセス → ログイン画面：OK
- 誤パスワード拒否：OK
- 正しいパスワードでログイン：OK
- AI添削：OK
- ログアウト：OK
- InPrivateで公開環境認証：OK

Phase 7.1 完了。

## Review Mode v1.1 - Phase 8（完了）

### Focused Review機能追加

Review Mode v1.0の利用・テストから、
具体的な修正要求に対してもGeneral Review形式で
回答する傾向があることを確認。

ユーザーの質問内容に応じて、
General Review / Focused Reviewを
自動的に切り替える機能をSystem Promptに追加した。

### 主な変更

- General Review / Focused Reviewの自動判定を追加
- Focused Review専用の回答形式を追加
- 具体的な質問では修正コードを回答の中心とするよう改善
- Focused Reviewでは無関係な全体レビューを抑制
- 既存コードへの変更を最小限にするルールを追加
- Focused Reviewでも関連範囲のCrossCheckを維持
- 目的達成を妨げる重大問題はFocused Reviewでも指摘
- General Review / Focused Reviewの回答形式分離ルールを追加

### テスト

TEST-F01～F05を作成し、
System Prompt変更前後でBefore / Afterテストを実施。

| TEST | 内容 | Before | After |
|---|---|---:|---:|
| F01 | 画像＋テキストを横並び | △ | ○ |
| F02 | ボタン中央配置・必要部分のみ | × | ○ |
| F03 | PC3列・スマホ1列 | × | ○ |
| F04 | JavaScript ID不一致 / CrossCheck | △ | ○ |
| F05 | General Review境界テスト | ○ | ○ ※ |

Mode判定は5ケースすべて成功。

F01～F04では、
具体的な質問に対してFocused Reviewへ切り替わり、
必要な変更箇所・修正コードを中心とした回答を確認。

F04ではFocused Review化後も、
HTML / JavaScript間のCrossCheck能力が
維持されていることを確認。

F05ではGeneral Reviewへの分類が正常に維持され、
Focused Review追加によるMode判定上の回帰は確認されなかった。

※ F05ではGeneral Review後半に、
Focused Reviewでも使用する見出しが一部出力される場合がある。
回答内容およびMode判定には問題がないため、
現時点では既知の軽微課題として許容する。

追加のPrompt制約による既存機能への副作用を避けるため、
現状のSystem Promptを基準としてFIXする。

### UI改善

#### UI-01：AI添削中インジケーター

- AI添削ボタン押下後に「AI添削中...」を表示
- 添削中にスピナーを表示
- 添削中はAI添削ボタンを無効化し、二重送信を防止
- 添削中はコードクリアボタンを表示したまま操作不可
- 回答完了後は通常状態へ復帰

#### UI-02：コードクリア機能

- HTML / CSS / JavaScriptを一括クリア
- 質問欄の入力内容は保持
- AI添削ボタン付近にコードクリアボタンを配置

### UI動作テスト

- UI-01：PASS
- UI-02：PASS
- AI添削中表示：OK
- スピナー表示：OK
- 二重送信防止：OK
- 添削中のコードクリア操作無効化：OK
- HTML / CSS / JavaScriptコードクリア：OK
- 質問欄保持：OK

### 公開

- ローカル最終確認：PASS
- Git commit：`a973c19 Add focused review and UI improvements`
- GitHub `master` へpush：完了
- Render Auto-Deploy：成功
- Render公開環境：Live
- 公開環境確認：PASS

### Phase 8 完了

Focused Reviewの追加およびUI改善を完了。

Focused Reviewでは、具体的な質問に対して必要な修正を中心に回答しながら、
関連するHTML / CSS / JavaScriptのCrossCheck能力を維持できることを確認した。

UI改善では、AI添削中の状態表示、二重送信防止、
コードクリア機能を追加し、ローカル環境およびRender公開環境で正常動作を確認した。

F05のGeneral Reviewに一部Focused Review系の見出しが混在する場合がある点は、
既知の軽微課題として許容する。

追加のPrompt制約による副作用を避け、
現在のSystem PromptをReview Mode v1.1の基準としてFIXする。

**Review Mode v1.1 / Phase 8：完了**

## Create Mode v0.1 - Phase 9（完了）

### Create Mode機能追加

自然な日本語で作りたいWebページの要望を入力すると、
AIがHTML / CSS / JavaScriptを生成するCreate Modeを追加した。

Review Modeとは処理およびDifyアプリを分離し、
既存のReview Mode v1.1へ影響を与えない構成とした。

### 主な変更

- `/create` にCreate Modeを追加
- Review Mode / Create Modeのモード切替UIを追加
- 自然言語からHTML / CSS / JavaScriptを生成
- HTML / CSS / JavaScriptを個別表示
- 各コードのコピー機能を追加
- JavaScript不要時は未使用メッセージを表示
- 生成結果の説明を表示
- PC / Smartphone Preview切替を追加
- iframeによるPreview分離
- AI生成中のスピナー表示
- 生成中の二重送信を防止
- 再生成中は直前の生成結果を保持
- Timeout / 通信 / HTTP / JSON解析 / 必須項目不足のエラー処理を追加
- Create Mode専用Dify APIキー `DIFY_CREATE_API_KEY` を追加

### Standalone対応

生成されたコードを以下の構成で保存した場合に、
単独のWebページとして動作できるようにした。

- `index.html`
- `style.css`
- `style.js`
- `images/`

HTMLから `style.css` を読み込み、
JavaScriptが必要な場合は `style.js` を読み込む。

画像は `images/` フォルダを参照する構成とした。

Previewでは外部の `style.css` / `style.js` を読み込まず、
生成されたCSS / JavaScriptをiframe内へ埋め込むことで、
アプリ本体から分離して表示・実行する構成とした。

### テスト

- C01～C05 Create Mode基本生成テスト：PASS
- JSなしStandaloneテスト：PASS
- JSありStandaloneテスト：PASS
- 画像ありStandaloneテスト：PASS
- Preview CSS反映：PASS
- Preview JavaScript動作：PASS
- PC / Smartphone切替：PASS
- HTML / CSS / JavaScript個別コピー：PASS
- JavaScriptなし時コピー無効化：PASS
- AI生成中表示・二重送信防止：PASS
- 再生成時の旧生成結果保持：PASS
- Timeoutエラー：PASS
- 通信エラー：PASS
- HTTPエラー：PASS
- JSON解析エラー：PASS
- 必須項目不足エラー：PASS

### Review Mode回帰テスト

Create Mode追加後にReview Mode v1.1の回帰確認を実施。

- General Review：PASS
- Focused Review：PASS
- General Review回答形式：正常
- Focused Review回答形式：正常
- HTML / CSS / JavaScript CrossCheck：正常

Create Mode追加によるReview Mode v1.1への
機能上の回帰は確認されなかった。

### 公開

- ローカル最終確認：PASS
- Git commit：`794dab9 Add Create Mode v0.1`
- GitHub `master` へpush：完了
- Render Environmentに `DIFY_CREATE_API_KEY` を追加
- Render Deploy：成功
- Render公開環境：Live
- 公開環境 Review Mode / Create Mode切替：PASS
- 公開環境 Create Mode JSなし生成：PASS
- 公開環境 Create Mode JSあり生成：PASS
- 公開環境 Smartphoneハンバーガーメニュー動作：PASS
- 公開環境 Preview：PASS
- 公開環境 PC / Smartphone切替：PASS
- 公開環境 説明表示：PASS

### Phase 9 完了

Create Mode v0.1の実装、ローカルテスト、
Review Mode v1.1の回帰テスト、
GitHubへの反映およびRender公開を完了した。

自然言語の要望からHTML / CSS / JavaScriptを生成し、
コードの個別コピー、Preview、PC / Smartphone表示確認までを
一つのWebアプリ内で実行できることを確認した。

また、生成コードをファイルへコピーすることで、
StandaloneのWebページとして利用できることも確認した。

**Create Mode v0.1 / Phase 9：完了**