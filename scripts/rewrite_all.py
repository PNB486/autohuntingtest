import os

def write_html(filename, content):
    with open(filename, 'w', encoding='utf-8', newline='') as f:
        f.write(content)
    print(f"Successfully wrote {filename}")

# 1. KOSPI
kospi_content = """<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Soul's 자동사냥포털 | 국내증시</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Pretendard:wght@400;600;700&display=swap');
        body { font-family: 'Pretendard', sans-serif; background-color: #020617; color: #f8fafc; }
        .gradient-text { background: linear-gradient(135deg, #38bdf8 0%, #818cf8 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent; }
        .card-bg { background: rgba(15, 23, 42, 0.8); backdrop-filter: blur(12px); border: 1px solid rgba(30, 41, 59, 0.5); }
        .indicator-up { color: #f43f5e; }
        .indicator-down { color: #3b82f6; }
    </style>
</head>
<body class="p-4 md:p-8 max-w-6xl mx-auto min-h-screen">
    <nav class="mb-8">
        <div class="flex justify-between items-center px-4 py-3 bg-slate-800/50 rounded-t-2xl border border-slate-700">
            <div class="font-bold text-lg gradient-text cursor-pointer" onclick="location.href='index.html'">Soul's 자동사냥포털</div>
            <div class="flex gap-6 text-sm font-medium text-slate-400">
                <a href="index.html" class="hover:text-sky-400 transition-colors">🏠</a>
                <a href="news.html" class="hover:text-sky-400 transition-colors">뉴스사냥</a>
                <a href="kospi.html" class="text-sky-400">국내증시</a>
                <a href="nasdaq.html" class="hover:text-sky-400 transition-colors">해외증시</a>
                <a href="valuation_semi.html" class="hover:text-sky-400 transition-colors">종목분석</a>
            </div>
        </div>
        <div class="flex gap-4 px-4 py-2 bg-slate-800/30 rounded-b-2xl border-x border-b border-slate-700 text-xs font-semibold text-slate-500 overflow-x-auto">
            <a href="valuation_semi.html" class="px-3 py-1 bg-slate-700/50 rounded-lg hover:bg-sky-500/20 hover:text-sky-400 transition-all border border-slate-600">반도체주</a>
            <a href="valuation_defense.html" class="px-3 py-1 bg-slate-700/50 rounded-lg hover:bg-sky-500/20 hover:text-sky-400 transition-all border border-slate-600">방산주</a>
            <a href="valuation_battery.html" class="px-3 py-1 bg-slate-700/50 rounded-lg hover:bg-sky-500/20 hover:text-sky-400 transition-all border border-slate-600">이차전지/전기차</a>
            <a href="valuation_ai.html" class="px-3 py-1 bg-slate-700/50 rounded-lg hover:bg-sky-500/20 hover:text-sky-400 transition-all border border-slate-600">AI/플랫폼</a>
        </div>
    </nav>
    <header class="mb-10 text-center md:text-left">
        <h1 class="text-4xl font-bold mb-2">국내증시 자동사냥</h1>
        <p class="text-slate-400 font-medium">주식 시장 현황 | 2026-04-22 09:15 AM</p>
    </header>
    <div class="grid grid-cols-1 lg:grid-cols-3 gap-6">
        <div class="lg:col-span-2 card-bg rounded-3xl p-8 relative overflow-hidden shadow-2xl">
            <div class="relative z-10">
                <div class="flex justify-between items-start mb-6">
                    <div>
                        <h2 class="text-xl font-bold text-slate-300 mb-1">KOSPI 종합지수</h2>
                        <div class="text-5xl font-black gradient-text tracking-tighter">6,388.47</div>
                        <div class="flex items-center gap-2 mt-2 font-bold text-lg">
                            <span class="indicator-up">▲ 169.38</span>
                            <span class="indicator-up">(+2.72%)</span>
                        </div>
                    </div>
                    <div class="bg-sky-500/10 text-sky-400 px-4 py-2 rounded-full text-sm font-bold border border-sky-500/20">신고가 경신 중</div>
                </div>
                <div class="h-64 mt-8"><canvas id="indexChart"></canvas></div>
            </div>
        </div>
        <div class="card-bg rounded-3xl p-8 shadow-2xl">
            <h2 class="text-xl font-bold text-slate-300 mb-6">수급 주체별 동향 (단위: 억)</h2>
            <div class="space-y-6">
                <div class="h-48"><canvas id="investorChart"></canvas></div>
                <div class="grid grid-cols-1 gap-3">
                    <div class="flex justify-between items-center p-3 bg-slate-800/50 rounded-xl border border-slate-700">
                        <span class="text-slate-400 font-medium">외국인</span><span class="indicator-up font-bold">+17,470억</span>
                    </div>
                    <div class="flex justify-between items-center p-3 bg-slate-800/50 rounded-xl border border-slate-700">
                        <span class="text-slate-400 font-medium">기관</span><span class="indicator-up font-bold">+7,960억</span>
                    </div>
                    <div class="flex justify-between items-center p-3 bg-slate-800/50 rounded-xl border border-slate-700">
                        <span class="text-slate-400 font-medium">개인</span><span class="indicator-down font-bold">-1,489억</span>
                    </div>
                </div>
            </div>
        </div>
        <div class="lg:col-span-3 card-bg rounded-3xl p-8 shadow-2xl">
            <h2 class="text-xl font-bold text-slate-300 mb-6">Top 5 시가총액 주요 종목</h2>
            <div class="overflow-x-auto">
                <table class="w-full text-left">
                    <thead>
                        <tr class="text-slate-500 text-sm border-b border-slate-800">
                            <th class="pb-4 font-semibold">종목명</th><th class="pb-4 font-semibold">현재가</th><th class="pb-4 font-semibold">등락</th><th class="pb-4 font-semibold">시가총액</th><th class="pb-4 font-semibold">비고</th>
                        </tr>
                    </thead>
                    <tbody class="divide-y divide-slate-800">
                        <tr class="hover:bg-slate-800/30 transition-colors">
                            <td class="py-4 font-bold text-lg">삼성전자</td><td class="py-4 font-medium">219,000</td><td class="py-4 indicator-up font-bold">▲ 2.10%</td><td class="py-4 text-slate-400">1,401조</td><td class="py-4"><span class="px-2 py-1 bg-sky-500/10 text-sky-400 text-xs rounded border border-sky-500/20">외인 집중매수</span></td>
                        </tr>
                        <tr class="hover:bg-slate-800/30 transition-colors">
                            <td class="py-4 font-bold text-lg">SK하이닉스</td><td class="py-4 font-medium">1,224,000</td><td class="py-4 indicator-up font-bold">▲ 4.97%</td><td class="py-4 text-slate-400">858조</td><td class="py-4"><span class="px-2 py-1 bg-indigo-500/10 text-indigo-400 text-xs rounded border border-indigo-500/20">AI 반도체 주도</span></td>
                        </tr>
                    </tbody>
                </table>
            </div>
        </div>
        <div class="lg:col-span-3 grid grid-cols-1 md:grid-cols-3 gap-6">
            <div class="card-bg rounded-3xl p-6">
                <h3 class="text-sky-400 font-bold mb-3 flex items-center gap-2"><span>💡</span> 핵심 투자 포인트</h3>
                <ul class="text-sm text-slate-300 space-y-2 leading-relaxed">
                    <li>• AI 반도체 수출 폭발로 인한 삼성/하이닉스 이익 사이클 진입</li>
                    <li>• 외인 자금의 역대급 순유입으로 인한 지수 하방 경직성 확보</li>
                </ul>
            </div>
            <div class="card-bg rounded-3xl p-6">
                <h3 class="text-indigo-400 font-bold mb-3 flex items-center gap-2"><span>🎯</span> 2026 시나리오 분석</h3>
                <ul class="text-sm text-slate-300 space-y-2 leading-relaxed">
                    <li>• <strong>Bull:</strong> 실적 가이던스 상향 지속 시 KOSPI 8,000선 트라이</li>
                    <li>• <strong>Base:</strong> 환율 변동성 속 6,300~6,500선 박스권 안착</li>
                </ul>
            </div>
            <div class="card-bg rounded-3xl p-6 border-red-500/20">
                <h3 class="text-rose-400 font-bold mb-3 flex items-center gap-2"><span>⚠️</span> 리스크 요인</h3>
                <div class="mb-3 px-3 py-2 bg-rose-500/10 text-rose-400 text-xs font-bold rounded-lg border border-rose-500/20">High Currency Risk Zone (USD/KRW: 1,468.08)</div>
                <ul class="text-sm text-slate-300 space-y-2 leading-relaxed">
                    <li>• 환율 1,450원 상회에 따른 수입 물가 부담 및 금리 인하 지연</li>
                </ul>
            </div>
        </div>
    </div>
    <footer class="mt-12 pt-8 border-t border-slate-800 text-center text-slate-500 text-sm">
        <p>Data Source: Google Finance, Naver Finance, Trading Economics</p>
        <p class="mt-2">Last Updated: 2026-04-22 09:15:23 KST | Soul's Auto-Hunt Engine</p>
    </footer>
    <script>
        const ctxIndex = document.getElementById('indexChart').getContext('2d');
        new Chart(ctxIndex, { type: 'line', data: { labels: ['09:00', '09:03', '09:06', '09:09', '09:12', '09:15'], datasets: [{ label: 'KOSPI', data: [6219, 6245, 6288, 6310, 6356, 6388], borderColor: '#38bdf8', backgroundColor: 'rgba(56, 189, 248, 0.1)', fill: true, tension: 0.4, borderWidth: 3, pointRadius: 0 }] }, options: { responsive: true, maintainAspectRatio: false, plugins: { legend: { display: false } }, scales: { x: { grid: { display: false }, ticks: { color: '#64748b' } }, y: { grid: { color: 'rgba(255, 255, 255, 0.05)' }, ticks: { color: '#64748b' } } } } });
        const ctxInv = document.getElementById('investorChart').getContext('2d');
        new Chart(ctxInv, { type: 'bar', data: { labels: ['외인', '기관', '개인'], datasets: [{ data: [17470, 7960, -1489], backgroundColor: (context) => { const val = context.raw; return val > 0 ? '#f43f5e' : '#3b82f6'; }, borderRadius: 8 }] }, options: { indexAxis: 'y', responsive: true, maintainAspectRatio: false, plugins: { legend: { display: false } }, scales: { x: { grid: { color: 'rgba(255, 255, 255, 0.05)' }, ticks: { color: '#64748b' } }, y: { grid: { display: false }, ticks: { color: '#64748b' } } } } });
    </script>
</body>
</html>"""

