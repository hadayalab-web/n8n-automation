# Cursor Agent Sessions レビュー依頼スクリプト

Write-Host "=== Cursor Agent Sessions レビュー依頼 ===" -ForegroundColor Cyan
Write-Host ""

# レビュー依頼ファイルを確認
$ReviewRequestFile = Join-Path $PSScriptRoot "..\docs\github-copilot-review-request.md"
$PromptFile = Join-Path $PSScriptRoot "..\review-request-prompt.txt"

if (-not (Test-Path $ReviewRequestFile)) {
    Write-Host "エラー: $ReviewRequestFile が見つかりません" -ForegroundColor Red
    exit 1
}

if (-not (Test-Path $PromptFile)) {
    Write-Host "エラー: $PromptFile が見つかりません" -ForegroundColor Red
    exit 1
}

Write-Host "レビュー依頼ファイル: $ReviewRequestFile" -ForegroundColor Green
Write-Host ""

# レビュー依頼メッセージをファイルから読み込む
$ReviewMessage = Get-Content $PromptFile -Raw

Write-Host "Cursor Agentにレビュー依頼を送信中..." -ForegroundColor Yellow
Write-Host ""
Write-Host "レビュー依頼内容:" -ForegroundColor Cyan
Write-Host $ReviewMessage
Write-Host ""

# Cursor Agentに送信（標準入力経由）
$ReviewMessage | cursor -

Write-Host ""
Write-Host "レビュー依頼が送信されました。" -ForegroundColor Green
Write-Host ""
Write-Host "次のステップ:" -ForegroundColor Yellow
Write-Host "1. Cursor Agent Sessionsでレビュー結果を確認"
Write-Host "2. フィードバックを記録"
Write-Host "3. 改善を実施"

