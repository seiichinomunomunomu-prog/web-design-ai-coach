# Development Plan

## 完了

- [x] FastAPI環境構築
- [x] Dify API接続
- [x] Markdown表示
- [x] HTML添削
- [x] CSS添削
- [x] JavaScript添削
- [x] レイアウト改善
- [x] テストセット作成

---

## 開発中

- [ ] Dify System Prompt Version1.0
- [ ] Dify Knowledge作成

---

## 次回予定

- [ ] AI添削品質改善
- [ ] Copyボタン追加
- [ ] AI添削中表示
- [ ] ボタン二重押し防止

---

## 将来

- [ ] React対応
- [ ] Vue対応
- [ ] ダークモード
- [ ] 履歴保存
- [ ] ログイン機能

# DEVELOPMENT PLAN

## 現在地

### Phase 1
基本Web画面

完了

### Phase 2
FastAPIによるHTML/CSS/JavaScript受付

完了

### Phase 3
Dify API連携

完了

### Phase 4
AIレビュー画面

完了

### Phase 5
RAG導入

完了

- ナレッジベース作成
- CrossCheck Guide登録
- Knowledge Retrieval設定
- LLM Context接続
- TEST00〜06再評価


---

# 次期開発

## Phase 6
総合レビュー品質の安定化

### 目的

ユーザーが詳細な評価項目を指定しなくても、

「このWebサイト全体をレビューしてください」

という自然な質問から、
AI Coach自身が必要な評価観点を判断できるようにする。


### 評価候補

- HTML
- CSS
- JavaScript
- CrossCheck
- UX
- Performance
- Security
- Accessibility
- 保守性


### 重要方針

すべての項目について無理に問題を作らない。

問題がある場合
→ 問題・理由・修正方法を提示

問題がない場合
→ 問題なし、または良い点として評価

コードから判断できない場合
→ 判断できないことを明示


---

## Phase 6-1
総合レビュー基準の整理

TEST06の期待回答を、
AI Coach用の総合レビュー基準として整理する。

検討対象：

- System Promptに入れる内容
- RAG Knowledgeに入れる内容
- 両方に入れるべき内容

役割を整理してから実装する。


---

## Phase 6-2
出力形式の安定化

回答を以下の優先順位で整理する。

1. 必ず修正
2. 改善推奨
3. 発展的な提案

必要に応じて、

- 改善コード
- 学習ポイント
- 総合評価

を表示する。


---

## Phase 6-3
総合スコア

100点満点評価の導入を検討。

例：

品質：88 / 100

ただし、単なるLLMの感覚的な点数にならないよう、
採点基準を先に定義する。

候補：

HTML
CSS
JavaScript
CrossCheck
UX
Performance
Security
Accessibility
保守性


---

## Phase 6-4
RAG精度評価

ナレッジが実際に検索されたかを
Difyログの「引用」で確認する。

必要に応じて、

- チャンク
- 検索設定
- ナレッジ内容

を調整する。


---

## Phase 7
Web Design AI Coachの実用化

候補：

- レビュー履歴保存
- Before / After比較
- 学習履歴
- レビュー結果エクスポート
- UI改善
- Render等への公開

### Review Mode v1.0 外部公開

Review Modeの基本機能とRAG評価が完了した段階で、
ローカル環境から外部公開環境へ移行する。

公開先候補：

- Render

実施項目：

- [ ] GitHubリポジトリの整理
- [ ] READMEの更新
- [ ] requirements.txtの確認
- [ ] .gitignoreの確認
- [ ] .envがGitHubへ公開されないことを確認
- [ ] Dify API Keyの環境変数化を確認
- [ ] Render Web Service作成
- [ ] GitHubリポジトリとRenderを接続
- [ ] Render側へ環境変数を設定
- [ ] FastAPI / Uvicorn起動設定
- [ ] 外部URLからReview Modeを起動
- [ ] HTML / CSS / JavaScript入力確認
- [ ] Dify API接続確認
- [ ] RAGを使用したAI添削確認
- [ ] スマートフォン表示確認

### 公開後テスト

ローカル環境だけでなく、
Render公開環境でもTEST00〜TEST06の主要テストを実施する。

最低限、

- TEST00：正常系
- TEST02：初心者ミス
- TEST04：CrossCheck
- TEST06：総合レビュー

を再確認する。

### 外部公開のゴール

第三者がブラウザからアクセスし、

HTML / CSS / JavaScript入力
↓
AI添削
↓
RAGによるレビュー
↓
結果表示

まで利用できる状態を
Review Mode v1.0の公開版とする。

### System Prompt改善① 結果

TEST01 / TEST06で再評価を実施。

結果：

- TEST01：成功
- TEST06：概ね成功
- 正常コードへの過剰な🔴判定が減少
- DOMContentLoadedの一律推奨が抑制された
- CrossCheck能力は維持
- RAG参照能力も維持
- 軽微な過剰提案は残る

結論：

System Promptの「レビュー優先順位」修正は有効。

現時点では追加修正を行わず、
現在のPromptを基準版として次の検証へ進む。

## Phase 6 完了評価

System Promptの「レビュー優先順位」を修正し、
TEST01〜TEST06による再評価を実施した。

### 確認できた改善

- 正常コードへの過剰な🔴判定を抑制
- 明確な重大問題の🔴判定を維持
- HTML・CSS・JavaScriptのCrossCheck能力を維持
- RAG利用能力を維持
- 改善推奨・発展提案の分類精度が向上

### 残課題

- aria-labelの過剰提案
- 一部問題で🔴 / 🟡の境界に揺れがある
- 一部の理由説明に技術的な精度改善余地がある
- 総合レビュー時の評価軸・100点評価は今後検討

