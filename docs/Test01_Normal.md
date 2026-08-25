# Test01 Normal（基本動作確認）

## 目的

正常なコードを入力し、AIが適切な改善提案を返すことを確認する。

---

## HTML

```html
<!DOCTYPE html>
<html lang="ja">
<head>
    <meta charset="UTF-8">
    <title>Sample</title>
</head>
<body>

<h1 id="title">Hello World</h1>

<button id="btn">クリック</button>

<p id="message"></p>

</body>
</html>
```

---

## CSS

```css
body{
    font-family: Arial, sans-serif;
    text-align:center;
    margin-top:40px;
}

h1{
    color:blue;
}
```

---

## JavaScript

```javascript
const button = document.getElementById("btn");
const message = document.getElementById("message");

button.addEventListener("click", function () {
    message.textContent = "こんにちは！";
});
```

---

## 質問

HTML・CSS・JavaScriptを総合的に添削してください。
初心者向けに改善点を説明してください。

---

## 期待する回答

- HTML改善
- CSS改善
- JavaScript改善
- より良い書き方

## RAG導入後評価

| 評価項目 | Test01結果 | 評価 |
|---|---|---|
| ① 問題検出 | 基本動作に重大な問題はないことを認識しつつ、アクセシビリティ上の改善点を検出 | ◎ |
| ② 誤検出 | HTML・CSS・JavaScriptの正常なID参照や基本構造を問題扱いしていない | ◎ |
| ③ 必須/改善の分類 | aria-labelを「必ず修正」、CSS・メッセージ表示・関数化等を「改善推奨/発展的提案」に分類 | ○ |
| ④ コード間整合性 | HTMLのid="btn"とJavaScriptのgetElementById("btn")の一致、message要素との関係を確認 | ◎ |
| ⑤ RAG利用 | Cross Check Guideの考え方に沿ってHTML・CSS・JavaScript間の参照関係を確認できている | ◎

### 総合評価

4.5 / 5

### 評価コメント

HTML・CSS・JavaScriptが基本的に正常に連携していることを正しく判断できている。

特にHTMLのIDとJavaScriptのgetElementById()の参照関係を確認しており、
RAG導入の目的である「コード単体だけではなくコード間の整合性を確認する」
というレビューが機能している。

また、CSS改善、メッセージ表示、JavaScriptの関数化などを
改善推奨・発展的提案として分離できており、初心者向けAIコーチとして
学習につながる提案になっている。

一方、aria-labelを「必ず修正」とした点についてはやや厳しい判定。
今回のボタンには表示テキストが存在するため、
必ずしもaria-labelが必須とは限らない。

そのため、重要度分類については今後の改善候補として記録する。

### Test01で確認できたRAG効果

- HTML ⇔ JavaScript のID一致確認：成功
- DOM要素の存在確認：成功
- HTML・CSS・JavaScript横断チェック：成功
- 正常コードの誤検出抑制：概ね成功
- 問題の重要度分類：改善余地あり


## Phase 6 System Prompt修正後
2026.08.17

### 結果

🔴 必ず修正：
「特に大きな問題は見当たりません」と判定。

以前はaria-label追加を必須修正として扱っていたが、
System Prompt修正後は必須修正から除外された。

### 改善確認

- 正常コードを無理に「必ず修正」と判定しなくなった
- 必須修正と改善提案の区別が改善した
- System Promptの優先順位ルール変更の効果を確認

### 残課題

可視テキストを持つbuttonに対して、
aria-label追加を「改善推奨」として提案している。

必須修正ではなくなったため大きく改善したが、
不要なアクセシビリティ提案をさらに抑制できる余地がある。

### 判定

Phase 6-1：成功
軽微な過剰提案あり