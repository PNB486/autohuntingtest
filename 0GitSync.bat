@echo off
chcp 65001 > nul
cd /d "C:\Users\S\Desktop\AI\Gemini\Stock"
echo ========================================
echo [Soul's Insight Portal] Syncing to GitHub
echo ========================================
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
echo Git Force Push Complete!
echo ========================================
timeout /t 5
