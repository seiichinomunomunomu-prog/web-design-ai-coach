# Focused Review 要件

## 目的

ユーザーから具体的な修正要求が与えられた場合、
コード全体の総合レビューではなく、
要求を実現するための変更箇所と修正コードを重点的に提示する。

## 判定

### General Review

以下のような広い質問。

- コードをレビューしてください
- 改善点を教えてください
- Webサイト全体を見てください

### Focused Review

以下のような具体的な目的を持つ質問。

- 画像とテキストを横並びにしたい
- ボタンを中央にしたい
- スマホでは1列にしたい
- JavaScriptが動かない原因を知りたい
- この部分だけ修正したい

## Focused Review回答項目

1. 対応方針
2. 変更する場所
3. 修正コード
4. 変更内容の説明
5. 必要な追加修正
6. 関連する注意点

## 回答方針

- 修正コードを回答の中心とする
- 質問と直接関係しない全体レビューは行わない
- 総合評価は原則表示しない
- 良い点の列挙は原則行わない
- 発展的な提案は必要な場合のみ行う
- HTML / CSS / JavaScript間の関連部分は確認する
- 目的達成を妨げる重大問題がある場合のみ優先して指摘する
- 初心者にも変更理由が分かるように説明する

---

## 実装・検証結果

### 実装結果

Dify System Promptを変更し、
ユーザーの質問内容に応じて
General Review / Focused Reviewを
自動判定する方式を実装した。

アプリ側（FastAPI）でMode判定処理を追加するのではなく、
DifyのSystem Prompt内で判定する方式とした。

---

## Mode判定仕様

### General Review

以下のような質問ではGeneral Reviewを使用する。

- コード全体を確認してほしい
- 問題点を確認してほしい
- 改善点を教えてほしい
- 特定の修正目的が指定されていない
- HTML / CSS / JavaScript全体の評価を求めている

例：

> このコードを改善したいです。  
> 問題点を確認してください。

---

### Focused Review

以下のように、
具体的な問題・変更目的・期待する動作が
指定されている場合はFocused Reviewを使用する。

- ○○を横並びにしたい
- ○○を中央に配置したい
- スマートフォンだけ1列にしたい
- ボタンを押しても動かない
- 原因を特定してほしい
- 必要な修正コードだけ知りたい

例：

> メニューボタンをクリックしてもメニューが開きません。  
> 原因を特定して、必要な修正コードだけ提示してください。

---

## Focused Review回答仕様

Focused Reviewでは、
質問された目的の解決を最優先する。

基本回答形式：

1. 原因・対応方針
2. 変更する場所
3. 修正コード
4. 変更内容の説明
5. 必要な追加修正
6. 注意点

質問内容によって不要な項目がある場合は、
無理に内容を追加しない。

---

## 最小変更の原則

Focused Reviewでは、
ユーザーの目的を達成するために必要な
最小限のコード変更を優先する。

### 方針

- 正常なコードはできるだけ変更しない
- HTML変更が不要ならHTMLは変更しない
- CSSだけで対応できる場合はCSSだけ変更する
- JavaScriptだけの問題なら必要なJavaScriptだけ変更する
- PC表示を維持する要求では既存PC用CSSを不要に変更しない
- コード全体を書き直さない
- 変更不要な箇所は必要に応じて「変更不要」と説明する

---

## CrossCheck仕様

Focused Reviewでも、
質問に関連する範囲については
HTML / CSS / JavaScriptを横断して確認する。

主な確認対象：

- HTMLのidとJavaScriptのDOM取得
- HTMLのclassとCSSセレクタ
- JavaScriptのイベント対象
- JavaScriptで追加・削除するclassとCSS
- レスポンシブCSSとの関係
- 質問された動作を妨げる構文・実行上の問題

Focused Reviewは
「回答対象を限定する」ものであり、
「必要な確認を行わない」ものではない。

---

## 重大問題の扱い

質問された目的を達成できなくする問題が存在する場合は、
Focused Reviewでも指摘する。

例：

- JavaScriptの構文エラー
- DOM取得対象のid不一致
- 存在しないclass / idの参照
- イベント処理が実行できない問題
- 質問された表示・動作を妨げるCSS

質問と無関係な改善提案まで
レビュー範囲を広げない。

---

## General Reviewとの分離

General Reviewでは従来のReview Mode v1.0の
全体レビュー能力を維持する。

基本回答形式：

1. 総合評価
2. 良い点
3. 🔴 必ず修正
4. 🟡 改善推奨
5. 🟢 発展的な提案
6. HTML・CSS・JavaScriptの整合性
7. 改善コード
8. 学習ポイント

Focused Review追加によって、
General Reviewの既存機能を低下させないことを
重要な要件とする。

---

## 検証テスト

Focused Review実装前後で、
同一のTEST-F01～F05を使用して
Before / After比較を実施した。

| TEST | テスト目的 | 期待Mode | Before | After |
|---|---|---|---:|---:|
| F01 | 画像＋テキスト横並び | Focused | △ | ○ |
| F02 | ボタン中央・最小変更 | Focused | × | ○ |
| F03 | PC3列・スマホ1列 | Focused | × | ○ |
| F04 | JS ID不一致 / CrossCheck | Focused | △ | ○ |
| F05 | Mode境界確認 | General | ○ | ○※ |

### 検証結果

Mode判定：

**5 / 5 成功**

F01～F04：
Focused Reviewとして正常に回答。

F05：
General Reviewとして正常に回答。

Focused Review導入後も、
HTML / CSS / JavaScript間のCrossCheck能力が
維持されていることを確認した。

---

## 既知の軽微課題

TEST-F05ではGeneral ReviewへのMode判定は正常だが、
回答後半にFocused Reviewでも使用する以下の見出しが
一部出力される場合がある。

- 変更内容の説明
- 必要な追加修正
- 注意点

回答内容およびMode判定には問題がない。

この見出し混在を完全に抑制するために
System Promptへさらに制約を追加すると、
正常に動作しているFocused Reviewや
General Reviewへ副作用を与える可能性がある。

そのため現時点では既知の軽微課題として許容し、
追加のPrompt変更は行わない。

---

## 現時点の判定

Focused Review機能：

**PASS**

General / Focused Mode自動判定：

**PASS（5 / 5）**

CrossCheck：

**PASS**

General Review回帰確認：

**PASS**

既知課題：

**General Reviewで軽微な見出し混在あり（許容）**

以上をもって、
Focused Reviewの仕様・System Prompt・基本動作を
現時点の基準としてFIXする。