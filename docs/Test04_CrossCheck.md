# Test04 CrossCheck（HTML・CSS・JavaScript整合性チェック）

## 目的

HTML・CSS・JavaScriptを個別ではなく、
相互の関連性まで含めてレビューできるか確認する。

確認ポイント

- HTMLとCSSの関連性
- HTMLとJavaScriptの関連性
- CSSセレクタの誤り
- 存在しないid/class
- JavaScriptイベント対象
- 全体の設計改善提案

---

## HTML

```html
<!DOCTYPE html>
<html lang="ja">

<head>
    <meta charset="UTF-8">
    <title>Cross Check</title>
</head>

<body>

<h1 class="title">
    Web Design AI Coach
</h1>

<button id="submit">
    送信
</button>

<p id="message"></p>

</body>

</html>
```

---

## CSS

```css
.main-title{

color:blue;

}

.button{

background:red;

color:white;

padding:10px;

}
```

---

## JavaScript

```javascript
const button=document.getElementById("btn");

const message=document.getElementById("result");

button.addEventListener("click",()=>{

message.textContent="送信しました";

});
```

---

## 質問

HTML・CSS・JavaScriptを総合的にレビューしてください。

特に、

- HTML
- CSS
- JavaScript

それぞれだけではなく、

相互の関連性も確認してください。

---

## 期待する回答

### HTML

- HTML構造は概ね適切
- semanticタグ追加提案
- class名・id名の改善提案

### CSS

以下を指摘できること

❌ .main-title

↓

HTMLは

class="title"

になっている。

適用されない。

---

❌ .button

↓

HTMLには

id="submit"

しか存在しない。

CSSが効かない。

---

### JavaScript

❌

```javascript
getElementById("btn")
```

↓

HTML

```html
id="submit"
```

---

❌

```javascript
getElementById("result")
```

↓

HTML

```html
id="message"
```

---

### Cross Check

AIが次のような説明をできること

- HTML・CSSのclass名が一致していない
- HTML・JavaScriptのid名が一致していない
- CSSが適用されない理由
- JavaScriptが動作しない理由

---

### 改善コード例

HTML

```html
<h1 class="main-title">

<button id="btn">

<p id="result">
```

または

CSS・JavaScript側を修正する提案。

---

### 総合評価

以下のようなコメントが望ましい。

- 個々のコードは大きな問題はない
- しかしファイル間の命名が統一されていない
- 保守性向上のため命名規則を統一すると良い
- HTML・CSS・JavaScriptは必ずセットで確認すること

## 評価結果(13/Aug/2026)

### Before System Prompt v1.0

- [x] HTML ⇔ CSS のclass不一致を検出
- [x] HTML ⇔ JavaScript のid不一致を検出
- [x] 存在しないDOM要素を検出
- [x] 未使用CSSを検出
- [x] 修正コードを提示
- [x] HTML・CSS・JavaScriptを横断して説明

### コメント

System Prompt設定前でも、
HTML・CSS・JavaScript間の主要な不整合を正しく検出した。

基本的なCross Check能力は高い。

今後は以下を確認する。

- 必須修正と改善提案の区別
- 問題の優先順位
- 回答構成の安定性
- 初心者向け学習ポイント

## RAG導入後評価

判定：◎ 合格

### 確認結果

- HTMLとJavaScript間のID不一致を正しく検出できた
- メッセージ表示先のID不一致を正しく検出できた
- HTMLとCSS間のclassの不整合を検出できた
- HTML・CSS・JavaScriptの3コード間の整合性を横断的に評価できた
- 問題点だけでなく修正方法・改善コードまで提示できた
- 学習ポイントとしてID・classの整合性の重要性を説明できた

### RAG評価

04_CrossCheck_Guide.mdで追加した
「HTML・CSS・JavaScript間の関連性・整合性確認」
が回答に反映されている。

RAG導入の効果を確認できた。

### 備考

改善提案の一部にMarkdown/HTML表示の軽微な崩れがあるが、
クロスチェック機能そのものには影響しない。

---

## Phase 6 System Prompt改善後 再評価

### 実施内容

レビュー優先順位に関するSystem Promptを修正し、
同一のTEST04コードで再評価を実施した。

今回の目的は、過剰な🔴判定を抑制した状態でも、
HTML・CSS・JavaScript間のCrossCheck能力が
維持されているかを確認すること。

### 確認結果

#### 🔴 必ず修正

以下のコード間不整合を正しく検出した。

1. HTMLとJavaScriptのID不一致

HTML：

`id="submit"`

JavaScript：

`document.getElementById("btn")`

IDが一致していないため、
JavaScriptがボタンを正しく取得できない問題を検出した。

2. メッセージ表示用要素のID不一致

HTML：

`id="message"`

JavaScript：

`document.getElementById("result")`

JavaScriptが対象要素を取得できない問題を検出した。

### 🟡 改善推奨

CSSで定義されている

- `.main-title`
- `.button`

がHTML側で使用されていないことを検出した。

これはコードの動作を直接停止させる問題ではないため、
「🔴必ず修正」ではなく
「🟡改善推奨」とした判定は適切。

### CrossCheck確認

以下の横断チェックが正常に機能した。

- HTML ↔ JavaScript：IDの整合性
- HTML ↔ CSS：classの整合性
- CSS ↔ JavaScript：コード全体への影響確認

特に、単一ファイルの問題としてではなく、
HTML・CSS・JavaScript間の関連性から
問題を検出できている。

### 改善コード確認

改善コードでは、

- JavaScriptのDOM取得IDをHTMLに合わせる
- HTML側にCSSで使用しているclassを設定する

という修正が行われた。

これにより、

HTML ↔ JavaScript

だけでなく、

HTML ↔ CSS

についても同時に整合性が改善されている。

### 改善確認

- 重大なID不一致を🔴として正しく検出
- 未使用classを🟡として適切に分類
- HTML・CSS・JavaScriptのCrossCheck能力を維持
- 問題のない部分を無理に🔴として扱っていない
- 修正コードでも3コード間の整合性を考慮できている

### 判定

**Phase 6 System Prompt改善：成功**

System Promptの優先順位ルールを変更した後も、
HTML・CSS・JavaScript間のCrossCheck能力は維持された。

また、

- 動作に影響するID不一致 → 🔴必ず修正
- 未使用CSS/class → 🟡改善推奨

と、問題の重大度に応じた分類もできている。

TEST04では、
過剰判定の抑制とCrossCheck精度の維持を
両立できていることを確認した。