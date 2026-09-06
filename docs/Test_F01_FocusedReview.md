# TEST-F01：画像とテキストを横並び

## テスト目的

具体的なレイアウト変更要求に対して、
General ReviewではなくFocused Reviewとして回答できるか確認する。

また、目的達成に必要な範囲だけコードを修正できるか確認する。

---

## HTML

```html
<section class="profile">
    <img src="profile.jpg" alt="プロフィール画像">

    <div class="profile-text">
        <h2>プロフィール</h2>
        <p>Webデザインを勉強しています。</p>
    </div>
</section>
```

## CSS

```css
.profile {
    width: 80%;
    margin: 40px auto;
    padding: 20px;
    border: 1px solid #ccc;
}

.profile img {
    width: 250px;
    height: auto;
}

.profile-text {
    margin-top: 20px;
}
```

## JavaScript

なし

## 質問

現在の縦並びになっている画像とテキストの組み合わせを、
画像を左、テキストを右の横並びにしたいです。
どこを修正すればよいですか？

## 期待する動作

- Focused Reviewとして回答する
- `.profile` を主な修正対象として特定する
- `display: flex` などを使った横並びコードを提示する
- 必要に応じて既存の余白を調整する
- HTMLに変更が不要なら、その旨を示す
- 無関係な全体レビューを行わない


Before：○○○△△、技術回答は適切だがGeneral Review形式が冗長

### TEST-F01 After結果

評価：○○○○○

- Focused Reviewへ正しく切り替わった
- General Reviewの「総合評価」「良い点」等は出力されなかった
- `.profile` を修正対象として正しく特定
- `display: flex` 等の具体的な修正コードを提示
- `.profile-text` の既存marginも適切に調整
- HTMLは変更不要と判断
- 修正理由も初心者向けに説明
- 回答がユーザーの具体的な要求に集中している

判定：PASS

---

## TEST-F01 最終評価

### 検証結果

System Prompt変更後、
具体的なレイアウト変更要求に対して
Focused Reviewへ正しく切り替わることを確認した。

また、回答範囲を質問内容に限定しながら、
目的達成に必要なHTML / CSSの関係を確認できていた。

### Before / After

| 項目 | Before | After |
|---|---|---|
| Focused Reviewへの切り替え | △ | ○ |
| 修正対象の特定 | ○ | ○ |
| 修正コードの適切さ | ○ | ○ |
| 不要な変更の抑制 | ○ | ○ |
| 回答範囲の適切さ | △ | ○ |

### 確認できたこと

- `.profile`を主な修正対象として正しく特定できた
- `display: flex`を使用した横並び方法を提示できた
- `.profile-text`の既存marginも関連箇所として確認できた
- HTMLに変更が不要であることを判断できた
- General Reviewの「総合評価」「良い点」等を出力しなかった
- ユーザーが質問したレイアウト変更に回答を集中できた
- 必要な修正理由を初心者向けに説明できた

### 結論

Beforeでは技術的な回答は適切だったが、
General Review形式による回答の冗長さが残っていた。

Afterでは技術的な回答能力を維持したまま、
回答形式がFocused Reviewへ改善された。

これにより、

**「具体的な変更要求に対して、必要な範囲だけをレビューする」**

というFocused Reviewの目的を達成できた。

**最終判定：PASS**