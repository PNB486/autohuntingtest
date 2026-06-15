# -*- coding: utf-8 -*-
import os
import re

def integrate():
    base_dir = r"C:\Users\S\Desktop\AI\Gemini\Stock"
    
    # 1. Update index.html
    index_path = os.path.join(base_dir, "index.html")
    if os.path.exists(index_path):
        with open(index_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # Add Chart.js to head
        head_end = content.find('</head>')
        if 'chart.umd.min.js' not in content:
            chart_script = '    <script src="https://cdn.jsdelivr.net/npm/chart.js@4.4.1/dist/chart.umd.min.js"></script>\n'
            content = content[:head_end] + chart_script + content[head_end:]
            
        # Add 5th Card to Main Navigation Grid
        # Let's locate the navigation grid closing </div> (before <!-- Valuation Sub-Grid -->)
        grid_start = content.find('<!-- Main Navigation Grid -->')
        grid_end = content.find('</div>', grid_start)
        # Wait, the grid spans multiple lines. Let's find the closing </div> of that grid.
        # It's right before <!-- Valuation Sub-Grid --> or <div id="valuation-section" class="mb-12">
        # In current index.html:
        # Line 77: <span class="mt-4 text-[10px] bg-slate-800 text-slate-400 px-2 py-1 rounded font-bold uppercase tracking-wider">DEEP ANALYSIS</span>
        # Line 78: </a>
        # Line 79: </div>
        # Let's target:
        old_grid_end = """            <a href="#valuation-section" class="card p-8 flex flex-col items-center text-center">
                <div class="w-16 h-16 bg-amber-500/10 rounded-2xl flex items-center justify-center text-3xl mb-4">🔍</div>
                <h3 class="text-xl font-bold mb-2">심층 밸류에이션</h3>
                <p class="text-sm text-slate-500 leading-relaxed">삼성전자/하이닉스 적정가 상향 및 리스크 분석</p>
                <span class="mt-4 text-[10px] bg-slate-800 text-slate-400 px-2 py-1 rounded font-bold uppercase tracking-wider">DEEP ANALYSIS</span>
            </a>
        </div>"""
        
        # Modify to lg:grid-cols-5
        content = content.replace('<div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6 mb-16">',
                                  '<div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-5 gap-4 mb-16">')
        
        new_grid_end = """            <a href="#valuation-section" class="card p-8 flex flex-col items-center text-center">
                <div class="w-16 h-16 bg-amber-500/10 rounded-2xl flex items-center justify-center text-3xl mb-4">🔍</div>
                <h3 class="text-xl font-bold mb-2">심층 밸류에이션</h3>
                <p class="text-sm text-slate-500 leading-relaxed">삼성전자/하이닉스 적정가 상향 및 리스크 분석</p>
                <span class="mt-4 text-[10px] bg-slate-800 text-slate-400 px-2 py-1 rounded font-bold uppercase tracking-wider">DEEP ANALYSIS</span>
            </a>
            <a href="valuation_interactive_demo.html" class="card p-8 flex flex-col items-center text-center border-sky-400/20 hover:border-sky-400">
                <div class="w-16 h-16 bg-sky-500/10 rounded-2xl flex items-center justify-center text-3xl mb-4">🎛️</div>
                <h3 class="text-xl font-bold mb-2">실시간 시뮬레이터</h3>
                <p class="text-sm text-slate-500 leading-relaxed">환율 및 리스크에 따른 적정가 시뮬레이션</p>
                <span class="mt-4 text-[10px] bg-sky-500/20 text-sky-400 px-2 py-1 rounded font-bold uppercase tracking-wider">INTERACTIVE</span>
            </a>
        </div>"""
        
        content = content.replace(old_grid_end, new_grid_end)
        
        # 2. Side Card for "Domestic 2 : US 1" Portfolio Chart
        valuation_section_old = """        <!-- Valuation Sub-Grid -->
        <div id="valuation-section" class="mb-12">
            <h2 class="text-2xl font-extrabold mb-8 flex items-center gap-3">
                <span class="w-2.5 h-8 bg-sky-400 rounded-full"></span>
                섹터별 실시간 가치 평가 리포트
            </h2>
            <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
                <a href="valuation_semi.html" class="flex items-center p-6 bg-slate-900/50 rounded-3xl border border-sky-600 hover:bg-slate-800/50 transition-all group shadow-lg shadow-sky-900/20">
                    <div class="text-3xl mr-6 filter grayscale group-hover:grayscale-0 transition-all">💾</div>
                    <div>
                        <h4 class="font-bold text-lg">반도체 섹터</h4>
                        <p class="text-xs text-slate-500 mt-1 leading-relaxed">HBM4 양산 모멘텀 반영, 목표가 48만 상향 (삼전)</p>
                        <p class="text-[10px] text-sky-400 mt-1 font-black uppercase tracking-tighter">Strong Bullish Bias</p>
                    </div>
                    <div class="ml-auto text-sky-400 font-black group-hover:translate-x-1 transition-transform">→</div>
                </a>
                <a href="valuation_defense.html" class="flex items-center p-6 bg-slate-900/50 rounded-3xl border border-slate-800 hover:bg-slate-800/50 transition-all group">
                    <div class="text-3xl mr-6 filter grayscale group-hover:grayscale-0 transition-all">🛡️</div>
                    <div>
                        <h4 class="font-bold text-lg">방산 섹터</h4>
                        <p class="text-xs text-slate-500 mt-1 leading-relaxed">수주잔고 및 해외 MRO 사업 모멘텀 분석</p>
                    </div>
                    <div class="ml-auto text-sky-400 font-black group-hover:translate-x-1 transition-transform">→</div>
                </a>
                <a href="valuation_battery.html" class="flex items-center p-6 bg-slate-900/50 rounded-3xl border border-slate-800 hover:bg-slate-800/50 transition-all group">
                    <div class="text-3xl mr-6 filter grayscale group-hover:grayscale-0 transition-all">🔋</div>
                    <div>
                        <h4 class="font-bold text-lg">이차전지/전기차</h4>
                        <p class="text-xs text-slate-500 mt-1 leading-relaxed">전기차 캐즘 돌파 및 실적 턴어라운드 진단</p>
                    </div>
                    <div class="ml-auto text-sky-400 font-black group-hover:translate-x-1 transition-transform">→</div>
                </a>
                <a href="valuation_ai.html" class="flex items-center p-6 bg-slate-900/50 rounded-3xl border border-slate-800 hover:bg-slate-800/50 transition-all group">
                    <div class="text-3xl mr-6 filter grayscale group-hover:grayscale-0 transition-all">🤖</div>
                    <div>
                        <h4 class="font-bold text-lg">AI/플랫폼 섹터</h4>
                        <p class="text-xs text-slate-500 mt-1 leading-relaxed">B2B 유료화 모델 및 글로벌 AI 경쟁력 분석</p>
                    </div>
                    <div class="ml-auto text-sky-400 font-black group-hover:translate-x-1 transition-transform">→</div>
                </a>
            </div>
        </div>"""
        
        valuation_section_new = """        <!-- Valuation & Portfolio Section -->
        <div id="valuation-section" class="mb-12">
            <div class="grid grid-cols-1 lg:grid-cols-3 gap-8">
                <!-- Left 2 columns: Valuation Reports -->
                <div class="lg:col-span-2">
                    <h2 class="text-2xl font-extrabold mb-8 flex items-center gap-3">
                        <span class="w-2.5 h-8 bg-sky-400 rounded-full"></span>
                        섹터별 실시간 가치 평가 리포트
                    </h2>
                    <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
                        <a href="valuation_semi.html" class="flex items-center p-6 bg-slate-900/50 rounded-3xl border border-sky-600 hover:bg-slate-800/50 transition-all group shadow-lg shadow-sky-900/20">
                            <div class="text-3xl mr-6 filter grayscale group-hover:grayscale-0 transition-all">💾</div>
                            <div>
                                <h4 class="font-bold text-lg">반도체 섹터</h4>
                                <p class="text-xs text-slate-500 mt-1 leading-relaxed">HBM4 양산 모멘텀 반영, 목표가 48만 상향 (삼전)</p>
                                <p class="text-[10px] text-sky-400 mt-1 font-black uppercase tracking-tighter">Strong Bullish Bias</p>
                            </div>
                            <div class="ml-auto text-sky-400 font-black group-hover:translate-x-1 transition-transform">→</div>
                        </a>
                        <a href="valuation_defense.html" class="flex items-center p-6 bg-slate-900/50 rounded-3xl border border-slate-800 hover:bg-slate-800/50 transition-all group">
                            <div class="text-3xl mr-6 filter grayscale group-hover:grayscale-0 transition-all">🛡️</div>
                            <div>
                                <h4 class="font-bold text-lg">방산 섹터</h4>
                                <p class="text-xs text-slate-500 mt-1 leading-relaxed">수주잔고 및 해외 MRO 사업 모멘텀 분석</p>
                            </div>
                            <div class="ml-auto text-sky-400 font-black group-hover:translate-x-1 transition-transform">→</div>
                        </a>
                        <a href="valuation_battery.html" class="flex items-center p-6 bg-slate-900/50 rounded-3xl border border-slate-800 hover:bg-slate-800/50 transition-all group">
                            <div class="text-3xl mr-6 filter grayscale group-hover:grayscale-0 transition-all">🔋</div>
                            <div>
                                <h4 class="font-bold text-lg">이차전지/전기차</h4>
                                <p class="text-xs text-slate-500 mt-1 leading-relaxed">전기차 캐즘 돌파 및 실적 턴어라운드 진단</p>
                            </div>
                            <div class="ml-auto text-sky-400 font-black group-hover:translate-x-1 transition-transform">→</div>
                        </a>
                        <a href="valuation_ai.html" class="flex items-center p-6 bg-slate-900/50 rounded-3xl border border-slate-800 hover:bg-slate-800/50 transition-all group">
                            <div class="text-3xl mr-6 filter grayscale group-hover:grayscale-0 transition-all">🤖</div>
                            <div>
                                <h4 class="font-bold text-lg">AI/플랫폼 섹터</h4>
                                <p class="text-xs text-slate-500 mt-1 leading-relaxed">B2B 유료화 모델 및 글로벌 AI 경쟁력 분석</p>
                            </div>
                            <div class="ml-auto text-sky-400 font-black group-hover:translate-x-1 transition-transform">→</div>
                        </a>
                    </div>
                </div>
                <!-- Right 1 column: Portfolio Summary Side Card -->
                <div class="card p-6 flex flex-col justify-between">
                    <div>
                        <h2 class="text-xl font-bold mb-2 flex items-center gap-2">
                            <span class="w-2 h-2 rounded-full bg-sky-400"></span>
                            실시간 포트폴리오 비중
                        </h2>
                        <p class="text-slate-400 text-xs mb-6">"Domestic 2 : US 1" 목표 자산 배분 현황</p>
                        <div class="relative h-[250px] mb-6">
                            <canvas id="portfolioChart"></canvas>
                        </div>
                    </div>
                    <div class="bg-slate-800/40 p-4 rounded-2xl text-xs text-slate-400 space-y-2">
                        <div class="flex justify-between">
                            <span>국내 주식 (KOSPI)</span>
                            <span class="font-bold text-sky-400">66.7%</span>
                        </div>
                        <div class="flex justify-between">
                            <span>해외 주식 (US)</span>
                            <span class="font-bold text-indigo-400">33.3%</span>
                        </div>
                    </div>
                </div>
            </div>
        </div>"""
        
        content = content.replace(valuation_section_old, valuation_section_new)
        
        # Add Javascript initialization for portfolio Chart.js doughnut chart
        js_code = """    <script>
        window.addEventListener('DOMContentLoaded', () => {
            try {
                const ctx = document.getElementById('portfolioChart').getContext('2d');
                new Chart(ctx, {
                    type: 'doughnut',
                    data: {
                        labels: ['국내 주식 (KOSPI)', '해외 주식 (US)'],
                        datasets: [{
                            data: [66.7, 33.3],
                            backgroundColor: ['#38bdf8', '#818cf8'],
                            borderColor: '#0f172a',
                            borderWidth: 3
                        }]
                    },
                    options: {
                        responsive: true,
                        maintainAspectRatio: false,
                        plugins: {
                            legend: {
                                position: 'bottom',
                                labels: {
                                    color: '#94a3b8',
                                    font: { family: 'Pretendard', size: 11 }
                                }
                            }
                        }
                    }
                });
            } catch (e) {
                console.error('Portfolio Chart initialization failed:', e);
            }
        });
    </script>"""
        
        content = content.replace('</body>', js_code + '\n</body>')
        
        # Save timestamp sync
        content = content.replace('2026-05-22 09:45:00 KST', '2026-05-26 11:53:00 KST')
        content = content.replace('2026-05-26 11:53:00 KST', '2026-05-26 11:53 KST')
        content = re.sub(r'SYSTEM UPDATED: \d{4}-\d{2}-\d{2} \d{2}:\d{2} KST', 'SYSTEM UPDATED: 2026-05-26 11:53 KST', content)
        
        with open(index_path, 'w', encoding='utf-8', newline='') as f:
            f.write(content)
        print("Updated index.html with 5th Card and Portfolio doughnut chart")

    # 2. Update valuation_semi.html with sliders and dynamic recalculated valuations
    semi_path = os.path.join(base_dir, "valuation_semi.html")
    if os.path.exists(semi_path):
        with open(semi_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # Update header risk badge to have id
        old_badge = """            <div class="risk-badge px-4 py-2 rounded-xl text-sm font-bold flex items-center gap-2">
                <span>⚠️ High Currency Risk Zone</span>
                <span class="bg-red-500 text-white px-2 py-0.5 rounded">1,517.43</span>
            </div>"""
            
        new_badge = """            <div class="risk-badge px-4 py-2 rounded-xl text-sm font-bold flex items-center gap-2" id="headerRiskBadge">
                <span id="headerRiskLabel">⚠️ High Currency Risk Zone</span>
                <span class="bg-red-500 text-white px-2 py-0.5 rounded" id="headerRiskVal">1,517.43</span>
            </div>"""
        content = content.replace(old_badge, new_badge)
        
        # Insert Slider Panel
        # We place it before the card container: <div class="grid grid-cols-1 md:grid-cols-2 gap-8 mb-12">
        slider_panel = """        <!-- Interactive Simulator Slider Panel -->
        <div class="card-bg p-6 rounded-3xl mb-8 border border-sky-500/20 shadow-lg shadow-sky-950/20">
            <h3 class="text-xl font-bold mb-4 flex items-center gap-2 text-sky-400">
                <span class="w-2.5 h-6 bg-sky-400 rounded-full"></span>
                실시간 매크로 시뮬레이터
            </h3>
            <p class="text-slate-400 text-xs mb-6">원/달러 환율 및 지정학적 리스크 슬라이더를 조정하여 반도체 적정가 및 영업이익 전망치를 실시간 시뮬레이션해 보세요.</p>
            <div class="grid grid-cols-1 md:grid-cols-2 gap-8">
                <!-- USD/KRW Slider -->
                <div class="space-y-2">
                    <div class="flex justify-between items-center text-sm font-semibold">
                        <span class="text-slate-300">원/달러 환율 (USD/KRW)</span>
                        <span class="text-sky-400 font-mono" id="exchangeRateVal">1,517.43 KRW</span>
                    </div>
                    <input type="range" id="exchangeRateSlider" min="1300" max="1700" step="1" value="1517" class="w-full h-2 bg-slate-800 rounded-lg appearance-none cursor-pointer accent-sky-400">
                    <div class="flex justify-between text-[10px] text-slate-500 font-mono">
                        <span>1,300</span>
                        <span>1,450 (위험 임계값)</span>
                        <span>1,700</span>
                    </div>
                </div>
                <!-- Geopolitical Risk Slider -->
                <div class="space-y-2">
                    <div class="flex justify-between items-center text-sm font-semibold">
                        <span class="text-slate-300">지정학적 리스크 지수</span>
                        <span class="text-sky-400 font-mono" id="geoRiskVal">50%</span>
                    </div>
                    <input type="range" id="geoRiskSlider" min="0" max="100" step="1" value="50" class="w-full h-2 bg-slate-800 rounded-lg appearance-none cursor-pointer accent-sky-400">
                    <div class="flex justify-between text-[10px] text-slate-500 font-mono">
                        <span>0% (평화)</span>
                        <span>50% (경계)</span>
                        <span>100% (위험 극대)</span>
                    </div>
                </div>
            </div>
            <!-- High Currency Risk Warning Box -->
            <div id="currencyRiskWarning" class="mt-6 p-4 rounded-2xl bg-red-500/10 border border-red-500/30 text-red-400 text-xs font-bold hidden flex items-center gap-2 animate-pulse">
                <span>🚨 Warning: High Currency Risk Zone! 환율이 1,450원을 초과하여 밸류에이션 리스크 할인이 자동 반영 중입니다.</span>
            </div>
        </div>\n"""
        
        content = content.replace('        <div class="grid grid-cols-1 md:grid-cols-2 gap-8 mb-12">',
                                  slider_panel + '        <div class="grid grid-cols-1 md:grid-cols-2 gap-8 mb-12">')
                                  
        # Add Ids to Samsung pricing block
        old_samsung_block = """                    <div class="flex justify-between text-sm">
                        <span class="text-slate-500">낙관 목표가 (Optimistic)</span>
                        <span class="font-bold text-slate-300">570,000</span>
                    </div>
                    <div class="flex justify-between text-sm">
                        <span class="text-sky-400 font-bold">가중 적정가 (-15% 환율할인)</span>
                        <span class="font-bold text-sky-400">484,500</span>
                    </div>
                    <div class="w-full bg-slate-800 h-2 rounded-full overflow-hidden">
                        <div class="bg-sky-400 h-full" style="width: 61.2%"></div>
                    </div>
                    <div class="text-xs text-slate-500 text-right">상승 여력: +61.23%</div>"""
                    
        new_samsung_block = """                    <div class="flex justify-between text-sm">
                        <span class="text-slate-500">낙관 목표가 (Optimistic)</span>
                        <span class="font-bold text-slate-300">570,000</span>
                    </div>
                    <div class="flex justify-between text-sm">
                        <span class="text-sky-400 font-bold" id="samsungDiscountLabel">가중 적정가 (-15% 리스크할인)</span>
                        <span class="font-bold text-sky-400" id="samsungAdjustedVal">484,500</span>
                    </div>
                    <div class="w-full bg-slate-800 h-2 rounded-full overflow-hidden">
                        <div class="bg-sky-400 h-full transition-all duration-300" id="samsungProgress" style="width: 61.2%"></div>
                    </div>
                    <div class="text-xs text-slate-500 text-right" id="samsungUpsideVal">상승 여력: +61.23%</div>"""
        content = content.replace(old_samsung_block, new_samsung_block)
        
        # Add Ids to SK Hynix pricing block
        old_hynix_block = """                    <div class="flex justify-between text-sm">
                        <span class="text-slate-500">기본 목표가 (Base)</span>
                        <span class="font-bold text-slate-300">2,500,000</span>
                    </div>
                    <div class="flex justify-between text-sm">
                        <span class="text-sky-400 font-bold">가중 적정가 (-15% 환율할인)</span>
                        <span class="font-bold text-sky-400">2,125,000</span>
                    </div>
                    <div class="w-full bg-slate-800 h-2 rounded-full overflow-hidden">
                        <div class="bg-sky-400 h-full" style="width: 84.7%"></div>
                    </div>
                    <div class="text-xs text-slate-500 text-right">상승 여력: +5.83%</div>"""
                    
        new_hynix_block = """                    <div class="flex justify-between text-sm">
                        <span class="text-slate-500">기본 목표가 (Base)</span>
                        <span class="font-bold text-slate-300">2,500,000</span>
                    </div>
                    <div class="flex justify-between text-sm">
                        <span class="text-sky-400 font-bold" id="hynixDiscountLabel">가중 적정가 (-15% 리스크할인)</span>
                        <span class="font-bold text-sky-400" id="hynixAdjustedVal">2,125,000</span>
                    </div>
                    <div class="w-full bg-slate-800 h-2 rounded-full overflow-hidden">
                        <div class="bg-sky-400 h-full transition-all duration-300" id="hynixProgress" style="width: 84.7%"></div>
                    </div>
                    <div class="text-xs text-slate-500 text-right" id="hynixUpsideVal">상승 여력: +5.83%</div>"""
        content = content.replace(old_hynix_block, new_hynix_block)
        
        # Replace script tag with interactive logic
        old_script_block = """    <script>
        window.addEventListener('DOMContentLoaded', () => {
            try {
                const ctx = document.getElementById('profitChart').getContext('2d');
                new Chart(ctx, {
                    type: 'line',
                    data: {
                        labels: ['25.3Q', '25.4Q', '26.1Q', '26.2Q(E)', '26.3Q(E)'],
                        datasets: [
                            {
                                label: '삼성전자 (조 원)',
                                data: [12.4, 14.1, 15.2, 19.5, 25.1],
                                borderColor: '#38bdf8',
                                backgroundColor: 'rgba(56, 189, 248, 0.1)',
                                tension: 0.3,
                                fill: true,
                                borderWidth: 3
                            },
                            {
                                label: 'SK하이닉스 (조 원)',
                                data: [4.2, 5.8, 7.1, 9.8, 12.5],
                                borderColor: '#818cf8',
                                backgroundColor: 'rgba(129, 140, 248, 0.1)',
                                tension: 0.3,
                                fill: true,
                                borderWidth: 3
                            }
                        ]
                    },
                    options: {
                        responsive: true,
                        maintainAspectRatio: false,
                        plugins: {
                            legend: { labels: { color: '#94a3b8', font: { family: 'Pretendard' } } }
                        },
                        scales: {
                            y: { grid: { color: '#1e293b' }, ticks: { color: '#94a3b8' } },
                            x: { grid: { display: false }, ticks: { color: '#94a3b8' } }
                        }
                    }
                });
            } catch (e) { console.error('Chart init failed:', e); }
        });
    </script>"""
    
        new_script_block = """    <script>
        window.addEventListener('DOMContentLoaded', () => {
            let chartInstance = null;
            try {
                const ctx = document.getElementById('profitChart').getContext('2d');
                chartInstance = new Chart(ctx, {
                    type: 'line',
                    data: {
                        labels: ['25.3Q', '25.4Q', '26.1Q', '26.2Q(E)', '26.3Q(E)'],
                        datasets: [
                            {
                                label: '삼성전자 (조 원)',
                                data: [12.4, 14.1, 15.2, 19.5, 25.1],
                                borderColor: '#38bdf8',
                                backgroundColor: 'rgba(56, 189, 248, 0.1)',
                                tension: 0.3,
                                fill: true,
                                borderWidth: 3
                            },
                            {
                                label: 'SK하이닉스 (조 원)',
                                data: [4.2, 5.8, 7.1, 9.8, 12.5],
                                borderColor: '#818cf8',
                                backgroundColor: 'rgba(129, 140, 248, 0.1)',
                                tension: 0.3,
                                fill: true,
                                borderWidth: 3
                            }
                        ]
                    },
                    options: {
                        responsive: true,
                        maintainAspectRatio: false,
                        plugins: {
                            legend: { labels: { color: '#94a3b8', font: { family: 'Pretendard' } } }
                        },
                        scales: {
                            y: { grid: { color: '#1e293b' }, ticks: { color: '#94a3b8' } },
                            x: { grid: { display: false }, ticks: { color: '#94a3b8' } }
                        }
                    }
                });
            } catch (e) { console.error('Chart init failed:', e); }

            // Interactive controls
            const exchangeRateSlider = document.getElementById('exchangeRateSlider');
            const geoRiskSlider = document.getElementById('geoRiskSlider');
            const exchangeRateVal = document.getElementById('exchangeRateVal');
            const geoRiskVal = document.getElementById('geoRiskVal');
            
            const samsungAdjustedVal = document.getElementById('samsungAdjustedVal');
            const samsungDiscountLabel = document.getElementById('samsungDiscountLabel');
            const samsungProgress = document.getElementById('samsungProgress');
            const samsungUpsideVal = document.getElementById('samsungUpsideVal');
            
            const hynixAdjustedVal = document.getElementById('hynixAdjustedVal');
            const hynixDiscountLabel = document.getElementById('hynixDiscountLabel');
            const hynixProgress = document.getElementById('hynixProgress');
            const hynixUpsideVal = document.getElementById('hynixUpsideVal');
            
            const currencyRiskWarning = document.getElementById('currencyRiskWarning');
            const headerRiskBadge = document.getElementById('headerRiskBadge');
            const headerRiskLabel = document.getElementById('headerRiskLabel');
            const headerRiskVal = document.getElementById('headerRiskVal');
            
            const samsungBaseTarget = 570000;
            const samsungCurrentPrice = 300500;
            const hynixBaseTarget = 2500000;
            const hynixCurrentPrice = 2008000;
            
            // Baseline profits data
            const samsungBaseProfits = [12.4, 14.1, 15.2, 19.5, 25.1];
            const hynixBaseProfits = [4.2, 5.8, 7.1, 9.8, 12.5];

            function updateValuations() {
                const exchangeRate = parseFloat(exchangeRateSlider.value);
                const geoRisk = parseFloat(geoRiskSlider.value);
                
                // Update slider text
                exchangeRateVal.textContent = exchangeRate.toLocaleString('ko-KR') + ' KRW';
                geoRiskVal.textContent = geoRisk + '%';
                
                // Show/hide High Currency Risk Zone Warning
                if (exchangeRate > 1450) {
                    currencyRiskWarning.classList.remove('hidden');
                    headerRiskBadge.className = 'risk-badge px-4 py-2 rounded-xl text-sm font-bold flex items-center gap-2 bg-red-500/10 border border-red-500/30 text-red-400';
                    headerRiskLabel.textContent = '⚠️ High Currency Risk Zone';
                    headerRiskVal.className = 'bg-red-500 text-white px-2 py-0.5 rounded';
                } else {
                    currencyRiskWarning.classList.add('hidden');
                    headerRiskBadge.className = 'px-4 py-2 rounded-xl text-sm font-bold flex items-center gap-2 bg-slate-800/50 border border-slate-700 text-slate-400';
                    headerRiskLabel.textContent = '🟢 Normal Currency Zone';
                    headerRiskVal.className = 'bg-emerald-500 text-white px-2 py-0.5 rounded';
                }
                headerRiskVal.textContent = exchangeRate.toLocaleString('ko-KR');

                // Calculate discount: exchange rate > 1450 gives 15% discount, geopolitical risk gives 0-15% discount
                let rateDiscount = exchangeRate > 1450 ? 0.15 : 0.0;
                let geoDiscount = (geoRisk / 100) * 0.15;
                let totalDiscount = rateDiscount + geoDiscount;
                let discountPercentStr = Math.round(totalDiscount * 100) + '%';
                
                samsungDiscountLabel.textContent = `가중 적정가 (-${discountPercentStr} 리스크할인)`;
                hynixDiscountLabel.textContent = `가중 적정가 (-${discountPercentStr} 리스크할인)`;
                
                let samsungAdjusted = Math.round(samsungBaseTarget * (1 - totalDiscount));
                let hynixAdjusted = Math.round(hynixBaseTarget * (1 - totalDiscount));
                
                samsungAdjustedVal.textContent = samsungAdjusted.toLocaleString('ko-KR');
                hynixAdjustedVal.textContent = hynixAdjusted.toLocaleString('ko-KR');
                
                // Upside
                let samsungUpside = ((samsungAdjusted - samsungCurrentPrice) / samsungCurrentPrice) * 100;
                let hynixUpside = ((hynixAdjusted - hynixCurrentPrice) / hynixCurrentPrice) * 100;
                
                samsungUpsideVal.textContent = `상승 여력: ${samsungUpside >= 0 ? '+' : ''}${samsungUpside.toFixed(2)}%`;
                hynixUpsideVal.textContent = `상승 여력: ${hynixUpside >= 0 ? '+' : ''}${hynixUpside.toFixed(2)}%`;
                
                // Progress bar (cap between 0% and 100%)
                let samsungProgressPercent = Math.max(0, Math.min(100, (samsungCurrentPrice / samsungAdjusted) * 100));
                let hynixProgressPercent = Math.max(0, Math.min(100, (hynixCurrentPrice / hynixAdjusted) * 100));
                
                samsungProgress.style.width = samsungProgressPercent + '%';
                hynixProgress.style.width = hynixProgressPercent + '%';
                
                // Update Chart.js data: Scale expected future profits (indices 3 and 4) based on risk factors
                if (chartInstance) {
                    const scaleFactor = 1 - (totalDiscount * 0.5); // moderate profit scaling
                    chartInstance.data.datasets[0].data[3] = +(samsungBaseProfits[3] * scaleFactor).toFixed(1);
                    chartInstance.data.datasets[0].data[4] = +(samsungBaseProfits[4] * scaleFactor).toFixed(1);
                    
                    chartInstance.data.datasets[1].data[3] = +(hynixBaseProfits[3] * scaleFactor).toFixed(1);
                    chartInstance.data.datasets[1].data[4] = +(hynixBaseProfits[4] * scaleFactor).toFixed(1);
                    chartInstance.update();
                }
            }

            // Bind events
            exchangeRateSlider.addEventListener('input', updateValuations);
            geoRiskSlider.addEventListener('input', updateValuations);
            
            // Run initial update to sync with pre-loaded slider state
            updateValuations();
        });
    </script>"""
        content = content.replace(old_script_block, new_script_block)
        
        with open(semi_path, 'w', encoding='utf-8', newline='') as f:
            f.write(content)
        print("Updated valuation_semi.html with sliders and reactive bindings")

if __name__ == '__main__':
    integrate()
