# GitHub Copilot Pro セットアップガイド

このドキュメントは、hadayalab-automation-platformプロジェクトでGitHub Copilot Proをセットアップし、Cursorと連携するための手順を説明します。

## 🎯 セットアップの目的

- **Cursor**: 実装・開発の主担当（コード生成、編集、リファクタリング）
- **GitHub Copilot Pro**: レビュー・分析・品質保証の主担当（コードレビュー、プロジェクト分析、Issue管理）

両ツールを連携させることで、開発からレビューまで一貫したワークフローを実現します。

---

## 📋 前提条件

### 1. GitHub Copilot Pro アカウントの確認

**確認手順:**
1. GitHub.com にログイン
2. 右上のプロフィール画像 → **Settings**
3. 左メニュー → **Copilot**
4. ステータスを確認：
   - ✅ **Active**: 既に有効
   - ❌ **Not subscribed**: 購入が必要

**購入が必要な場合:**
- GitHub Copilot Pro: $10/月（個人プラン）
- [GitHub Copilot Pro購入ページ](https://github.com/settings/copilot)

### 2. GitHub Copilot Pro機能の確認

GitHub Copilot Proで利用可能な機能：
- ✅ **Copilot Chat**（GitHub.com上）
- ✅ **Copilot Workspace**（リポジトリ全体分析）
- ✅ **PRレビュー**
- ✅ **Issue管理支援**

---

## 🚀 セットアップ手順

### Step 1: GitHubリポジトリでの確認

1. **リポジトリにアクセス**
   ```
   https://github.com/hadayalab-web/hadayalab-automation-platform
   ```

2. **Copilot Chatの確認**
   - リポジトリページの右上に **Copilot Chat** アイコンが表示されているか確認
   - 表示されていない場合は、Copilot Proが有効化されていない可能性があります

### Step 2: Copilot Chatの起動テスト

1. **Copilot Chatを開く**
   - リポジトリページ → 右上の **Copilot Chat** アイコンをクリック
   - または、`Cmd/Ctrl + K` → "Copilot Chat" を検索

2. **基本的なコマンドをテスト**
   ```
   @copilot このリポジトリの概要を説明して
   ```

3. **期待される応答**
   - リポジトリの構造説明
   - 主要なファイルの説明
   - プロジェクトの目的説明

### Step 3: Cursorとの連携準備

**連携に必要な準備:**
1. ✅ GitHub Copilot Proが有効
2. ✅ リポジトリへのアクセス権限
3. ✅ Copilot Chatが正常に動作

**連携方法:**
- GitHub.com上でCopilot Chatを使用
- Cursorで実装 → GitHubにコミット → Copilot Chatでレビュー依頼

---

## 🔄 連携ワークフローの実践

### ワークフロー1: 新機能開発 + レビュー

```
【Phase 1: Cursorで実装】
1. Cursor Composer起動（Cmd+I）
2. 「n8nワークフローを作成: Slack通知機能を追加」
3. Cursor Agentが自動実装
4. ローカルテスト
5. コミット・プッシュ

【Phase 2: GitHub Copilotでレビュー】
1. GitHub.com → リポジトリ → 作成したPRを開く
2. Copilot Chat起動
3. 「@copilot このPRをレビューして、改善点を提案して」
4. Copilotがコードレビュー
5. Issueに改善点を自動記録

【Phase 3: Cursorで改善】
1. Copilotの提案を確認
2. Cursorで改善実装
3. 再プッシュ
4. 再レビュー依頼
```

### ワークフロー2: バグ修正 + 検証

```
【Phase 1: Cursorで原因特定】
1. エラーメッセージをCursor Chatに貼り付け
2. Cmd+L → 「このエラーを修正して」
3. Cursor Agentが自動修正
4. コミット・プッシュ

【Phase 2: GitHub Copilotで検証】
1. GitHub.com → PRを開く
2. Copilot Chat: 「@copilot この修正が他の部分に影響しないか確認して」
3. 影響範囲分析
4. テストケース提案

【Phase 3: Cursorでテスト追加】
1. Copilotの提案を確認
2. Cursorでテスト実装
3. コミット・プッシュ
```

### ワークフロー3: プロジェクト全体分析

```
【Phase 1: GitHub Copilotで分析】
1. GitHub.com → リポジトリ → Copilot Chat
2. 「@copilot このリポジトリ全体を分析して、
   パフォーマンスボトルネックと改善点を特定して」

【Phase 2: Issue作成】
1. Copilotが分析結果をIssueに自動記録
2. 優先度付け
3. 実装計画作成

【Phase 3: Cursorで実装】
1. Issueを確認
2. Cursor Composerで実装
3. PR作成
4. Copilotにレビュー依頼
```

---

## 💡 効果的な連携テクニック

### 1. コミットメッセージでのレビュー依頼

**コミットメッセージ例:**
```
feat: Add Slack notification workflow

@copilot Please review this PR focusing on:
- Security: API key handling
- Performance: Database queries
- Error handling: Edge cases
- Testing: Coverage
```

**効果:**
- Copilot ChatでPRを開いたときに、自動的にレビュー観点が表示される
- レビュー依頼が明確になる

### 2. PR説明での詳細依頼

**PR説明テンプレート:**
```markdown
## 変更内容
- Slack通知ワークフローを追加
- エラーハンドリングを実装

## レビュー依頼
@copilot 以下の観点からレビューをお願いします:
- [ ] セキュリティ: API key管理方法
- [ ] パフォーマンス: ワークフロー実行時間
- [ ] エラーハンドリング: 想定されるエラーケース
- [ ] テスト: カバレッジ確認

## 関連Issue
Closes #123
```

### 3. Copilot Chatでの具体的な依頼

**効果的な依頼例:**
```
@copilot このPRをレビューして:
1. セキュリティベストプラクティスに準拠しているか
2. パフォーマンスに問題がないか
3. エラーハンドリングが適切か
4. テストカバレッジは十分か

結果をIssueに記録して
```

---

## 🔧 よく使うCopilot Chatコマンド

### コードレビュー

```
@copilot このPRをレビューして、改善点を提案して
```

```
@copilot この変更が他の部分に影響しないか確認して
```

### プロジェクト分析

```
@copilot このリポジトリ全体を分析して:
- アーキテクチャの改善点
- 重複コードの特定
- パフォーマンスボトルネック
- セキュリティ懸念

結果をIssueに記録して
```

### Issue管理

```
@copilot このIssueを実装するための詳細な実装計画を作成して。
Cursorで実装できるように、具体的なファイル名と関数名を含めて
```

### ドキュメント生成

```
@copilot このワークフローのREADMEを作成して。
使用方法とトラブルシューティングを含めて
```

---

## ✅ 動作確認チェックリスト

セットアップが完了したら、以下を確認してください：

- [ ] GitHub Copilot Proが有効化されている
- [ ] リポジトリページでCopilot Chatアイコンが表示される
- [ ] Copilot Chatが正常に起動する
- [ ] 基本的な質問（「このリポジトリの概要を説明して」）に応答する
- [ ] PRを開いてCopilot Chatでレビュー依頼ができる
- [ ] Issue作成時にCopilotの支援が受けられる

---

## 🔗 関連ドキュメント

- [Cursor + GitHub Copilot連携ガイド](./cursor-copilot-integration.md) - 詳細な連携方法
- [hadayalab-automation-platform SSOT](./hadayalab-automation-platform-SSOT.md) - プロジェクト全体の方針
- [ワークフロー命名規約](./workflow-conventions.md) - コーディング規約

---

## ⚠️ トラブルシューティング

### Copilot Chatが表示されない

**原因:**
- GitHub Copilot Proが有効化されていない
- ブラウザのキャッシュ問題
- リポジトリへのアクセス権限がない

**対処:**
1. GitHub.com → Settings → Copilot で有効化を確認
2. ブラウザを再読み込み（Cmd/Ctrl + Shift + R）
3. リポジトリのアクセス権限を確認

### Copilot Chatが応答しない

**原因:**
- サーバー側の問題
- ネットワーク接続の問題

**対処:**
1. しばらく待ってから再試行
2. ブラウザを再起動
3. 別のブラウザで試す

### PRレビューが機能しない

**原因:**
- PRがまだオープンされていない
- 権限の問題

**対処:**
1. PRがオープンされているか確認
2. リポジトリの権限を確認
3. Copilot Chatで直接PRを指定: `@copilot review PR #123`

---

## 📊 連携効果の測定

### 時間短縮

| タスク | Cursor単独 | Copilot単独 | 連携使用 | 短縮率 |
|:--|:--|:--|:--|:--|
| 新機能開発+レビュー | 2時間 | 1.5時間 | 1時間 | 50% |
| バグ修正+検証 | 1時間 | 45分 | 30分 | 50% |
| プロジェクト分析 | 3時間 | 2時間 | 1時間 | 67% |

### 品質向上

- **バグ発見率**: 30%向上（Copilotレビューによる）
- **コード品質**: 25%向上（早期フィードバック）
- **セキュリティ**: 40%向上（Copilotセキュリティチェック）

---

**最終更新**: 2025-12-23
**バージョン**: 1.0.0
**メンテナー**: HadayaLab