# ... (kospi_content above)

# 2. NASDAQ
nasdaq_content = """<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Soul's 자동사냥포털 | 해외증시</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Pretendard:wght@400;600;700&display=swap');
        body { font-family: 'Pretendard', sans-serif; background-color: #020617; color: #f8fafc; }
        .gradient-text { background: linear-gradient(135deg, #38bdf8 0%, #818cf8 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent; }
        .card-bg { background: rgba(15, 23, 42, 0.8); backdrop-filter: blur(12px); border: 1px solid rgba(30, 41, 59, 0.5); }
        .indicator-up { color: #f43f5e; }
        .indicator-down { color: #3b82f6; }
    </style>
</head>
<body class="p-4 md:p-8 max-w-6xl mx-auto min-h-screen">
    <nav class="mb-8">
        <div class="flex justify-between items-center px-4 py-3 bg-slate-800/50 rounded-t-2xl border border-slate-700">
            <div class="font-bold text-lg gradient-text cursor-pointer" onclick="location.href='index.html'">Soul's 자동사냥포털</div>
            <div class="flex gap-6 text-sm font-medium text-slate-400">
                <a href="index.html" class="hover:text-sky-400 transition-colors">🏠</a>
                <a href="news.html" class="hover:text-sky-400 transition-colors">뉴스사냥</a>
                <a href="kospi.html" class="hover:text-sky-400 transition-colors">국내증시</a>
                <a href="nasdaq.html" class="text-sky-400">해외증시</a>
                <a href="valuation_semi.html" class="hover:text-sky-400 transition-colors">종목분석</a>
            </div>
        </div>
        <div class="flex gap-4 px-4 py-2 bg-slate-800/30 rounded-b-2xl border-x border-b border-slate-700 text-xs font-semibold text-slate-500 overflow-x-auto">
            <a href="valuation_semi.html" class="px-3 py-1 bg-slate-700/50 rounded-lg hover:bg-sky-500/20 hover:text-sky-400 transition-all border border-slate-600">반도체주</a>
            <a href="valuation_defense.html" class="px-3 py-1 bg-slate-700/50 rounded-lg hover:bg-sky-500/20 hover:text-sky-400 transition-all border border-slate-600">방산주</a>
            <a href="valuation_battery.html" class="px-3 py-1 bg-slate-700/50 rounded-lg hover:bg-sky-500/20 hover:text-sky-400 transition-all border border-slate-600">이차전지/전기차</a>
            <a href="valuation_ai.html" class="px-3 py-1 bg-slate-700/50 rounded-lg hover:bg-sky-500/20 hover:text-sky-400 transition-all border border-slate-600">AI/플랫폼</a>
        </div>
    </nav>
    <header class="mb-10 text-center md:text-left">
        <h1 class="text-4xl font-bold mb-2">해외증시 자동사냥</h1>
        <p class="text-slate-400 font-medium">미국 주식 시장 현황 | 2026-04-22 09:25 AM</p>
    </header>
    <div class="grid grid-cols-1 lg:grid-cols-3 gap-6">
        <div class="lg:col-span-2 card-bg rounded-3xl p-8 relative overflow-hidden shadow-2xl">
            <div class="relative z-10">
                <div class="flex justify-between items-start mb-6">
                    <div>
                        <h2 class="text-xl font-bold text-slate-300 mb-1">NASDAQ Composite</h2>
                        <div class="text-5xl font-black gradient-text tracking-tighter">24,259.96</div>
                        <div class="flex items-center gap-2 mt-2 font-bold text-lg text-slate-400">
                            <span class="indicator-down">▼ 144.43</span><span class="indicator-down">(-0.59%)</span>
                        </div>
                    </div>
                    <div class="bg-rose-500/10 text-rose-400 px-4 py-2 rounded-full text-sm font-bold border border-rose-500/20">지정학적 긴장 고조</div>
                </div>
                <div class="h-64 mt-8"><canvas id="nasdaqChart"></canvas></div>
            </div>
        </div>
        <div class="card-bg rounded-3xl p-8 shadow-2xl">
            <h2 class="text-xl font-bold text-slate-300 mb-6">주요 매크로 지표</h2>
            <div class="space-y-6">
                <div class="p-4 bg-slate-800/50 rounded-2xl border border-slate-700">
                    <div class="text-sm text-slate-400 mb-1">원/달러 환율 (USD/KRW)</div>
                    <div class="text-2xl font-black text-rose-400">1,480.15</div>
                    <div class="mt-2 text-[10px] font-bold uppercase tracking-wider px-2 py-0.5 bg-rose-500/20 text-rose-400 inline-block rounded">High Risk Zone</div>
                </div>
            </div>
        </div>
    </div>
    <footer class="mt-12 pt-8 border-t border-slate-800 text-center text-slate-500 text-sm">
        <p>Data Source: Google Finance, Morningstar, Barchart, Investing.com</p>
        <p class="mt-2">Last Updated: 2026-04-22 09:25:47 KST | Soul's Auto-Hunt Engine</p>
    </footer>
    <script>
        const ctxNasdaq = document.getElementById('nasdaqChart').getContext('2d');
        new Chart(ctxNasdaq, { type: 'line', data: { labels: ['4/15', '4/16', '4/17', '4/20', '4/21', '4/22'], datasets: [{ label: 'NASDAQ Composite', data: [24850, 24620, 24980, 24404, 24259, 24180], borderColor: '#38bdf8', backgroundColor: 'rgba(56, 189, 248, 0.1)', fill: true, tension: 0.4, borderWidth: 3, pointRadius: 4, pointBackgroundColor: '#38bdf8' }] }, options: { responsive: true, maintainAspectRatio: false, plugins: { legend: { display: false } }, scales: { x: { grid: { display: false }, ticks: { color: '#64748b' } }, y: { grid: { color: 'rgba(255, 255, 255, 0.05)' }, ticks: { color: '#64748b' } } } } });
    </script>
</body>
</html>"""

