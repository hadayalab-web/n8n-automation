# n8n Workflows

管理方法:
- Cursor + n8n-mcp で作成
- GitHubにコミット・プッシュ後、n8n Cloud UIでURLからインポート

## 📋 ワークフロー一覧

### @simple-time-check
- **ファイル**: `workflows/simple-time-check.json`
- **説明**: 簡単な実験用ワークフロー（現在時刻取得）
- **機能**: Webhook TriggerでHTTPリクエストを受け取り、World Time APIから東京の現在時刻を取得してJSONで返す
- **タグ**: test, experiment, simple
- **参照方法**: `@workflows/simple-time-check.json` または `@simple-time-check`
- **n8n Cloudへのインポート方法**:

  **方法1: ファイルから直接インポート（推奨）**
  1. n8n Dashboardで「Import from File」を選択
  2. `workflows/simple-time-check.json` ファイルを選択してインポート

  **方法2: URLからインポート（GitHubにコミット・プッシュ後）**
  1. このファイルをGitHubにコミット・プッシュしてください：
     ```bash
     git add workflows/simple-time-check.json
     git commit -m "Add simple-time-check workflow"
     git push origin main
     ```
  2. n8n Dashboardで「Import Workflow from URL」を開き、以下のURLを入力してください：
     ```
     https://raw.githubusercontent.com/hadayalab-web/hadayalab-automation-platform/main/workflows/simple-time-check.json
     ```

  **注意**: ファイルがGitHubにプッシュされていない場合、URLからのインポートは404エラーになります。その場合は方法1を使用してください。

### @manual-hello-world-test
- **ファイル**: `workflows/manual-hello-world-test.json`
- **説明**: MCPテスト用ワークフロー
- **機能**: Manual Triggerで「Hello from n8n-mcp!」メッセージを返す
- **タグ**: test, mcp, validated
- **参照方法**: `@workflows/manual-hello-world-test.json` または `@manual-hello-world-test`

## 🔍 Cursor Chatでの使用方法

### ワークフローを参照する

```
@workflows/simple-time-check.json を検証して
@workflows/simple-time-check.json をn8n Cloudにインポートして
@simple-time-check ワークフローを実行して
```

### ワークフロー一覧を確認する

```
@workflows/workflow-index.md を参照して、利用可能なワークフローを表示して
```

詳細は [Cursor Chatでワークフローをメンションする方法](../docs/cursor-workflow-mention-guide.md) を参照してください。

