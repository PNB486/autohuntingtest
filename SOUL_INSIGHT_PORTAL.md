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
- **Real-time Verification**: All prices must be verified in real-time via Google/Naver Finance during generation.

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
*Last Updated: 2026-04-08 17:00 KST*
