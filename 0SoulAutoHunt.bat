@echo off
title Soul's Auto-Hunt Engine Running...
setlocal enabledelayedexpansion

:: Set working directory
cd /d "C:\Users\S\Desktop\AI\Gemini\Stock"

:: Get current date and time
for /f "tokens=*" %%a in ('powershell -Command "Get-Date -Format 'yyyy-MM-dd HH:mm'"') do set NOW=%%a
for /f "tokens=*" %%a in ('powershell -Command "Get-Date -Format 'yyyy. MM. dd. HH:mm'"') do set NOW_DOT=%%a

echo ========================================
echo [Soul's Insight Portal] Starting Auto-Hunt
echo Start Time: %NOW%
echo ========================================

echo.
echo [1/8] Hunting real-time news...
node "C:\Users\S\Desktop\AI\Gemini\Stock\scripts\fetch_news.cjs"

echo.
echo [2-6] Updating data (Refer to manual instructions for skill execution)...
:: Note: The actual content update for KOSPI/NASDAQ/Valuation is handled via Gemini CLI triggers.

echo.
echo [7/8] Syncing Portal Index and All Timestamps (UTF-8 Safe)...
:: Using PowerShell with explicit UTF-8 (No BOM) handling
powershell -NoProfile -Command "$utf8NoBom = New-Object System.Text.UTF8Encoding($false); $files = Get-ChildItem -Path *.html; foreach ($file in $files) { $content = [System.IO.File]::ReadAllText($file.FullName); $content = $content -replace '\d{4}\. \d{2}\. \d{2}\. \d{2}:\d{2}', '%NOW_DOT%'; $content = $content -replace '\d{4}-\d{2}-\d{2} \d{2}:\d{2}(:\d{2})?', '%NOW%'; $content = $content -replace 'Last Portal Update: \d{4}-\d{2}-\d{2} \d{2}:\d{2}', ('Last Portal Update: ' + '%NOW%'); [System.IO.File]::WriteAllText($file.FullName, $content, $utf8NoBom) }"

echo.
echo [8/8] Recording changes and syncing online...
git add .
git commit -m "Auto Hunt Portal Update (UTF-8 Fixed): %NOW%"
git push origin main

echo.
echo ========================================
echo Hunt Complete! All pages updated with timestamp: %NOW%
echo ========================================
timeout /t 5
