# -*- coding: utf-8 -*-
import os
import re

def update_all_files():
    base_dir = r"C:\Users\S\Desktop\AI\Gemini\Stock"
    print("Starting KOSPI/NASDAQ/Valuations update for June 18, 2026 (09:02)...")

    # Data constants
    date_str = "2026. 06. 18. 09:02"
    date_hyphen = "2026-06-18 09:02"
    date_korean = "2026년 6월 18일 9시 02분"
    
    kospi_val = "8,864.24"
    kospi_change = "▲ 137.64 (+1.58%)"
    kospi_change_only = "+1.58%"
    
    nasdaq_val = "26,021.66"
    nasdaq_change = "▼ 354.68 (-1.34%)"
    nasdaq_change_only = "-1.34%"
    
    exchange_rate = "1,513.40"

    # Stock values (June 17 Close)
    samsung_price = "346,500"
    samsung_change = "▲ 3,500 (+1.02%)"
    samsung_change_only = "+1.02%"
    
    hynix_price = "2,521,000"
    hynix_change = "▲ 139,000 (+5.84%)"
    hynix_change_only = "+5.84%"
    
    lg_price = "416,000"
    lg_change = "▲ 5,500 (+1.34%)"
    lg_change_only = "+1.34%"
    
    naver_price = "243,500"
    naver_change_str = "▲ 1,500 (+0.62%)"
    naver_change_only = "+0.62%"
    
    hyundai_price = "618,000"
    hyundai_change = "▼ 22,000 (-3.44%)"
    hyundai_change_only = "-3.44%"
    
    hanwha_price = "1,224,000"
    hanwha_change = "▲ 41,000 (+3.47%)"
    hanwha_change_only = "+3.47%"
    
    lig_price = "950,000"
    lig_change = "▼ 52,000 (-5.19%)"
    lig_change_only = "-5.19%"
    
    sdi_price = "550,000"
    sdi_change = "▲ 1,000 (+0.18%)"
    sdi_change_only = "+0.18%"

    # US Stocks
    nvda_price = "$208.04"
    nvda_change = "+0.43%"
    aapl_price = "$295.95"
    aapl_change = "-1.14%"
    msft_price = "$378.91"
    msft_change = "-3.37%"
    googl_price = "$363.79"
    googl_change = "-2.07%"
    amzn_price = "$239.50"
    amzn_change = "+0.34%"
    
    tsmc_price = "$438.54"
    tsmc_change = "+2.98%"
    amd_price = "$523.69"
    amd_change = "+3.23%"
    asml_price = "$1,867.83"
    asml_change = "+3.54%"
    broadcom_price = "$392.89"
    broadcom_change = "+0.35%"

    # Helper function to replace stock info in table rows
    def update_stock_in_html(content, stock_name, new_price, new_change):
        escaped_name = re.escape(stock_name)
        color_name = "rose-500" if ("+" in new_change or "▲" in new_change) else "blue-400"
        
        # Matches:
        # <td class="py-4 font-bold">삼성전자 (005930)</td>
        # <td class="py-4 text-right">343,000</td>
        # <td class="py-4 text-right text-rose-500">+1.78%</td>
        # Allowing optional $ sign in price, different class spacing, and any current values
        pattern = rf'(<td class="py-4 font-bold"\s*>{escaped_name}</td>\s*<td class="py-4 text-right"\s*>)[^<]+(</td>\s*<td class="py-4 text-right\s+text-)(rose-500|blue-400|emerald-400)(">)[^<]+(</td>)'
        
        replacement = rf'\g<1>{new_price}\g<2>{color_name}\g<4>{new_change}\g<5>'
        
        new_content, count = re.subn(pattern, replacement, content, flags=re.DOTALL)
        return new_content, count

    # 1. Update index.html
    index_path = os.path.join(base_dir, "index.html")
    if os.path.exists(index_path):
        with open(index_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # Update KOSPI
        content = content.replace("8,726.60", kospi_val)
        content = content.replace("▲ 2.11%", "▲ 1.58%")
        
        # Update NASDAQ
        content = content.replace("26,376.34", nasdaq_val)
        content = content.replace("▼ 1.15%", "▼ 1.34%")
        
        # Update USD/KRW
        content = content.replace("1,511.60", exchange_rate)
        
        # Update Timestamps
        content = content.replace("SYSTEM UPDATED: 2026-06-17 09:00 KST", f"SYSTEM UPDATED: {date_hyphen} KST")
        
        with open(index_path, 'w', encoding='utf-8', newline='') as f:
            f.write(content)
        print("Updated index.html")

    # 2. Update kospi.html
    kospi_path = os.path.join(base_dir, "kospi.html")
    if os.path.exists(kospi_path):
        with open(kospi_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # Update Title Date
        content = content.replace("주식 시장 현황 | 2026. 06. 17. 09:00", f"주식 시장 현황 | {date_str}")
        
        # Update Index
        content = content.replace("8,726.60", kospi_val)
        content = content.replace("▲ 180.62 (+2.11%)", kospi_change)
        
        # Update stocks in table
        content, c1 = update_stock_in_html(content, "삼성전자 (005930)", samsung_price, samsung_change_only)
        content, c2 = update_stock_in_html(content, "SK하이닉스 (000660)", hynix_price, hynix_change_only)
        content, c3 = update_stock_in_html(content, "LG에너지솔루션 (373220)", lg_price, lg_change_only)
        content, c4 = update_stock_in_html(content, "NAVER (035420)", naver_price, naver_change_only)
        content, c5 = update_stock_in_html(content, "현대차 (005380)", hyundai_price, hyundai_change_only)
        print(f"Updated KOSPI stock rows: {c1}, {c2}, {c3}, {c4}, {c5}")
        
        # Su-geub indicators:
        # 개인: +5,254억 (rose-500)
        # 외국인: -9,945억 (blue-400)
        # 기관: +5,956억 (rose-500)
        # Let's target the exact blocks:
        # 외국인
        content = content.replace(
            '<span class="text-slate-400 font-medium">외국인</span>\n                            <span class="text-rose-500 font-bold">+15,300억</span>',
            '<span class="text-slate-400 font-medium">외국인</span>\n                            <span class="text-blue-400 font-bold">-9,945억</span>'
        )
        content = content.replace(
            '<span class="text-slate-400 font-medium">기관</span>\n                            <span class="text-blue-400 font-bold">+7,042억</span>',
            '<span class="text-slate-400 font-medium">기관</span>\n                            <span class="text-rose-500 font-bold">+5,956억</span>'
        )
        content = content.replace(
            '<span class="text-slate-400 font-medium">개인</span>\n                            <span class="text-rose-500 font-bold">-21,800억</span>',
            '<span class="text-slate-400 font-medium">개인</span>\n                            <span class="text-rose-500 font-bold">+5,254억</span>'
        )

        # Let's support CRLF as well just in case
        content = content.replace(
            '<span class="text-slate-400 font-medium">외국인</span>\r\n                            <span class="text-rose-500 font-bold">+15,300억</span>',
            '<span class="text-slate-400 font-medium">외국인</span>\r\n                            <span class="text-blue-400 font-bold">-9,945억</span>'
        )
        content = content.replace(
            '<span class="text-slate-400 font-medium">기관</span>\r\n                            <span class="text-blue-400 font-bold">+7,042억</span>',
            '<span class="text-slate-400 font-medium">기관</span>\r\n                            <span class="text-rose-500 font-bold">+5,956억</span>'
        )
        content = content.replace(
            '<span class="text-slate-400 font-medium">개인</span>\r\n                            <span class="text-rose-500 font-bold">-21,800억</span>',
            '<span class="text-slate-400 font-medium">개인</span>\r\n                            <span class="text-rose-500 font-bold">+5,254억</span>'
        )
        
        # Charts dataset
        content = content.replace("data: [8390, 8470, 8530, 8545.98, 8726.60]", f"data: [8390, 8470, 8530, 8545.98, {kospi_val.replace(',', '')}]")
        content = content.replace("data: [15300, 7042, -21800]", "data: [-9945, 5956, 5254]")
        
        # Risk factors
        content = content.replace("1,511.60원", f"{exchange_rate}원")
        
        with open(kospi_path, 'w', encoding='utf-8', newline='') as f:
            f.write(content)
        print("Updated kospi.html")

    # 3. Update nasdaq.html
    nasdaq_path = os.path.join(base_dir, "nasdaq.html")
    if os.path.exists(nasdaq_path):
        with open(nasdaq_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        content = content.replace("미국 주식 시장 현황 | 2026. 06. 17. 09:00", f"미국 주식 시장 현황 | {date_str}")
        content = content.replace("26,376.34", nasdaq_val)
        content = content.replace("▼ 307.60 (-1.15%)", nasdaq_change)
        content = content.replace("text-rose-500\">▼ 307.60 (-1.15%)", f"text-blue-400\">{nasdaq_change}")
        content = content.replace("text-rose-500\">\n                    ▼ 307.60 (-1.15%)", f"text-blue-400\">\n                    {nasdaq_change}")
        
        content = content.replace("1,511.60 KRW", f"{exchange_rate} KRW")
        content = content.replace("High Currency Risk Zone (1,511.60)", f"High Currency Risk Zone ({exchange_rate})")
        
        # Nvidia block in Currency/Macro Card
        content = content.replace("$207.15", nvda_price)
        content = content.replace("▼ 2.23% 하락", "▲ 0.43% 상승")
        content = content.replace("text-rose-500\">▼ 2.23% 하락", "text-rose-500\">▲ 0.43% 상승")
        content = content.replace("text-blue-400\">▼ 2.23% 하락", "text-rose-500\">▲ 0.43% 상승")
        
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
        content = content.replace("data: [25500, 25650, 25888.84, 26200, 26376.34]", f"data: [25500, 25650, 25888.84, 26200, {nasdaq_val.replace(',', '')}]")
        
        # Risk factors
        content = content.replace("1,511.60원", f"{exchange_rate}원")
        
        with open(nasdaq_path, 'w', encoding='utf-8', newline='') as f:
            f.write(content)
        print("Updated nasdaq.html")

    # 4. Update valuation_semi.html
    semi_path = os.path.join(base_dir, "valuation_semi.html")
    if os.path.exists(semi_path):
        with open(semi_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        content = content.replace("주요 종목 적정가 및 리스크 진단 | 2026. 06. 17. 09:00", f"주요 종목 적정가 및 리스크 진단 | {date_str}")
        content = content.replace("Last Updated: 2026. 06. 17. 09:00 KST", f"Last Updated: {date_str} KST")
        
        content = content.replace("1,511.60", exchange_rate)
        
        # Samsung Electronics
        content = content.replace("343,000 <span class=\"text-sm\">KRW</span>", f"{samsung_price} <span class=\"text-sm\">KRW</span>")
        content = content.replace("▲ 6,000 (+1.78%)", samsung_change)
        
        # SK Hynix
        content = content.replace("2,382,000 <span class=\"text-sm\">KRW</span>", f"{hynix_price} <span class=\"text-sm\">KRW</span>")
        content = content.replace("▲ 94,000 (+4.11%)", hynix_change)
        
        # JS constants
        content = content.replace("const samsungCurrentPrice = 343000;", f"const samsungCurrentPrice = {samsung_price.replace(',', '')};")
        content = content.replace("const hynixCurrentPrice = 2382000;", f"const hynixCurrentPrice = {hynix_price.replace(',', '')};")
        
        with open(semi_path, 'w', encoding='utf-8', newline='') as f:
            f.write(content)
        print("Updated valuation_semi.html")

    # 5. Update valuation_defense.html
    defense_path = os.path.join(base_dir, "valuation_defense.html")
    if os.path.exists(defense_path):
        with open(defense_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        content = content.replace("글로벌 지정학적 리스크 및 수주 가치 진단 | 2026. 06. 17. 09:00", f"글로벌 지정학적 리스크 및 수주 가치 진단 | {date_str}")
        content = content.replace("Last Updated: 2026. 06. 17. 09:00 KST", f"Last Updated: {date_str} KST")
        
        content = content.replace("1,511.60", exchange_rate)
        
        # Hanwha Aerospace
        content = content.replace("1,183,000 <span class=\"text-sm\">KRW</span>", f"{hanwha_price} <span class=\"text-sm\">KRW</span>")
        content = content.replace("▲ 99,000 (+9.13%)", hanwha_change)
        content = content.replace("style=\"width: 87.0%\"", "style=\"width: 90.0%\"")
        content = content.replace("상승 여력: +14.96%", "상승 여력: +11.11%")
        
        # LIG Nex1
        content = content.replace("1,002,000 <span class=\"text-sm\">KRW</span>", f"{lig_price} <span class=\"text-sm\">KRW</span>")
        content = content.replace("text-rose-500 text-sm font-semibold\">▲ 157,000 (+18.58%)", f"text-blue-400 text-sm font-semibold\">{lig_change}")
        content = content.replace("상승 여력: -6.69%", "상승 여력: -1.58%")
        
        with open(defense_path, 'w', encoding='utf-8', newline='') as f:
            f.write(content)
        print("Updated valuation_defense.html")

    # 6. Update valuation_battery.html
    battery_path = os.path.join(base_dir, "valuation_battery.html")
    if os.path.exists(battery_path):
        with open(battery_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        content = content.replace("전기차 캐즘 돌파 및 실적 턴어라운드 진단 | 2026. 06. 17. 09:00", f"전기차 캐즘 돌파 및 실적 턴어라운드 진단 | {date_str}")
        content = content.replace("Last Updated: 2026. 06. 17. 09:00 KST", f"Last Updated: {date_str} KST")
        
        content = content.replace("1,511.60", exchange_rate)
        
        # LG Energy Solution
        content = content.replace("410,500 <span class=\"text-sm\">KRW</span>", f"{lg_price} <span class=\"text-sm\">KRW</span>")
        content = content.replace("text-blue-400 text-sm font-semibold\">▼ 10,000 (-2.38%)", f"text-rose-500 text-sm font-semibold\">{lg_change}")
        content = content.replace("style=\"width: 80.5%\"", "style=\"width: 81.6%\"")
        content = content.replace("상승 여력: +24.24%", "상승 여력: +22.60%")
        
        # Samsung SDI
        content = content.replace("549,000 <span class=\"text-sm\">KRW</span>", f"{sdi_price} <span class=\"text-sm\">KRW</span>")
        content = content.replace("text-blue-400 text-sm font-semibold\">▼ 9,000 (-1.61%)", f"text-rose-500 text-sm font-semibold\">{sdi_change}")
        content = content.replace("style=\"width: 76.0%\"", "style=\"width: 76.1%\"")
        content = content.replace("상승 여력: +31.60%", "상승 여력: +31.36%")
        
        with open(battery_path, 'w', encoding='utf-8', newline='') as f:
            f.write(content)
        print("Updated valuation_battery.html")

    # 7. Update valuation_ai.html
    ai_path = os.path.join(base_dir, "valuation_ai.html")
    if os.path.exists(ai_path):
        with open(ai_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        content = content.replace("Updated: 2026-06-17 09:00 KST", f"Updated: {date_hyphen} KST")
        content = content.replace("고환율 리스크 존 (1,511.60)", f"고환율 리스크 존 ({exchange_rate})")
        content = content.replace("1,511.60", exchange_rate)
        content = content.replace("환율 1,511.60원", f"환율 {exchange_rate}원")
        content = content.replace("USD/KRW 환율이 **1,511.60**", f"USD/KRW 환율이 **{exchange_rate}**")
        
        # NVIDIA
        content = content.replace("$207.15", nvda_price)
        content = content.replace("text-red-400 text-sm font-bold\">▼ 2.23% <span class=\"text-slate-500 font-normal ml-1\">(하락)</span></div>",
                                  f"text-emerald-400 text-sm font-bold\">▲ 0.43% <span class=\"text-slate-500 font-normal ml-1\">(상승)</span></div>")
        
        # Microsoft
        content = content.replace("$390.74 <span class=\"text-emerald-400 text-sm font-normal\">▲ 1.02%</span>",
                                  f"{msft_price} <span class=\"text-red-400 text-sm font-normal\">▼ 3.37%</span>")
        
        # Alphabet
        content = content.replace("$359.68 <span class=\"text-emerald-400 text-sm font-normal\">▲ 3.12%</span>",
                                  f"{googl_price} <span class=\"text-red-400 text-sm font-normal\">▼ 2.07%</span>")
        
        # Action Guide current position
        content = content.replace("현재 위치: $205.19", f"현재 위치: {nvda_price}")
        
        with open(ai_path, 'w', encoding='utf-8', newline='') as f:
            f.write(content)
        print("Updated valuation_ai.html")

    # 8. Update valuation_interactive_demo.html
    demo_path = os.path.join(base_dir, "valuation_interactive_demo.html")
    if os.path.exists(demo_path):
        with open(demo_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        content = content.replace("매크로 변수에 따른 종목별 할인율 및 적정가 리계산 | 2026. 06. 17. 09:00", f"매크로 변수에 따른 종목별 할인율 및 적정가 리계산 | {date_str}")
        content = content.replace("Last Updated: 2026. 06. 17. 09:00 KST", f"Last Updated: {date_str} KST")
        
        content = content.replace("1,511.60", exchange_rate)
        
        # HTML displays
        content = content.replace("₩343,000", f"₩{samsung_price}")
        content = content.replace("₩2,382,000", f"₩{hynix_price}")
        content = content.replace("₩410,500", f"₩{lg_price}")
        
        # JS values
        content = content.replace("const samsungCurrent = 343000;", f"const samsungCurrent = {samsung_price.replace(',', '')};")
        content = content.replace("const hynixCurrent = 2382000;", f"const hynixCurrent = {hynix_price.replace(',', '')};")
        content = content.replace("const lgCurrent = 410500;", f"const lgCurrent = {lg_price.replace(',', '')};")
        
        with open(demo_path, 'w', encoding='utf-8', newline='') as f:
            f.write(content)
        print("Updated valuation_interactive_demo.html")

    # 9. Update news.html timestamps
    news_path = os.path.join(base_dir, "news.html")
    if os.path.exists(news_path):
        with open(news_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        content = re.sub(
            r'최신 뉴스 실시간 자동사냥\s*\|\s*\d+년 \d+월 \d+일 \d+(?::\d+|시 \d+분)',
            f'최신 뉴스 실시간 자동사냥 | {date_korean}',
            content
        )
        
        with open(news_path, 'w', encoding='utf-8', newline='') as f:
            f.write(content)
        print("Updated news.html timestamps")

if __name__ == '__main__':
    update_all_files()
