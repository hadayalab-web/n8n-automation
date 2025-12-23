# n8n Cloud同期運用

## 概要

このリポジトリは **n8n Cloud** (https://hadayalab.app.n8n.cloud) の
ワークフローSSOT（Single Source of Truth）です。

## 環境構成

- **実行環境**: n8n Cloud
- **開発ツール**: Cursor + n8n-mcp
- **バージョン管理**: GitHub

## 運用フロー

### Phase 1: 手動同期（現在）

1. **作成**: Cursor + n8n-mcp でワークフロー作成
   - Cursorでワークフローを作成・編集
   - `workflows/*.json` として保存

2. **検証**: GitHub Actions（自動）
   - `npm run format` # ローカル整形
   - `npm run format:check` # CI検証

3. **同期**: n8n Cloud UI で手動Import
   - Workflows → Import from File
   - `workflows/*.json` を選択

### Phase 2: 自動同期（計画中）

- `main` マージ時、GitHub Actionsで自動デプロイ
- n8n Cloud API経由でワークフロー更新

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

