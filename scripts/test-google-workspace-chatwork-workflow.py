#!/usr/bin/env python3
"""
Google Workspace / Chatwork Control ワークフローのテストスクリプト
"""

import json
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

import os

# .envファイルを読み込む（.env.envも確認）
env_path = Path(__file__).parent.parent / ".env"
if not env_path.exists():
    env_path = Path(__file__).parent.parent / ".env.env"
load_env_file(env_path)

# ワークフローのWebhook URL
WEBHOOK_URL = "https://hadayalab.app.n8n.cloud/webhook/google-workspace-chatwork-control"

def test_chatwork_send_message():
    """Chatworkメッセージ送信をテスト"""
    print("=" * 80)
    print("テスト: Chatworkメッセージ送信")
    print("=" * 80)
    
    # テストデータ（実際のroomIdはユーザーが設定する必要がある）
    payload = {
        "action": "chatwork_send_message",
        "roomId": "123456789",  # 実際のルームIDに置き換える必要があります
        "message": "テストメッセージ from n8n workflow"
    }
    
    print(f"リクエスト: {json.dumps(payload, indent=2, ensure_ascii=False)}")
    print(f"URL: {WEBHOOK_URL}")
    print()
    
    try:
        response = requests.post(WEBHOOK_URL, json=payload, timeout=30)
        print(f"ステータスコード: {response.status_code}")
        print(f"レスポンス: {json.dumps(response.json(), indent=2, ensure_ascii=False)}")
        
        if response.status_code == 200:
            result = response.json()
            if result.get('success'):
                print("\n[OK] テスト成功")
                return True
            else:
                print(f"\n[ERROR] テスト失敗: {result.get('error')}")
                return False
        else:
            print(f"\n[ERROR] HTTPエラー: {response.status_code}")
            print(f"レスポンス: {response.text}")
            return False
    except Exception as e:
        print(f"\n[ERROR] 例外が発生しました: {str(e)}")
        return False

def test_workflow_info():
    """ワークフロー情報を表示"""
    print("=" * 80)
    print("ワークフロー情報")
    print("=" * 80)
    print(f"Webhook URL: {WEBHOOK_URL}")
    print(f"ワークフローID: bELMAoceJ0vFNMaa")
    print(f"ワークフローURL: https://hadayalab.app.n8n.cloud/workflow/bELMAoceJ0vFNMaa")
    print()
    print("サポートするアクション:")
    print("  - gmail_send")
    print("  - sheets_read")
    print("  - chatwork_send_message")
    print("  - chatwork_create_task")
    print()

def main():
    test_workflow_info()
    
    print("=" * 80)
    print("注意事項")
    print("=" * 80)
    print("1. このテストスクリプトは、実際のroomIdが必要です")
    print("2. Google Workspaceアクション（gmail_send, sheets_read）のテストは、")
    print("   認証情報が設定されている必要があります")
    print("3. Chatworkアクションのテストは、有効なroomIdが必要です")
    print()
    print("実際のテストを実行する場合は、以下のコマンドを使用してください：")
    print("  python scripts/test-google-workspace-chatwork-workflow.py --test chatwork")
    print()
    
    if len(sys.argv) > 1 and sys.argv[1] == "--test":
        if len(sys.argv) > 2 and sys.argv[2] == "chatwork":
            test_chatwork_send_message()
        else:
            print("使用方法: python test-google-workspace-chatwork-workflow.py --test chatwork")
    else:
        print("テストを実行するには、--testオプションを指定してください")

if __name__ == "__main__":
    main()

