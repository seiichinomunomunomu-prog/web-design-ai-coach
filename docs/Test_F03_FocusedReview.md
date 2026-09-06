# TEST-F03：レスポンシブ修正

## テスト目的

正常に動作しているPC用レイアウトを維持したまま、
指定されたスマホ表示だけを変更できるか確認する。

---

## HTML

```html
<section class="card-list">
    <article class="card">
        <h2>HTML</h2>
        <p>HTMLの基本を学習します。</p>
    </article>

    <article class="card">
        <h2>CSS</h2>
        <p>CSSでレイアウトやデザインを整えます。</p>
    </article>

    <article class="card">
        <h2>JavaScript</h2>
        <p>JavaScriptで動きを追加します。</p>
    </article>
</section>
```

## CSS

```css
.card-list {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 20px;
    width: 90%;
    margin: 40px auto;
}

.card {
    padding: 20px;
    border: 1px solid #ccc;
    border-radius: 8px;
}

.card h2 {
    margin-top: 0;
}
```

## JavaScript

なし

## 質問

PCでは現在の3列表示をそのまま残して、
スマホではカードを1列表示にしたいです。
必要なCSSだけ教えてください。

## 期待する動作

- Focused Reviewとして回答する
- PCの3列表示は変更しない
- スマホ用のメディアクエリを提示する
- `.card-list` の `grid-template-columns` をスマホ時だけ変更する
- 必要なCSSだけを提示する
- 無関係なHTMLやCSSを書き換えない


### TEST-F03 Before結果

評価：○○○××

- PC 3列維持／スマホ1列という要求を正しく理解
- .card-list を正しく特定
- @media を使った必要最小限のCSSを提示
- PC側の既存CSSを不要に変更していない
- ただし「必要なCSSだけ」という要求にもかかわらず
  General Review形式で回答
- 技術回答ではなく回答フォーマット制御が課題

### TEST-F03 After結果

評価：○○○○○

- Focused Reviewへ正しく切り替わった
- PCの3列表示を維持する要求を正しく理解
- `.card-list` を修正対象として正しく特定
- `@media (max-width: 768px)` を追加
- スマホ時のみ `grid-template-columns: 1fr` に変更
- PC用の既存CSSは変更していない
- HTML・JavaScriptへの不要な変更なし
- General Review形式は出力されなかった
- 最小変更の原則が機能している

判定：PASS

---

## TEST-F03 最終評価

### 検証結果

System Prompt変更後、
「PCでは現在の3列表示を維持し、
スマホでは1列表示にしたい」という
具体的なレスポンシブ変更要求に対して、
Focused Reviewへ正しく切り替わることを確認した。

また、既存のPC用CSSを変更せず、
スマートフォン表示に必要なmedia queryだけを
追加する最小限の修正を提示できていた。

### Before / After

| 項目 | Before | After |
|---|---|---|
| Focused Reviewへの切り替え | × | ○ |
| 修正対象の特定 | ○ | ○ |
| 修正コードの適切さ | ○ | ○ |
| 既存PC表示の維持 | ○ | ○ |
| 回答範囲の適切さ | × | ○ |

### 確認できたこと

- `.card-list`を主な修正対象として正しく特定できた
- PCの既存3列表示を変更しなかった
- スマートフォン用のmedia queryを追加する方法を提示できた
- スマートフォン時のみ`grid-template-columns: 1fr`へ変更できた
- HTMLを不要に変更しなかった
- 既存の`.card`等のCSSを不要に変更しなかった
- General Reviewの「総合評価」「良い点」等を出力しなかった
- 「必要なCSSだけ」というユーザーの要求に回答を集中できた

### 修正方法の確認

Afterでは、中心となる修正として以下のような
スマートフォン用CSSが提示された。

```css
@media (max-width: 768px) {
    .card-list {
        grid-template-columns: 1fr;
    }
}