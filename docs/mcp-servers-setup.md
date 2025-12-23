# MCPサーバー導入ガイド

このドキュメントは、n8n-automationプロジェクトで使用するMCP（Model Context Protocol）サーバーの設定方法を説明します。

## 📋 MCPサーバー一覧

### 必須MCP（既存）

#### 1. n8n-mcp v2.30.2

**状況**: ✅ 導入済み、JSONパースエラー解決済み

**役割**: ワークフロー開発の中核

**統合対象**: 以下すべてのAPIをn8n経由で管理

**設定:**
```json
{
  "n8n": {
    "command": "npx",
    "args": ["-y", "n8n-mcp"],
    "env": {
      "N8N_API_URL": "https://hadayalab.app.n8n.cloud",
      "N8N_API_KEY": "<YOUR_N8N_API_KEY>",
      "LOG_LEVEL": "error",
      "NODE_NO_WARNINGS": "1"
    }
  }
}
```

**機能:**
- ワークフロー作成・更新・削除
- ノード検索（543個）
- テンプレート検索（2,700+）
- ワークフロー検証
- 実行管理

---

#### 2. GitHub MCP Server

**状況**: ✅ Cursor標準搭載

**役割**: リポジトリ管理、PR作成

**使用頻度**: 高

**設定**: Cursor標準機能のため、追加設定不要

**機能:**
- リポジトリ操作
- プルリクエスト作成・管理
- イシュー管理
- コードレビュー

---

### 新規導入推奨MCP

#### 3. Vercel MCP Server

**必須理由**: Vercel運用中

**機能:**
- プロジェクト管理（作成、削除、リスト）
- デプロイメント管理（トリガー、ロールバック）
- ログ分析
- 環境変数設定
- カスタムドメイン管理

**設定方法:**

1. **Vercel Access Token取得**
   ```bash
   # Vercel Dashboard → Settings → Tokens → Create Token
   ```

2. **MCP設定追加**
   ```json
   {
     "vercel": {
       "command": "npx",
       "args": ["-y", "@modelcontextprotocol/server-vercel"],
       "env": {
         "VERCEL_ACCESS_TOKEN": "<YOUR_VERCEL_TOKEN>",
         "LOG_LEVEL": "error",
         "NODE_NO_WARNINGS": "1"
       }
     }
   }
   ```

**n8nとの連携:**
- Vercelデプロイメントをn8nワークフローで自動化
- デプロイメント通知をSlack等に送信
- 環境変数の一括管理

---

#### 4. Google Workspace MCP Server

**必須理由**: Google Workspaceを利用中

**機能:**
- Gmail自動化
- Google Drive操作
- Google Sheets連携
- Google Calendar管理

**設定方法:**

1. **Google Cloud Console設定**
   ```bash
   # 1. Google Cloud Consoleでプロジェクト作成
   # 2. Google Workspace APIを有効化
   # 3. OAuth 2.0認証情報を作成
   # 4. リダイレクトURIを設定
   ```

2. **認証情報取得**
   ```bash
   # Client ID, Client Secret, Refresh Tokenを取得
   ```

3. **MCP設定追加**
   ```json
   {
     "google-workspace": {
       "command": "npx",
       "args": ["-y", "@modelcontextprotocol/server-google-workspace"],
       "env": {
         "GOOGLE_CLIENT_ID": "<YOUR_GOOGLE_CLIENT_ID>",
         "GOOGLE_CLIENT_SECRET": "<YOUR_GOOGLE_CLIENT_SECRET>",
         "GOOGLE_REFRESH_TOKEN": "<YOUR_GOOGLE_REFRESH_TOKEN>",
         "LOG_LEVEL": "error",
         "NODE_NO_WARNINGS": "1"
       }
     }
   }
   ```

**n8nとの連携:**
- Workspace APIをn8nワークフローで自動化
- Gmail受信トリガーでワークフロー実行
- Google Sheetsデータをn8nで処理
- Calendarイベントをn8nで管理

---

#### 5. PostgreSQL/Supabase MCP Server

**必須理由**: データベース操作の効率化

**機能:**
- データベースクエリ実行
- スキーマ管理
- Supabase Vector Store
- データ分析

**設定方法:**

1. **接続文字列取得**
   ```bash
   # PostgreSQLの場合
   postgresql://user:password@host:port/database

   # Supabaseの場合
   postgresql://postgres:[YOUR-PASSWORD]@[PROJECT-REF].supabase.co:5432/postgres
   ```

2. **MCP設定追加**
   ```json
   {
     "postgres": {
       "command": "npx",
       "args": ["-y", "@modelcontextprotocol/server-postgres"],
       "env": {
         "POSTGRES_CONNECTION_STRING": "<YOUR_CONNECTION_STRING>",
         "LOG_LEVEL": "error",
         "NODE_NO_WARNINGS": "1"
       }
     }
   }
   ```

