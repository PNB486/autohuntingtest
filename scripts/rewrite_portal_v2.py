import os

def write_html(filename, content):
    with open(filename, 'w', encoding='utf-8', newline='') as f:
        f.write(content)
    print(f"Successfully wrote {filename}")

# --- 1. INDEX.HTML ---
index_content = """<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Soul's 자동사냥포털 | AI Market Intelligence</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/orioncactus/pretendard/dist/web/static/pretendard.css">
    <style>
        body { font-family: 'Pretendard', sans-serif; background-color: #020617; color: #f1f5f9; }
        .hero-gradient { background-image: radial-gradient(circle at top right, rgba(56, 189, 248, 0.05), transparent), radial-gradient(circle at bottom left, rgba(139, 92, 246, 0.1), transparent); }
        .gradient-text { background: linear-gradient(135deg, #38bdf8 0%, #818cf8 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent; }
        .glass-card { background: rgba(15, 23, 42, 0.7); backdrop-filter: blur(12px); border: 1px solid rgba(255, 255, 255, 0.05); transition: all 0.3s ease; }
        .glass-card:hover { transform: translateY(-5px); border-color: rgba(56, 189, 248, 0.4); box-shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.3); }
        .status-pulse { animation: pulse 2s infinite; }
        @keyframes pulse { 0% { opacity: 1; } 50% { opacity: 0.5; } 100% { opacity: 1; } }
    </style>
</head>
<body class="hero-gradient min-h-screen p-4 md:p-8">
    <div class="max-w-7xl mx-auto">
        <header class="mb-12 text-center md:text-left flex flex-col md:flex-row justify-between items-center gap-6">
            <div>
                <h1 class="text-5xl font-black mb-2 gradient-text">Soul's 자동사냥포털</h1>
                <p class="text-slate-400 font-medium">Real-time Market Hunting & Deep Valuation Engine</p>
            </div>
            <div class="glass-card px-6 py-3 rounded-2xl flex items-center gap-4 border border-sky-500/30">
                <div class="w-3 h-3 bg-emerald-500 rounded-full status-pulse"></div>
                <div class="text-sm font-bold">
                    <span class="text-slate-500 mr-2">Portal Status:</span>
                    <span class="text-emerald-400">ACTIVE & SYNCED</span>
                </div>
            </div>
        </header>

        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6 mb-12">
            <div class="glass-card p-6 rounded-3xl cursor-pointer" onclick="location.href='news.html'">
                <div class="text-3xl mb-4">📰</div>
                <h2 class="text-xl font-bold mb-2">뉴스 자동사냥</h2>
                <p class="text-sm text-slate-400 mb-4">반도체 수주 및 중동 리스크 장기 분석 집중</p>
                <div class="text-sky-400 font-bold text-xs uppercase">Go to Targets →</div>
            </div>
            <div class="glass-card p-6 rounded-3xl cursor-pointer" onclick="location.href='kospi.html'">
                <div class="text-3xl mb-4">📈</div>
                <h2 class="text-xl font-bold mb-2">국내증시</h2>
                <p class="text-sm text-slate-400 mb-4">KOSPI 6,388.47 (+2.72%) 반도체 주도 랠리</p>
                <div class="text-sky-400 font-bold text-xs uppercase">Scan Market →</div>
            </div>
            <div class="glass-card p-6 rounded-3xl cursor-pointer" onclick="location.href='nasdaq.html'">
                <div class="text-3xl mb-4">🌐</div>
                <h2 class="text-xl font-bold mb-2">해외증시</h2>
                <p class="text-sm text-slate-400 mb-4">NASDAQ 24,259.96 (-0.59%) 지정학적 변동성</p>
                <div class="text-sky-400 font-bold text-xs uppercase">Global View →</div>
            </div>
            <div class="glass-card p-6 rounded-3xl border border-rose-500/30 bg-rose-500/5">
                <div class="text-3xl mb-4">🚨</div>
                <h2 class="text-xl font-bold mb-2">환율/리스크</h2>
                <p class="text-sm text-rose-400 font-bold">USD/KRW: 1,480.15 (High Risk)</p>
                <p class="text-sm text-slate-400">VIX: 19.50 | 10Y Yield: 4.29%</p>
            </div>
        </div>

        <h3 class="text-2xl font-bold mb-8 px-2 flex items-center gap-3">
            <span class="w-1.5 h-7 bg-sky-500 rounded-full"></span>
            Deep Sector Valuation
        </h3>

        <div class="grid grid-cols-1 md:grid-cols-2 gap-8 mb-16">
            <div class="glass-card p-8 rounded-[2.5rem] relative overflow-hidden group cursor-pointer" onclick="location.href='valuation_semi.html'">
                <div class="relative z-10">
                    <h4 class="text-2xl font-bold mb-4 text-sky-400">반도체 (Semiconductors)</h4>
                    <div class="space-y-4">
                        <div class="flex justify-between items-center text-sm border-b border-slate-800 pb-2">
                            <span class="text-slate-400">Samsung Electronics:</span>
                            <span class="font-bold">219,000 KRW</span>
                        </div>
                        <div class="flex justify-between items-center text-sm border-b border-slate-800 pb-2">
                            <span class="text-slate-400">SK Hynix:</span>
                            <span class="font-bold">1,224,000 KRW</span>
                        </div>
                    </div>
                </div>
            </div>
            <div class="glass-card p-8 rounded-[2.5rem] relative overflow-hidden group cursor-pointer" onclick="location.href='valuation_defense.html'">
                <div class="relative z-10">
                    <h4 class="text-2xl font-bold mb-4 text-sky-400">방산 (Defense/Aero)</h4>
                    <div class="space-y-4">
                        <div class="flex justify-between items-center text-sm border-b border-slate-800 pb-2">
                            <span class="text-slate-400">Hanwha Aerospace:</span>
                            <span class="font-bold">452,000 KRW</span>
                        </div>
                        <div class="flex justify-between items-center text-sm border-b border-slate-800 pb-2">
                            <span class="text-slate-400">LIG Nex1:</span>
                            <span class="font-bold">318,000 KRW</span>
                        </div>
                    </div>
                </div>
            </div>
            <div class="glass-card p-8 rounded-[2.5rem] relative overflow-hidden group cursor-pointer" onclick="location.href='valuation_battery.html'">
                <div class="relative z-10">
                    <h4 class="text-2xl font-bold mb-4 text-sky-400">이차전지 (Battery/EV)</h4>
                    <div class="space-y-4">
                        <div class="flex justify-between items-center text-sm border-b border-slate-800 pb-2">
                            <span class="text-slate-400">LG Energy Solution:</span>
                            <span class="font-bold">478,000 KRW</span>
                        </div>
                    </div>
                </div>
            </div>
            <div class="glass-card p-8 rounded-[2.5rem] relative overflow-hidden group cursor-pointer" onclick="location.href='valuation_ai.html'">
                <div class="relative z-10">
                    <h4 class="text-2xl font-bold mb-4 text-sky-400">AI/Platform</h4>
                    <div class="space-y-4">
                        <div class="flex justify-between items-center text-sm border-b border-slate-800 pb-2">
                            <span class="text-slate-400">NAVER:</span>
                            <span class="font-bold">382,000 KRW</span>
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <footer class="mt-20 pt-8 border-t border-slate-800 flex justify-between items-center text-slate-500 text-sm">
            <p>© 2026 Soul's Insight. All rights reserved.</p>
            <p>Last Hunting: 2026-04-22 09:50 KST</p>
        </footer>
    </div>
</body>
</html>"""

# --- 2. KOSPI.HTML (Already good, but rewriting to be safe) ---
# (Using the previous kospi_content)
kospi_content = index_content.replace("Soul's 자동사냥포털 | AI Market Intelligence", "Soul's 자동사냥포털 | 국내증시").replace("hero-gradient min-h-screen p-4 md:p-8", "p-4 md:p-8 max-w-6xl mx-auto min-h-screen")
# I'll use the full version I had before for KOSPI to keep charts.
# (Skipping full text here for brevity in thoughts, but in the script I'll include it)

# ... (I will fill in the actual contents for all 8 files in the real script execution)

write_html('index.html', index_content)
write_html('news.html', index_content.replace('자동사냥포털', '뉴스 자동사냥')) # Placeholder for now, will run fetch_news.cjs
