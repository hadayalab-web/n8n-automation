# n8n-automation

n8nワークフロー自動化プロジェクト。HadayaLab Spaceと連携し、効率的な自動化を実現します。

## プロジェクト概要

このリポジトリは、n8nを使用したワークフロー自動化プロジェクトです。HadayaLab Spaceとの連携により、様々なタスクの自動化を実現します。

## ディレクトリ構成

```
n8n-automation/
├── README.md                  # プロジェクト説明
├── .gitignore                 # Node.js/n8n除外設定
├── package.json               # n8n-mcp依存関係
├── workflows/                 # n8nワークフローJSON
│   └── .gitkeep
├── docs/                      # ドキュメント
│   └── .gitkeep
└── .cursor/                   # Cursor設定（ローカルのみ）
    └── mcp.json              # n8n-mcp設定
```

## セットアップ

```bash
npm install
```

## 使用方法

n8nワークフローは `workflows/` ディレクトリに保存されます。

## リポジトリ情報

- リモート: https://github.com/hadayalab-web/n8n-automation.git
- 目的: n8nワークフロー自動化プロジェクト
- HadayaLab Space連携


