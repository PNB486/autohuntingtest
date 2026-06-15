# -*- coding: utf-8 -*-
import os
import re
import sys

# Add scripts directory to path to import revalidate_portal
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

def main():
    base_dir = r"C:\Users\S\Desktop\AI\Gemini\Stock"
    print("Starting automated auto-hunt update...")

    # --- 1. index.html ---
    index_path = os.path.join(base_dir, "index.html")
    if os.path.exists(index_path):
        with open(index_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Replace KOSPI
        content = content.replace(
            '<span class="text-xl font-bold text-sky-400">7,888.49</span>\n                    <span class="text-blue-400 text-sm ml-1 font-bold">▼ 2.57%</span>',
            '<span class="text-xl font-bold text-sky-400">7,912.45</span>\n                    <span class="text-blue-400 text-sm ml-1 font-bold">▼ 2.27%</span>'
        )
        content = content.replace(
            '<span class="text-xl font-bold text-sky-400">7,888.49</span>\r\n                    <span class="text-blue-400 text-sm ml-1 font-bold">▼ 2.57%</span>',
            '<span class="text-xl font-bold text-sky-400">7,912.45</span>\n                    <span class="text-blue-400 text-sm ml-1 font-bold">▼ 2.27%</span>'
        )
        
        # Replace USD/KRW
        content = content.replace(
            '<span class="text-xl font-bold text-rose-500">1,525.00</span>',
            '<span class="text-xl font-bold text-rose-500">1,528.00</span>'
        )
        
        # Update timestamp
        content = content.replace(
            'SYSTEM UPDATED: 2026-06-10 09:08 KST',
            'SYSTEM UPDATED: 2026-06-10 11:52 KST'
        )
        
        with open(index_path, 'w', encoding='utf-8', newline='') as f:
            f.write(content)
        print("index.html updated successfully.")

    # --- 2. kospi.html ---
    kospi_path = os.path.join(base_dir, "kospi.html")
    if os.path.exists(kospi_path):
        with open(kospi_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Update Subtitle timestamp
        content = content.replace(
            '주식 시장 현황 | 2026. 06. 10. 09:08',
            '주식 시장 현황 | 2026. 06. 10. 11:52'
        )

        # Update KOSPI Index values
        content = content.replace(
            '<span class="text-5xl font-black text-sky-400">7,888.49</span>\n                    <span class="text-2xl font-bold text-blue-400">▼ 208.08 (-2.57%)</span>',
            '<span class="text-5xl font-black text-sky-400">7,912.45</span>\n                    <span class="text-2xl font-bold text-blue-400">▼ 183.84 (-2.27%)</span>'
        )
        content = content.replace(
            '<span class="text-5xl font-black text-sky-400">7,888.49</span>\r\n                    <span class="text-2xl font-bold text-blue-400">▼ 208.08 (-2.57%)</span>',
            '<span class="text-5xl font-black text-sky-400">7,912.45</span>\n                    <span class="text-2xl font-bold text-blue-400">▼ 183.84 (-2.27%)</span>'
        )

        # Top 5 Stocks Table Replacements
        old_table = """                            <tr class="border-b border-slate-800/50">
                                <td class="py-4 font-bold">삼성전자 (005930)</td>
                                <td class="py-4 text-right">322,000</td>
                                <td class="py-4 text-right text-rose-500">+8.97%</td>
                            </tr>
                            <tr class="border-b border-slate-800/50">
                                <td class="py-4 font-bold">SK하이닉스 (000660)</td>
                                <td class="py-4 text-right">2,215,000</td>
                                <td class="py-4 text-right text-rose-500">+15.91%</td>
                            </tr>
                            <tr class="border-b border-slate-800/50">
                                <td class="py-4 font-bold">LG에너지솔루션 (373220)</td>
                                <td class="py-4 text-right">396,500</td>
                                <td class="py-4 text-right text-rose-500">+2.06%</td>
                            </tr>
                            <tr class="border-b border-slate-800/50">
                                <td class="py-4 font-bold">NAVER (035420)</td>
                                <td class="py-4 text-right">257,000</td>
                                <td class="py-4 text-right text-blue-400">-7.89%</td>
                            </tr>
                            <tr>
                                <td class="py-4 font-bold">현대차 (005380)</td>
                                <td class="py-4 text-right">639,000</td>
                                <td class="py-4 text-right text-slate-400">0.00%</td>
                            </tr>"""

        new_table = """                            <tr class="border-b border-slate-800/50">
                                <td class="py-4 font-bold">삼성전자 (005930)</td>
                                <td class="py-4 text-right">306,500</td>
                                <td class="py-4 text-right text-blue-400">-4.81%</td>
                            </tr>
                            <tr class="border-b border-slate-800/50">
                                <td class="py-4 font-bold">SK하이닉스 (000660)</td>
                                <td class="py-4 text-right">2,124,000</td>
                                <td class="py-4 text-right text-blue-400">-4.11%</td>
                            </tr>
                            <tr class="border-b border-slate-800/50">
                                <td class="py-4 font-bold">LG에너지솔루션 (373220)</td>
                                <td class="py-4 text-right">394,500</td>
                                <td class="py-4 text-right text-blue-400">-0.50%</td>
                            </tr>
                            <tr class="border-b border-slate-800/50">
                                <td class="py-4 font-bold">NAVER (035420)</td>
                                <td class="py-4 text-right">257,000</td>
                                <td class="py-4 text-right text-slate-400">0.00%</td>
                            </tr>
                            <tr>
                                <td class="py-4 font-bold">현대차 (005380)</td>
                                <td class="py-4 text-right">639,000</td>
                                <td class="py-4 text-right text-slate-400">0.00%</td>
                            </tr>"""

        content = content.replace(old_table.replace('\r\n', '\n'), new_table)
        content = content.replace(old_table.replace('\n', '\r\n'), new_table)

        # Risk factors USD/KRW text
        content = content.replace(
            '원/달러 환율이 <strong>1,525.00원 (High Currency Risk Zone)</strong>',
            '원/달러 환율이 <strong>1,528.00원 (High Currency Risk Zone)</strong>'
        )

        # Chart.js data last point
        content = content.replace(
            'data: [8096, 8050, 8010, 7960, 7920, 7888.49],',
            'data: [8096, 8050, 8010, 7960, 7920, 7912.45],'
        )

        with open(kospi_path, 'w', encoding='utf-8', newline='') as f:
            f.write(content)
        print("kospi.html updated successfully.")

    # --- 3. nasdaq.html ---
    nasdaq_path = os.path.join(base_dir, "nasdaq.html")
    if os.path.exists(nasdaq_path):
        with open(nasdaq_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Subtitle
        content = content.replace(
            '미국 주식 시장 현황 | 2026. 06. 10. 09:08',
            '미국 주식 시장 현황 | 2026. 06. 10. 11:52'
        )

        # USD/KRW metrics
        content = content.replace(
            '<span class="text-3xl font-bold text-rose-500">1,525.00 KRW</span>',
            '<span class="text-3xl font-bold text-rose-500">1,528.00 KRW</span>'
        )
        content = content.replace(
            'High Currency Risk Zone (1,525.00)',
            'High Currency Risk Zone (1,528.00)'
        )

        # Risk text
        content = content.replace(
            '원/달러 환율이 <strong>1,525.00원 (High Currency Risk Zone)</strong>',
            '원/달러 환율이 <strong>1,528.00원 (High Currency Risk Zone)</strong>'
        )

        with open(nasdaq_path, 'w', encoding='utf-8', newline='') as f:
            f.write(content)
        print("nasdaq.html updated successfully.")

    # --- 4. news.html ---
    news_path = os.path.join(base_dir, "news.html")
    if os.path.exists(news_path):
        with open(news_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Update news update timestamp
        content = re.sub(
            r'실시간 자동사냥 \| \d{4}년 \d{1,2}월 \d{1,2}일 \d{2}:\d{2}',
            '실시간 자동사냥 | 2026년 6월 10일 11:52',
            content
        )
        content = re.sub(
            r'실시간 자동사냥 \| \d{4}년 \d{1,2}월 \d{1,2}일 \d{1,2}:\d{2}',
            '실시간 자동사냥 | 2026년 6월 10일 11:52',
            content
        )

        with open(news_path, 'w', encoding='utf-8', newline='') as f:
            f.write(content)
        print("news.html updated successfully.")

    # --- 5. valuation_semi.html ---
    semi_path = os.path.join(base_dir, "valuation_semi.html")
    if os.path.exists(semi_path):
        with open(semi_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Timestamps
        content = content.replace(
            '주요 종목 적정가 및 리스크 진단 | 2026. 06. 10. 09:08',
            '주요 종목 적정가 및 리스크 진단 | 2026. 06. 10. 11:52'
        )
        content = content.replace(
            'Last Updated: 2026. 06. 10. 09:08 KST',
            'Last Updated: 2026. 06. 10. 11:52 KST'
        )

        # Risk Badge & Exchange rate
        content = content.replace(
            '<span class="bg-red-500 text-white px-2 py-0.5 rounded" id="headerRiskVal">1,525.00</span>',
            '<span class="bg-red-500 text-white px-2 py-0.5 rounded" id="headerRiskVal">1,528.00</span>'
        )
        content = content.replace(
            '<span class="text-sky-400 font-mono" id="exchangeRateVal">1,525.00 KRW</span>',
            '<span class="text-sky-400 font-mono" id="exchangeRateVal">1,528.00 KRW</span>'
        )
        content = content.replace(
            'value="1525"',
            'value="1528"'
        )

        # Samsung Electronics
        content = content.replace(
            '<div class="text-3xl font-bold text-sky-400">322,000 <span class="text-sm">KRW</span></div>\n                        <div class="text-rose-500 text-sm font-semibold">▲ 26,500 (+8.97%)</div>',
            '<div class="text-3xl font-bold text-sky-400">306,500 <span class="text-sm">KRW</span></div>\n                        <div class="text-blue-400 text-sm font-semibold">▼ 15,500 (-4.81%)</div>'
        )
        content = content.replace(
            '<div class="text-3xl font-bold text-sky-400">322,000 <span class="text-sm">KRW</span></div>\r\n                        <div class="text-rose-500 text-sm font-semibold">▲ 26,500 (+8.97%)</div>',
            '<div class="text-3xl font-bold text-sky-400">306,500 <span class="text-sm">KRW</span></div>\n                        <div class="text-blue-400 text-sm font-semibold">▼ 15,500 (-4.81%)</div>'
        )

        # Pre-calculated Discount Valuations for Samsung
        # Samsung target = 570000. Under 1,528 exchange rate and 50% geo risk = 23% discount (total discount = 15% + 7.5% = 22.5%, rounds to 23%).
        # Samsung adjusted: 570000 * 0.775 = 441750. Upside = (441750 - 306500) / 306500 = +44.13%. Progress width = 306500 / 441750 = 69.38% (69.4%)
        content = content.replace(
            '<span class="text-sky-400 font-bold" id="samsungDiscountLabel">가중 적정가 (-15% 리스크할인)</span>\n                        <span class="font-bold text-sky-400" id="samsungAdjustedVal">484,500</span>',
            '<span class="text-sky-400 font-bold" id="samsungDiscountLabel">가중 적정가 (-23% 리스크할인)</span>\n                        <span class="font-bold text-sky-400" id="samsungAdjustedVal">441,750</span>'
        )
        content = content.replace(
            '<span class="text-sky-400 font-bold" id="samsungDiscountLabel">가중 적정가 (-15% 리스크할인)</span>\r\n                        <span class="font-bold text-sky-400" id="samsungAdjustedVal">484,500</span>',
            '<span class="text-sky-400 font-bold" id="samsungDiscountLabel">가중 적정가 (-23% 리스크할인)</span>\n                        <span class="font-bold text-sky-400" id="samsungAdjustedVal">441,750</span>'
        )
        content = content.replace(
            'id="samsungProgress" style="width: 66.5%"',
            'id="samsungProgress" style="width: 69.4%"'
        )
        content = content.replace(
            'id="samsungUpsideVal">상승 여력: +50.47%',
            'id="samsungUpsideVal">상승 여력: +44.13%'
        )

        # SK Hynix
        content = content.replace(
            '<div class="text-3xl font-bold text-sky-400">2,215,000 <span class="text-sm">KRW</span></div>\n                        <div class="text-rose-500 text-sm font-semibold">▲ 304,000 (+15.91%)</div>',
            '<div class="text-3xl font-bold text-sky-400">2,124,000 <span class="text-sm">KRW</span></div>\n                        <div class="text-blue-400 text-sm font-semibold">▼ 91,000 (-4.11%)</div>'
        )
        content = content.replace(
            '<div class="text-3xl font-bold text-sky-400">2,215,000 <span class="text-sm">KRW</span></div>\r\n                        <div class="text-rose-500 text-sm font-semibold">▲ 304,000 (+15.91%)</div>',
            '<div class="text-3xl font-bold text-sky-400">2,124,000 <span class="text-sm">KRW</span></div>\n                        <div class="text-blue-400 text-sm font-semibold">▼ 91,000 (-4.11%)</div>'
        )

        # Pre-calculated Discount Valuations for Hynix
        # Hynix target = 2500000. Hynix adjusted: 2500000 * 0.775 = 1937500. Upside = (1937500 - 2124000) / 2124000 = -8.78%. Progress = 100%
        content = content.replace(
            '<span class="text-sky-400 font-bold" id="hynixDiscountLabel">가중 적정가 (-15% 리스크할인)</span>\n                        <span class="font-bold text-sky-400" id="hynixAdjustedVal">2,125,000</span>',
            '<span class="text-sky-400 font-bold" id="hynixDiscountLabel">가중 적정가 (-23% 리스크할인)</span>\n                        <span class="font-bold text-sky-400" id="hynixAdjustedVal">1,937,500</span>'
        )
        content = content.replace(
            '<span class="text-sky-400 font-bold" id="hynixDiscountLabel">가중 적정가 (-15% 리스크할인)</span>\r\n                        <span class="font-bold text-sky-400" id="hynixAdjustedVal">2,125,000</span>',
            '<span class="text-sky-400 font-bold" id="hynixDiscountLabel">가중 적정가 (-23% 리스크할인)</span>\n                        <span class="font-bold text-sky-400" id="hynixAdjustedVal">1,937,500</span>'
        )
        content = content.replace(
            'id="hynixProgress" style="width: 100%"',
            'id="hynixProgress" style="width: 100%"'
        )
        content = content.replace(
            'id="hynixUpsideVal">상승 여력: -4.06%',
            'id="hynixUpsideVal">상승 여력: -8.78%'
        )

        # Risk text exchange rate
        content = content.replace(
            '원/달러 환율이 <strong>1,525.00원 (High Currency Risk Zone)</strong>',
            '원/달러 환율이 <strong>1,528.00원 (High Currency Risk Zone)</strong>'
        )

        # JS constants
        content = content.replace(
            'const samsungCurrentPrice = 322000;',
            'const samsungCurrentPrice = 306500;'
        )
        content = content.replace(
            'const hynixCurrentPrice = 2215000;',
            'const hynixCurrentPrice = 2124000;'
        )

        with open(semi_path, 'w', encoding='utf-8', newline='') as f:
            f.write(content)
        print("valuation_semi.html updated successfully.")

    # --- 6. valuation_defense.html ---
    defense_path = os.path.join(base_dir, "valuation_defense.html")
    if os.path.exists(defense_path):
        with open(defense_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Timestamps
        content = content.replace(
            '글로벌 지정학적 리스크 및 수주 가치 진단 | 2026. 06. 10. 09:08',
            '글로벌 지정학적 리스크 및 수주 가치 진단 | 2026. 06. 10. 11:52'
        )
        content = content.replace(
            'Last Updated: 2026. 06. 10. 09:08 KST',
            'Last Updated: 2026. 06. 10. 11:52 KST'
        )

        # Risk badge
        content = content.replace(
            '⚠️ High Currency Risk Zone (1,525.00)',
            '⚠️ High Currency Risk Zone (1,528.00)'
        )
        content = content.replace(
            '<h4 class="text-red-400 font-bold text-sm mb-2">High Currency Risk Zone (1,525.00)</h4>',
            '<h4 class="text-red-400 font-bold text-sm mb-2">High Currency Risk Zone (1,528.00)</h4>'
        )

        with open(defense_path, 'w', encoding='utf-8', newline='') as f:
            f.write(content)
        print("valuation_defense.html updated successfully.")

    # --- 7. valuation_battery.html ---
    battery_path = os.path.join(base_dir, "valuation_battery.html")
    if os.path.exists(battery_path):
        with open(battery_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Timestamps
        content = content.replace(
            '전기차 캐즘 돌파 및 실적 턴어라운드 진단 | 2026. 06. 10. 09:08',
            '전기차 캐즘 돌파 및 실적 턴어라운드 진단 | 2026. 06. 10. 11:52'
        )
        content = content.replace(
            'Last Updated: 2026. 06. 10. 09:08 KST',
            'Last Updated: 2026. 06. 10. 11:52 KST'
        )

        # Risk badge
        content = content.replace(
            '⚠️ High Currency Risk Zone (1,525.00)',
            '⚠️ High Currency Risk Zone (1,528.00)'
        )
        content = content.replace(
            '<span class="font-bold">High Currency Risk Zone (1,525.00)</span>',
            '<span class="font-bold">High Currency Risk Zone (1,528.00)</span>'
        )

        # LG Energy Solution
        content = content.replace(
            '<div class="text-3xl font-bold text-sky-400">396,500 <span class="text-sm">KRW</span></div>\n                        <div class="text-rose-500 text-sm font-semibold">▲ 8,000 (+2.06%)</div>',
            '<div class="text-3xl font-bold text-sky-400">394,500 <span class="text-sm">KRW</span></div>\n                        <div class="text-blue-400 text-sm font-semibold">▼ 2,000 (-0.50%)</div>'
        )
        content = content.replace(
            '<div class="text-3xl font-bold text-sky-400">396,500 <span class="text-sm">KRW</span></div>\r\n                        <div class="text-rose-500 text-sm font-semibold">▲ 8,000 (+2.06%)</div>',
            '<div class="text-3xl font-bold text-sky-400">394,500 <span class="text-sm">KRW</span></div>\n                        <div class="text-blue-400 text-sm font-semibold">▼ 2,000 (-0.50%)</div>'
        )

        # LG Energy Solution progress & upside (upside = 29.28%, progress = 77.4%)
        # Replace the LG energy progress percentage style
        content = content.replace(
            '<div class="bg-sky-400 h-full" style="width: 77.8%"></div>',
            '<div class="bg-sky-400 h-full" style="width: 77.4%"></div>'
        )
        content = content.replace(
            '상승 여력: +28.63%',
            '상승 여력: +29.28%'
        )

        with open(battery_path, 'w', encoding='utf-8', newline='') as f:
            f.write(content)
        print("valuation_battery.html updated successfully.")

    # --- 8. valuation_ai.html ---
    ai_path = os.path.join(base_dir, "valuation_ai.html")
    if os.path.exists(ai_path):
        with open(ai_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Timestamps & Header Risk
        content = content.replace(
            '<div class="text-slate-500 text-sm font-mono mb-1">Updated: 2026-06-10 09:08 KST</div>\n                <div class="inline-flex items-center px-3 py-1 rounded-full bg-red-500/10 border border-red-500/20 text-red-400 text-xs font-bold animate-pulse">\n                    ⚠️ 고환율 리스크 존 (1,525.00)\n                </div>',
            '<div class="text-slate-500 text-sm font-mono mb-1">Updated: 2026-06-10 11:52 KST</div>\n                <div class="inline-flex items-center px-3 py-1 rounded-full bg-red-500/10 border border-red-500/20 text-red-400 text-xs font-bold animate-pulse">\n                    ⚠️ 고환율 리스크 존 (1,528.00)\n                </div>'
        )
        content = content.replace(
            '<div class="text-slate-500 text-sm font-mono mb-1">Updated: 2026-06-10 09:08 KST</div>\r\n                <div class="inline-flex items-center px-3 py-1 rounded-full bg-red-500/10 border border-red-500/20 text-red-400 text-xs font-bold animate-pulse">\r\n                    ⚠️ 고환율 리스크 존 (1,525.00)\r\n                </div>',
            '<div class="text-slate-500 text-sm font-mono mb-1">Updated: 2026-06-10 11:52 KST</div>\n                <div class="inline-flex items-center px-3 py-1 rounded-full bg-red-500/10 border border-red-500/20 text-red-400 text-xs font-bold animate-pulse">\n                    ⚠️ 고환율 리스크 존 (1,528.00)\n                </div>'
        )

        # Exchange rate metric card
        content = content.replace(
            '<div class="text-3xl font-black metric-value mb-1">1,525.00</div>',
            '<div class="text-3xl font-black metric-value mb-1">1,528.00</div>'
        )

        # Risk sections text
        content = content.replace('* 환율 1,525.00원 돌파에 따라', '* 환율 1,528.00원 돌파에 따라')
        content = content.replace('USD/KRW 환율이 **1,525.00**을 기록하며', 'USD/KRW 환율이 **1,528.00**을 기록하며')

        with open(ai_path, 'w', encoding='utf-8', newline='') as f:
            f.write(content)
        print("valuation_ai.html updated successfully.")

    # --- 9. valuation_interactive_demo.html ---
    demo_path = os.path.join(base_dir, "valuation_interactive_demo.html")
    if os.path.exists(demo_path):
        with open(demo_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Timestamps
        content = content.replace(
            '매크로 변수에 따른 종목별 할인율 및 적정가 리계산 | 2026. 06. 10. 09:08',
            '매크로 변수에 따른 종목별 할인율 및 적정가 리계산 | 2026. 06. 10. 11:52'
        )
        content = content.replace(
            'Last Updated: 2026. 06. 10. 09:08 KST',
            'Last Updated: 2026. 06. 10. 11:52 KST'
        )

        # Header Risk Badge & Exchange rate
        content = content.replace(
            '<span class="bg-red-500 text-white px-2 py-0.5 rounded" id="headerRiskVal">1,525.00</span>',
            '<span class="bg-red-500 text-white px-2 py-0.5 rounded" id="headerRiskVal">1,528.00</span>'
        )
        content = content.replace(
            '<span class="text-sky-400 font-mono" id="exchangeRateVal">1,525.00 KRW</span>',
            '<span class="text-sky-400 font-mono" id="exchangeRateVal">1,528.00 KRW</span>'
        )
        content = content.replace(
            'value="1525"',
            'value="1528"'
        )

        # Samsung Electronics
        content = content.replace(
            '<div class="font-bold text-slate-300">₩322,000</div>',
            '<div class="font-bold text-slate-300">₩306,500</div>'
        )
        content = content.replace(
            'const samsungCurrent = 322000;',
            'const samsungCurrent = 306500;'
        )

        # SK Hynix
        content = content.replace(
            '<div class="font-bold text-slate-300">₩2,215,000</div>',
            '<div class="font-bold text-slate-300">₩2,124,000</div>'
        )
        content = content.replace(
            'const hynixCurrent = 2215000;',
            'const hynixCurrent = 2124000;'
        )

        # LG Energy Solution
        content = content.replace(
            '<div class="font-bold text-slate-300">₩396,500</div>',
            '<div class="font-bold text-slate-300">₩394,500</div>'
        )
        content = content.replace(
            'const lgCurrent = 396500;',
            'const lgCurrent = 394500;'
        )

        # Recalculate static display values for 15% rate discount (which was baseline in demo HTML)
        # Samsung: ₩484,500. Upside for 306,500 is (484500-306500)/306500 = +58.07%. Progress is 306500/484500 = 63.3%.
        # SK Hynix: ₩2,125,000. Upside for 2,124,000 is (2125000-2124000)/2124000 = +0.05%. Progress is 2124000/2125000 = 100.0%
        # LG Energy: ₩510,000. Upside for 394,500 is (510000-394500)/394500 = +29.28%. Progress is 394500/510000 = 77.4%
        
        # Samsung progress & upside replacement
        content = content.replace(
            'id="samsungProgress" style="width: 66.5%"',
            'id="samsungProgress" style="width: 63.3%"'
        )
        content = content.replace(
            'id="samsungUpside">상승여력: +50.47%',
            'id="samsungUpside">상승여력: +58.07%'
        )

        # Hynix progress & upside replacement
        content = content.replace(
            'id="hynixProgress" style="width: 100%"',
            'id="hynixProgress" style="width: 100%"'
        )
        content = content.replace(
            'id="hynixUpside">상승여력: -4.06%',
            'id="hynixUpside">상승여력: +0.05%'
        )

        # LG progress & upside replacement
        content = content.replace(
            'id="lgProgress" style="width: 77.8%"',
            'id="lgProgress" style="width: 77.4%"'
        )
        content = content.replace(
            'id="lgUpside">상승여력: +28.63%',
            'id="lgUpside">상승여력: +29.28%'
        )

        with open(demo_path, 'w', encoding='utf-8', newline='') as f:
            f.write(content)
        print("valuation_interactive_demo.html updated successfully.")

    print("\nAutomated auto-hunt updates complete.")

if __name__ == "__main__":
    main()
