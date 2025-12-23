# n8n Cloud同期運用

## 概要

このリポジトリは **n8n Cloud** (https://hadayalab.app.n8n.cloud) の
ワークフローSSOT（Single Source of Truth）です。

## 環境構成

- **実行環境**: n8n Cloud
- **開発ツール**: Cursor + n8n-mcp
- **バージョン管理**: GitHub

## 運用方針

- **パターン1（GitHub→Cloud一方向）を採用**
- **GitHubが唯一の信頼できる情報源（SSOT）**
- **n8n Cloud UIは動作確認・モニタリング用途**

## 標準フロー（GitHub→Cloud）

1. Cursorでワークフロー編集
2. ローカル検証（`npm run format:check`）
3. GitHubへpush
4. GitHub Actions自動検証
5. n8n-mcp経由でCloud反映
6. Cloud UIで動作確認

## 例外フロー（Cloud→GitHub取り込み）

緊急時にCloud UIで編集した場合の手順:

1. Cloud UIで編集実施
2. 直後にExport（JSONダウンロード）
3. `workflows/`へ保存（命名規約準拠）
4. `npm run format`（自動整形）
5. GitHubへpush（取り込み）
6. 以降GitHubを正とする

## 重要な注意事項

- **同じワークフローをCloudとGitHub両方で同時編集禁止**
- **UI編集後は必ず取り込みコミット作成**
- **Credentials/Secretsは環境依存（JSON非含有）**

## なぜGitHub Actionsが必要か

- CloudからのExport JSONはフォーマット揺れあり
- 壊れたJSONがSSOTに混入するのを防止
- Prettierで差分を読みやすく保持

## Import時の注意事項

- **上書き vs 新規**: n8n Cloud UIでImportする際、既存ワークフローを上書きするか、新規作成するかを選択できます
- **有効化状態**: Importされたワークフローはデフォルトで無効（Inactive）状態です。必要に応じてActivateしてください
- **資格情報（Credentials）**: JSONに含まれません。Import後、手動で設定が必要です
- **Webhook URL**: n8n Cloud固有のURLが自動生成されます

## セットアップ

### Cursor MCP設定

`~/.cursor/mcp.json`:
```json
{
  "mcpServers": {
    "n8n": {
      "command": "n8n-mcp",
      "args": [],
      "env": {
        "N8N_API_URL": "https://hadayalab.app.n8n.cloud",
        "N8N_API_KEY": "your_api_key"
      }
    }
  }
}
```

参考: `.env.example`

