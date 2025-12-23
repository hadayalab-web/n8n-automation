# MCP設定チェックリスト

このドキュメントは、MCPサーバーの設定を一つずつ進めるためのチェックリストです。

## 📋 設定状況

### ✅ 既に設定済み
- [x] **n8n-mcp** - ワークフロー開発の中核（既に動作中）
- [x] **GitHub MCP** - Cursor標準搭載（設定不要）

### ⏳ 設定が必要
- [ ] **Vercel MCP Server** - Vercel運用中
- [ ] **Google Workspace MCP Server** - Google Workspace利用中
- [ ] **PostgreSQL/Supabase MCP Server** - データベース操作
- [ ] **Context7 MCP Server** - 技術ドキュメント（Perplexity代替）
- [ ] **Stack Overflow MCP Server** - エラー解決（API Key不要）
- [ ] **Brave Search MCP Server** - Web検索（Perplexity代替）

---

## 🔧 設定順序（推奨）

### Step 1: Stack Overflow（最も簡単 - API Key不要）

**なぜ最初**: API Keyが不要で、すぐに設定完了

**設定内容:**
```json
{
  "stackoverflow": {
    "command": "npx",
    "args": ["-y", "@modelcontextprotocol/server-stackoverflow"],
    "env": {
      "LOG_LEVEL": "error",
      "NODE_NO_WARNINGS": "1"
    }
  }
}
```

**確認方法:**
```
Cursor Chat: @stackoverflow エラーメッセージを検索して
```

---

### Step 2: Vercel（重要度：高）

**必須理由**: Vercel運用中

**必要なもの**: Vercel Access Token

**取得手順:**
1. Vercel Dashboardにログイン: https://vercel.com/dashboard
2. Settings → Tokens
3. "Create Token" をクリック
4. トークン名を入力（例: "Cursor MCP"）
5. Full Access を選択
6. トークンをコピー（一度しか表示されない）

**設定内容:**
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

**確認方法:**
```
Cursor Chat: @vercel プロジェクト一覧を表示して
```

---

### Step 3: Context7（Perplexity代替 - 重要度：中）

**必須理由**: 最新技術ドキュメントへの常時アクセス

**必要なもの**: Context7 API Key

**取得手順:**
1. Context7 Dashboard: https://context7.com/
2. API Keys → Create API Key
3. キーをコピー

**設定内容:**
```json
{
  "context7": {
    "command": "npx",
    "args": ["-y", "@context7/mcp-server"],
    "env": {
      "CONTEXT7_API_KEY": "<YOUR_CONTEXT7_KEY>",
      "LOG_LEVEL": "error",
      "NODE_NO_WARNINGS": "1"
    }
  }
}
```

**確認方法:**
```
Cursor Chat: @context7 最新のNext.jsドキュメントを検索して
```

---

### Step 4: Brave Search（Perplexity代替 - 重要度：中）

**必須理由**: リアルタイムWeb検索

**必要なもの**: Brave Search API Key

**取得手順:**
1. Brave Search API: https://brave.com/search/api/
2. "Get API Key" をクリック
3. アカウント作成（無料プランあり）
4. API Keyをコピー

**設定内容:**
```json
{
  "brave-search": {
    "command": "npx",
    "args": ["-y", "@modelcontextprotocol/server-brave-search"],
    "env": {
      "BRAVE_API_KEY": "<YOUR_BRAVE_KEY>",
      "LOG_LEVEL": "error",
      "NODE_NO_WARNINGS": "1"
    }
  }
}
```

**確認方法:**
```
Cursor Chat: @brave-search 最新技術情報を検索して
```

---

### Step 5: PostgreSQL/Supabase（重要度：中）

**必須理由**: データベース操作の効率化

**必要なもの**: PostgreSQL接続文字列

**取得手順:**
- **PostgreSQL**: `postgresql://user:password@host:port/database`
- **Supabase**: Dashboard → Project Settings → Database → Connection String

**設定内容:**
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

**確認方法:**
```
Cursor Chat: @postgres データベース一覧を表示して
```

---

### Step 6: Google Workspace（重要度：低 - 複雑）

**必須理由**: Google Workspace利用中

**必要なもの**: OAuth 2.0認証情報（Client ID, Client Secret, Refresh Token）

**取得手順:**
1. Google Cloud Console: https://console.cloud.google.com/
2. プロジェクト作成（または既存プロジェクトを選択）
3. Google Workspace APIを有効化
4. OAuth 2.0認証情報を作成
5. Client ID, Client Secretを取得
6. OAuth認証フローを実行してRefresh Tokenを取得

**設定内容:**
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

**確認方法:**
```
Cursor Chat: @google-workspace 利用可能なツールを表示して
```

---

## 📝 進め方

1. **まずはStep 1（Stack Overflow）から**
   - API Key不要なので、すぐに設定完了
   - 動作確認まで実施

2. **次にStep 2（Vercel）**
   - Vercel DashboardでToken取得
   - 設定を追加して動作確認

3. **以降、優先度順に進める**
   - 必要度の高いものから順に設定

4. **各ステップごとに動作確認**
   - 設定後に必ずCursor Chatで動作確認
   - エラーがあれば修正してから次へ

---

## 🎯 現在の進捗

どのステップから始めますか？

1. **Stack Overflow**（最も簡単）
2. **Vercel**（Vercel運用中なので重要）
3. **その他**

---

**最終更新**: 2025-12-23
**バージョン**: 1.0.0

