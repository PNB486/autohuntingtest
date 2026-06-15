# -*- coding: utf-8 -*-
import os
import re

def update_all_files():
    base_dir = r"C:\Users\S\Desktop\AI\Gemini\Stock"
    print("Starting KOSPI/NASDAQ/Valuations update for June 17, 2026...")

    # Data constants
    date_str = "2026. 06. 17. 09:00"
    date_hyphen = "2026-06-17 09:00"
    
    kospi_val = "8,726.60"
    kospi_change = "▲ 180.62 (+2.11%)"
    kospi_change_only = "▲ 2.11%"
    
    nasdaq_val = "26,376.34"
    nasdaq_change = "▼ 307.60 (-1.15%)"
    nasdaq_change_only = "▼ 1.15%"
    
    exchange_rate = "1,511.60"
    
    # Stock values (June 16 Close)
    samsung_price = "343,000"
    samsung_change = "▲ 6,000 (+1.78%)"
    samsung_change_only = "+1.78%"
    
    hynix_price = "2,382,000"
    hynix_change = "▲ 94,000 (+4.11%)"
    hynix_change_only = "+4.11%"
    
    lg_price = "410,500"
    lg_change = "▼ 10,000 (-2.38%)"
    lg_change_only = "-2.38%"
    
    naver_price = "242,000"
    naver_change = "▼ 5,000 (-2.02%)" # Wait, Naver closed at 242,000 on June 16. What was previous close? Wait, search results said NAVER fell 7.89% on June 16, closing at 242,000. Let's check if the change is -7.89% or -2.02%. The search summary said "NAVER: -7.89%". So let's write -7.89% or -20,800 (-7.89%). Let's use: -7.89%
    naver_change_str = "▼ 20,700 (-7.89%)"
    naver_change_only = "-7.89%"
    
    hyundai_price = "640,000"
    hyundai_change = "▼ 7,000 (-1.08%)"
    hyundai_change_only = "-1.08%"
    
    hanwha_price = "1,183,000"
    hanwha_change = "▲ 99,000 (+9.13%)"
    hanwha_change_only = "+9.13%"
    
    lig_price = "1,002,000"
    lig_change = "▲ 157,000 (+18.58%)"
    lig_change_only = "+18.58%"
    
    sdi_price = "549,000"
    sdi_change = "▼ 9,000 (-1.61%)"
    sdi_change_only = "-1.61%"

    # US Stocks
    nvda_price = "$207.15"
    nvda_change = "▼ 2.23%"
    aapl_price = "$299.37"
    aapl_change = "+2.83%"
    msft_price = "$392.11"
    msft_change = "-1.91%"
    googl_price = "$371.47"
    googl_change = "+1.19%"
    amzn_price = "$238.70"
    amzn_change = "+0.06%"
    
    tsmc_price = "$425.83"
    tsmc_change = "-3.53%"
    amd_price = "$507.29"
    amd_change = "-4.62%"
    asml_price = "$1,803.89"
    asml_change = "-4.69%"
    broadcom_price = "$391.50"
    broadcom_change = "-3.01%"

    # 1. Update index.html
    index_path = os.path.join(base_dir, "index.html")
    if os.path.exists(index_path):
        with open(index_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        content = re.sub(
            r'<!--\s*KOSPI\s*-->.*?<span class="text-xl font-bold text-sky-400">.*?</span>\s*<span class="text-rose-500 text-sm ml-1 font-bold">.*?</span>',
            f'<span class="text-xl font-bold text-sky-400">{kospi_val}</span>\n                    <span class="text-rose-500 text-sm ml-1 font-bold">▲ 2.11%</span>',
            content, flags=re.DOTALL
        )
        content = content.replace("8,696.55", kospi_val)
        content = content.replace("▲ 1.76%", "▲ 2.11%")
        
        content = content.replace("26,683.94", nasdaq_val)
        content = content.replace("▲ 3.10%", "▼ 1.15%")
        content = content.replace("text-rose-500 text-sm ml-1 font-bold\">▲ 3.10%", "text-blue-400 text-sm ml-1 font-bold\">▼ 1.15%")
        content = content.replace("text-rose-500 text-sm ml-1 font-bold\">▼ 1.15%", "text-blue-400 text-sm ml-1 font-bold\">▼ 1.15%")
        
        content = content.replace("1,514.65", exchange_rate)
        content = content.replace("SYSTEM UPDATED: 2026-06-16 09:07 KST", f"SYSTEM UPDATED: {date_hyphen} KST")
        
        with open(index_path, 'w', encoding='utf-8', newline='') as f:
            f.write(content)
        print("Updated index.html")

    # 2. Update kospi.html
    kospi_path = os.path.join(base_dir, "kospi.html")
    if os.path.exists(kospi_path):
        with open(kospi_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        content = content.replace("주식 시장 현황 | 2026. 06. 16. 09:07", f"주식 시장 현황 | {date_str}")
        content = content.replace("8,696.55", kospi_val)
        content = content.replace("▲ 150.57 (+1.76%)", kospi_change)
        
        # Table top 5
        old_table = """                            <tr class="border-b border-slate-800/50">
                                <td class="py-4 font-bold">삼성전자 (005930)</td>
                                <td class="py-4 text-right">340,500</td>
                                <td class="py-4 text-right text-rose-500">+4.77%</td>
                            </tr>
                            <tr class="border-b border-slate-800/50">
                                <td class="py-4 font-bold">SK하이닉스 (000660)</td>
                                <td class="py-4 text-right">2,320,000</td>
                                <td class="py-4 text-right text-rose-500">+9.43%</td>
                            </tr>
                            <tr class="border-b border-slate-800/50">
                                <td class="py-4 font-bold">LG에너지솔루션 (373220)</td>
                                <td class="py-4 text-right">420,500</td>
                                <td class="py-4 text-right text-rose-500">+6.59%</td>
                            </tr>
                            <tr class="border-b border-slate-800/50">
                                <td class="py-4 font-bold">NAVER (035420)</td>
                                <td class="py-4 text-right">247,000</td>
                                <td class="py-4 text-right text-blue-400">-2.37%</td>
                            </tr>
                            <tr>
                                <td class="py-4 font-bold">현대차 (005380)</td>
                                <td class="py-4 text-right">647,000</td>
                                <td class="py-4 text-right text-rose-500">+6.42%</td>
                            </tr>"""
                            
        new_table = f"""                            <tr class="border-b border-slate-800/50">
                                <td class="py-4 font-bold">삼성전자 (005930)</td>
                                <td class="py-4 text-right">{samsung_price}</td>
                                <td class="py-4 text-right text-rose-500">{samsung_change_only}</td>
                            </tr>
                            <tr class="border-b border-slate-800/50">
                                <td class="py-4 font-bold">SK하이닉스 (000660)</td>
                                <td class="py-4 text-right">{hynix_price}</td>
                                <td class="py-4 text-right text-rose-500">{hynix_change_only}</td>
                            </tr>
                            <tr class="border-b border-slate-800/50">
                                <td class="py-4 font-bold">LG에너지솔루션 (373220)</td>
                                <td class="py-4 text-right">{lg_price}</td>
                                <td class="py-4 text-right text-blue-400">{lg_change_only}</td>
                            </tr>
                            <tr class="border-b border-slate-800/50">
                                <td class="py-4 font-bold">NAVER (035420)</td>
                                <td class="py-4 text-right">{naver_price}</td>
                                <td class="py-4 text-right text-blue-400">{naver_change_only}</td>
                            </tr>
                            <tr>
                                <td class="py-4 font-bold">현대차 (005380)</td>
                                <td class="py-4 text-right">{hyundai_price}</td>
                                <td class="py-4 text-right text-blue-400">{hyundai_change_only}</td>
                            </tr>"""
        
        content = content.replace(old_table.replace('\r\n', '\n'), new_table)
        content = content.replace(old_table, new_table)
        
        # Su-geub indicators
        content = content.replace("+2,625억", "+15,300억")
        content = content.replace("-3,211억", "+7,042억")
        content = content.replace("text-blue-400 font-bold\">-3,211억", "text-rose-500 font-bold\">+7,042억")
        content = content.replace("+490억", "-21,800억")
        content = content.replace("text-rose-500 font-bold\">+490억", "text-blue-400 font-bold\">-21,800억")
        
        # Charts dataset
        content = content.replace("data: [8390, 8470, 8530, 8545.98, 8696.55]", f"data: [8390, 8470, 8530, 8545.98, {kospi_val.replace(',', '')}]")
        content = content.replace("data: [2625, -3211, 490]", "data: [15300, 7042, -21800]")
        
        # Risk factors
        content = content.replace("1,514.65원", f"{exchange_rate}원")
        
        with open(kospi_path, 'w', encoding='utf-8', newline='') as f:
            f.write(content)
        print("Updated kospi.html")

    # 3. Update nasdaq.html
    nasdaq_path = os.path.join(base_dir, "nasdaq.html")
    if os.path.exists(nasdaq_path):
        with open(nasdaq_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        content = content.replace("미국 주식 시장 현황 | 2026. 06. 16. 09:07", f"미국 주식 시장 현황 | {date_str}")
        content = content.replace("26,683.94", nasdaq_val)
        content = content.replace("▲ 795.10 (+3.10%)", nasdaq_change)
        content = content.replace("text-rose-500\">▲ 795.10 (+3.10%)", "text-blue-400\">▼ 307.60 (-1.15%)")
        
        content = content.replace("1,514.65 KRW", f"{exchange_rate} KRW")
        content = content.replace("High Currency Risk Zone (1,514.65)", f"High Currency Risk Zone ({exchange_rate})")
        
        # Nvidia macro block
        content = content.replace("$211.88", "$207.15")
        content = content.replace("▲ 3.26% 상승", "▼ 2.23% 하락")
        content = content.replace("text-rose-500\">▲ 3.26% 상승", "text-blue-400\">▼ 2.23% 하락")
        
        # Top 5 Table
        old_us_table = """                            <tr class="border-b border-slate-800/50">
                                <td class="py-4 font-bold">엔비디아 (NVDA)</td>
                                <td class="py-4 text-right">$211.88</td>
                                <td class="py-4 text-right text-rose-500">+3.26%</td>
                            </tr>
                            <tr class="border-b border-slate-800/50">
                                <td class="py-4 font-bold">애플 (AAPL)</td>
                                <td class="py-4 text-right">$291.13</td>
                                <td class="py-4 text-right text-blue-400">-1.63%</td>
                            </tr>
                            <tr class="border-b border-slate-800/50">
                                <td class="py-4 font-bold">마이크로소프트 (MSFT)</td>
                                <td class="py-4 text-right">$395.12</td>
                                <td class="py-4 text-right text-rose-500">+1.12%</td>
                            </tr>
                            <tr class="border-b border-slate-800/50">
                                <td class="py-4 font-bold">알파벳 (GOOGL)</td>
                                <td class="py-4 text-right">$367.11</td>
                                <td class="py-4 text-right text-rose-500">+2.07%</td>
                            </tr>
                            <tr>
                                <td class="py-4 font-bold">아마존 (AMZN)</td>
                                <td class="py-4 text-right">$238.55</td>
                                <td class="py-4 text-right text-rose-500">+0.41%</td>
                            </tr>"""
                            
        new_us_table = f"""                            <tr class="border-b border-slate-800/50">
                                <td class="py-4 font-bold">엔비디아 (NVDA)</td>
                                <td class="py-4 text-right">{nvda_price}</td>
                                <td class="py-4 text-right text-blue-400">{nvda_change}</td>
                            </tr>
                            <tr class="border-b border-slate-800/50">
                                <td class="py-4 font-bold">애플 (AAPL)</td>
                                <td class="py-4 text-right">{aapl_price}</td>
                                <td class="py-4 text-right text-rose-500">{aapl_change}</td>
                            </tr>
                            <tr class="border-b border-slate-800/50">
                                <td class="py-4 font-bold">마이크로소프트 (MSFT)</td>
                                <td class="py-4 text-right">{msft_price}</td>
                                <td class="py-4 text-right text-blue-400">{msft_change}</td>
                            </tr>
                            <tr class="border-b border-slate-800/50">
                                <td class="py-4 font-bold">알파벳 (GOOGL)</td>
                                <td class="py-4 text-right">{googl_price}</td>
                                <td class="py-4 text-right text-rose-500">{googl_change}</td>
                            </tr>
                            <tr>
                                <td class="py-4 font-bold">아마존 (AMZN)</td>
                                <td class="py-4 text-right">{amzn_price}</td>
                                <td class="py-4 text-right text-rose-500">{amzn_change}</td>
                            </tr>"""
                            
        content = content.replace(old_us_table.replace('\r\n', '\n'), new_us_table)
        content = content.replace(old_us_table, new_us_table)

        # Semis Table
        old_semi_table = """                            <tr class="border-b border-slate-800/50">
                                <td class="py-4 font-bold">엔비디아 (NVDA)</td>
                                <td class="py-4 text-right">$211.88</td>
                                <td class="py-4 text-right text-rose-500">+3.26%</td>
                            </tr>
                            <tr class="border-b border-slate-800/50">
                                <td class="py-4 font-bold">TSMC (TSM)</td>
                                <td class="py-4 text-right">$423.93</td>
                                <td class="py-4 text-right text-rose-500">+1.02%</td>
                            </tr>
                            <tr class="border-b border-slate-800/50">
                                <td class="py-4 font-bold">브로드컴 (AVGO)</td>
                                <td class="py-4 text-right">$382.07</td>
                                <td class="py-4 text-right text-blue-400">-0.84%</td>
                            </tr>
                            <tr class="border-b border-slate-800/50">
                                <td class="py-4 font-bold">AMD (AMD)</td>
                                <td class="py-4 text-right">$511.57</td>
                                <td class="py-4 text-right text-rose-500">+7.38%</td>
                            </tr>
                            <tr>
                                <td class="py-4 font-bold">ASML (ASML)</td>
                                <td class="py-4 text-right">$1,629.60</td>
                                <td class="py-4 text-right text-rose-500">+3.40%</td>
                            </tr>"""
                            
        new_semi_table = f"""                            <tr class="border-b border-slate-800/50">
                                <td class="py-4 font-bold">엔비디아 (NVDA)</td>
                                <td class="py-4 text-right">{nvda_price}</td>
                                <td class="py-4 text-right text-blue-400">{nvda_change}</td>
                            </tr>
                            <tr class="border-b border-slate-800/50">
                                <td class="py-4 font-bold">TSMC (TSM)</td>
                                <td class="py-4 text-right">{tsmc_price}</td>
                                <td class="py-4 text-right text-blue-400">{tsmc_change}</td>
                            </tr>
                            <tr class="border-b border-slate-800/50">
                                <td class="py-4 font-bold">브로드컴 (AVGO)</td>
                                <td class="py-4 text-right">{broadcom_price}</td>
                                <td class="py-4 text-right text-blue-400">{broadcom_change}</td>
                            </tr>
                            <tr class="border-b border-slate-800/50">
                                <td class="py-4 font-bold">AMD (AMD)</td>
                                <td class="py-4 text-right">{amd_price}</td>
                                <td class="py-4 text-right text-blue-400">{amd_change}</td>
                            </tr>
                            <tr>
                                <td class="py-4 font-bold">ASML (ASML)</td>
                                <td class="py-4 text-right">{asml_price}</td>
                                <td class="py-4 text-right text-blue-400">{asml_change}</td>
                            </tr>"""
                            
        content = content.replace(old_semi_table.replace('\r\n', '\n'), new_semi_table)
        content = content.replace(old_semi_table, new_semi_table)
        
        # Charts dataset
        content = content.replace("data: [25500, 25650, 25888.84, 26200, 26683.94]", f"data: [25500, 25650, 25888.84, 26200, {nasdaq_val.replace(',', '')}]")
        
        # Risk factors
        content = content.replace("1,514.65원", f"{exchange_rate}원")

        with open(nasdaq_path, 'w', encoding='utf-8', newline='') as f:
            f.write(content)
        print("Updated nasdaq.html")

    # 4. Update valuation_semi.html
    semi_path = os.path.join(base_dir, "valuation_semi.html")
    if os.path.exists(semi_path):
        with open(semi_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        content = content.replace("주요 종목 적정가 및 리스크 진단 | 2026. 06. 16. 09:07", f"주요 종목 적정가 및 리스크 진단 | {date_str}")
        content = content.replace("Last Updated: 2026. 06. 16. 09:07 KST", f"Last Updated: {date_str} KST")
        
        content = content.replace("1,514.65", exchange_rate)
        content = content.replace("value=\"1515\"", "value=\"1512\"")
        
        # Samsung
        content = content.replace("340,500 <span class=\"text-sm\">KRW</span>", f"{samsung_price} <span class=\"text-sm\">KRW</span>")
        content = content.replace("▲ 18,500 (+5.75%)", samsung_change)
        
        # SK Hynix
        content = content.replace("2,320,000 <span class=\"text-sm\">KRW</span>", f"{hynix_price} <span class=\"text-sm\">KRW</span>")
        content = content.replace("▲ 196,000 (+9.23%)", hynix_change)
        
        # JS current prices
        content = content.replace("const samsungCurrentPrice = 340500;", f"const samsungCurrentPrice = {samsung_price.replace(',', '')};")
        content = content.replace("const hynixCurrentPrice = 2320000;", f"const hynixCurrentPrice = {hynix_price.replace(',', '')};")
        
        with open(semi_path, 'w', encoding='utf-8', newline='') as f:
            f.write(content)
        print("Updated valuation_semi.html")

    # 5. Update valuation_defense.html
    defense_path = os.path.join(base_dir, "valuation_defense.html")
    if os.path.exists(defense_path):
        with open(defense_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        content = content.replace("글로벌 지정학적 리스크 및 수주 가치 진단 | 2026. 06. 16. 09:07", f"글로벌 지정학적 리스크 및 수주 가치 진단 | {date_str}")
        content = content.replace("Last Updated: 2026. 06. 16. 09:07 KST", f"Last Updated: {date_str} KST")
        
        content = content.replace("1,514.65", exchange_rate)
        
        # Hanwha
        content = content.replace("1,085,000 <span class=\"text-sm\">KRW</span>", f"{hanwha_price} <span class=\"text-sm\">KRW</span>")
        content = content.replace("▲ 7,000 (+0.65%)", hanwha_change)
        content = content.replace("style=\"width: 79.8%\"", "style=\"width: 87.0%\"")
        content = content.replace("상승 여력: +25.35%", "상승 여력: +14.96%")
        
        # LIG Nex1
        content = content.replace("785,000 <span class=\"text-sm\">KRW</span>", f"{lig_price} <span class=\"text-sm\">KRW</span>")
        content = content.replace("▲ 13,000 (+1.68%)", lig_change)
        content = content.replace("style=\"width: 84.0%\"", "style=\"width: 100%\"")
        content = content.replace("상승 여력: +19.11%", "상승 여력: -6.69%")
        
        with open(defense_path, 'w', encoding='utf-8', newline='') as f:
            f.write(content)
        print("Updated valuation_defense.html")

    # 6. Update valuation_battery.html
    battery_path = os.path.join(base_dir, "valuation_battery.html")
    if os.path.exists(battery_path):
        with open(battery_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        content = content.replace("전기차 캐즘 돌파 및 실적 턴어라운드 진단 | 2026. 06. 16. 09:07", f"전기차 캐즘 돌파 및 실적 턴어라운드 진단 | {date_str}")
        content = content.replace("Last Updated: 2026. 06. 16. 09:07 KST", f"Last Updated: {date_str} KST")
        
        content = content.replace("1,514.65", exchange_rate)
        
        # LG Energy
        content = content.replace("420,500 <span class=\"text-sm\">KRW</span>", f"{lg_price} <span class=\"text-sm\">KRW</span>")
        content = content.replace("text-rose-500 text-sm font-semibold\">▲ 26,000 (+6.59%)", f"text-blue-400 text-sm font-semibold\">{lg_change}")
        content = content.replace("style=\"width: 81.5%\"", "style=\"width: 80.5%\"")
        content = content.replace("상승 여력: +22.74%", "상승 여력: +24.24%")
        
        # Samsung SDI
        content = content.replace("558,000 <span class=\"text-sm\">KRW</span>", f"{sdi_price} <span class=\"text-sm\">KRW</span>")
        content = content.replace("text-rose-500 text-sm font-semibold\">▲ 19,000 (+3.53%)", f"text-blue-400 text-sm font-semibold\">{sdi_change}")
        content = content.replace("style=\"width: 77.2%\"", "style=\"width: 76.0%\"")
        content = content.replace("상승 여력: +29.48%", "상승 여력: +31.60%")
        
        with open(battery_path, 'w', encoding='utf-8', newline='') as f:
            f.write(content)
        print("Updated valuation_battery.html")

    # 7. Update valuation_ai.html
    ai_path = os.path.join(base_dir, "valuation_ai.html")
    if os.path.exists(ai_path):
        with open(ai_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        content = content.replace("Updated: 2026-06-16 09:07 KST", f"Updated: {date_hyphen} KST")
        content = content.replace("고환율 리스크 존 (1,514.65)", f"고환율 리스크 존 ({exchange_rate})")
        
        # Metrics
        content = content.replace("1,514.65", exchange_rate)
        
        # Nvidia
        old_nvda = """        <div class="card p-6">
            <div class="text-slate-500 text-xs font-bold mb-2 uppercase">NVIDIA (NVDA)</div>
            <div class="text-3xl font-black metric-value mb-1">$211.88</div>
            <div class="text-emerald-400 text-sm font-bold">▲ 3.26% <span class="text-slate-500 font-normal ml-1">(상승)</span></div>
        </div>"""
        
        new_nvda = f"""        <div class="card p-6">
            <div class="text-slate-500 text-xs font-bold mb-2 uppercase">NVIDIA (NVDA)</div>
            <div class="text-3xl font-black metric-value mb-1">{nvda_price}</div>
            <div class="text-red-400 text-sm font-bold">▼ 2.23% <span class="text-slate-500 font-normal ml-1">(하락)</span></div>
        </div>"""
        
        content = content.replace(old_nvda.replace('\r\n', '\n'), new_nvda)
        content = content.replace(old_nvda, new_nvda)
        
        with open(ai_path, 'w', encoding='utf-8', newline='') as f:
            f.write(content)
        print("Updated valuation_ai.html")

    # 8. Update valuation_interactive_demo.html
    demo_path = os.path.join(base_dir, "valuation_interactive_demo.html")
    if os.path.exists(demo_path):
        with open(demo_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        content = content.replace("매크로 변수에 따른 종목별 할인율 및 적정가 리계산 | 2026. 06. 16. 09:07", f"매크로 변수에 따른 종목별 할인율 및 적정가 리계산 | {date_str}")
        content = content.replace("Last Updated: 2026. 06. 16. 09:07 KST", f"Last Updated: {date_str} KST")
        
        content = content.replace("1,514.65", exchange_rate)
        content = content.replace("value=\"1515\"", "value=\"1512\"")
        
        # HTML prices display
        content = content.replace("<div class=\"font-bold text-slate-300\">₩340,500</div>", f"<div class=\"font-bold text-slate-300\">₩{samsung_price}</div>")
        content = content.replace("<div class=\"font-bold text-slate-300\">₩2,320,000</div>", f"<div class=\"font-bold text-slate-300\">₩{hynix_price}</div>")
        content = content.replace("<div class=\"font-bold text-slate-300\">₩420,500</div>", f"<div class=\"font-bold text-slate-300\">₩{lg_price}</div>")
        
        # JS values
        content = content.replace("const samsungCurrent = 340500;", f"const samsungCurrent = {samsung_price.replace(',', '')};")
        content = content.replace("const hynixCurrent = 2320000;", f"const hynixCurrent = {hynix_price.replace(',', '')};")
        content = content.replace("const lgCurrent = 420500;", f"const lgCurrent = {lg_price.replace(',', '')};")
        
        # Initial upsides and progress
        content = content.replace("id=\"samsungProgress\" style=\"width: 70.6%\"", "id=\"samsungProgress\" style=\"width: 70.8%\"")
        content = content.replace("상승여력: +41.67%", "상승여력: +41.25%")
        
        content = content.replace("상승여력: -6.14%", "상승여력: -10.79%")
        
        content = content.replace("id=\"lgProgress\" style=\"width: 78.8%\"", "id=\"lgProgress\" style=\"width: 80.5%\"")
        content = content.replace("상승여력: +26.87%", "상승여력: +24.24%")
        
        with open(demo_path, 'w', encoding='utf-8', newline='') as f:
            f.write(content)
        print("Updated valuation_interactive_demo.html")

if __name__ == '__main__':
    update_all_files()
