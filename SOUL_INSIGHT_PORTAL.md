# 🌌 Soul's Insight Portal (Auto-Hunt Project)

This project is an automated financial analysis and news aggregation portal designed for real-time market monitoring and valuation. It leverages the Gemini CLI and specialized AI skills to hunt, analyze, and publish data autonomously.

## 📂 Project Structure
- **Root**: `C:\Users\S\Desktop\AI\Gemini\Stock`
- **Automation**: `0SoulAutoHunt.bat` (The core execution engine)
- **News Script**: `scripts/fetch_news.cjs` (Puppeteer-based Naver News scraper)
- **HTML Reports**:
  - `index.html`: Main dashboard with project navigation and sector overviews.
  - `news.html`: Real-time news cards with OG image support.
  - `kospi.html`: Domestic market analysis (KOSPI/KOSDAQ).
  - `nasdaq.html`: US market analysis (NASDAQ/S&P 500/Macro).
  - `valuation_*.html`: Deep-dive valuation reports (Semi, Defense, Battery, AI).

## 🛡️ Reliability & Design Mandates
- **Encoding & Validation (CRITICAL)**:
  - All HTML files **MUST** be saved in **UTF-8 (No BOM)** encoding.
  - **Never** read or write HTML files using system default encodings (CP949/EUC-KR).
  - Always use `chcp 65001` in batch scripts and specify `utf8` in PowerShell/Python/Node.js.
  - **Mandatory Validation**: Every `0SoulAutoHunt.bat` run **MUST** execute `scripts/revalidate_portal.py` to check for mojibake before any Git operations.
- **Dark Tone Theme**: All reports must strictly follow the `index.html` aesthetic:
  - **Background**: #020617 (Slate 950)
  - **Card BG**: #0f172a (Slate 900) | **Card Border**: #1e293b (Slate 800)
  - **Accent**: Sky Blue (`sky-400` / `#38bdf8`) consistently across ALL sectors.
- **Visuals**: **Never** use specific aircraft images (e.g., F-22) in valuation reports. Use professional military/strategic gradients or neutral visual elements.
- **Real-time Verification**: All prices and indices must be verified in real-time via Google/Naver Finance. To prevent caching stale morning data, the agent must perform separate, targeted search queries for each ticker (e.g., "KOSPI index quote", "Samsung Electronics stock price") at the exact moment of the update request. All HTML timestamps and internal variables must be synchronized with the precise execution time of the request.
- **Investor Trading Trends**: Always verify the real-time net buy/sell amounts of Retail, Foreigners, and Institutions (개인/외국인/기관 수급) on KOSPI and synchronize them in the `kospi.html` dashboard table and Chart.js datasets (red/rose for net buy, blue for net sell).

## 🔍 Verification & Git Sync Validation Process (검증 및 Git 동기화 확인 절차)
자동 업데이트 완료 후, 다음 4단계 검증 프로세스를 실행하여 무결성을 보장합니다.
1. **HTML 정밀 검증 (mojibake 방지)**
   - `python scripts/revalidate_portal.py`를 실행하여 인코딩 오류, 깨진 문자(모지바케), 필수 배경색, Chart.js 컨테이너 규격 등을 체크합니다.
2. **로컬 업데이트 상태 점검**
   - 업데이트된 모든 HTML 파일이 정상적으로 저장되었는지와 수정 시간(Timestamp)이 현재 시간(KST)으로 동기화되었는지 확인합니다.
3. **Git 반영 검증**
   - `git diff` 및 `git status`로 변경 사항을 최종 점검합니다.
   - `git add .` 및 `git commit --amend` 실행 후 원격 저장소에 push합니다.
4. **원격 저장소 동기화 교차 검증 (Cross-Check)**
   - Push 완료 후 `git fetch origin main`을 실행하여 로컬과 원격의 커밋 해시가 정확히 일치하는지 비교 검증합니다:
     ```powershell
     $localHash = (git rev-parse HEAD).Trim()
     $remoteHash = (git rev-parse origin/main).Trim()
     if ($localHash -eq $remoteHash) { "Git 동기화 성공" } else { "Git 동기화 불일치 오류" }
     ```
   - 검증 결과를 테이블 형태의 최종 상태 리포트로 출력합니다.


## ⚙️ Core Automation: Auto-Hunt Workflow
1. **News Hunting**: Scrape latest headlines.
2. **Market Update**: Trigger `market-analyst` and `us-market-analyst` skills.
3. **Deep Valuation**: Sequentially update sector reports with verified prices and recalibrated target prices.
4. **Timestamp Sync**: PowerShell sync to current **Korea Standard Time (KST)**.
5. **Deployment**: **ONLY on explicit command.** Manual execution of `git push` logic to preserve local-only update capability.

## 🤖 AI Skills & Branding
- **Branding**: Always uses **"Soul's"** and follows a **Personal Insight** style.
- **Logic**:
  - **Domestic 2 : US 1** stock composition ratio.
  - **Macro Risk Discounting**: Includes War, Currency (>1,450 KRW), and Supply Chain factors.
  - **Valuation Models**: Optimistic, Base, and Bear scenarios with Weighted Average Target Prices.

---
*Last Updated: 2026-06-11 11:31 KST*