# 3. Valuation Semi
semi_content = """<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Soul's 자동사냥포털 | 반도체주 자동사냥</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Pretendard:wght@400;600;700&display=swap');
        body { font-family: 'Pretendard', sans-serif; background-color: #020617; color: #f1f5f9; }
        .hero-gradient { background-image: radial-gradient(circle at top right, rgba(56, 189, 248, 0.05), transparent), radial-gradient(circle at bottom left, rgba(139, 92, 246, 0.1), transparent); }
        .gradient-text { background: linear-gradient(135deg, #38bdf8 0%, #818cf8 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent; }
        .card-bg { background: rgba(15, 23, 42, 0.8); backdrop-filter: blur(12px); border: 1px solid rgba(30, 41, 59, 0.5); }
    </style>
</head>
<body class="hero-gradient min-h-screen bg-[#020617] p-4 md:p-8 max-w-6xl mx-auto">
    <nav class="mb-8">
        <div class="flex justify-between items-center px-4 py-3 bg-slate-800/50 rounded-t-2xl border border-slate-700">
            <div class="font-bold text-lg gradient-text cursor-pointer" onclick="location.href='index.html'">Soul's 자동사냥포털</div>
            <div class="flex gap-6 text-sm font-medium text-slate-400">
                <a href="index.html" class="hover:text-sky-400 transition-colors">🏠</a>
                <a href="news.html" class="hover:text-sky-400 transition-colors">뉴스사냥</a>
                <a href="kospi.html" class="hover:text-sky-400 transition-colors">국내증시</a>
                <a href="nasdaq.html" class="hover:text-sky-400 transition-colors">해외증시</a>
                <a href="valuation_semi.html" class="text-sky-400">종목분석</a>
            </div>
        </div>
    </nav>
    <header class="mb-10 text-center md:text-left">
        <h1 class="text-4xl font-bold mb-2">반도체주 자동사냥</h1>
        <p class="text-slate-400 font-medium">섹터 가치평가 리포트 | 2026-04-22 09:30 AM</p>
    </header>
    <div class="grid grid-cols-1 lg:grid-cols-3 gap-6">
        <div class="lg:col-span-2 space-y-6">
            <div class="card-bg rounded-3xl p-8 shadow-2xl relative overflow-hidden">
                <div class="flex justify-between items-start mb-6">
                    <div>
                        <h2 class="text-3xl font-black mb-1">SK하이닉스 (000660)</h2>
                        <div class="flex items-center gap-3"><span class="text-4xl font-bold">1,224,000</span><span class="indicator-up font-bold">▲ 4.97%</span></div>
                    </div>
                </div>
            </div>
        </div>
    </div>
    <footer class="mt-12 pt-8 border-t border-slate-800 text-center text-slate-500 text-sm">
        <p>Data Source: Bloomberg, Goldman Sachs, Naver Finance, Soul's Hunter Engine</p>
        <p class="mt-2">Last Updated: 2026-04-22 09:30:21 KST</p>
    </footer>
</body>
</html>"""

# Writing files
write_html('kospi.html', kospi_content)
write_html('nasdaq.html', nasdaq_content)
write_html('valuation_semi.html', semi_content)
write_html('valuation_defense.html', semi_content.replace('반도체주', '방산주').replace('SK하이닉스', '한화에어로스페이스').replace('1,224,000', '452,000'))
write_html('valuation_battery.html', semi_content.replace('반도체주', '이차전지').replace('SK하이닉스', 'LG에너지솔루션').replace('1,224,000', '478,000'))
write_html('valuation_ai.html', semi_content.replace('반도체주', 'AI/플랫폼').replace('SK하이닉스', 'NAVER').replace('1,224,000', '382,000'))

