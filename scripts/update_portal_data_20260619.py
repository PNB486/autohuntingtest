# -*- coding: utf-8 -*-
import os
import re

def update_all_files():
    base_dir = r"C:\Users\S\Desktop\AI\Gemini\Stock"
    print("Starting KOSPI/NASDAQ/Valuations update for June 19, 2026 (09:02)...")

    # Data constants for June 19, 2026
    date_str = "2026. 06. 19. 09:02"
    date_hyphen = "2026-06-19 09:02"
    date_korean = "2026년 6월 19일 9시 02분"
    
    kospi_val = "9,063.84"
    kospi_change = "▲ 199.60 (+2.25%)"
    kospi_change_only = "+2.25%"
    
    nasdaq_val = "26,517.93"
    nasdaq_change = "▲ 496.27 (+1.91%)"
    nasdaq_change_only = "+1.91%"
    
    exchange_rate = "1,527.10"

    # Stock values (June 18 Close / June 19 morning verified)
    samsung_price = "362,500"
    samsung_change = "▲ 16,000 (+4.62%)"
    samsung_change_only = "+4.62%"
    
    hynix_price = "2,685,000"
    hynix_change = "▲ 164,000 (+6.51%)"
    hynix_change_only = "+6.51%"
    
    lg_price = "400,000"
    lg_change = "▼ 16,000 (-3.85%)"
    lg_change_only = "-3.85%"
    
    naver_price = "235,000"
    naver_change = "▼ 8,500 (-3.49%)"
    naver_change_only = "-3.49%"
    
    hyundai_price = "602,000"
    hyundai_change = "▼ 16,000 (-2.59%)"
    hyundai_change_only = "-2.59%"
    
    hanwha_price = "1,189,000"
    hanwha_change = "▼ 35,000 (-2.86%)"
    hanwha_change_only = "-2.86%"
    
    lig_price = "884,000"
    lig_change = "▼ 66,000 (-6.95%)"
    lig_change_only = "-6.95%"
    
    sdi_price = "522,000"
    sdi_change = "▼ 28,000 (-5.09%)"
    sdi_change_only = "-5.09%"

    # US Stocks
    nvda_price = "$210.69"
    nvda_change = "+1.27%"
    aapl_price = "$295.95"
    aapl_change = "0.00%"
    msft_price = "$379.40"
    msft_change = "+0.13%"
    googl_price = "$367.93"
    googl_change = "+1.14%"
    amzn_price = "$244.39"
    amzn_change = "+2.04%"
    
    tsmc_price = "$462.12"
    tsmc_change = "+5.38%"
    amd_price = "$536.67"
    amd_change = "+2.48%"
    asml_price = "$1,929.68"
    asml_change = "+3.31%"
    broadcom_price = "$407.23"
    broadcom_change = "+3.65%"

    # Helper function to replace stock info in table rows
    def update_stock_in_html(content, stock_name, new_price, new_change):
        escaped_name = re.escape(stock_name)
        if "0.00%" in new_change:
            color_name = "slate-400"
        elif "+" in new_change or "▲" in new_change:
            color_name = "rose-500"
        else:
            color_name = "blue-400"
        
        # Matches table cells for stock prices and change indicators
        pattern = rf'(<td class="py-4 font-bold"\s*>{escaped_name}</td>\s*<td class="py-4 text-right"\s*>)[^<]+(</td>\s*<td class="py-4 text-right\s+text-)(rose-500|blue-400|emerald-400|slate-400)(">)[^<]+(</td>)'
        replacement = rf'\g<1>{new_price}\g<2>{color_name}\g<4>{new_change}\g<5>'
        
        new_content, count = re.subn(pattern, replacement, content, flags=re.DOTALL)
        return new_content, count

    # 1. Update index.html
    index_path = os.path.join(base_dir, "index.html")
    if os.path.exists(index_path):
        with open(index_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # Update KOSPI
        content = content.replace("8,864.24", kospi_val)
        content = content.replace("▲ 1.58%", "▲ 2.25%")
        
        # Update NASDAQ
        content = content.replace("26,021.66", nasdaq_val)
        # Handle direction change from down to up (blue-400 to rose-500)
        content = content.replace(
            '<span class="text-blue-400 text-sm ml-1 font-bold">▼ 1.34%</span>',
            '<span class="text-rose-500 text-sm ml-1 font-bold">▲ 1.91%</span>'
        )
        
        # Update USD/KRW
        content = content.replace("1,513.40", exchange_rate)
        
        # Update Timestamps
        content = content.replace("SYSTEM UPDATED: 2026-06-18 09:02 KST", f"SYSTEM UPDATED: {date_hyphen} KST")
        
        with open(index_path, 'w', encoding='utf-8', newline='') as f:
            f.write(content)
        print("Updated index.html")

    # 2. Update kospi.html
    kospi_path = os.path.join(base_dir, "kospi.html")
    if os.path.exists(kospi_path):
        with open(kospi_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # Update Title Date
        content = content.replace("주식 시장 현황 | 2026. 06. 18. 09:02", f"주식 시장 현황 | {date_str}")
        
        # Update Index
        content = content.replace("8,864.24", kospi_val)
        content = content.replace("▲ 137.64 (+1.58%)", kospi_change)
        
        # Update stocks in table
        content, c1 = update_stock_in_html(content, "삼성전자 (005930)", samsung_price, samsung_change_only)
        content, c2 = update_stock_in_html(content, "SK하이닉스 (000660)", hynix_price, hynix_change_only)
        content, c3 = update_stock_in_html(content, "LG에너지솔루션 (373220)", lg_price, lg_change_only)
        content, c4 = update_stock_in_html(content, "NAVER (035420)", naver_price, naver_change_only)
        content, c5 = update_stock_in_html(content, "현대차 (005380)", hyundai_price, hyundai_change_only)
        print(f"Updated KOSPI stock rows: {c1}, {c2}, {c3}, {c4}, {c5}")
        
        # Su-geub indicators using robust regex
        pattern_foreign = r'(<span class="text-slate-400 font-medium">외국인</span>\s*<span class="text-)(blue-400|rose-500)( font-bold">)[^<]+(</span>)'
        content = re.sub(pattern_foreign, r'\g<1>blue-400\g<3>-5,611억\g<4>', content)
        
        pattern_inst = r'(<span class="text-slate-400 font-medium">기관</span>\s*<span class="text-)(blue-400|rose-500)( font-bold">)[^<]+(</span>)'
        content = re.sub(pattern_inst, r'\g<1>rose-500\g<3>+1,215억\g<4>', content)
        
        pattern_retail = r'(<span class="text-slate-400 font-medium">개인</span>\s*<span class="text-)(blue-400|rose-500)( font-bold">)[^<]+(</span>)'
        content = re.sub(pattern_retail, r'\g<1>rose-500\g<3>+5,243억\g<4>', content)
        
        # Charts dataset
        content = content.replace("data: [8390, 8470, 8530, 8545.98, 8864.24]", f"data: [8390, 8470, 8530, 8545.98, {kospi_val.replace(',', '')}]")
        content = content.replace("data: [-9945, 5956, 5254]", "data: [-5611, 1215, 5243]")
        
        # Risk factors
        content = content.replace("1,513.40원", f"{exchange_rate}원")
        
        with open(kospi_path, 'w', encoding='utf-8', newline='') as f:
            f.write(content)
        print("Updated kospi.html")

    # 3. Update nasdaq.html
    nasdaq_path = os.path.join(base_dir, "nasdaq.html")
    if os.path.exists(nasdaq_path):
        with open(nasdaq_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        content = content.replace("미국 주식 시장 현황 | 2026. 06. 18. 09:02", f"미국 주식 시장 현황 | {date_str}")
        
        # Update Index and change direction (down to up)
        pattern_nasdaq_change = r'(NASDAQ 지수</h3>\s*<div class="flex items-baseline gap-4 mb-6">\s*<span class="text-5xl font-black text-sky-400">)26,021.66(</span>\s*<span class="text-2xl font-bold text-)(rose-500|blue-400)(">)[^<]+(</span>)'
        content = re.sub(pattern_nasdaq_change, r'\g<1>26,517.93\g<2>rose-500\g<4>▲ 496.27 (+1.91%)\g<5>', content)
        
        content = content.replace("1,513.40 KRW", f"{exchange_rate} KRW")
        content = content.replace("High Currency Risk Zone (1,513.40)", f"High Currency Risk Zone ({exchange_rate})")
        
        # Nvidia block in Currency/Macro Card
        pattern_nvda_macro = r'(NVIDIA \(NVDA\)\s*</span>\s*<span class="text-3xl font-bold text-sky-400">)[^<]+(</span>\s*<span class="ml-2 text-xs text-)(rose-500|blue-400)(">)[^<]+(</span>)'
        content = re.sub(pattern_nvda_macro, r'\g<1>$210.69\g<2>rose-500\g<4>▲ 1.27% 상승\g<5>', content)
        
        # Top 5 Table
        content, c1 = update_stock_in_html(content, "엔비디아 (NVDA)", nvda_price, nvda_change)
        content, c2 = update_stock_in_html(content, "애플 (AAPL)", aapl_price, aapl_change)
        content, c3 = update_stock_in_html(content, "마이크로소프트 (MSFT)", msft_price, msft_change)
        content, c4 = update_stock_in_html(content, "알파벳 (GOOGL)", googl_price, googl_change)
        content, c5 = update_stock_in_html(content, "아마존 (AMZN)", amzn_price, amzn_change)
        
        # Semis Table
        content, c6 = update_stock_in_html(content, "TSMC (TSM)", tsmc_price, tsmc_change)
        content, c7 = update_stock_in_html(content, "브로드컴 (AVGO)", broadcom_price, broadcom_change)
        content, c8 = update_stock_in_html(content, "AMD (AMD)", amd_price, amd_change)
        content, c9 = update_stock_in_html(content, "ASML (ASML)", asml_price, asml_change)
        
        print(f"Updated NASDAQ stock rows: {c1}, {c2}, {c3}, {c4}, {c5}, {c6}, {c7}, {c8}, {c9}")
        
        # Charts dataset
        content = content.replace("data: [25500, 25650, 25888.84, 26200, 26021.66]", f"data: [25500, 25650, 25888.84, 26200, {nasdaq_val.replace(',', '')}]")
        
        # Risk factors
        content = content.replace("1,513.40원", f"{exchange_rate}원")
        
        with open(nasdaq_path, 'w', encoding='utf-8', newline='') as f:
            f.write(content)
        print("Updated nasdaq.html")

    # 4. Update valuation_semi.html
    semi_path = os.path.join(base_dir, "valuation_semi.html")
    if os.path.exists(semi_path):
        with open(semi_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        content = content.replace("주요 종목 적정가 및 리스크 진단 | 2026. 06. 18. 09:02", f"주요 종목 적정가 및 리스크 진단 | {date_str}")
        content = content.replace("Last Updated: 2026. 06. 18. 09:02 KST", f"Last Updated: {date_str} KST")
        
        content = content.replace("1,513.40", exchange_rate)
        content = content.replace('value="1512"', 'value="1527"')
        
        # Samsung Electronics
        content = content.replace("346,500 <span class=\"text-sm\">KRW</span>", f"{samsung_price} <span class=\"text-sm\">KRW</span>")
        content = content.replace("▲ 3,500 (+1.02%)", samsung_change)
        
        # SK Hynix
        content = content.replace("2,521,000 <span class=\"text-sm\">KRW</span>", f"{hynix_price} <span class=\"text-sm\">KRW</span>")
        content = content.replace("▲ 139,000 (+5.84%)", hynix_change)
        
        # JS constants
        content = content.replace("const samsungCurrentPrice = 346500;", f"const samsungCurrentPrice = {samsung_price.replace(',', '')};")
        content = content.replace("const hynixCurrentPrice = 2521000;", f"const hynixCurrentPrice = {hynix_price.replace(',', '')};")
        
        with open(semi_path, 'w', encoding='utf-8', newline='') as f:
            f.write(content)
        print("Updated valuation_semi.html")

    # 5. Update valuation_defense.html
    defense_path = os.path.join(base_dir, "valuation_defense.html")
    if os.path.exists(defense_path):
        with open(defense_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        content = content.replace("글로벌 지정학적 리스크 및 수주 가치 진단 | 2026. 06. 18. 09:02", f"글로벌 지정학적 리스크 및 수주 가치 진단 | {date_str}")
        content = content.replace("Last Updated: 2026. 06. 18. 09:02 KST", f"Last Updated: {date_str} KST")
        
        content = content.replace("1,513.40", exchange_rate)
        
        # Hanwha Aerospace
        content = content.replace("1,224,000 <span class=\"text-sm\">KRW</span>", f"{hanwha_price} <span class=\"text-sm\">KRW</span>")
        # Change direction (up to down)
        content = content.replace(
            '<div class="text-rose-500 text-sm font-semibold">▲ 41,000 (+3.47%)</div>',
            f'<div class="text-blue-400 text-sm font-semibold">{hanwha_change}</div>'
        )
        content = content.replace("style=\"width: 90.0%\"", "style=\"width: 87.4%\"")
        content = content.replace("상승 여력: +11.11%", "상승 여력: +14.38%")
        
        # LIG Nex1
        content = content.replace("950,000 <span class=\"text-sm\">KRW</span>", f"{lig_price} <span class=\"text-sm\">KRW</span>")
        content = content.replace(
            '<div class="text-blue-400 text-sm font-semibold">▼ 52,000 (-5.19%)</div>',
            f'<div class="text-blue-400 text-sm font-semibold">{lig_change}</div>'
        )
        content = content.replace("style=\"width: 100%\"", "style=\"width: 94.5%\"")
        content = content.replace("상승 여력: -1.58%", "상승 여력: +5.77%")
        
        with open(defense_path, 'w', encoding='utf-8', newline='') as f:
            f.write(content)
        print("Updated valuation_defense.html")

    # 6. Update valuation_battery.html
    battery_path = os.path.join(base_dir, "valuation_battery.html")
    if os.path.exists(battery_path):
        with open(battery_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        content = content.replace("전기차 캐즘 돌파 및 실적 턴어라운드 진단 | 2026. 06. 18. 09:02", f"전기차 캐즘 돌파 및 실적 턴어라운드 진단 | {date_str}")
        content = content.replace("Last Updated: 2026. 06. 18. 09:02 KST", f"Last Updated: {date_str} KST")
        
        content = content.replace("1,513.40", exchange_rate)
        
        # LG Energy Solution
        content = content.replace("416,000 <span class=\"text-sm\">KRW</span>", f"{lg_price} <span class=\"text-sm\">KRW</span>")
        # Change direction (up to down)
        content = content.replace(
            '<div class="text-rose-500 text-sm font-semibold">▲ 5,500 (+1.34%)</div>',
            f'<div class="text-blue-400 text-sm font-semibold">{lg_change}</div>'
        )
        content = content.replace("style=\"width: 81.6%\"", "style=\"width: 78.4%\"")
        content = content.replace("상승 여력: +22.60%", "상승 여력: +27.50%")
        
        # Samsung SDI
        content = content.replace("550,000 <span class=\"text-sm\">KRW</span>", f"{sdi_price} <span class=\"text-sm\">KRW</span>")
        # Change direction (up to down)
        content = content.replace(
            '<div class="text-rose-500 text-sm font-semibold">▲ 1,000 (+0.18%)</div>',
            f'<div class="text-blue-400 text-sm font-semibold">{sdi_change}</div>'
        )
        content = content.replace("style=\"width: 76.1%\"", "style=\"width: 72.2%\"")
        content = content.replace("상승 여력: +31.36%", "상승 여력: +38.41%")
        
        with open(battery_path, 'w', encoding='utf-8', newline='') as f:
            f.write(content)
        print("Updated valuation_battery.html")

    # 7. Update valuation_ai.html
    ai_path = os.path.join(base_dir, "valuation_ai.html")
    if os.path.exists(ai_path):
        with open(ai_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        content = content.replace("Updated: 2026-06-18 09:02 KST", f"Updated: {date_hyphen} KST")
        content = content.replace("1,513.40", exchange_rate)
        
        # NVIDIA
        content = content.replace("$208.04", nvda_price)
        content = content.replace(
            '<div class="text-emerald-400 text-sm font-bold">▲ 0.43% <span class="text-slate-500 font-normal ml-1">(상승)</span></div>',
            f'<div class="text-emerald-400 text-sm font-bold">▲ 1.27% <span class="text-slate-500 font-normal ml-1">(상승)</span></div>'
        )
        
        # Microsoft
        content = content.replace(
            f'$378.91 <span class="text-red-400 text-sm font-normal">▼ 3.37%</span>',
            f'{msft_price} <span class="text-emerald-400 text-sm font-normal">▲ 0.13%</span>'
        )
        
        # Alphabet
        content = content.replace(
            f'$363.79 <span class="text-red-400 text-sm font-normal">▼ 2.07%</span>',
            f'{googl_price} <span class="text-emerald-400 text-sm font-normal">▲ 1.14%</span>'
        )
        
        # Action Guide current position
        content = content.replace("현재 위치: $208.04", f"현재 위치: {nvda_price}")
        
        with open(ai_path, 'w', encoding='utf-8', newline='') as f:
            f.write(content)
        print("Updated valuation_ai.html")

    # 8. Update valuation_interactive_demo.html
    demo_path = os.path.join(base_dir, "valuation_interactive_demo.html")
    if os.path.exists(demo_path):
        with open(demo_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        content = content.replace("매크로 변수에 따른 종목별 할인율 및 적정가 리계산 | 2026. 06. 18. 09:02", f"매크로 변수에 따른 종목별 할인율 및 적정가 리계산 | {date_str}")
        content = content.replace("Last Updated: 2026. 06. 18. 09:02 KST", f"Last Updated: {date_str} KST")
        
        content = content.replace("1,513.40", exchange_rate)
        content = content.replace('value="1512"', 'value="1527"')
        
        # HTML displays
        content = content.replace("₩346,500", f"₩{samsung_price}")
        content = content.replace("₩2,521,000", f"₩{hynix_price}")
        content = content.replace("₩416,000", f"₩{lg_price}")
        
        # JS values
        content = content.replace("const samsungCurrent = 346500;", f"const samsungCurrent = {samsung_price.replace(',', '')};")
        content = content.replace("const hynixCurrent = 2521000;", f"const hynixCurrent = {hynix_price.replace(',', '')};")
        content = content.replace("const lgCurrent = 416000;", f"const lgCurrent = {lg_price.replace(',', '')};")
        
        with open(demo_path, 'w', encoding='utf-8', newline='') as f:
            f.write(content)
        print("Updated valuation_interactive_demo.html")

    # 9. Update news.html timestamps
    news_path = os.path.join(base_dir, "news.html")
    if os.path.exists(news_path):
        with open(news_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # Robustly replace whatever datetime tag exists in the header
        content = re.sub(
            r'주요 분야 최신 뉴스 실시간 자동사냥\s*\|\s*[^<]+',
            f'주요 분야 최신 뉴스 실시간 자동사냥 | {date_korean}',
            content
        )
        
        with open(news_path, 'w', encoding='utf-8', newline='') as f:
            f.write(content)
        print("Updated news.html timestamps")

if __name__ == '__main__':
    update_all_files()
