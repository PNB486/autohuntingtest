# -*- coding: utf-8 -*-
import os
import re

def update_portal():
    base_dir = r"C:\Users\S\Desktop\AI\Gemini\Stock"
    
    print("Starting updates for 17:00 KST...")

    # 1. Update index.html
    index_path = os.path.join(base_dir, "index.html")
    if os.path.exists(index_path):
        with open(index_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # KOSPI
        content = content.replace(
            '<span class="text-xl font-bold text-sky-400">8,531.41</span>\n                    <span class="text-rose-500 text-sm ml-1 font-bold">▲ 5.02%</span>',
            '<span class="text-xl font-bold text-sky-400">8,545.98</span>\n                    <span class="text-rose-500 text-sm ml-1 font-bold">▲ 5.20%</span>'
        )
        content = content.replace(
            '<span class="text-xl font-bold text-sky-400">8,531.41</span>\r\n                    <span class="text-rose-500 text-sm ml-1 font-bold">▲ 5.02%</span>',
            '<span class="text-xl font-bold text-sky-400">8,545.98</span>\n                    <span class="text-rose-500 text-sm ml-1 font-bold">▲ 5.20%</span>'
        )
        
        # USD/KRW
        content = content.replace(
            '<span class="text-xl font-bold text-rose-500">1,508.55</span>',
            '<span class="text-xl font-bold text-rose-500">1,511.10</span>'
        )
        content = content.replace(
            'High Currency Risk Zone (1,508.55)',
            'High Currency Risk Zone (1,511.10)'
        )
        
        with open(index_path, 'w', encoding='utf-8', newline='') as f:
            f.write(content)
        print("index.html updated successfully.")

    # 2. Update kospi.html
    kospi_path = os.path.join(base_dir, "kospi.html")
    if os.path.exists(kospi_path):
        with open(kospi_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # KOSPI Index and Change
        content = content.replace(
            '<span class="text-5xl font-black text-sky-400">8,531.41</span>\n                    <span class="text-2xl font-bold text-rose-500">▲ 407.79 (+5.02%)</span>',
            '<span class="text-5xl font-black text-sky-400">8,545.98</span>\n                    <span class="text-2xl font-bold text-rose-500">▲ 422.36 (+5.20%)</span>'
        )
        content = content.replace(
            '<span class="text-5xl font-black text-sky-400">8,531.41</span>\r\n                    <span class="text-2xl font-bold text-rose-500">▲ 407.79 (+5.02%)</span>',
            '<span class="text-5xl font-black text-sky-400">8,545.98</span>\n                    <span class="text-2xl font-bold text-rose-500">▲ 422.36 (+5.20%)</span>'
        )
        
        # Top 5 Stocks Table
        old_table = """                            <tr class="border-b border-slate-800/50">
                                <td class="py-4 font-bold">삼성전자 (005930)</td>
                                <td class="py-4 text-right">339,000</td>
                                <td class="py-4 text-right text-rose-500">+5.12%</td>
                            </tr>
                            <tr class="border-b border-slate-800/50">
                                <td class="py-4 font-bold">SK하이닉스 (000660)</td>
                                <td class="py-4 text-right">2,280,000</td>
                                <td class="py-4 text-right text-rose-500">+6.05%</td>
                            </tr>
                            <tr class="border-b border-slate-800/50">
                                <td class="py-4 font-bold">LG에너지솔루션 (373220)</td>
                                <td class="py-4 text-right">412,000</td>
                                <td class="py-4 text-right text-rose-500">+3.00%</td>
                            </tr>
                            <tr class="border-b border-slate-800/50">
                                <td class="py-4 font-bold">NAVER (035420)</td>
                                <td class="py-4 text-right">249,000</td>
                                <td class="py-4 text-right text-rose-500">+0.81%</td>
                            </tr>
                            <tr>
                                <td class="py-4 font-bold">현대차 (005380)</td>
                                <td class="py-4 text-right">628,000</td>
                                <td class="py-4 text-right text-rose-500">+2.95%</td>
                            </tr>"""

        new_table = """                            <tr class="border-b border-slate-800/50">
                                <td class="py-4 font-bold">삼성전자 (005930)</td>
                                <td class="py-4 text-right">337,000</td>
                                <td class="py-4 text-right text-rose-500">+4.50%</td>
                            </tr>
                            <tr class="border-b border-slate-800/50">
                                <td class="py-4 font-bold">SK하이닉스 (000660)</td>
                                <td class="py-4 text-right">2,288,000</td>
                                <td class="py-4 text-right text-rose-500">+7.02%</td>
                            </tr>
                            <tr class="border-b border-slate-800/50">
                                <td class="py-4 font-bold">LG에너지솔루션 (373220)</td>
                                <td class="py-4 text-right">415,500</td>
                                <td class="py-4 text-right text-rose-500">+3.88%</td>
                            </tr>
                            <tr class="border-b border-slate-800/50">
                                <td class="py-4 font-bold">NAVER (035420)</td>
                                <td class="py-4 text-right">253,000</td>
                                <td class="py-4 text-right text-rose-500">+2.43%</td>
                            </tr>
                            <tr>
                                <td class="py-4 font-bold">현대차 (005380)</td>
                                <td class="py-4 text-right">630,000</td>
                                <td class="py-4 text-right text-rose-500">+3.79%</td>
                            </tr>"""
                            
        content = content.replace(old_table.replace('\r\n', '\n'), new_table)
        content = content.replace(old_table.replace('\n', '\r\n'), new_table)
        
        # Investor Trends Card Text
        content = content.replace('+5,648억', '+10,118억')
        content = content.replace('+8,193억', '+5,438억')
        content = content.replace('-13,741억', '-14,925억')
        
        # Investor Chart.js JS
        content = content.replace('data: [2848, 9326, -11971],', 'data: [10118, 5438, -14925],')
        
        # KOSPI Chart.js JS Last value
        content = content.replace('[8200, 8280, 8390, 8470, 8531.41]', '[8200, 8280, 8390, 8470, 8545.98]')
        
        # Risk Factor Exchange Rate Text
        content = content.replace('1,508.55원', '1,511.10원')
        
        with open(kospi_path, 'w', encoding='utf-8', newline='') as f:
            f.write(content)
        print("kospi.html updated successfully.")

    # 3. Update nasdaq.html
    nasdaq_path = os.path.join(base_dir, "nasdaq.html")
    if os.path.exists(nasdaq_path):
        with open(nasdaq_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        content = content.replace('1,508.55 KRW', '1,511.10 KRW')
        content = content.replace('High Currency Risk Zone (1,508.55)', 'High Currency Risk Zone (1,511.10)')
        content = content.replace('1,508.55원', '1,511.10원')
        
        with open(nasdaq_path, 'w', encoding='utf-8', newline='') as f:
            f.write(content)
        print("nasdaq.html updated successfully.")

    # 4. Update valuation_semi.html
    semi_path = os.path.join(base_dir, "valuation_semi.html")
    if os.path.exists(semi_path):
        with open(semi_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # Risk Badge and Exchange Rate
        content = content.replace('id="headerRiskVal">1,508.55</span>', 'id="headerRiskVal">1,511.10</span>')
        content = content.replace('id="exchangeRateVal">1,508.55 KRW</span>', 'id="exchangeRateVal">1,511.10 KRW</span>')
        content = content.replace('value="1509"', 'value="1511"')
        content = content.replace('1,508.55원', '1,511.10원')
        
        # Samsung
        content = content.replace('339,000 <span class="text-sm">KRW</span>', '337,000 <span class="text-sm">KRW</span>')
        content = content.replace('▲ 16,500 (+5.12%)', '▲ 14,500 (+4.50%)')
        content = content.replace('const samsungCurrentPrice = 339000;', 'const samsungCurrentPrice = 337000;')
        
        # Hynix
        content = content.replace('2,280,000 <span class="text-sm">KRW</span>', '2,288,000 <span class="text-sm">KRW</span>')
        content = content.replace('▲ 130,000 (+6.05%)', '▲ 150,000 (+7.02%)')
        content = content.replace('const hynixCurrentPrice = 2280000;', 'const hynixCurrentPrice = 2288000;')
        
        with open(semi_path, 'w', encoding='utf-8', newline='') as f:
            f.write(content)
        print("valuation_semi.html updated successfully.")

    # 5. Update valuation_defense.html
    defense_path = os.path.join(base_dir, "valuation_defense.html")
    if os.path.exists(defense_path):
        with open(defense_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        content = content.replace('High Currency Risk Zone (1,508.55)', 'High Currency Risk Zone (1,511.10)')
        
        # Hanwha Aerospace
        content = content.replace('1,035,000 <span class="text-sm">KRW</span>', '1,085,000 <span class="text-sm">KRW</span>')
        content = content.replace('▲ 21,000 (+2.07%)', '▲ 7,000 (+0.65%)')
        content = content.replace('style="width: 75.7%"', 'style="width: 79.8%"')
        content = content.replace('상승 여력: +32.04%', '상승 여력: +25.35%')
        
        # LIG Nex1
        content = content.replace('732,000 <span class="text-sm">KRW</span>', '785,000 <span class="text-sm">KRW</span>')
        content = content.replace('▲ 36,000 (+5.17%)', '▲ 13,000 (+1.68%)')
        content = content.replace('style="width: 77.5%"', 'style="width: 84.0%"')
        content = content.replace('상승 여력: +28.97%', '상승 여력: +19.11%')
        
        with open(defense_path, 'w', encoding='utf-8', newline='') as f:
            f.write(content)
        print("valuation_defense.html updated successfully.")

    # 6. Update valuation_battery.html
    battery_path = os.path.join(base_dir, "valuation_battery.html")
    if os.path.exists(battery_path):
        with open(battery_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        content = content.replace('High Currency Risk Zone (1,508.55)', 'High Currency Risk Zone (1,511.10)')
        
        # LG Energy Solution
        content = content.replace('412,000 <span class="text-sm">KRW</span>', '415,500 <span class="text-sm">KRW</span>')
        content = content.replace('▲ 12,000 (+3.00%)', '▲ 15,500 (+3.88%)')
        content = content.replace('style="width: 78.8%"', 'style="width: 81.5%"')
        content = content.replace('상승 여력: +26.87%', '상승 여력: +22.74%')
        
        # Samsung SDI
        content = content.replace('468,000 <span class="text-sm">KRW</span>', '558,000 <span class="text-sm">KRW</span>')
        content = content.replace('▼ 47,000 (-9.13%)', '▲ 19,000 (+3.53%)')
        content = content.replace('style="width: 71.3%"', 'style="width: 77.2%"')
        content = content.replace('상승 여력: +40.29%', '상승 여력: +29.48%')
        
        with open(battery_path, 'w', encoding='utf-8', newline='') as f:
            f.write(content)
        print("valuation_battery.html updated successfully.")

    # 7. Update valuation_ai.html
    ai_path = os.path.join(base_dir, "valuation_ai.html")
    if os.path.exists(ai_path):
        with open(ai_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        content = content.replace('고환율 리스크 존 (1,508.55)', '고환율 리스크 존 (1,511.10)')
        content = content.replace('1,508.55</div>', '1,511.10</div>')
        content = content.replace('1,508.55원', '1,511.10원')
        content = content.replace('**1,508.55**', '**1,511.10**')
        
        with open(ai_path, 'w', encoding='utf-8', newline='') as f:
            f.write(content)
        print("valuation_ai.html updated successfully.")

    # 8. Update valuation_interactive_demo.html
    demo_path = os.path.join(base_dir, "valuation_interactive_demo.html")
    if os.path.exists(demo_path):
        with open(demo_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        content = content.replace('id="headerRiskVal">1,508.55</span>', 'id="headerRiskVal">1,511.10</span>')
        content = content.replace('id="exchangeRateVal">1,508.55 KRW</span>', 'id="exchangeRateVal">1,511.10 KRW</span>')
        content = content.replace('value="1509"', 'value="1511"')
        
        # Samsung
        content = content.replace('₩339,000</div>', '₩337,000</div>')
        content = content.replace('const samsungCurrent = 339000;', 'const samsungCurrent = 337000;')
        
        # Hynix
        content = content.replace('₩2,280,000</div>', '₩2,288,000</div>')
        content = content.replace('const hynixCurrent = 2280000;', 'const hynixCurrent = 2288000;')
        
        # LG
        content = content.replace('₩412,000</div>', '₩415,500</div>')
        content = content.replace('const lgCurrent = 412000;', 'const lgCurrent = 415500;')
        
        with open(demo_path, 'w', encoding='utf-8', newline='') as f:
            f.write(content)
        print("valuation_interactive_demo.html updated successfully.")

if __name__ == "__main__":
    update_portal()
