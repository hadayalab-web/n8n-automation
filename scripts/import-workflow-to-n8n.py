#!/usr/bin/env python3
"""
n8n Cloudにワークフローをインポートするスクリプト
n8n APIを使用してワークフローを作成
"""

import json
import os
import sys
import requests
from pathlib import Path

# .envファイルを読み込む
def load_env_file(env_path: Path):
    """.envファイルを読み込んで環境変数に設定"""
    if not env_path.exists():
        return

    with open(env_path, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith('#') and '=' in line:
                key, value = line.split('=', 1)
                key = key.strip()
                value = value.strip().strip('"').strip("'")
                os.environ[key] = value

# .envファイルを読み込む（.env.envも確認）
env_path = Path(__file__).parent.parent / ".env"
if not env_path.exists():
    # .env.envも確認
    env_path = Path(__file__).parent.parent / ".env.env"
load_env_file(env_path)

# 環境変数から設定を取得
N8N_API_URL = os.getenv("N8N_API_URL", "https://hadayalab.app.n8n.cloud")
N8N_API_KEY = os.getenv("N8N_API_KEY")

if not N8N_API_KEY:
    print("ERROR: N8N_API_KEY環境変数が設定されていません")
    print("n8n Cloud Dashboard → Settings → API → Personal Access Tokens でトークンを取得してください")
    sys.exit(1)

def import_workflow(workflow_path: str):
    """ワークフローファイルをn8n Cloudにインポート"""

    # ワークフローファイルを読み込む
    workflow_file = Path(workflow_path)
    if not workflow_file.exists():
        print(f"ERROR: ワークフローファイルが見つかりません: {workflow_path}")
        sys.exit(1)

    with open(workflow_file, 'r', encoding='utf-8') as f:
        workflow_data = json.load(f)

    # n8n APIが受け付けるプロパティのみを保持
    # n8n APIは name, nodes, connections, settings のみを受け付ける（tagsは読み取り専用）
    workflow_data_clean = {
        'name': workflow_data.get('name'),
        'nodes': workflow_data.get('nodes', []),
        'connections': workflow_data.get('connections', {}),
    }
    if 'settings' in workflow_data:
        workflow_data_clean['settings'] = workflow_data['settings']

    # PersonalフォルダのプロジェクトIDを追加（オプション）
    # project_id = "fPT5foO8DCTDBr0k"  # Personalフォルダ
    # workflow_data_clean['projectId'] = project_id  # プロジェクトIDはAPIでは設定できない場合がある

    # n8n APIエンドポイント
    api_endpoint = f"{N8N_API_URL}/api/v1/workflows"

    # ヘッダー
    headers = {
        "X-N8N-API-KEY": N8N_API_KEY,
        "Content-Type": "application/json"
    }

    # ワークフローを作成
    print(f"ワークフローをインポート中: {workflow_data_clean.get('name', 'unknown')}")
    response = requests.post(api_endpoint, json=workflow_data_clean, headers=headers)

    if response.status_code in [200, 201]:
        workflow = response.json()
        print(f"[OK] ワークフローが正常にインポートされました")
        print(f"   ID: {workflow.get('id')}")
        print(f"   名前: {workflow.get('name')}")
        print(f"   URL: {N8N_API_URL}/workflow/{workflow.get('id')}")
        return workflow
    else:
        print(f"ERROR: ワークフローのインポートに失敗しました")
        print(f"   ステータスコード: {response.status_code}")
        print(f"   エラーメッセージ: {response.text}")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("使用方法: python import-workflow-to-n8n.py <workflow.json>")
        sys.exit(1)

    workflow_path = sys.argv[1]
    import_workflow(workflow_path)

