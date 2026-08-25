# HTML / CSS / JavaScript Cross Check Guide

## 目的

このガイドは、HTML、CSS、JavaScriptを個別に確認するだけでなく、
3つのコード間の関連性・整合性を確認するためのレビュー基準です。

コードが単体では正しく見えても、
HTML・CSS・JavaScript間の参照が一致していないことで
Webページが正しく動作しない場合があります。

レビューでは、各コードの構文確認に加えて、
必ずコード間の関連性も確認してください。


# 1. HTML ⇔ JavaScript

###IDの一致

JavaScriptでHTML要素を取得する場合、
指定しているIDがHTML側に存在するか確認します。

HTML

```html
<button id="submit">送信</button>

JavaScript
const button = document.getElementById("submit");
この場合、IDは一致しています。

###ID不一致の例

HTML

<button id="btn">送信</button>

JavaScript

const button = document.getElementById("button");

btnとbuttonが一致していないため、
JavaScriptは対象要素を取得できません。

この問題は動作に影響するため、
「必ず修正」として扱います。

DOM要素の存在確認

JavaScriptが参照している要素が
HTML側に存在するか確認します。

例：

const message = document.getElementById("message");

HTMLにid="message"の要素が存在しない場合、
正しくDOM要素を取得できません。

##2. HTML ⇔ CSS
class名の一致

HTMLで指定しているclassと
CSSセレクタが一致しているか確認します。

HTML

<h1 class="main-title">タイトル</h1>

CSS

.main-title {
    color: blue;
}

この場合は一致しています。

class名不一致の例

HTML

<h1 class="title">タイトル</h1>

CSS

.main-title {
    color: blue;
}

titleとmain-titleが一致していないため、
CSSは適用されません。

未使用セレクタ

CSSに定義されているclassやIDが
HTMLで使用されているか確認します。

ただし、JavaScriptによって動的に追加されるclassの可能性があるため、
HTMLだけを見て未使用と断定しないでください。

##3. CSS ⇔ JavaScript

JavaScriptでclassを追加・削除・切り替えている場合、
そのclassがCSS側に定義されているか確認します。

例：

element.classList.add("active");

CSS

.active {
    display: block;
}

JavaScriptで使用しているactiveが
CSSに存在するため整合しています。

##4. イベント対象の確認

JavaScriptでイベントを設定している要素が
HTML側に存在するか確認します。

button.addEventListener("click", function () {
    // 処理
});

この場合、button変数が正しいHTML要素を取得できているか確認します。

##5. 問題の優先順位

コード間の不整合を発見した場合、
以下の基準で分類します。

必ず修正
JavaScriptが対象DOMを取得できない
HTMLとJavaScriptのID不一致
HTMLとCSSのclass不一致によって必要なスタイルが適用されない
JavaScriptが存在しない要素を操作している
JavaScriptで使用するclassとCSS定義が一致していない
改善推奨
命名が分かりにくい
classやIDの命名規則が統一されていない
コードの可読性・保守性を下げる構造
発展的な提案
より再利用しやすい構造
JavaScriptの関数化
CSS設計の整理
コンポーネント化
##6. レビュー時の注意

問題を見つけるためだけに、
存在しない問題を作らないでください。

HTML・CSS・JavaScriptのいずれかに情報がない場合は、
推測で断定しないでください。

改善の必要がない部分については、
無理に改善案を提示しないでください。

「動作しない問題」と
「より良くするための改善」を明確に区別してください。


### このKnowledgeで特に重要なところ

単なる、

> 「HTMLのIDとJavaScriptのIDを合わせましょう」

だけではありません。

例えば、

```text
CSSに .active がある
HTMLには class="active" がない

        ↓

「未使用CSSだ！」 ← まだ断定しない

        ↓

JavaScript
classList.add("active")

        ↓

動的に使用しているので正常