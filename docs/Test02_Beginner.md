# Test02 Beginner（初心者がよくやるミス）

## 目的

初心者がよく起こすHTML・CSS・JavaScriptのミスをAIが正しく検出できるか確認する。

確認ポイント

- HTMLとJavaScriptの関連性
- CSSのスペルミス
- インデント
- innerHTMLの使用
- 初心者向け説明

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

<h1>こんにちは</h1>

<button id="btn">送信</button>

<p id="message"></p>

</body>

</html>
```

---

## CSS

```css
h1{

cplor:red;

}
```

---

## JavaScript

```javascript
const button=document.getElementById("button");

button.addEventListener("click",function(){

message.innerHTML="こんにちは";

});
```

---

## 質問



初心者にも分かるように、

- 問題点
- 理由
- 修正方法

を説明してください。

---

## 期待する回答

### HTML

- HTMLとJavaScriptのID不一致を指摘
- HTML構造の改善提案
HTML・CSS・JavaScriptを総合的に添削してください。
### CSS

- cplor → color を指摘

### JavaScript

- getElementById("button") を指摘
- textContent推奨
- インデント改善

### 総合

- HTML・CSS・JavaScriptを関連付けて説明
- 優先順位を付けて説明

## 評価結果(13/Aug/2026)

### Before System Prompt v1.0

- [x] HTMLとJavaScriptのID不一致を検出
- [x] CSSの cplor → color を検出
- [x] messageのDOM取得漏れを検出
- [x] 修正コードを提示
- [x] 初心者向けに理由を説明

### コメント

System Prompt設定前でも主要な問題を正しく検出。
基本的なコード添削能力は高い。

今後は、問題の優先順位、
HTML・CSS・JavaScriptの横断チェック、
学習ポイントなどの回答安定性を確認する。

### After System Prompt v1.0
(13/Aug/2026)

- [x] HTMLとJavaScriptのID不一致を検出
- [x] CSSの cplor → color を検出
- [x] messageのDOM取得漏れを検出
- [x] 必須修正と改善提案を区別
- [x] HTML・CSS・JavaScriptの整合性を説明
- [x] 修正コードを提示
- [x] 学習ポイントを提示

### Beforeとの比較

問題検出能力はBeforeでも高かった。

System Prompt v1.0追加後は、
回答の優先順位・構成・初心者向け説明が大きく改善した。

### 今後の確認事項

アクセシビリティ改善としてaria-labelを提案したが、
可視テキストがあるボタンでは必須ではない。

不要な改善提案を抑制できるか今後確認する。

## RAG導入後評価

| 評価項目 | Test02結果 | 評価 |
|---|---|---|
| ① 問題検出 | JavaScriptのID不一致、CSS構文エラー、message要素の未定義をすべて検出 | ◎ |
| ② 誤検出 | 正常なHTML構造やh1などを誤って問題扱いしていない | ◎ |
| ③ 必須/改善の分類 | 動作・表示に直接影響する3問題を「必ず修正」に分類 | ◎ |
| ④ コード間整合性 | HTML ⇔ JavaScriptのID参照、DOM要素の存在、CSS適用を横断確認 | ◎ |
| ⑤ RAG利用 | Cross Check Guideの主要チェック項目に沿った判断ができている | ◎  |

### 総合評価

4.5 / 5
※DifyログでKnowledge引用確認後、5 / 5に確定可能。

### 検出できた問題

#### 1. JavaScriptのID不一致

HTML：

button id="btn"

JavaScript：

document.getElementById("button")

この不一致を正しく検出し、
JavaScript側を "btn" に修正する提案ができている。

#### 2. CSSの構文エラー

誤：

color:red;

ではなく、今回入力された誤ったプロパティ名を検出し、
正しい `color` への修正を提案できている。

CSS単体の構文確認も正常に機能している。

#### 3. message要素の未定義

JavaScript：

message.innerHTML = "こんにちは";

に対して、message変数が定義されていないことを検出。

さらに、

document.getElementById("message")

によってHTML側の要素を取得する必要があることまで提案できている。

### コード間整合性評価

今回特に重要なのは、

HTML
↓
JavaScriptのID参照
↓
DOM要素取得
↓
イベント処理

というコード間の関係を確認できたこと。

単純なHTML・CSS・JavaScriptの個別チェックではなく、
RAG導入の目的である「コード間のCross Check」が機能している。

### 改善提案について

変数名の可読性やアクセシビリティなどを
「改善推奨」として必須修正から分離できている。

Test01ではaria-labelを「必ず修正」としていたが、
Test02では「改善推奨」に分類されている。

この分類の方が適切であり、Test01で確認された
重要度判定の揺れについては引き続き観察する。

### Test02で確認できたRAG効果

- HTML ⇔ JavaScript ID一致確認：成功
- DOM要素存在確認：成功
- CSS構文チェック：成功
- 複数問題の同時検出：成功
- 必須修正と改善提案の分離：成功
- HTML・CSS・JavaScript横断チェック：成功

---

## Phase 6 System Prompt改善後 再評価

### 実施内容

レビュー優先順位に関するSystem Promptを修正し、
同一のTEST02コードで再評価を実施した。

今回の目的は、正常コードへの過剰な🔴判定を抑制した結果、
本当に修正が必要な問題まで🔴判定されなくなっていないかを確認すること。

### 確認結果

#### 🔴 必ず修正

以下の明確な問題を「必ず修正」として検出した。

1. JavaScriptのDOM取得ID不一致

HTML：

`id="btn"`

JavaScript：

`document.getElementById("button")`

HTMLとJavaScriptのIDが一致していないため、
ボタンを正しく取得できない問題を検出した。

2. CSSプロパティ名の誤り

`cplor:red;`

を誤りとして検出し、

`color:red;`

への修正を提示した。

### 改善推奨

JavaScriptで使用している `message` について、
明示的なDOM取得が必要であることを指摘した。

`const message = document.getElementById("message");`

という適切な改善コードも提示された。

ただし、この問題はコードの安定した動作に関係するため、
「🟡改善推奨」ではなく
「🔴必ず修正」と判定してもよい内容と考えられる。

### CrossCheck確認

HTML・CSS・JavaScriptを個別に確認するだけでなく、

- HTMLのidとJavaScriptのDOM取得
- CSSプロパティの有効性
- JavaScriptが参照するHTML要素

について横断的に確認できている。

特に `btn` と `button` のID不一致を検出できたことから、
CrossCheck機能は維持されていると判断する。

### 改善確認

- 正常コードへの過剰な🔴判定を抑制しながら、実際の重大問題は🔴として検出できた
- ID不一致を正しく検出できた
- CSSの構文上の問題を正しく検出できた
- 修正コードまで正しく提示できた
- HTML・CSS・JavaScriptの横断チェック能力を維持できた

### 残課題

`message` のDOM取得不足について、
問題自体は正しく認識しているが、
優先順位が「🟡改善推奨」となった。

問題検出能力ではなく、
🔴必ず修正と🟡改善推奨の境界について
さらに評価する余地がある。

### 判定

**Phase 6 System Prompt改善：成功**

正常なコードでは無理に🔴を作らず、
実際に動作へ影響する問題が存在する場合には
🔴必ず修正として検出できることを確認した。

TEST01とTEST02の比較から、

- 正常系 → 🔴を作らない
- 異常系 → 必要な🔴を検出する

という優先順位判定が機能していることを確認した。