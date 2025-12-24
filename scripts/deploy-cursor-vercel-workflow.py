#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Cursor-Vercel連携ワークフローをn8nにデプロイするスクリプト
"""

import json
import os
import sys
import urllib.request
import urllib.parse
import urllib.error

def get_infisical_secret(secret_name, token, project_id):
    """Infisicalからシークレットを取得"""
    import subprocess
    try:
        cmd = [
            "infisical", "secrets", "get", secret_name,
            "--token", token,
            "--projectId", project_id,
            "--output", "json"
        ]
        result = subprocess.run(cmd, capture_output=True, text=True, encoding='utf-8')

        if result.returncode != 0:
            print(f"[ERROR] Failed to get {secret_name}: {result.stderr}")
            return None

        # JSON出力を解析
        output = result.stdout.strip()
        # 警告メッセージを除外
        lines = output.split('\n')
        json_lines = [line for line in lines if line.strip().startswith('{') or line.strip().startswith('[')]

        if not json_lines:
            print(f"[ERROR] No JSON found in output for {secret_name}")
            return None

        data = json.loads(json_lines[-1])
        if isinstance(data, list) and len(data) > 0:
            secret_value = data[0].get('secretValue')
            if secret_value == '*not found*':
                print(f"[WARNING] {secret_name} not found in Infisical")
                return None
            return secret_value
        elif isinstance(data, dict):
            secret_value = data.get('secretValue')
            if secret_value == '*not found*':
                print(f"[WARNING] {secret_name} not found in Infisical")
                return None
            return secret_value
        return None
    except Exception as e:
        print(f"[ERROR] Error getting {secret_name}: {e}")
        return None

def load_workflow_json(file_path):
    """ワークフローJSONファイルを読み込む"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception as e:
        print(f"[ERROR] Failed to load workflow JSON: {e}")
        return None

def create_workflow(n8n_api_url, api_key, workflow_data, project_id=None):
    """n8nにワークフローを作成"""
    url = f"{n8n_api_url}/rest/workflows"
    if project_id:
        url = f"{n8n_api_url}/rest/workflows?projectId={project_id}"

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    # ワークフローデータを準備
    payload = workflow_data

    try:
        req = urllib.request.Request(url, data=json.dumps(payload).encode('utf-8'), headers=headers, method='POST')
        with urllib.request.urlopen(req) as response:
            result = json.loads(response.read().decode('utf-8'))
            return result
    except urllib.error.HTTPError as e:
        error_body = e.read().decode('utf-8')
        print(f"[ERROR] HTTP {e.code}: {error_body}")
        return None
    except Exception as e:
        print(f"[ERROR] Failed to create workflow: {e}")
        return None

def main():
    print("[INFO] Starting Cursor-Vercel workflow deployment...")

    # Infisical設定
    token = os.environ.get("INFISICAL_TOKEN", "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhdXRoTWV0aG9kIjoiZ29vZ2xlIiwiYXV0aFRva2VuVHlwZSI6ImFjY2Vzc1Rva2VuIiwidXNlcklkIjoiMjBhZTM5NjktODQ0NS00OWNhLTlkY2UtYzUwNmQ1YTMxMzI5IiwidG9rZW5WZXJzaW9uSWQiOiJmZTI0YWY0ZS0zNDZhLTRkZDYtYjZkNy00NWY3Y2JhNDRhNWQiLCJhY2Nlc3NWZXJzaW9uIjoxLCJvcmdhbml6YXRpb25JZCI6IjE2ZjQ0M2I1LWZhMTYtNGZhZC1hNGE5LTgwMjc4MDllZTM1NyIsImlhdCI6MTc2NjU0Njc0NSwiZXhwIjoxNzY3NDEwNzQ1fQ.wZnwKPLkAYBSpz9QBarfb8mcl0h3Fj2EfUbMzC0Q_4o")
    project_id = os.environ.get("INFISICAL_PROJECT_ID", "446f131c-be8d-45e5-a83a-4154e34501a5")

    # n8n API設定を取得（Personal Access Tokenを使用）
    print("[INFO] Getting N8N_PERSONAL_ACCESS_TOKEN from Infisical...")
    n8n_api_key = get_infisical_secret("N8N_PERSONAL_ACCESS_TOKEN", token, project_id)
    n8n_api_url = "https://hadayalab.app.n8n.cloud"

    if not n8n_api_key:
        print("[ERROR] Failed to get N8N_PERSONAL_ACCESS_TOKEN from Infisical")
        print("[INFO] Please ensure N8N_PERSONAL_ACCESS_TOKEN is set in Infisical")
        print("[INFO] You can create it in n8n Dashboard → Settings → Personal Access Tokens")
        sys.exit(1)

    print(f"[OK] N8N_PERSONAL_ACCESS_TOKEN retrieved (preview: {n8n_api_key[:20]}...)")

    # n8n API URLを正規化（末尾のスラッシュを削除）
    n8n_api_url = n8n_api_url.rstrip('/')

    print(f"[INFO] n8n API URL: {n8n_api_url}")

    # ワークフローJSONを読み込む
    workflow_file = os.path.join(os.path.dirname(__file__), "..", "workflow-cursor-vercel-deploy.json")
    workflow_data = load_workflow_json(workflow_file)

    if not workflow_data:
        print("[ERROR] Failed to load workflow JSON")
        sys.exit(1)

    print(f"[INFO] Loaded workflow: {workflow_data.get('name', 'Unknown')}")

    # プロジェクトIDを取得（オプション）
    n8n_project_id = os.environ.get("N8N_PROJECT_ID", "9D29Es58GIo6IPkZ")

    # プロジェクトIDをワークフローデータに追加
    if n8n_project_id:
        workflow_data['projectId'] = n8n_project_id

    # ワークフローを作成
    print("[INFO] Creating workflow in n8n...")
    result = create_workflow(n8n_api_url, n8n_api_key, workflow_data, n8n_project_id)

    if result:
        print(f"[OK] Workflow created successfully!")
        workflow_id = result.get('data', {}).get('id') or result.get('id', 'N/A')
        print(f"[INFO] Workflow ID: {workflow_id}")
        print(f"[INFO] Workflow Name: {result.get('data', {}).get('name') or result.get('name', 'N/A')}")
        print(f"[INFO] Webhook URL: {n8n_api_url}/webhook/cursor-vercel-deploy")
        print(f"\n[INFO] 次のステップ:")
        print(f"1. n8n Dashboardでワークフローを開く:")
        print(f"   {n8n_api_url}/workflow/{workflow_id}?projectId={n8n_project_id}")
        print(f"2. Settings → Environment Variables で以下を設定:")
        print(f"   - VERCEL_API_TOKEN: Vercel API Token")
        print(f"3. ワークフローをActive化")
        print(f"4. GitHub Webhookを設定:")
        print(f"   URL: {n8n_api_url}/webhook/cursor-vercel-deploy")
    else:
        print("[ERROR] Failed to create workflow")
        sys.exit(1)

if __name__ == "__main__":
    main()

