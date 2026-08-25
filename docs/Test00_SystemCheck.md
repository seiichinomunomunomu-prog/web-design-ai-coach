# Test00 SystemCheck（システム動作確認）

## 目的

AIコーチの基本機能が正常に動作しているか確認する。

確認ポイント

- Web画面が表示される
- HTML・CSS・JavaScript入力欄が表示される
- 入力内容が保持される
- Dify APIと通信できる
- AI回答がWeb画面へ表示される
- Markdownが正しく表示される

---

## HTML

```html
<h1>Hello World</h1>
```

---

## CSS

```css
h1{
    color:red;
}
```

---

## JavaScript

```javascript
console.log("Hello World");
```

---

## 質問

このHTML・CSS・JavaScriptを初心者向けに添削してください。

---

## 期待する回答

### システム

- Web画面が表示される
- エラーが発生しない
- AI回答が表示される
- Markdownが崩れない

### HTML

- h1の改善提案

### CSS

- color指定についてコメント

### JavaScript

- console.logについてコメント

### 総合

- HTML・CSS・JavaScriptをそれぞれ添削
- 初心者向けの説明
- 改善案を提示

---

## 評価結果

### Version 1.0

画面表示

□ OK

Dify通信

□ OK

Markdown表示

□ OK

入力保持

□ OK

AI回答

□ OK

総合評価

□ /100

## RAG導入後評価

| 評価項目 | Test00結果 | 評価 |
|---|---|---|
| ① 問題検出 | 致命的な問題なしと判断 | ◎ |
| ② 誤検出 | 正常なコードを「必ず修正」にしていない | ◎ |
| ③ 必須/改善の分類 | セマンティクス、CSS整理、JS拡張を「改善提案」に分類 | ◎ |
| ④ コード間整合性 | HTML/CSSは関連、JSはHTML要素を直接操作していない点まで確認 | ◎ |
| ⑤ RAG利用 | Web Design AI Coach Knowledge の引用を確認 | ◎

### 総合評価

 5 / 5

### 評価コメント

「問題なし → 必須修正なし → 改善案を提示」という適切な判断ができている。

HTML・CSS・JavaScriptの整合性についても確認しており、
JavaScriptが現在HTML要素を直接操作していないことを認識できている。

RAG導入後のTest00として良好な結果。