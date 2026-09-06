# WEB Design AI Coach

WEB Design AI Coachは、
HTML・CSS・JavaScriptを学習している初心者〜中級者向けの
AIコードレビュー・学習支援Webアプリです。

入力されたコードをAIが確認し、
問題点、修正理由、改善方法、学習ポイントを
優先順位付きで説明します。

---

## Current Version

**Review Mode v1.0**

Status：公開・動作確認済み

---

## Review Mode v1.0 でできること

### 1. コード入力

以下のコードを入力できます。

- HTML
- CSS
- JavaScript

HTMLのみ、CSSのみ、JavaScriptのみなど、
一部のコードだけでもレビューできます。

---

### 2. 質問・相談

コードと一緒に質問を入力できます。

例：

- このHTMLをレビューしてください
- レイアウトが崩れる原因を教えてください
- JavaScriptが動かない原因を教えてください
- 初心者にも分かるように説明してください

---

### 3. AIコードレビュー

入力されたコードについて、

- 問題点
- 問題となる理由
- 修正方法
- 改善例

をAIが説明します。

---

### 4. HTML / CSS / JavaScript CrossCheck

複数のコードを横断して整合性を確認できます。

例：

- HTMLのidとJavaScriptのDOM取得
- HTMLのclassとCSSセレクタ
- JavaScriptから参照しているHTML要素の存在
- HTML / CSS / JavaScript間の不整合

---

### 5. 修正優先順位

レビュー結果を重要度に応じて分類します。

- 🔴 必ず修正
- 🟡 改善推奨
- 🟢 発展的な提案

初心者が「まず何を直すべきか」を判断しやすい構成にしています。

---

### 6. 改善コードの提示

必要に応じて、

- HTML
- CSS
- JavaScript

の改善コードを提示します。

---

### 7. 学習支援

単に修正コードを提示するだけではなく、

- なぜ問題なのか
- なぜこの修正が必要なのか
- 良い点
- 今後覚えておくとよいポイント

を初心者向けに説明します。

---

### 8. RAG Knowledge

DifyのKnowledgeを利用し、
独自のレビュー基準をAIへ提供しています。

CrossCheck GuideなどのKnowledgeを参照し、
レビュー品質の安定化を図っています。

---

### 9. Web公開

FastAPIアプリをRenderへデプロイしています。

GitHubのmasterブランチへのpush後、
Render Auto-Deployによって公開版へ変更が反映されます。

---

### 10. 簡易パスワード認証

公開中の開発版を保護するため、
簡易パスワード認証を実装しています。

- 未認証アクセスをログイン画面へ転送
- ログインSession管理
- `/review` の未認証利用を防止
- ログアウト機能

秘密情報はソースコードへ直接記述せず、
環境変数で管理しています。

---

## Technology Stack

- Python
- FastAPI
- Uvicorn
- Jinja2
- HTML
- CSS
- JavaScript
- Dify API
- Dify Knowledge / RAG
- Git
- GitHub
- Render

---

## 現在未実装の主な機能

Review Mode v1.0では、以下はまだ実装していません。

- Create Mode（構想からコードを生成）
- ファイルアップロード
- 画像・ワイヤーフレーム解析
- レビュー履歴保存
- コードのワンクリックコピー
- ユーザーごとのアカウント
- 利用回数管理
- 有料プラン・決済
- 複数プロジェクト管理
- GitHubリポジトリの直接レビュー

---

## Development Status

- Phase 6：Review Mode評価 / System Prompt v1.0 FIX ✅
- Phase 7：Review Mode v1.0 Render公開 ✅
- Phase 7.1：簡易パスワード認証 ✅
- Phase 8：機能改善・拡張検討