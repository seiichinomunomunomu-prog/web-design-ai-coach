# TEST-F04：JavaScriptデバッグ / CrossCheck

## テスト目的

具体的なJavaScript不具合について、
HTMLとJavaScriptを横断して原因を特定できるか確認する。

また、Focused ReviewでもCrossCheck能力が維持されるか確認する。

---

## HTML

```html
<nav class="menu">
    <button id="menu-button">
        メニュー
    </button>

    <ul id="menu-list" class="menu-list">
        <li><a href="#">ホーム</a></li>
        <li><a href="#">サービス</a></li>
        <li><a href="#">お問い合わせ</a></li>
    </ul>
</nav>
```

## CSS

```css
.menu-list {
    display: none;
}

.menu-list.is-open {
    display: block;
}
```

## JavaScript

```javascript
const button = document.getElementById("menu-btn");
const menu = document.getElementById("menu-list");

button.addEventListener("click", () => {
    menu.classList.toggle("is-open");
});
```

## 質問

メニューボタンをクリックしてもメニューが開きません。
原因を特定して、必要な修正コードだけ提示してください。

## 仕込み

HTML：

`id="menu-button"`

JavaScript：

`getElementById("menu-btn")`

でIDを意図的に不一致にしている。

## 期待する動作

- Focused Reviewとして回答する
- HTMLとJavaScriptをCrossCheckする
- `menu-button` と `menu-btn` の不一致を原因として特定する
- JavaScriptの必要箇所だけを修正する
- 不要なHTML/CSS変更を行わない
- 無関係な全体レビューを行わない


### TEST-F04 Before結果

評価：○○○△△

- HTML / JavaScriptのCrossCheckに成功
- `menu-button` と `menu-btn` のID不一致を正確に特定
- 不具合原因を正しく説明
- JavaScriptの必要箇所だけを修正
- 不要なHTML/CSS変更は行っていない
- F01〜F03よりFocused Reviewに近い回答
- ただし「総合評価」「良い点」は具体的なデバッグ依頼では不要
- Focused化後も現在のCrossCheck能力を維持すること

### TEST-F04 After結果

評価：○○○○○

- Focused Reviewへ正しく切り替わった
- 「メニューが開かない」という不具合を正しく理解
- HTML / JavaScriptのCrossCheckに成功
- HTMLの `menu-button` とJavaScriptの `menu-btn` の不一致を正確に特定
- JavaScriptの必要箇所だけを修正
- HTML・CSSへの不要な変更なし
- `.is-open` とCSSの関係も確認できている
- General Review形式は出力されなかった
- Focused化後もCrossCheck能力が維持されている

判定：PASS