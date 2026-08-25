# Test05 JavaScriptDebug（JavaScriptデバッグ能力）

## 目的

JavaScriptの構文エラー・実行時エラー・ロジックエラーを検出し、
原因・修正方法・改善案を初心者向けに説明できるか確認する。

確認ポイント

- 構文エラー
- DOM取得
- イベント処理
- nullエラー
- 条件分岐
- エラーハンドリング
- デバッグ能力

---

## HTML

```html
<!DOCTYPE html>
<html lang="ja">

<head>
    <meta charset="UTF-8">
    <title>JavaScript Debug</title>
</head>

<body>

<input
    id="name"
    type="text"
    placeholder="名前">

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

margin:40px;

}

button{

padding:10px;

}
```

---

## JavaScript

```javascript
const button = document.getElementById("btn");

button.addEventListener("click", () => {

const name = document.getElementById("username").value;

if(name=""){

result.innerHTML="名前を入力してください";

}else{

result.innerHTML="こんにちは"+name;

}

});
```

---

## このコードに意図的に入れているバグ

① id取得ミス

```javascript
document.getElementById("username")
```

↓

HTMLは

```html
id="name"
```

---

② if文

```javascript
if(name="")
```

↓

比較ではなく代入になっている

---

③ result取得なし

```javascript
result.innerHTML
```

↓

resultを取得していない

---

④ innerHTML

textContent推奨

---

⑤ テンプレートリテラル未使用

```javascript
"こんにちは"+name
```

↓

```
`こんにちは ${name}`
```

---

⑥ trim()なし

空白だけでも通ってしまう

---

## 質問

JavaScriptが動きません。

原因を特定し、

初心者にも分かるように

- 問題点
- 理由
- 修正方法

を説明してください。

さらに、

より良いJavaScriptになる改善案も教えてください。

---

## 期待する回答

### HTML

- id="name" を確認

---

### JavaScript

- usernameが存在しない
- if(name="")を指摘
- result取得漏れ
- textContent推奨
- trim()提案
- テンプレートリテラル推奨

---

### デバッグ

実行すると

```text
Cannot read properties of null
```

になる可能性を説明できる。

---

### 改善コード

修正版コードを提示する。

---

### 学習ポイント

- == と = の違い
- DOM取得
- nullとは何か
- textContent
- trim()

---

## 評価結果

### Version 1.0

構文エラー

□ 検出

実行時エラー

□ 検出

DOM取得

□ 検出

修正コード

□ 提示

初心者向け説明

□ 分かりやすい

総合評価

□ /100

## RAG導入後評価

判定：◎ 合格

### 確認結果

- HTMLとJavaScript間のID不一致を正しく検出できた
- username と name の不一致を特定できた
- if(name="") の代入演算子の誤りを検出できた
- result が未定義であることを検出できた
- 各問題について理由と修正方法を提示できた
- HTML・CSS・JavaScript間の整合性を横断的に評価できた
- 改善コードを提示できた
- 学習ポイントまで説明できた

### RAG評価

クロスチェック用ナレッジの考え方が回答に反映されており、
単体コードだけでなくHTMLとJavaScript間の参照関係を確認できている。

RAG導入の効果を確認できた。

### 補足

比較演算子について「== または ===」と説明しているが、
初心者向け教材としては原則 `===` を推奨する方が望ましい。

## Phase 6 System Prompt修正後 再評価

### 評価結果

**判定：◎ 合格**

System Promptの「レビューの優先順位」修正後にTEST05を再実行した。

### 確認結果

- HTMLの `id="name"` に対して、JavaScriptが `getElementById("username")` を参照している不一致を正しく検出した。
- `if(name="")` で比較演算子ではなく代入演算子 `=` を使用している問題を「🔴 必ず修正」と判定した。
- `result.innerHTML` を使用しているにもかかわらず、`result` が未定義である問題を「🔴 必ず修正」と判定した。
- HTML・CSS・JavaScriptの整合性についても確認できている。
- 修正コードでは、DOM参照、条件式、result取得が適切に修正されている。
- 不要な重大問題（🔴）の指摘は見られなかった。

### 注意点

`if(name="")` について、AIは「常にtrueになる」と説明したが、
厳密には `name = ""` の評価結果は空文字となるため、JavaScriptの条件式ではfalseとして評価される。

問題自体の検出と `===` への修正は正しいため、重大な評価ミスではないが、
説明精度上の軽微な課題として記録する。

### Phase 6での評価

TEST05では、実際に動作へ影響する問題を適切に「🔴 必ず修正」として検出できた。

TEST01で確認した「正常なコードを不要に🔴判定しない」改善と合わせると、

**重大問題の検出能力を維持しながら、🔴判定の精度が改善した**

と評価できる。