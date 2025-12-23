# ワークフロー命名規約

## ファイル名規則

`<category>-<purpose>[-version].json`

### カテゴリ

- `webhook`: Webhook トリガー
- `schedule`: スケジュール実行
- `manual`: 手動実行
- `email`: メールトリガー

### 例

- `webhook-slack-notification.json`
- `schedule-daily-report-v2.json`
- `manual-hello-world-test.json`
- `email-support-automation.json`

## タグ運用（ワークフローJSON内）

```json
{
  "tags": ["production", "mcp", "slack"]
}
```

### 推奨タグ

- `test`: テスト用
- `production`: 本番稼働
- `mcp`: MCP経由で作成
- `draft`: ドラフト

## ワークフロー構造

- 必須: `name`, `nodes`, `connections`
- 推奨: `tags`, `settings`, `pinData`

## Cloud UIからの取り込み時

- Export後は必ず `npm run format` 実行
- 命名規約を厳守（接頭辞 + 説明 + .json）
- 取り込みコミットメッセージに `"Import from Cloud:"` プレフィックス

