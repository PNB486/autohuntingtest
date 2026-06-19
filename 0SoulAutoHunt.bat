@echo off
chcp 65001 > nul
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
echo [Sync] Aligning workspace with remote GitHub repository...
git fetch origin main >nul 2>&1
git reset --hard origin/main

echo.
echo [1/8] Hunting real-time news...
node "C:\Users\S\Desktop\AI\Gemini\Stock\scripts\fetch_news.cjs"

echo.
echo [2-7] Updating Indices, Prices, and Valuations (Auto-Update)...
python "C:\Users\S\Desktop\AI\Gemini\Stock\scripts\auto_update_market_data.py"

echo.
echo [8/8] Verifying integrity and recording changes...
:: Run validation script before committing
python "C:\Users\S\Desktop\AI\Gemini\Stock\scripts\revalidate_portal.py"
if %errorlevel% neq 0 (
    echo.
    echo [ERROR] Validation failed. Changes will not be committed.
    pause
    exit /b %errorlevel%
)

git add .
git commit --amend -m "Auto Hunt Portal Update" >nul 2>&1
if %errorlevel% neq 0 (
    git commit -m "Auto Hunt Portal Update"
)
git push origin main --force

echo.
echo [Verification] Cross-checking Git Remote Sync...
git fetch origin main >nul 2>&1
for /f "tokens=*" %%a in ('git rev-parse HEAD') do set LOCAL_HASH=%%a
for /f "tokens=*" %%a in ('git rev-parse origin/main') do set REMOTE_HASH=%%a

if "%LOCAL_HASH%"=="%REMOTE_HASH%" (
    echo [OK] Git Remote Sync Verified successfully!
    echo Local:  %LOCAL_HASH%
    echo Remote: %REMOTE_HASH%
) else (
    echo [ERROR] Git Sync Mismatch!
    echo Local:  %LOCAL_HASH%
    echo Remote: %REMOTE_HASH%
    pause
)

echo.
echo ========================================
echo Hunt Complete! All pages updated with timestamp: %NOW%
echo ========================================
ping 127.0.0.1 -n 6 >nul
