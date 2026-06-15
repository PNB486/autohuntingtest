# -*- coding: utf-8 -*-
import os
import re

def update_to_june_16():
    base_dir = r"C:\Users\S\Desktop\AI\Gemini\Stock"
    print("Starting updates for June 16, 2026 09:07 KST...")

    # Define standard updates
    kospi_val = "8,696.55"
    kospi_change = "▲ 150.57 (+1.76%)"
    kospi_change_index = "▲ 1.76%"
    
    nasdaq_val = "26,683.94"
    nasdaq_change = "▲ 795.10 (+3.10%)"
    nasdaq_change_index = "▲ 3.10%"
    
    usd_krw_val = "1,514.65"
    usd_krw_val_short = "1515"  # for slider values

    # 1. Update index.html
    index_path = os.path.join(base_dir, "index.html")
    if os.path.exists(index_path):
        print("Updating index.html...")
        with open(index_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # Replace KOSPI
        content = re.sub(
            r'<span class="text-xl font-bold text-sky-400">8,545.98</span>\s*<span class="text-rose-500 text-sm ml-1 font-bold">▲ 5.20%</span>',
            f'<span class="text-xl font-bold text-sky-400">{kospi_val}</span>\n                    <span class="text-rose-500 text-sm ml-1 font-bold">{kospi_change_index}</span>',
            content
        )
        
        # Replace NASDAQ
        content = re.sub(
            r'<span class="text-xl font-bold text-sky-400">25,888.84</span>\s*<span class="text-rose-500 text-sm ml-1 font-bold">▲ 0.31%</span>',
            f'<span class="text-xl font-bold text-sky-400">{nasdaq_val}</span>\n                    <span class="text-rose-500 text-sm ml-1 font-bold">{nasdaq_change_index}</span>',
            content
        )
        
        # Replace USD/KRW
        content = re.sub(
            r'<span class="text-xl font-bold text-rose-500">1,511.10</span>',
            f'<span class="text-xl font-bold text-rose-500">{usd_krw_val}</span>',
            content
        )
        
        # Replace Timestamp
        content = re.sub(
            r'SYSTEM UPDATED: \d{4}-\d{2}-\d{2} \d{2}:\d{2} KST',
            'SYSTEM UPDATED: 2026-06-16 09:07 KST',
            content
        )
        content = re.sub(
            r'SYSTEM UPDATED: \d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2} KST',
            'SYSTEM UPDATED: 2026-06-16 09:07 KST',
            content
        )
        
        with open(index_path, 'w', encoding='utf-8', newline='') as f:
            f.write(content)
        print("index.html updated.")

    # 2. Update kospi.html
    kospi_path = os.path.join(base_dir, "kospi.html")
    if os.path.exists(kospi_path):
        print("Updating kospi.html...")
        with open(kospi_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # Timestamp
        content = re.sub(
            r'주식 시장 현황 \| \d{4}\. \d{2}\. \d{2}\. \d{2}:\d{2}',
            '주식 시장 현황 | 2026. 06. 16. 09:07',
            content
        )
        
        # KOSPI Index and Change
        content = re.sub(
            r'<span class="text-5xl font-black text-sky-400">8,545.98</span>\s*<span class="text-2xl font-bold text-rose-500">▲ 422.36 \(\+5.20%\)</span>',
            f'<span class="text-5xl font-black text-sky-400">{kospi_val}</span>\n                    <span class="text-2xl font-bold text-rose-500">{kospi_change}</span>',
            content
        )
        
        # Top 5 table row replacements
        # Samsung
        content = re.sub(
            r'<td class="py-4 font-bold">삼성전자 \(005930\)</td>\s*<td class="py-4 text-right">337,000</td>\s*<td class="py-4 text-right text-rose-500">\+4.50%</td>',
            '<td class="py-4 font-bold">삼성전자 (005930)</td>\n                                <td class="py-4 text-right">340,500</td>\n                                <td class="py-4 text-right text-rose-500">+4.77%</td>',
            content
        )
        # SK Hynix
        content = re.sub(
            r'<td class="py-4 font-bold">SK하이닉스 \(000660\)</td>\s*<td class="py-4 text-right">2,288,000</td>\s*<td class="py-4 text-right text-rose-500">\+7.02%</td>',
            '<td class="py-4 font-bold">SK하이닉스 (000660)</td>\n                                <td class="py-4 text-right">2,320,000</td>\n                                <td class="py-4 text-right text-rose-500">+9.43%</td>',
            content
        )
        # LG Energy
        content = re.sub(
            r'<td class="py-4 font-bold">LG에너지솔루션 \(373220\)</td>\s*<td class="py-4 text-right">415,500</td>\s*<td class="py-4 text-right text-rose-500">\+3.88%</td>',
            '<td class="py-4 font-bold">LG에너지솔루션 (373220)</td>\n                                <td class="py-4 text-right">420,500</td>\n                                <td class="py-4 text-right text-rose-500">+6.59%</td>',
            content
        )
        # NAVER
        content = re.sub(
            r'<td class="py-4 font-bold">NAVER \(035420\)</td>\s*<td class="py-4 text-right">253,000</td>\s*<td class="py-4 text-right text-rose-500">\+2.43%</td>',
            '<td class="py-4 font-bold">NAVER (035420)</td>\n                                <td class="py-4 text-right">247,000</td>\n                                <td class="py-4 text-right text-blue-400">-2.37%</td>',
            content
        )
        # Hyundai Motor
        content = re.sub(
            r'<td class="py-4 font-bold">현대차 \(005380\)</td>\s*<td class="py-4 text-right">630,000</td>\s*<td class="py-4 text-right text-rose-500">\+3.79%</td>',
            '<td class="py-4 font-bold">현대차 (005380)</td>\n                                <td class="py-4 text-right">647,000</td>\n                                <td class="py-4 text-right text-rose-500">+6.42%</td>',
            content
        )
        
        # Investor Trends Card Text
        content = content.replace('+10,118억', '+16,000억')
        content = content.replace('+5,438억', '+9,100억')
        content = content.replace('-14,925억', '-25,100억')
        
        # Investor Chart.js JS
        content = content.replace('data: [10118, 5438, -14925],', 'data: [16000, 9100, -25100],')
        
        # KOSPI Chart.js JS Last value
        content = content.replace('data: [8200, 8280, 8390, 8470, 8545.98],', 'data: [8390, 8470, 8530, 8545.98, 8696.55],')
        
        # Risk Factor Exchange Rate Text
        content = content.replace('1,511.10원', f'{usd_krw_val}원')
        
        with open(kospi_path, 'w', encoding='utf-8', newline='') as f:
            f.write(content)
        print("kospi.html updated.")

    # 3. Update nasdaq.html
    nasdaq_path = os.path.join(base_dir, "nasdaq.html")
    if os.path.exists(nasdaq_path):
        print("Updating nasdaq.html...")
        with open(nasdaq_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # Timestamp
        content = re.sub(
            r'미국 주식 시장 현황 \| \d{4}\. \d{2}\. \d{2}\. \d{2}:\d{2}',
            '미국 주식 시장 현황 | 2026. 06. 16. 09:07',
            content
        )
        
        # NASDAQ Index and Change
        content = re.sub(
            r'<span class="text-5xl font-black text-sky-400">25,888.84</span>\s*<span class="text-2xl font-bold text-rose-500">▲ 79.18 \(\+0.31%\)</span>',
            f'<span class="text-5xl font-black text-sky-400">{nasdaq_val}</span>\n                    <span class="text-2xl font-bold text-rose-500">{nasdaq_change}</span>',
            content
        )
        
        # Exchange rates
        content = content.replace('1,511.10 KRW', f'{usd_krw_val} KRW')
        content = content.replace('High Currency Risk Zone (1,511.10)', f'High Currency Risk Zone ({usd_krw_val})')
        content = content.replace('1,511.10원', f'{usd_krw_val}원')
        
        # NVIDIA price in Currency/Macro Card
        content = re.sub(
            r'<span class="text-3xl font-bold text-sky-400">\$205.19</span>\s*<span class="ml-2 text-xs text-rose-500">▲ 1.14% 상승</span>',
            '<span class="text-3xl font-bold text-sky-400">$211.88</span>\n                        <span class="ml-2 text-xs text-rose-500">▲ 3.26% 상승</span>',
            content
        )
        
        # USA Top 5 table row replacements (NVIDIA, Apple, Microsoft, Alphabet, Amazon)
        # NVIDIA
        content = re.sub(
            r'<td class="py-4 font-bold">엔비디아 \(NVDA\)</td>\s*<td class="py-4 text-right">\$205.19</td>\s*<td class="py-4 text-right text-rose-500">\+1.14%</td>',
            '<td class="py-4 font-bold">엔비디아 (NVDA)</td>\n                                <td class="py-4 text-right">$211.88</td>\n                                <td class="py-4 text-right text-rose-500">+3.26%</td>',
            content
        )
        # Microsoft
        content = re.sub(
            r'<td class="py-4 font-bold">마이크로소프트 \(MSFT\)</td>\s*<td class="py-4 text-right">\$390.74</td>\s*<td class="py-4 text-right text-rose-500">\+1.02%</td>',
            '<td class="py-4 font-bold">마이크로소프트 (MSFT)</td>\n                                <td class="py-4 text-right">$395.12</td>\n                                <td class="py-4 text-right text-rose-500">+1.12%</td>',
            content
        )
        # Alphabet
        content = re.sub(
            r'<td class="py-4 font-bold">알파벳 \(GOOGL\)</td>\s*<td class="py-4 text-right">\$359.68</td>\s*<td class="py-4 text-right text-rose-500">\+3.12%</td>',
            '<td class="py-4 font-bold">알파벳 (GOOGL)</td>\n                                <td class="py-4 text-right">$367.11</td>\n                                <td class="py-4 text-right text-rose-500">+2.07%</td>',
            content
        )
        
        # Semiconductor table row replacements (NVIDIA)
        content = re.sub(
            r'<td class="py-4 font-bold">엔비디아 \(NVDA\)</td>\s*<td class="py-4 text-right">\$205.19</td>\s*<td class="py-4 text-right text-rose-500">\+1.14%</td>',
            '<td class="py-4 font-bold">엔비디아 (NVDA)</td>\n                                <td class="py-4 text-right">$211.88</td>\n                                <td class="py-4 text-right text-rose-500">+3.26%</td>',
            content
        )
        
        # NASDAQ Chart.js JS
        content = content.replace('data: [25200, 25350, 25500, 25650, 25888.84],', 'data: [25500, 25650, 25888.84, 26200, 26683.94],')
        
        with open(nasdaq_path, 'w', encoding='utf-8', newline='') as f:
            f.write(content)
        print("nasdaq.html updated.")

    # 4. Update valuation_semi.html
    semi_path = os.path.join(base_dir, "valuation_semi.html")
    if os.path.exists(semi_path):
        print("Updating valuation_semi.html...")
        with open(semi_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # Timestamp
        content = re.sub(
            r'주요 종목 적정가 및 리스크 진단 \| \d{4}\. \d{2}\. \d{2}\. \d{2}:\d{2}',
            '주요 종목 적정가 및 리스크 진단 | 2026. 06. 16. 09:07',
            content
        )
        content = re.sub(
            r'Last Updated: \d{4}\. \d{2}\. \d{2}\. \d{2}:\d{2} KST',
            'Last Updated: 2026. 06. 16. 09:07 KST',
            content
        )
        
        # Risk Badge and Exchange Rate
        content = content.replace('id="headerRiskVal">1,511.10</span>', f'id="headerRiskVal">{usd_krw_val}</span>')
        content = content.replace('id="exchangeRateVal">1,511.10 KRW</span>', f'id="exchangeRateVal">{usd_krw_val} KRW</span>')
        content = content.replace('value="1511"', f'value="{usd_krw_val_short}"')
        content = content.replace('1,511.10원', f'{usd_krw_val}원')
        
        # Samsung
        content = re.sub(
            r'<div class="text-3xl font-bold text-sky-400">337,000 <span class="text-sm">KRW</span></div>\s*<div class="text-rose-500 text-sm font-semibold">▲ 14,500 \(\+4\.50%\)</div>',
            '<div class="text-3xl font-bold text-sky-400">340,500 <span class="text-sm">KRW</span></div>\n                        <div class="text-rose-500 text-sm font-semibold">▲ 18,500 (+5.75%)</div>',
            content
        )
        content = content.replace('const samsungCurrentPrice = 337000;', 'const samsungCurrentPrice = 340500;')
        
        # Hynix
        content = re.sub(
            r'<div class="text-3xl font-bold text-sky-400">2,288,000 <span class="text-sm">KRW</span></div>\s*<div class="text-rose-500 text-sm font-semibold">▲ 150,000 \(\+7\.02%\)</div>',
            '<div class="text-3xl font-bold text-sky-400">2,320,000 <span class="text-sm">KRW</span></div>\n                        <div class="text-rose-500 text-sm font-semibold">▲ 196,000 (+9.23%)</div>',
            content
        )
        content = content.replace('const hynixCurrentPrice = 2288000;', 'const hynixCurrentPrice = 2320000;')
        
        with open(semi_path, 'w', encoding='utf-8', newline='') as f:
            f.write(content)
        print("valuation_semi.html updated.")

    # 5. Update valuation_defense.html
    defense_path = os.path.join(base_dir, "valuation_defense.html")
    if os.path.exists(defense_path):
        print("Updating valuation_defense.html...")
        with open(defense_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # Timestamp
        content = re.sub(
            r'글로벌 지정학적 리스크 및 수주 가치 진단 \| \d{4}\. \d{2}\. \d{2}\. \d{2}:\d{2}',
            '글로벌 지정학적 리스크 및 수주 가치 진단 | 2026. 06. 16. 09:07',
            content
        )
        content = re.sub(
            r'Last Updated: \d{4}\. \d{2}\. \d{2}\. \d{2}:\d{2} KST',
            'Last Updated: 2026. 06. 16. 09:07 KST',
            content
        )
        
        # Exchange Rate
        content = content.replace('High Currency Risk Zone (1,511.10)', f'High Currency Risk Zone ({usd_krw_val})')
        
        with open(defense_path, 'w', encoding='utf-8', newline='') as f:
            f.write(content)
        print("valuation_defense.html updated.")

    # 6. Update valuation_battery.html
    battery_path = os.path.join(base_dir, "valuation_battery.html")
    if os.path.exists(battery_path):
        print("Updating valuation_battery.html...")
        with open(battery_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # Timestamp
        content = re.sub(
            r'전기차 캐즘 돌파 및 실적 턴어라운드 진단 \| \d{4}\. \d{2}\. \d{2}\. \d{2}:\d{2}',
            '전기차 캐즘 돌파 및 실적 턴어라운드 진단 | 2026. 06. 16. 09:07',
            content
        )
        content = re.sub(
            r'Last Updated: \d{4}\. \d{2}\. \d{2}\. \d{2}:\d{2} KST',
            'Last Updated: 2026. 06. 16. 09:07 KST',
            content
        )
        
        # Exchange Rate
        content = content.replace('High Currency Risk Zone (1,511.10)', f'High Currency Risk Zone ({usd_krw_val})')
        
        # LG Energy Solution
        content = re.sub(
            r'<div class="text-3xl font-bold text-sky-400">415,500 <span class="text-sm">KRW</span></div>\s*<div class="text-rose-500 text-sm font-semibold">▲ 15,500 \(\+3\.88%\)</div>',
            '<div class="text-3xl font-bold text-sky-400">420,500 <span class="text-sm">KRW</span></div>\n                        <div class="text-rose-500 text-sm font-semibold">▲ 26,000 (+6.59%)</div>',
            content
        )
        
        with open(battery_path, 'w', encoding='utf-8', newline='') as f:
            f.write(content)
        print("valuation_battery.html updated.")

    # 7. Update valuation_ai.html
    ai_path = os.path.join(base_dir, "valuation_ai.html")
    if os.path.exists(ai_path):
        print("Updating valuation_ai.html...")
        with open(ai_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # Timestamp
        content = re.sub(
            r'Updated: \d{4}-\d{2}-\d{2} \d{2}:\d{2} KST',
            'Updated: 2026-06-16 09:07 KST',
            content
        )
        
        # Exchange rates
        content = content.replace('고환율 리스크 존 (1,511.10)', f'고환율 리스크 존 ({usd_krw_val})')
        content = content.replace('1,511.10</div>', f'{usd_krw_val}</div>')
        content = content.replace('1,511.10원', f'{usd_krw_val}원')
        content = content.replace('**1,511.10**', f'**{usd_krw_val}**')
        
        # NVIDIA price in metrics card
        content = re.sub(
            r'<div class="text-3xl font-black metric-value mb-1">\$205.19</div>\s*<div class="text-emerald-400 text-sm font-bold">▲ 1.23% <span class="text-slate-500 font-normal ml-1">\(상승\)</span></div>',
            '<div class="text-3xl font-black metric-value mb-1">$211.88</div>\n            <div class="text-emerald-400 text-sm font-bold">▲ 3.26% <span class="text-slate-500 font-normal ml-1">(상승)</span></div>',
            content
        )
        
        with open(ai_path, 'w', encoding='utf-8', newline='') as f:
            f.write(content)
        print("valuation_ai.html updated.")

    # 8. Update valuation_interactive_demo.html
    demo_path = os.path.join(base_dir, "valuation_interactive_demo.html")
    if os.path.exists(demo_path):
        print("Updating valuation_interactive_demo.html...")
        with open(demo_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # Timestamp
        content = re.sub(
            r'매크로 변수에 따른 종목별 할인율 및 적정가 리계산 \| \d{4}\. \d{2}\. \d{2}\. \d{2}:\d{2}',
            '매크로 변수에 따른 종목별 할인율 및 적정가 리계산 | 2026. 06. 16. 09:07',
            content
        )
        content = re.sub(
            r'Last Updated: \d{4}\. \d{2}\. \d{2}\. \d{2}:\d{2} KST',
            'Last Updated: 2026. 06. 16. 09:07 KST',
            content
        )
        
        # Exchange rate fields
        content = content.replace('id="headerRiskVal">1,511.10</span>', f'id="headerRiskVal">{usd_krw_val}</span>')
        content = content.replace('id="exchangeRateVal">1,511.10 KRW</span>', f'id="exchangeRateVal">{usd_krw_val} KRW</span>')
        content = content.replace('value="1511"', f'value="{usd_krw_val_short}"')
        
        # Static price displays
        content = content.replace('₩337,000</div>', '₩340,500</div>')
        content = content.replace('₩2,288,000</div>', '₩2,320,000</div>')
        content = content.replace('₩415,500</div>', '₩420,500</div>')
        
        # Current price JS constants
        content = content.replace('const samsungCurrent = 337000;', 'const samsungCurrent = 340500;')
        content = content.replace('const hynixCurrent = 2288000;', 'const hynixCurrent = 2320000;')
        content = content.replace('const lgCurrent = 415500;', 'const lgCurrent = 420500;')
        
        with open(demo_path, 'w', encoding='utf-8', newline='') as f:
            f.write(content)
        print("valuation_interactive_demo.html updated.")

    # 9. Update news.html timestamp precisely to 09:07 KST
    news_path = os.path.join(base_dir, "news.html")
    if os.path.exists(news_path):
        print("Updating news.html timestamp...")
        with open(news_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        content = re.sub(
            r'실시간 자동사냥 \| \d{4}년 \d{1,2}월 \d{1,2}일 \d{1,2}:\d{2}',
            '실시간 자동사냥 | 2026년 6월 16일 09:07',
            content
        )
        
        with open(news_path, 'w', encoding='utf-8', newline='') as f:
            f.write(content)
        print("news.html timestamp updated.")

    print("All updates completed successfully!")

if __name__ == '__main__':
    update_to_june_16()
