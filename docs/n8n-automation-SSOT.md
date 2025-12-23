# n8n-automation SSOT（Single Source of Truth）

このドキュメントは、n8n-automationプロジェクト全体の**唯一の信頼できる情報源**として機能します。

## 1. プロジェクト概要

- **プロジェクト名**: n8n-automation
- **目的**: n8nワークフローの自動化と管理
- **リポジトリ**: https://github.com/hadayalab-web/n8n-automation
- **実行環境**: n8n Cloud (https://hadayalab.app.n8n.cloud)

## 2. SSOT原則

### ドキュメント優先順位

本書（n8n-automation-SSOT.md）がプロジェクト全体の最高位ドキュメントです。

矛盾がある場合の優先順位：

1. **本書（n8n-automation-SSOT.md）** - プロジェクト全体方針
2. **n8n-cloud-sync.md** - 同期フロー詳細手順
3. **workflow-conventions.md** - 命名規約・コーディング規約

### GitHubがSSOT

- **GitHubが唯一の信頼できる情報源（Single Source of Truth）**
- すべての変更はGitHubを起点とする
- n8n Cloud UIは動作確認・モニタリング用途のみ

### SSOTの重要性

- ワークフローの真実の状態は常にGitHubリポジトリに存在
- n8n Cloudは実行環境であり、ソース管理ではない
- 変更の追跡・レビュー・ロールバックはすべてGitHubで実施

## 3. 開発環境

### 実装担当
- **Cursor**: ワークフロー作成・編集の実装ツール

### レビュー担当
- **GitHub Copilot**: コードレビュー・品質保証

### ツール連携
- **n8n-mcp**: GitHub ⇔ n8n Cloud同期ツール
  - 設定: `~/.cursor/mcp.json`
  - 参考: `.env.example`

## 4. ワークフロー管理運用

### 標準フロー（GitHub → n8n Cloud）

詳細は [n8n Cloud同期運用](./n8n-cloud-sync.md) を参照
※「標準フロー（GitHub→Cloud）」セクションを参照

1. Cursorでワークフロー編集
2. ローカル検証
   - `npm run format`（自動整形）
   - `npm run format:check`（確認）
3. GitHubへpush
4. GitHub Actions自動検証
   - ※push後、GitHub Actionsが自動実行されgreenになることを確認してから次のステップへ（推奨）
5. n8n-mcp経由でCloud反映
6. Cloud UIで動作確認

### 例外フロー（Cloud → GitHub取り込み）

詳細は [n8n Cloud同期運用](./n8n-cloud-sync.md) を参照
※「例外フロー（Cloud→GitHub取り込み）」セクションを参照

緊急時にCloud UIで編集した場合の手順:

1. Cloud UIで編集実施
2. 直後にExport（JSONダウンロード）
3. `workflows/`へ保存（命名規約準拠）
4. `npm run format`（自動整形）
5. GitHubへpush（取り込み）
6. 以降GitHubを正とする

### 命名規約

詳細は [ワークフロー命名規約](./workflow-conventions.md) を参照

- ファイル名規則: `<category>-<purpose>[-version].json`
- カテゴリ: `webhook`, `schedule`, `manual`, `email`
- タグ運用: `test`, `production`, `mcp`, `draft`

## 5. 品質保証

### GitHub Actions

- **ワークフローJSON検証**: Prettierフォーマットチェック
- **JSON構文検証**: jqによる構文検証
- **自動実行**: `workflows/**/*.json` 変更時に自動実行

### Prettier

- **差分可読性向上**: 一貫したフォーマットで差分を読みやすく
- **自動整形**: `npm run format` で自動整形
- **CI検証**: `npm run format:check` でCI検証

### レビュープロセス

1. **Cursor実装**: ワークフロー作成・編集
2. **Copilot先生レビュー**: コードレビュー・品質保証
3. **GitHub Actions**: 自動検証
4. **マージ**: レビュー通過後マージ

## 6. 重要な運用原則

### 同時編集禁止

- **同じワークフローをCloudとGitHub両方で同時編集禁止**
- 編集前に必ずGitHubの最新状態を確認
- 競合を防ぐため、編集権限を明確化

### UI編集後の取り込み

- **UI編集後は必ず取り込みコミット作成**
- Export → 整形 → push の手順を厳守
- 取り込みコミットメッセージに `"Import from Cloud:"` プレフィックス

### Credentials/Secrets管理

- **Credentials/Secretsは環境依存（JSON非含有）**
- JSONファイルには含まれない
- Import後、手動で設定が必要

### Import/Deployの違い

- **Import（UI）＝デプロイ**: n8n Cloud UIでの「Import」は上書き（デプロイ）
- **取り込み＝Export→GitHub push**: Cloud変更のGitHub反映は必ずExport→取り込み手順を実施

### Export JSONの特性

- Export時にメタデータ（updatedAt等）含有
- 差分が荒れるのは仕様
- Prettierで整形されるが、重要な変更のみに注目

## 7. ドキュメント構造

### 主要ドキュメント

- **README.md**: プロジェクト概要と運用方針
- **docs/n8n-automation-SSOT.md**: プロジェクト全体SSOT（このファイル）
- **docs/n8n-cloud-sync.md**: GitHub⇔n8n Cloud同期詳細
- **docs/workflow-conventions.md**: ワークフロー命名規約
- **docs/README.md**: ドキュメント一覧

### ドキュメントの役割

| ドキュメント | 役割 |
|------------|------|
| README.md | プロジェクトの入り口、概要とクイックスタート |
| n8n-automation-SSOT.md | プロジェクト全体の真実の唯一の情報源 |
| n8n-cloud-sync.md | 同期運用の詳細手順 |
| workflow-conventions.md | 命名規約と構造ルール |

## 8. 参照リンク

### 内部ドキュメント

- [n8n Cloud同期運用](./n8n-cloud-sync.md)
- [ワークフロー命名規約](./workflow-conventions.md)
- [ドキュメント一覧](./README.md)

### 外部リソース

- [n8n Cloud](https://hadayalab.app.n8n.cloud)
- [n8n-mcp](https://www.npmjs.com/package/n8n-mcp)
- [HadayaLab](https://github.com/hadayalab-web)

### 関連SSOT

- [汎用開発環境SSOT](../Cursor-Pro-GitHub-Copilot-Pro-最強開発環境-SSOT-v3.1.md)（参照先が存在する場合）

## 9. トラブルシューティング

### よくある問題

#### GitHub Actionsが失敗する

1. Prettierフォーマットエラー: `npm run format` で自動整形
2. JSON構文エラー: jqで構文検証
3. パス指定エラー: `workflows/**/*.json` パターンを確認

#### CloudとGitHubで不整合

1. GitHubの最新状態を確認
2. Cloud UIでExportして取り込み
3. 以降GitHubを正とする

#### ワークフローが動作しない

1. Cloud UIで有効化（Activate）確認
2. Credentials設定確認
3. Webhook URL確認

#### Activate状態の確認

- **症状**: ワークフローが実行されない
- **原因**: Import後にInactiveになっている
- **対処**: n8n Cloud UIでワークフローを開き、Activateボタンをクリック

#### Webhook URLの環境依存

- **注意**: Cloud固有のWebhook URLは再生成される
- **対応**: Import後にWebhook URLを確認・更新

## 10. 今後の運用

### 迷ったときは

1. **このSSOTドキュメントを最初に参照**
2. 関連ドキュメントを確認
3. GitHub Copilot先生にレビュー依頼

### 最短判断ツリー

#### Cloud UIで編集してしまった？

- **Yes** → 例外フロー実施（Export→整形→コミット）
- **No** → 標準フロー継続

#### GitHub Actions が red？

- **Fix first（修正が最優先）**
- **redのままCloudへ反映禁止**

#### Credentials関連？

- JSONには含まれない（環境依存）
- `.env` と Cloud UI で個別設定

#### 例外フローを常態化させない

- 緊急時のみ許可（P1障害、期限対応など）
- **原則は標準フロー**

### ドキュメント更新

- SSOT原則に基づき、このドキュメントを最新に保つ
- 運用方針変更時は必ずこのドキュメントを更新
- 更新後はGitHub Copilot先生にレビュー依頼

---

**最終更新**: 2025-12-23
**バージョン**: 1.0.0
**メンテナー**: HadayaLab

