# Test03 Intermediate（中級者向け）

## 目的

コードは動作するが、
保守性・可読性・安全性・パフォーマンスまで提案できるか確認する。

確認ポイント

- リファクタリング
- 可読性
- エラーハンドリング
- UX改善
- 保守性

---

## HTML

```html
<!DOCTYPE html>
<html lang="ja">

<head>
    <meta charset="UTF-8">
    <title>User Greeting</title>
</head>

<body>

<input
    id="name"
    type="text"
    placeholder="名前を入力">

<button id="btn">

表示

</button>

<p id="result"></p>

</body>

</html>
```

---

## CSS

```css
body{

font-family:Arial,sans-serif;

margin-top:40px;

text-align:center;

}

input{

width:250px;

padding:8px;

}

button{

padding:10px;

}
```

---

## JavaScript

```javascript
const btn=document.getElementById("btn");

btn.addEventListener("click",()=>{

const name=document.getElementById("name").value;

document.getElementById("result").innerHTML=

"こんにちは "+name;

});
```

---

## 質問

HTML・CSS・JavaScriptをレビューしてください。

初心者向け説明に加え、

保守性・可読性・セキュリティも評価してください。

---

## 期待する回答

### HTML

- label追加提案
- mainタグ提案
- アクセシビリティ改善

### CSS

- インデント整理
- rem使用提案
- 余白改善

### JavaScript

- textContent推奨
- trim()提案
- 空入力チェック
- テンプレートリテラル推奨

例

```javascript
result.textContent = `こんにちは ${name}`;
```

### 保守性

- DOM取得をまとめる
- 関数分割
- 変数名改善

### UX

- 未入力時のメッセージ
- Enterキー対応
- ボタン無効化

### セキュリティ

- innerHTML使用の注意

## RAG導入後評価

| 評価項目 | Test03結果 | 評価 |
|---|---|---|
| ① 問題検出 | XSS（クロスサイトスクリプティング）の可能性を正しく検出 | ◎ |
| ② 誤検出 | HTML・CSS・JavaScriptの基本構造や正常なID参照を誤って問題扱いしていない | ◎ |
| ③ 必須/改善の分類 | XSSリスクを「必ず修正」、可読性・保守性・UXを「改善推奨」に分類 | ◎ |
| ④ コード間整合性 | HTML入力 → JavaScript取得 → HTMLへの出力というデータの流れを確認 | ◎ |
| ⑤ RAG利用 | Cross Check Guideの考え方に沿ってHTML・JavaScript間の関係を確認できている | ◎  |

### 総合評価

4.5 / 5

※DifyログでKnowledge引用確認後、5 / 5に確定可能。

### 検出できた問題

#### 1. XSS（クロスサイトスクリプティング）の可能性

ユーザー入力値を取得し、その値をHTMLへ表示する処理について、
XSSにつながる可能性があることを検出している。

ユーザーが入力した内容にスクリプト等が含まれた場合の
セキュリティリスクとして「必ず修正」に分類できている。

### 修正方法

`innerHTML` ではなく `textContent` を使用し、
ユーザー入力をHTMLとして解釈させず、
通常のテキストとして表示する方法を提案している。

### コード間整合性評価

今回特に重要なのは、

HTMLフォーム
↓
ユーザー入力
↓
JavaScriptで値を取得
↓
DOMへ出力

というデータの流れを確認できていること。

HTML・JavaScriptを単体で見るのではなく、
ユーザー入力が最終的にどこへ出力されるかまで確認しており、
コード間のCross Checkが機能している。

また、HTML・CSS・JavaScript間の整合性については
基本的に問題なしと判断できている。

### 改善提案について

以下を必須修正とは分離して提案できている。

- イベント処理の可読性向上
- クラス等を利用した保守性向上
- ボタン表示などのUX改善
- form構造の改善
- Enterキーによる送信への対応

重大な問題と品質向上の提案を分離できており、
重要度分類も適切。

### Test03で確認できたRAG効果

- HTML → JavaScript → DOM出力の関係確認：成功
- ユーザー入力の扱いの確認：成功
- セキュリティ問題の検出：成功
- 必須修正と改善提案の分離：成功
- HTML・CSS・JavaScript横断チェック：成功
- 正常部分の誤検出抑制：成功

---

## Phase 6 System Prompt改善後 再評価

### 実施内容

レビュー優先順位に関するSystem Promptを修正し、
同一のTEST03コードで再評価を実施した。

今回の目的は、

- 正常コードへの過剰な🔴判定が抑制されているか
- セキュリティ・UX・アクセシビリティの改善提案を
  適切な優先順位で分類できるか
- 存在しない問題を作り出していないか

を確認すること。

### 確認結果

#### 🔴 必ず修正

「特に重大な問題は見当たりません」

と判定された。

今回のコードには、
直ちに動作を停止させる重大な不具合はないため、
この判定は適切。

正常なコードに対して
無理に🔴必ず修正を作る傾向は抑制されている。

### 🟡 改善推奨

#### 1. innerHTML → textContent

ユーザー入力を画面へ表示する処理について、

`innerHTML`

ではなく、

`textContent`

を使用することを提案した。

これはXSSなどのリスクを抑える観点から
有効な改善提案。

重大な動作不良として🔴にせず、
🟡改善推奨として分類した点も適切。

#### 2. aria-labelの追加

可視テキスト「表示」を持つbuttonに対して、

`aria-label="名前を表示"`

の追加を提案した。

しかし、今回のbuttonにはすでに
「表示」という可視テキストが存在する。

System Promptでは、

「すでに十分なアクセシブルネームを持つ要素に、
不要なaria-labelの追加を推奨しない」

と指定しているため、
この提案は過剰なアクセシビリティ提案と判断する。

### UX確認

JavaScriptにはすでに、

`name.trim() === ""`

による未入力チェックが実装されている。

AIはこれを認識しており、

「入力チェックが存在しない」

などの誤った指摘は行わなかった。

存在しない問題を無理に作らないという
System Promptの方針は機能している。

### CrossCheck確認

以下の整合性を適切に確認できている。

- HTMLとJavaScriptのID
- JavaScriptが参照するHTML要素
- CSSの適用状態
- 入力値とDOM出力処理

HTML・CSS・JavaScript間に重大な不整合はないと
正しく判断できている。

### 改善確認

- 正常コードへの不要な🔴判定を抑制
- セキュリティ改善を🟡として適切に分類
- 既存の入力チェックを正しく認識
- 存在しない問題を重大問題として作り出していない
- CrossCheck能力を維持

### 残課題

TEST01に続き、
可視テキストを持つbuttonに対する
aria-label追加提案が再度発生した。

TEST01とTEST03の両方で再現したため、
一時的な回答の揺らぎではなく、
アクセシビリティに関する過剰提案の傾向が
残っている可能性がある。

今後、

- System Prompt
- RAGナレッジ
- モデル側の一般知識

のどこからこの提案が生じているかを
切り分けて確認する。

### 判定

**Phase 6 System Prompt改善：概ね成功**

正常コードへの過剰な🔴判定、
セキュリティ分類、
CrossCheckについては改善効果を確認できた。

一方で、
不要なaria-label追加提案が
TEST01・TEST03の2ケースで再現した。

この問題はPhase 6の残課題として記録し、
原因を切り分けて評価する。