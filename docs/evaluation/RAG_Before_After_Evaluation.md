# RAG導入前 vs RAG導入後 総合評価

## 目的

Web Design AI CoachにRAG（ナレッジ検索）を導入することで、
HTML・CSS・JavaScriptのレビュー品質がどのように変化するかを確認する。

特に以下を評価する。

- 問題検出精度
- 問題の理由説明
- 修正方法
- HTML・CSS・JavaScript間の整合性確認
- 初心者向け説明
- 実務レベルの改善提案
- UX
- Accessibility
- Performance
- Security
- 保守性


---

## RAG導入前

LLM単体でも、HTML・CSS・JavaScriptそれぞれの
基本的な問題を検出することはできていた。

一方で、以下の課題があった。

- コード単体のレビューになりやすい
- HTML・CSS・JavaScript間の関連性確認が弱い
- ID/classの不一致を安定して検出できない場合がある
- DOM参照関係の確認にばらつきがある
- レビュー基準がLLMの判断に依存する
- テストによって回答の観点にばらつきがある


---

## RAG導入内容

Web Design AI Coach用のナレッジベースを作成。

特にCrossCheck Guideを追加し、

- HTML ↔ JavaScript
- HTML ↔ CSS
- CSS ↔ JavaScript

の関連性・整合性を確認するレビュー基準を与えた。

Difyワークフローを以下の構成に変更。

ユーザー入力
↓
知識検索
↓
LLM
↓
回答

知識検索結果をLLMのコンテキストとして使用する構成とした。


---

## RAG導入後 TEST00〜06

### TEST00

判定：○ 合格

基本的なHTML・CSS・JavaScriptレビューが可能。

改善提案、発展的提案、改善コード、学習ポイントまで提示できた。


### TEST01

判定：○ 合格

アクセシビリティを含むレビューができた。

aria-labelなど、初心者向けレビューから一段進んだ改善提案を確認。


### TEST02

判定：◎ 合格

複数の明確な不具合を正しく検出。

- JavaScript ID不一致
- CSS構文エラー
- JavaScript変数未定義

問題 → 理由 → 修正方法まで説明できた。


### TEST03

判定：◎ 合格

フォーム入力からJavaScript処理、
Webページへの表示までの流れを確認できた。

セキュリティ、UX、フォーム処理など、
単純な構文チェック以外の観点も確認できた。


### TEST04

判定：◎ 合格

CrossCheck Guideの効果を特に確認できた。

- HTML ↔ JavaScript ID不一致
- メッセージ表示先ID不一致
- HTML ↔ CSS class不整合

など、複数コード間の関連性を横断的に確認できた。


### TEST05

判定：◎ 合格

- username / name の不一致
- 条件式の代入演算子の誤り
- result未定義
- 表示処理改善

などを検出。

HTMLとJavaScriptを横断したレビューが安定して行われた。


### TEST06

判定：○ 合格（期待仕様の一部未達）

ユーザーからは、

「このWebサイト全体をレビューしてください。
初心者向けの説明だけでなく、
現場で使われるレベルを意識して、
改善点と理由を教えてください。」

という抽象度の高い質問のみを入力した。

それにもかかわらずAIは自発的に、

- HTML
- CSS
- JavaScript
- CrossCheck
- UX
- Accessibility
- Performance
- 保守性

など複数の観点からレビューを行った。

これは総合レビュー能力として評価できる。

一方で、事前に設定した期待仕様のうち、

- Security評価
- 一部の網羅的チェック
- 100点満点による総合評価

などは十分に出力されなかった。

したがって完全合格ではなく、
「総合レビューは成立しているが、評価軸と出力形式の安定性には改善余地あり」
と評価する。


---

# RAG導入前後の比較

| 評価項目 | RAG導入前 | RAG導入後 |
|---|---|---|
| HTML単体レビュー | ○ | ○ |
| CSS単体レビュー | ○ | ○ |
| JavaScript単体レビュー | ○ | ○ |
| 問題理由の説明 | ○ | ◎ |
| 修正方法 | ○ | ◎ |
| HTML ↔ JavaScript | △ | ◎ |
| HTML ↔ CSS | △ | ◎ |
| CSS ↔ JavaScript | △ | ○〜◎ |
| ID/class整合性 | △ | ◎ |
| DOM参照確認 | △ | ◎ |
| UX | ○ | ○ |
| Accessibility | ○ | ○ |
| Performance | △〜○ | ○ |
| Security | △ | △ |
| 保守性 | ○ | ○ |
| 回答形式の安定性 | △ | ○ |
| 総合点数評価 | △ | △ |


---

# 総合評価

RAG導入による最も大きな改善は、

「HTML・CSS・JavaScriptを個別に見るAI」

から、

「HTML・CSS・JavaScriptの関係まで確認するAI」

へ進んだことである。

特にTEST04・TEST05ではCrossCheck Guideの効果が明確に確認できた。

一方、TEST06では新しい課題も確認された。

ユーザーが「Webサイト全体をレビューしてください」とだけ質問した場合でも、
複数観点から自律的にレビューできているが、

- Security
- Performance
- Accessibility
- UX
- 保守性
- CrossCheck
- 総合点数

などの評価軸を毎回安定して網羅するところまでは到達していない。

今後は質問文に評価項目を列挙するのではなく、
AI Coach自身がレビュー対象を判断し、
必要な評価軸を自律的に選択できる設計を目指す。


---

## RAG導入総合判定

RAG導入：成功

特にCrossCheck能力について明確な改善効果を確認。

次の開発テーマは、

「検索精度の改善」だけではなく、
「総合レビュー基準と出力形式の安定化」

とする。