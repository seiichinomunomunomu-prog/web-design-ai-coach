# Prompt History

## Version 1.0

### 目的
WEB Design AI Coachとしての基本的な添削方針を定義。

### 主な設定
- 初心者～中級者向け
- HTML / CSS / JavaScriptを対象
- 3言語の横断チェック
- エラーを優先して指摘
- 修正理由を説明
- 改善コードを提示
- 学習ポイントを提示

### Knowledge
未使用

### 備考
System Prompt単体の効果を確認する初期バージョン。

## Version 1.1

### 変更理由

Test02 / Test04で、可視テキストを持つボタンに
aria-labelを追加する提案が繰り返し発生した。

### 変更内容

- 改善点がない項目は無理に提案しない
- UX・アクセシビリティは明確な改善効果がある場合のみ提案
- 十分なアクセシブルネームを持つ要素への
  不要なaria-label追加を推奨しない

### Test結果

Test02：主要問題をすべて検出
Test04：HTML / CSS / JavaScript間の不整合を検出

System Prompt v1.0により、
問題の優先順位と回答構成は大きく改善した。

### 再テスト結果

Test02を再実行。

- 主要3問題の検出能力を維持
- 必須修正 / 改善推奨 / 発展提案の分類を維持
- HTML / CSS / JavaScript横断チェックを維持
- 不要なaria-label提案が解消

→ System Prompt v1.1を採用。