# Google Workspace / Chatwork Control ワークフロー テスト結果

**テスト日**: 2025-12-26
**ワークフローID**: `bELMAoceJ0vFNMaa`
**ワークフロー名**: `google-workspace-chatwork-control`

---

## 📋 ワークフロー情報

- **Webhook URL**: `https://hadayalab.app.n8n.cloud/webhook/google-workspace-chatwork-control`
- **ワークフローURL**: https://hadayalab.app.n8n.cloud/workflow/bELMAoceJ0vFNMaa
- **フォルダ**: Personal（プロジェクトID: `fPT5foO8DCTDBr0k`）
- **ステータス**: ✅ Published（有効化済み）

---

## 🧪 テスト項目

### 1. ワークフロー基本動作確認

#### 1.1 Webhook URLの確認

**テスト方法**:
```bash
curl -X POST https://hadayalab.app.n8n.cloud/webhook/google-workspace-chatwork-control \
  -H "Content-Type: application/json" \
  -d '{"action": "invalid_action"}'
```

**期待結果**:
- HTTP 200レスポンス
- `{"success": false, "error": "..."}` 形式のレスポンス

**テスト結果**: 
- [ ] 未実施
- [ ] ✅ 成功
- [ ] ❌ 失敗

---

### 2. Chatworkアクション

#### 2.1 Chatworkメッセージ送信 (`chatwork_send_message`)

**テスト方法**:
```bash
curl -X POST https://hadayalab.app.n8n.cloud/webhook/google-workspace-chatwork-control \
  -H "Content-Type: application/json" \
  -d '{
    "action": "chatwork_send_message",
    "roomId": "実際のルームID",
    "message": "テストメッセージ from n8n workflow"
  }'
```

**テスト結果**: 
- [ ] 未実施
- [ ] ✅ 成功
- [ ] ❌ 失敗

**備考**: 
- 実際のルームIDが必要です
- Chatwork API Tokenは設定済み（`e973fd7311ae06d1deb377bd1ecb7d8e`）

#### 2.2 Chatworkタスク作成 (`chatwork_create_task`)

**テスト方法**:
```bash
curl -X POST https://hadayalab.app.n8n.cloud/webhook/google-workspace-chatwork-control \
  -H "Content-Type: application/json" \
  -d '{
    "action": "chatwork_create_task",
    "roomId": "実際のルームID",
    "taskBody": "テストタスク",
    "toIds": "担当者ID",
    "limit": "2025-12-31T23:59:59Z"
  }'
```

**テスト結果**: 
- [ ] 未実施
- [ ] ✅ 成功
- [ ] ❌ 失敗

---

### 3. Google Workspaceアクション

#### 3.1 Gmail送信 (`gmail_send`)

**前提条件**: Gmail OAuth2認証情報が設定されている必要があります

**テスト方法**:
```bash
curl -X POST https://hadayalab.app.n8n.cloud/webhook/google-workspace-chatwork-control \
  -H "Content-Type: application/json" \
  -d '{
    "action": "gmail_send",
    "to": "test@example.com",
    "subject": "テストメール",
    "message": "テストメッセージ"
  }'
```

**テスト結果**: 
- [ ] 未実施（認証情報未設定）
- [ ] ✅ 成功
- [ ] ❌ 失敗

**備考**: 
- Gmail OAuth2認証情報の設定が必要です
- `admin@cryptotradeacademy.io` の認証情報を使用

#### 3.2 Google Sheets読み取り (`sheets_read`)

**前提条件**: Google Sheets OAuth2認証情報が設定されている必要があります

**テスト方法**:
```bash
curl -X POST https://hadayalab.app.n8n.cloud/webhook/google-workspace-chatwork-control \
  -H "Content-Type: application/json" \
  -d '{
    "action": "sheets_read",
    "spreadsheetId": "実際のスプレッドシートID",
    "sheetName": "Sheet1",
    "range": "A1:C10"
  }'
```

**テスト結果**: 
- [ ] 未実施（認証情報未設定）
- [ ] ✅ 成功
- [ ] ❌ 失敗

**備考**: 
- Google Sheets OAuth2認証情報の設定が必要です
- `admin@cryptotradeacademy.io` の認証情報を使用

---

## 📊 テスト結果サマリー

| アクション | ステータス | 備考 |
|-----------|----------|------|
| chatwork_send_message | ⏳ 未実施 | 実際のルームIDが必要 |
| chatwork_create_task | ⏳ 未実施 | 実際のルームIDと担当者IDが必要 |
| gmail_send | ⏳ 未実施 | Gmail OAuth2認証情報の設定が必要 |
| sheets_read | ⏳ 未実施 | Google Sheets OAuth2認証情報の設定が必要 |

---

## 🔍 次のステップ

1. **認証情報の確認**
   - Gmail OAuth2認証情報が設定されているか確認
   - Google Sheets OAuth2認証情報が設定されているか確認

2. **実際のデータでのテスト**
   - ChatworkのルームIDを取得
   - Google SheetsのスプレッドシートIDを準備
   - 各アクションを実際のデータでテスト

3. **エラーハンドリングの確認**
   - 無効なアクションのテスト
   - 必須パラメータ不足のテスト
   - 認証エラーのテスト

---

**最終更新**: 2025-12-26

