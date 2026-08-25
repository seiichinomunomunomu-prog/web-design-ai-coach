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