### Phase 6 総合判定

**Phase 6 System Prompt改善：成功**

現在のSystem Promptを

**Review Mode v1.0 基準Prompt**

としてFIXする。

今後の実環境評価やKnowledge改善の結果に応じて、
Review Mode v1.1以降で改善する。

---

## 次フェーズ

### Phase 7：実用化

- Review Mode v1.0を基準として実環境で動作確認
- Renderへ公開
- 公開環境でのレビュー品質確認
- UI / UXの改善
- エラー処理
- 実利用を想定した追加評価

### 将来拡張

Review Modeの実用化後、

**Create Mode（構想 → HTML / CSS / JavaScript生成）**

の開発へ進む。

### 公開後確認③：全コード未入力時の挙動

#### 実施内容

HTML・CSS・JavaScriptをすべて空欄にし、
質問欄のみ入力してAI添削を実行した。

#### 結果

Dify APIまで正常にリクエストされ、
AIから

「コードが提示されていないためレビューできない」

という適切な回答が返った。

#### 判定

**機能上はPASS。ただし改善対象あり。**

#### 改善課題

コードがすべて未入力の場合は、
Dify APIを呼び出す前にFastAPI側で入力チェックを行い、

「レビューするコードを入力してください」

と画面に表示する方が望ましい。

これにより、

- 不要なAPI呼び出しを削減
- 応答時間を短縮
- ユーザーにより直接的な案内を表示

できる。

#### 対応方針

公開後確認を一巡した後、
Phase 7の改善項目としてまとめて対応する。

### 公開後確認④：別ブラウザ・別端末

#### 結果

以下の環境から公開URLへのアクセスを確認。

- Firefox：OK
- Chrome：OK
- スマートフォン Safari：OK

#### 判定

**PASS**

複数ブラウザ・別端末から公開Webアプリへ正常にアクセスできることを確認した。

### 公開後確認⑤：Render Free環境のスリープ復帰

#### 状態

未確認（保留）

#### 確認方法

一定時間アクセスしない状態を作り、
その後公開URLへアクセスする。

#### 確認ポイント

- 初回表示に通常より時間がかかるか
- 待機後に正常表示されるか
- AI添削が正常に実行できるか

Freeプランの仕様による起動遅延と、
アプリ障害を混同しないこと。

### 公開後確認⑥：Renderログ確認

#### 確認結果

- GET / → 200 OK
- POST /review → 200 OK
- style.css → 304 Not Modified（正常なキャッシュ動作）
- DIFY STATUS → 200
- Render上のFastAPIからDify APIへの接続成功
- WebアプリからAI添削まで正常動作

#### 判定

**PASS**

#### 改善課題

現在デバッグ目的で
`DIFY RESPONSE` の内容をRenderログへ出力している。

正式運用前に、回答全文をログへ出力する
`print("DIFY RESPONSE:", response.text)`
を削除または無効化する。

## Phase 7 公開後確認⑦：Review Mode v1.0 公開版 最終判定

### 総合結果

RenderへReview Mode v1.0をデプロイし、
公開環境で動作確認を実施した。

### 確認済み

- 公開URLから正常アクセス
- HTML / CSS / JavaScript入力画面の表示
- Dify APIとの接続
- AI添削結果の正常表示
- RAGを利用したレビュー
- 部分入力レビュー
- GitHub push → Render Auto-Deploy
- Firefox / Chrome / Safariからのアクセス
- Renderログ上でGET / POST /review 200 OK確認
- DIFY STATUS 200確認

### 公開後に発見・修正した問題

HTMLまたはCSSを空欄にすると
FastAPIのForm必須チェックにより
`Field required` が発生した。

対応：

`Form(...)`

から

`Form("")`

へ変更し、
HTML / CSS / JavaScriptを個別に任意入力可能とした。

GitHubへpush後、
Render Auto-Deployで自動反映され、
再テストで正常動作を確認した。

### 残課題

- 全コード未入力時のFastAPI側入力チェック
- DIFY RESPONSE全文のログ出力停止
- Render Free環境のスリープ復帰確認
- 必要に応じたスマートフォンUI改善

### 最終判定

**Review Mode v1.0 公開版：合格**

主要機能は本番環境で正常動作しており、
第三者がブラウザから利用できる状態になった。

残課題はv1.0公開を妨げる重大問題ではなく、
今後の改善項目として管理する。

## Phase 7：Render公開・公開後確認

### Status

**COMPLETED - Review Mode v1.0 公開版**

### 完了内容

- GitHubリポジトリ作成
- ローカルGitとの接続
- GitHubへのpush
- Render Web Service作成
- GitHub / Render連携
- DIFY_API_KEYのEnvironment Variables設定
- FastAPIアプリ公開
- 公開URL動作確認
- AI添削動作確認
- 部分入力レビュー確認
- 公開後不具合修正
- Render Auto-Deploy確認
- Firefox / Chrome / Safari確認
- Renderログ確認
- Dify API接続確認

### 公開版

Review Mode v1.0

### 最終判定

**PASS**

主要機能はRender本番環境で正常動作しており、
インターネット経由で利用できる状態になった。

### 継続課題

- [ ] 全コード未入力時のFastAPI側バリデーション
- [ ] DIFY RESPONSE全文ログ出力停止
- [ ] Render Freeスリープ復帰確認
- [ ] スマートフォンUIの必要に応じた改善

### 次Phase

Phase 8へ進む。

Phase 7で公開基盤が完成したため、
今後はReview Mode v1.0を基準として機能改善・拡張を進める。