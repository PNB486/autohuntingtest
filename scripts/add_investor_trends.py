# -*- coding: utf-8 -*-
import os

def add_trends():
    kospi_path = r"C:\Users\S\Desktop\AI\Gemini\Stock\kospi.html"
    if not os.path.exists(kospi_path):
        print("kospi.html not found!")
        return

    with open(kospi_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Update grid layout
    old_grid = 'grid grid-cols-1 md:grid-cols-2 gap-6 mb-10'
    new_grid = 'grid grid-cols-1 lg:grid-cols-3 gap-6 mb-10'
    content = content.replace(old_grid, new_grid)

    # 2. Insert Investor Chart Card
    target_card_end = """            </div>
        </div>

        <!-- Analysis Section -->"""
    
    replacement_card = """            </div>

            <!-- 수급 주체별 동향 Card -->
            <div class="card p-6 rounded-2xl shadow-xl">
                <h3 class="text-slate-400 text-sm font-semibold uppercase mb-4">수급 주체별 동향 (단위: 억)</h3>
                <div class="space-y-6">
                    <div class="relative h-[200px]">
                        <canvas id="investorChart"></canvas>
                    </div>
                    <div class="grid grid-cols-1 gap-2 text-xs">
                        <div class="flex justify-between items-center p-2.5 bg-slate-800/50 rounded-xl border border-slate-700">
                            <span class="text-slate-400 font-medium">외국인</span>
                            <span class="text-blue-400 font-bold">-19,264억</span>
                        </div>
                        <div class="flex justify-between items-center p-2.5 bg-slate-800/50 rounded-xl border border-slate-700">
                            <span class="text-slate-400 font-medium">기관</span>
                            <span class="text-rose-500 font-bold">+7,583억</span>
                        </div>
                        <div class="flex justify-between items-center p-2.5 bg-slate-800/50 rounded-xl border border-slate-700">
                            <span class="text-slate-400 font-medium">개인</span>
                            <span class="text-rose-500 font-bold">+10,654억</span>
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <!-- Analysis Section -->"""
    
    content = content.replace(target_card_end, replacement_card)

    # 3. Insert Chart.js Initialization
    chart_init_target = """                            pointRadius: 0
                        }]
                    },
                    options: {
                        responsive: true,
                        maintainAspectRatio: false,
                        plugins: { legend: { display: false } },
                        scales: {
                            x: { grid: { display: false }, ticks: { color: '#64748b' } },
                            y: { grid: { color: '#1e293b' }, ticks: { color: '#64748b' } }
                        }
                    }
                });
            } catch (e) { console.error('Chart init failed:', e); }"""

    chart_init_replacement = """                            pointRadius: 0
                        }]
                    },
                    options: {
                        responsive: true,
                        maintainAspectRatio: false,
                        plugins: { legend: { display: false } },
                        scales: {
                            x: { grid: { display: false }, ticks: { color: '#64748b' } },
                            y: { grid: { color: '#1e293b' }, ticks: { color: '#64748b' } }
                        }
                    }
                });

                // Investor Chart Init
                const ctxInv = document.getElementById('investorChart').getContext('2d');
                new Chart(ctxInv, {
                    type: 'bar',
                    data: {
                        labels: ['외인', '기관', '개인'],
                        datasets: [{
                            data: [-19264, 7583, 10654],
                            backgroundColor: (context) => {
                                const val = context.raw;
                                return val > 0 ? 'rgba(239, 68, 68, 0.8)' : 'rgba(59, 130, 246, 0.8)';
                            },
                            borderRadius: 6
                        }]
                    },
                    options: {
                        indexAxis: 'y',
                        responsive: true,
                        maintainAspectRatio: false,
                        plugins: { legend: { display: false } },
                        scales: {
                            x: { grid: { color: '#1e293b' }, ticks: { color: '#64748b' } },
                            y: { grid: { display: false }, ticks: { color: '#64748b' } }
                        }
                    }
                });
            } catch (e) { console.error('Chart init failed:', e); }"""

    content = content.replace(chart_init_target, chart_init_replacement)

    with open(kospi_path, 'w', encoding='utf-8', newline='') as f:
        f.write(content)
    print("Successfully updated kospi.html with 수급 주체별 동향 Card!")

if __name__ == "__main__":
    add_trends()