**n8nとの連携:**
- データベース操作をn8nワークフローで自動化
- データ同期・変換
- レポート自動生成
- データ分析の自動化

---

## 🔧 完全なmcp.json設定例

```json
{
  "mcpServers": {
    "n8n": {
      "command": "npx",
      "args": ["-y", "n8n-mcp"],
      "env": {
        "N8N_API_URL": "https://hadayalab.app.n8n.cloud",
        "N8N_API_KEY": "<YOUR_N8N_API_KEY>",
        "LOG_LEVEL": "error",
        "NODE_NO_WARNINGS": "1"
      }
    },
    "vercel": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-vercel"],
      "env": {
        "VERCEL_ACCESS_TOKEN": "<YOUR_VERCEL_TOKEN>",
        "LOG_LEVEL": "error",
        "NODE_NO_WARNINGS": "1"
      }
    },
    "google-workspace": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-google-workspace"],
      "env": {
        "GOOGLE_CLIENT_ID": "<YOUR_GOOGLE_CLIENT_ID>",
        "GOOGLE_CLIENT_SECRET": "<YOUR_GOOGLE_CLIENT_SECRET>",
        "GOOGLE_REFRESH_TOKEN": "<YOUR_GOOGLE_REFRESH_TOKEN>",
        "LOG_LEVEL": "error",
        "NODE_NO_WARNINGS": "1"
      }
    },
    "postgres": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-postgres"],
      "env": {
        "POSTGRES_CONNECTION_STRING": "<YOUR_POSTGRES_CONNECTION_STRING>",
        "LOG_LEVEL": "error",
        "NODE_NO_WARNINGS": "1"
      }
    }
  }
}
```

---

## 📝 設定手順

### 1. 認証情報の準備

各MCPサーバーに必要な認証情報を取得：

- **n8n**: API Key（既に取得済み）
- **Vercel**: Access Token
- **Google Workspace**: Client ID, Client Secret, Refresh Token
- **PostgreSQL**: Connection String

### 2. mcp.jsonの更新

1. `C:\Users\USERNAME\.cursor\mcp.json` を開く
2. 上記の設定例を参考に、認証情報を埋める
3. JSON構文を検証

### 3. Cursor再起動

1. すべてのCursorウィンドウを閉じる
2. 30秒待機
3. Cursorを再起動

### 4. 動作確認

各MCPサーバーの接続を確認：

```bash
# Cursor AIチャットで実行
@n8n 利用可能なツールを表示して
@vercel プロジェクト一覧を表示して
@google-workspace 利用可能なツールを表示して
@postgres データベース一覧を表示して
```

---

## 🔗 n8nとの統合

すべてのMCPサーバーは、n8nワークフロー経由で統合管理されます：

### 統合フロー

```
Cursor AI
  ↓
MCP Servers (n8n, Vercel, Google Workspace, PostgreSQL)
  ↓
n8n Workflows
  ↓
Automated Actions
```

### 使用例

1. **Vercelデプロイメント自動化**
   - GitHub push → n8nワークフロー → Vercelデプロイ

2. **Google Workspace連携**
   - Gmail受信 → n8nワークフロー → Google Sheets更新

3. **データベース操作**
   - n8nワークフロー → PostgreSQLクエリ → レポート生成

---

## ⚠️ 注意事項

### セキュリティ

- **認証情報の管理**: `.env`ファイルや環境変数で管理
- **mcp.json**: Gitにコミットしない（`.gitignore`に追加）
- **トークンの有効期限**: 定期的に更新

### パフォーマンス

- **LOG_LEVEL**: すべてのMCPサーバーで`"error"`に設定
- **NODE_NO_WARNINGS**: `"1"`に設定して警告を抑制
- **同時接続数**: 必要に応じて制限

### トラブルシューティング

詳細は [mcp-troubleshooting.md](./mcp-troubleshooting.md) を参照

---

## 📚 参考リンク

- [n8n-mcp Documentation](https://www.npmjs.com/package/n8n-mcp)
- [Vercel MCP Server](https://www.npmjs.com/package/@modelcontextprotocol/server-vercel)
- [Google Workspace MCP Server](https://www.npmjs.com/package/@modelcontextprotocol/server-google-workspace)
- [PostgreSQL MCP Server](https://www.npmjs.com/package/@modelcontextprotocol/server-postgres)
- [Model Context Protocol](https://modelcontextprotocol.io/)

---

**最終更新**: 2025-12-23  
**バージョン**: 1.0.0

