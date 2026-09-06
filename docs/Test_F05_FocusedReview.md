# TEST-F05：境界テスト / General Review

## テスト目的

具体的な修正要求がない場合に、
Focused ReviewではなくGeneral Reviewを選択できるか確認する。

Focused Review追加後も、
従来のGeneral Review機能が維持されているか確認する回帰テストでもある。

---

## HTML

```html
<section class="features">
    <div class="feature-card">
        <h2>HTML</h2>
        <p>HTMLの基本を学びます。</p>
    </div>

    <div class="feature-card">
        <h2>CSS</h2>
        <p>CSSでデザインを整えます。</p>
    </div>

    <div class="feature-card">
        <h2>JavaScript</h2>
        <p>JavaScriptで動きを追加します。</p>
    </div>
</section>
```

## CSS

```css
.features {
    display: flex;
    gap: 20px;
    width: 90%;
    margin: 40px auto;
}

.feature-card {
    flex: 1;
    padding: 20px;
    border: 1px solid #ccc;
    border-radius: 8px;
}
```

## JavaScript

```javascript
const cards = document.querySelectorAll(".feature-card");

cards.forEach((card) => {
    card.addEventListener("click", () => {
        console.log("カードがクリックされました");
    });
});
```

## 質問

このコードを改善したいです。
問題点を確認してください。

## 期待する動作

- General Reviewとして回答する
- コード全体を確認する
- HTML・CSS・JavaScriptを横断して確認する
- 必要に応じて 🔴 必ず修正 / 🟡 改善推奨 / 🟢 発展的な提案 に分類する
- HTML・CSS・JavaScriptの整合性を確認する
- 必要に応じて改善コードを提示する
- 学習ポイントを提示する
- Focused Reviewに誤分類しない


Before：5項目すべて○／General ReviewとしてPASS


### TEST-F05 After結果

評価：○○○○△

- General Reviewへ正しく分類された
- Focused Reviewへ誤分類されなかった
- 「総合評価」「良い点」「🔴必ず修正」「🟡改善推奨」が出力された
- 明確な動作不良がないため「🔴必ず修正」を無理に作らなかった
- HTML / CSS / JavaScript全体を確認できている
- アクセシビリティやUX改善をGeneral Reviewとして提案した

#### 確認された課題

General Reviewとして開始しているが、
後半に以下のFocused Review用見出しが混在した。

- 変更する場所
- 修正コード
- 変更内容の説明
- 必要な追加修正
- 注意点

Mode判定自体は成功しているが、
General / Focusedそれぞれの回答形式を
より明確に分離できる余地がある。

判定：条件付きPASS

### TEST-F05 After最終結果

Mode判定：PASS

- General Reviewへ正しく分類された
- 総合評価、良い点、🔴必ず修正、🟡改善推奨、🟢発展的提案を出力
- HTML / CSS / JavaScriptの整合性を確認
- 改善コードを提示
- Focused Reviewへの誤分類は発生しなかった

#### 既知の軽微課題

General Review後半に、
Focused Reviewで使用している以下の見出しが一部出力された。

- 変更内容の説明
- 必要な追加修正
- 注意点

回答内容およびMode判定には問題がないため、
現時点では許容する。

今後、回答フォーマットの厳格化が必要になった場合に
再検討する。

判定：PASS（軽微課題あり）