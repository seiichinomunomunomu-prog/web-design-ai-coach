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