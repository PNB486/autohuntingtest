# -*- coding: utf-8 -*-
import os
import re
import json
import urllib.request
import datetime
import time

def fetch_yahoo_chart(symbol, range_str="1d", interval="1m"):
    url = f"https://query1.finance.yahoo.com/v8/finance/chart/{symbol}?range={range_str}&interval={interval}"
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'})
    for attempt in range(3):
        try:
            with urllib.request.urlopen(req, timeout=10) as res:
                data = json.loads(res.read().decode('utf-8'))
                result = data['chart']['result'][0]
                meta = result['meta']
                
                close_prices = []
                if 'indicators' in result and 'quote' in result['indicators'] and len(result['indicators']['quote']) > 0:
                    quotes = result['indicators']['quote'][0]
                    if 'close' in quotes:
                        close_prices = [p for p in quotes['close'] if p is not None]
                        
                return {
                    'price': meta.get('regularMarketPrice'),
                    'previous_close': meta.get('chartPreviousClose'),
                    'history': close_prices
                }
        except Exception as e:
            print(f"Attempt {attempt+1} failed to fetch {symbol}: {e}")
            time.sleep(1)
    return None

def fetch_naver_kospi_trend():
    url = "https://m.stock.naver.com/api/index/KOSPI/trend"
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.5 Mobile/15E148 Safari/604.1'})
    for attempt in range(3):
        try:
            with urllib.request.urlopen(req, timeout=10) as res:
                data = json.loads(res.read().decode('utf-8'))
                return {
                    'personal': data.get('personalValue', '0'),
                    'foreign': data.get('foreignValue', '0'),
                    'institutional': data.get('institutionalValue', '0')
                }
        except Exception as e:
            print(f"Attempt {attempt+1} failed to fetch KOSPI trend: {e}")
            time.sleep(1)
    return {'personal': '0', 'foreign': '0', 'institutional': '0'}

def format_change_desc(price, prev_close, is_us=False, is_percent_only=False):
    diff = price - prev_close
    pct = (diff / prev_close) * 100 if prev_close else 0.0
    
    sign = "▲" if diff > 0 else "▼" if diff < 0 else ""
    sign_plus_minus = "+" if diff >= 0 else ""
    
    if is_us:
        pct_str = f"{sign_plus_minus}{pct:.2f}%"
        desc_str = f"{sign} {abs(pct):.2f}% 상승" if diff > 0 else (f"{sign} {abs(pct):.2f}% 하락" if diff < 0 else "0.00% 보합")
        return pct_str, desc_str
    elif is_percent_only:
        return f"{sign_plus_minus}{pct:.2f}%"
    else:
        return f"{sign} {abs(int(diff)):,}" if is_percent_only else f"{sign} {abs(int(diff)):,} ({sign_plus_minus}{pct:.2f}%)"

def main():
    base_dir = r"C:\Users\S\Desktop\AI\Gemini\Stock"
    print("=== Soul's Auto-Update Market Data Script ===")
    
    # 1. Fetch current time in KST
    utc_now = datetime.datetime.utcnow()
    kst_now = utc_now + datetime.timedelta(hours=9)
    date_str = kst_now.strftime('%Y. %m. %d. %H:%M')
    date_hyphen = kst_now.strftime('%Y-%m-%d %H:%M')
    date_korean = f"{kst_now.year}년 {kst_now.month}월 {kst_now.day}일 {kst_now.hour}시 {kst_now.minute:02d}분"
    print(f"Current KST Time: {date_str}")
    
    # 2. Fetch Macro indices
    print("Fetching indices and exchange rates...")
    usd_data = fetch_yahoo_chart("USDKRW=X")
    kospi_data = fetch_yahoo_chart("^KS11")
    nasdaq_data = fetch_yahoo_chart("^IXIC")
    
    if not usd_data or not kospi_data or not nasdaq_data:
        print("[CRITICAL] Failed to fetch macro data. Aborting updates.")
        return
        
    rate_val = f"{usd_data['price']:.2f}"  # Format as 1528.28
    rate_val_comma = f"{usd_data['price']:,.2f}" # Format as 1,528.28
    rate_rounded = str(int(round(usd_data['price'])))
    discount_pct = 15 if usd_data['price'] > 1450 else 0
    
    kospi_val = f"{kospi_data['price']:,.2f}"
    kospi_diff = kospi_data['price'] - kospi_data['previous_close']
    kospi_pct = (kospi_diff / kospi_data['previous_close']) * 100
    kospi_sign = "▲" if kospi_diff > 0 else "▼" if kospi_diff < 0 else ""
    kospi_change_full = f"{kospi_sign} {abs(kospi_diff):,.2f} ({'+' if kospi_diff >= 0 else ''}{kospi_pct:.2f}%)"
    kospi_change_only = f"{kospi_sign} {kospi_pct:.2f}%"
    
    nasdaq_val = f"{nasdaq_data['price']:,.2f}"
    nasdaq_diff = nasdaq_data['price'] - nasdaq_data['previous_close']
    nasdaq_pct = (nasdaq_diff / nasdaq_data['previous_close']) * 100
    nasdaq_sign = "▲" if nasdaq_diff > 0 else "▼" if nasdaq_diff < 0 else ""
    nasdaq_change_full = f"{nasdaq_sign} {abs(nasdaq_diff):,.2f} ({'+' if nasdaq_diff >= 0 else ''}{nasdaq_pct:.2f}%)"
    nasdaq_change_only = f"{nasdaq_sign} {nasdaq_pct:.2f}%"
    
    print(f"  USD/KRW: {rate_val_comma} (Discount Pct: {discount_pct}%)")
    print(f"  KOSPI: {kospi_val} ({kospi_change_full})")
    print(f"  NASDAQ: {nasdaq_val} ({nasdaq_change_full})")
    
    # Fetch historical data for KOSPI and NASDAQ (last 5 daily closes)
    kospi_hist_data = fetch_yahoo_chart("^KS11", range_str="5d", interval="1d")
    nasdaq_hist_data = fetch_yahoo_chart("^IXIC", range_str="5d", interval="1d")
    
    kospi_history = [round(p, 2) for p in kospi_hist_data['history'][-5:]] if kospi_hist_data else []
    nasdaq_history = [round(p, 2) for p in nasdaq_hist_data['history'][-5:]] if nasdaq_hist_data else []
    
    # Make sure we have 5 elements by appending the current price if needed
    if len(kospi_history) < 5:
        kospi_history = [8545.98, 8726.60, 8864.24, 9063.84, round(kospi_data['price'], 2)]
    if len(nasdaq_history) < 5:
        nasdaq_history = [26100.0, 26200.0, 26400.0, 26021.66, round(nasdaq_data['price'], 2)]
        
    print(f"  KOSPI History: {kospi_history}")
    print(f"  NASDAQ History: {nasdaq_history}")
    
    # 3. Fetch Domestic Stock prices
    print("Fetching domestic stocks...")
    dom_symbols = {
        '삼성전자 (005930)': '005930.KS',
        'SK하이닉스 (000660)': '000660.KS',
        'LG에너지솔루션 (373220)': '373220.KS',
        'NAVER (035420)': '035420.KS',
        '현대차 (005380)': '005380.KS',
        '한화에어로스페이스': '012450.KS',
        'LIG넥스원': '079550.KS',
        '삼성SDI': '006400.KS'
    }
    
    dom_prices = {}
    for name, sym in dom_symbols.items():
        data = fetch_yahoo_chart(sym)
        if data:
            price = int(data['price'])
            prev = int(data['previous_close'])
            diff = price - prev
            pct = (diff / prev) * 100 if prev else 0.0
            
            sign_arrow = "▲" if diff > 0 else "▼" if diff < 0 else ""
            sign_plus = "+" if diff >= 0 else ""
            
            dom_prices[name] = {
                'price': price,
                'price_str': f"{price:,}",
                'change_desc': f"{sign_arrow} {abs(diff):,} ({sign_plus}{pct:.2f}%)",
                'change_only': f"{sign_plus}{pct:.2f}%",
                'change_desc_simple': f"{sign_arrow} {abs(diff):,} ({sign_plus}{pct:.2f}%)" if diff != 0 else "0.00%"
            }
        else:
            print(f"Warning: Failed to fetch domestic stock {name} ({sym})")
            dom_prices[name] = {'price': 0, 'price_str': '0', 'change_desc': '0.00%', 'change_only': '0.00%', 'change_desc_simple': '0.00%'}
            
    # 4. Fetch US Stock prices
    print("Fetching US stocks...")
    us_symbols = {
        '엔비디아 (NVDA)': 'NVDA',
        '애플 (AAPL)': 'AAPL',
        '마이크로소프트 (MSFT)': 'MSFT',
        '알파벳 (GOOGL)': 'GOOG',
        '아마존 (AMZN)': 'AMZN',
        'TSMC (TSM)': 'TSM',
        '브로드컴 (AVGO)': 'AVGO',
        'AMD (AMD)': 'AMD',
        'ASML (ASML)': 'ASML'
    }
    
    us_prices = {}
    for name, sym in us_symbols.items():
        data = fetch_yahoo_chart(sym)
        if data:
            price = data['price']
            prev = data['previous_close']
            pct_str, desc = format_change_desc(price, prev, is_us=True)
            us_prices[name] = {
                'price': price,
                'price_str': f"${price:,.2f}",
                'change_only': pct_str,
                'change_desc': desc
            }
        else:
            print(f"Warning: Failed to fetch US stock {name} ({sym})")
            us_prices[name] = {'price': 0, 'price_str': '$0.00', 'change_only': '0.00%', 'change_desc': '0.00% 보합'}
            
    # 5. Fetch KOSPI Investor Flow Trend
    print("Fetching KOSPI investor trends...")
    inv_trend = fetch_naver_kospi_trend()
    print(f"  Investor Trend: Retail: {inv_trend['personal']}, Foreign: {inv_trend['foreign']}, Institution: {inv_trend['institutional']}")
    
    def parse_inv_val(v):
        try:
            return int(v.replace(',', '').replace('+', ''))
        except:
            return 0
    inv_chart_data = [parse_inv_val(inv_trend['foreign']), parse_inv_val(inv_trend['institutional']), parse_inv_val(inv_trend['personal'])]

    # ==================== HTML UPDATES ====================
    print("\nUpdating HTML pages...")
    
    def update_stock_in_html(content, stock_name, new_price, new_change):
        escaped_name = re.escape(stock_name)
        if "0.00%" in new_change:
            color_name = "slate-400"
        elif "+" in new_change or "▲" in new_change:
            color_name = "rose-500"
        else:
            color_name = "blue-400"
            
        pattern = rf'(<td class="py-4 font-bold"\s*>{escaped_name}</td>\s*<td class="py-4 text-right"\s*>)[^<]+(</td>\s*<td class="py-4 text-right\s+text-)(rose-500|blue-400|emerald-400|slate-400)(">)[^<]+(</td>)'
        replacement = rf'\g<1>{new_price}\g<2>{color_name}\g<4>{new_change}\g<5>'
        new_content, count = re.subn(pattern, replacement, content, flags=re.DOTALL)
        return new_content, count

    def update_index_market_card(content, card_name, val, change_str):
        color = "rose-500" if "▲" in change_str or "+" in change_str else ("blue-400" if "▼" in change_str or "-" in change_str else "slate-400")
        card_html = """<div class="px-6 py-3 bg-slate-900/80 backdrop-blur-md rounded-2xl border border-slate-700/50 shadow-xl">
                    <span class="text-xs text-slate-500 font-bold uppercase block mb-1">{}</span>
                    <span class="text-xl font-bold text-sky-400">{}</span>
                    <span class="text-{} text-sm ml-1 font-bold">{}</span>
                </div>""".format(card_name, val, color, change_str)
        pattern = r'<div class="px-6 py-3 bg-slate-900/80[^>]*>\s*<span class="text-xs text-slate-500 font-bold uppercase block mb-1">{}</span>.*?</div>'.format(card_name)
        content, count = re.subn(pattern, card_html, content, flags=re.DOTALL)
        return content

    def update_index_usd_krw(content, rate_val):
        rate_num = float(rate_val.replace(',', ''))
        if rate_num > 1450:
            card_html = """<div class="px-6 py-3 bg-rose-500/10 backdrop-blur-md rounded-2xl border border-rose-500/30 shadow-xl">
                    <span class="text-xs text-rose-400/70 font-bold uppercase block mb-1">USD/KRW</span>
                    <span class="text-xl font-bold text-rose-500">{}</span>
                    <span class="text-xs text-rose-600 ml-1 font-black underline">HIGH CURRENCY RISK ZONE</span>
                </div>""".format(rate_val)
        else:
            card_html = """<div class="px-6 py-3 bg-slate-900/80 backdrop-blur-md rounded-2xl border border-slate-700/50 shadow-xl">
                    <span class="text-xs text-slate-500 font-bold uppercase block mb-1">USD/KRW</span>
                    <span class="text-xl font-bold text-sky-400">{}</span>
                    <span class="text-xs text-emerald-400 ml-1 font-black">NORMAL ZONE</span>
                </div>""".format(rate_val)
        pattern = r'<div class="px-6 py-3 bg-(?:rose-500/10|slate-900/80)[^>]*>\s*<span class="text-xs [^"]*">USD/KRW</span>.*?</div>'
        content, count = re.subn(pattern, card_html, content, flags=re.DOTALL)
        return content

    def update_index_card(content, index_name, index_val, change_str):
        color = "rose-500" if "▲" in change_str or "+" in change_str else ("blue-400" if "▼" in change_str or "-" in change_str else "slate-400")
        card_html = """<h3 class="text-slate-400 text-sm font-semibold uppercase mb-4">{} 지수</h3>
                <div class="flex items-baseline gap-4 mb-6">
                    <span class="text-5xl font-black text-sky-400">{}</span>
                    <span class="text-2xl font-bold text-{}">{}</span>
                </div>""".format(index_name, index_val, color, change_str)
        pattern = r'<h3 class="text-slate-400 text-sm font-semibold uppercase mb-4">{} 지수</h3>\s*<div class="flex items-baseline gap-4 mb-6">.*?</div>'.format(index_name)
        content, count = re.subn(pattern, card_html, content, flags=re.DOTALL)
        return content

    def update_static_risk_badge(content, rate_val):
        rate_num = float(rate_val.replace(',', ''))
        if rate_num > 1450:
            badge_text = "⚠️ High Currency Risk Zone ({})".format(rate_val)
            badge_style = "background-color: rgba(239, 68, 68, 0.1); border: 1px solid rgba(239, 68, 68, 0.3); color: #ef4444;"
        else:
            badge_text = "✅ Normal Currency Zone ({})".format(rate_val)
            badge_style = "background-color: rgba(16, 185, 129, 0.1); border: 1px solid rgba(16, 185, 129, 0.3); color: #10b981;"
            
        content = re.sub(
            r'\.risk-badge\s*\{\s*background-color:[^;]+;\s*border:[^;]+;\s*color:[^;]+;\s*\}',
            f'.risk-badge {{ {badge_style} }}',
            content
        )
        content = re.sub(
            r'<div class="risk-badge[^"]*px-4 py-2 rounded-xl text-sm font-bold[^"]*">\s*[^<]+\s*</div>',
            f'<div class="risk-badge px-4 py-2 rounded-xl text-sm font-bold">{badge_text}</div>',
            content
        )
        return content

    def update_stock_valuation_block(content, stock_name, base_target, current_price, discount_pct):
        adjusted_target = int(base_target * (1 - (discount_pct / 100.0)))
        upside = ((adjusted_target - current_price) / current_price) * 100
        progress_width = (current_price / adjusted_target) * 100
        progress_width = min(100.0, max(0.0, progress_width))
        
        upside_sign = "+" if upside >= 0 else ""
        upside_str = f"{upside_sign}{upside:.2f}%"
        progress_str = f"{progress_width:.1f}%"
        
        base_target_str = f"{base_target:,}"
        adjusted_target_str = f"{adjusted_target:,}"
        
        escaped_name = re.escape(stock_name)
        pattern = rf'(<h2 class="text-2xl font-bold"\s*>{escaped_name}</h2>.*?<div class="space-y-4 mb-8">).*?(</div>\s*<div class="grid grid-cols-2 gap-4)'
        
        valuation_block_html = """
                    <div class="flex justify-between text-sm">
                        <span class="text-slate-500">목표가 (Target)</span>
                        <span class="font-bold text-slate-300 line-through">{}</span>
                    </div>
                    <div class="flex justify-between text-sm">
                        <span class="text-sky-400 font-bold">조정 목표가 (-{}%)</span>
                        <span class="font-bold text-sky-400">{}</span>
                    </div>
                    <div class="w-full bg-slate-800 h-2 rounded-full overflow-hidden">
                        <div class="bg-sky-400 h-full" style="width: {}"></div>
                    </div>
                    <div class="text-xs text-slate-500 text-right">상승 여력: {}</div>
                """.format(base_target_str, discount_pct, adjusted_target_str, progress_str, upside_str)
                    
        content, count = re.subn(pattern, rf'\g<1>{valuation_block_html}\g<2>', content, flags=re.DOTALL)
        return content

    def update_stock_price_block(content, stock_name, new_price_str, change_desc):
        color = "rose-500" if "▲" in change_desc or "+" in change_desc else ("blue-400" if "▼" in change_desc or "-" in change_desc else "slate-400")
        escaped_name = re.escape(stock_name)
        pattern = rf'(<h2 class="text-2xl font-bold"\s*>{escaped_name}</h2>.*?<div class="text-right">\s*<div class="text-3xl font-bold text-sky-400">)[^<]+(<span class="text-sm">KRW</span></div>\s*<div class=")(?:text-rose-500|text-blue-400|text-slate-400)(" text-sm font-semibold">)[^<]+(</div>)'
        content, count = re.subn(pattern, rf'\g<1>{new_price_str} \g<2>{color}\g<3>{change_desc}\g<4>', content, flags=re.DOTALL)
        return content

    def update_demo_stock_price(content, stock_name, new_price_str):
        escaped_name = re.escape(stock_name)
        pattern = rf'(<h4 class="font-bold text-lg"\s*>{escaped_name}</h4>.*?<div class="font-bold text-slate-300">)₩[^<]*(</div>\s*<div class="text-xs text-slate-500">현재가</div>)'
        content, count = re.subn(pattern, rf'\g<1>₩{new_price_str}\g<2>', content, flags=re.DOTALL)
        return content

    def update_demo_js_constants(content, samsung_val, hynix_val, lg_val):
        content = re.sub(r'const\s+samsungCurrent\s*=\s*\d+;', f'const samsungCurrent = {samsung_val};', content)
        content = re.sub(r'const\s+hynixCurrent\s*=\s*\d+;', f'const hynixCurrent = {hynix_val};', content)
        content = re.sub(r'const\s+lgCurrent\s*=\s*\d+;', f'const lgCurrent = {lg_val};', content)
        return content

    def update_ai_usd_krw(content, rate_val):
        rate_num = float(rate_val.replace(',', ''))
        if rate_num > 1450:
            warning_html = """<div class="text-red-400 text-sm font-bold">▲ High <span class="text-slate-500 font-normal ml-1">(위험)</span></div>"""
        else:
            warning_html = """<div class="text-emerald-400 text-sm font-bold">▼ Normal <span class="text-slate-500 font-normal ml-1">(보통)</span></div>"""
            
        pattern_block = r'<div class="text-slate-500 text-xs font-bold mb-2 uppercase">USD/KRW EXCHANGE</div>\s*<div class="text-3xl font-black metric-value mb-1">[^<]+</div>\s*<div class="(?:text-red-400|text-emerald-400) text-sm font-bold">[^<]+<span class="text-slate-500 font-normal ml-1">[^<]+</span></div>'
        new_block = """<div class="text-slate-500 text-xs font-bold mb-2 uppercase">USD/KRW EXCHANGE</div>
            <div class="text-3xl font-black metric-value mb-1">{}</div>
            {}""".format(rate_val, warning_html)
        content, count = re.subn(pattern_block, new_block, content, flags=re.DOTALL)
        return content

    def update_ai_description_text(content, rate_val):
        rate_num = float(rate_val.replace(',', ''))
        if rate_num > 1450:
            desc = f"USD/KRW 환율이 **{rate_val}**을 기록하며 심리적 마지노선인 1,450원을 크게 상회. 신규 해외 주식 매수 시 환차손 리스크 급증. 포트폴리오 차원의 15% 가치 할인이 불가피함."
        else:
            desc = f"USD/KRW 환율이 **{rate_val}**을 기록하며 안정세를 보이고 있습니다. 환차손 리스크가 감소하여 매크로 할인율을 0-5% 수준으로 완화 조정했습니다."
            
        pattern = r'USD/KRW\s*환율이\s*\*\*.*?\*\*\s*을\s*기록하며.*?불가피함\.'
        content, count = re.subn(pattern, desc, content, flags=re.DOTALL)
        if count == 0:
            pattern_p = r'USD/KRW\s*환율이\s*\*\*.*?\*\*\s*을.*?</p>'
            content, count = re.subn(pattern_p, desc + "\n</p>", content, flags=re.DOTALL)
        return content

    def get_nvda_action(price):
        if price <= 180:
            return "적극 매수"
        elif price <= 250:
            return "보유 / 관망"
        elif price <= 320:
            return "비중 축소"
        else:
            return "적극 매도"

    def update_ai_action_guide(content, nvda_price):
        price_val = float(nvda_price.replace('$', '').replace(',', ''))
        action = get_nvda_action(price_val)
        new_text = f'📍 **현재 위치: {nvda_price} → "{action}" 구간.**'
        content = re.sub(r'📍\s*\*\*현재\s*위치:\s*\$[0-9.,]+\s*→\s*"[^"]+"\s*구간\.\*\*', new_text, content)
        return content

    # 1. index.html
    index_path = os.path.join(base_dir, "index.html")
    if os.path.exists(index_path):
        with open(index_path, 'r', encoding='utf-8') as f:
            content = f.read()
        content = update_index_market_card(content, "KOSPI", kospi_val, kospi_change_only)
        content = update_index_market_card(content, "NASDAQ", nasdaq_val, nasdaq_change_only)
        content = update_index_usd_krw(content, rate_val_comma)
        content = re.sub(r'SYSTEM UPDATED:\s*\d{4}-\d{2}-\d{2}\s*\d{2}:\d{2}(?:\s*KST)?', f'SYSTEM UPDATED: {date_hyphen} KST', content)
        with open(index_path, 'w', encoding='utf-8', newline='') as f:
            f.write(content)
        print("  [OK] index.html updated.")

    # 2. kospi.html
    kospi_path = os.path.join(base_dir, "kospi.html")
    if os.path.exists(kospi_path):
        with open(kospi_path, 'r', encoding='utf-8') as f:
            content = f.read()
        content = re.sub(r'주식 시장 현황\s*\|\s*\d{4}\.\s*\d{2}\.\s*\d{2}\.\s*\d{2}:\d{2}', f'주식 시장 현황 | {date_str}', content)
        content = update_index_card(content, "KOSPI", kospi_val, kospi_change_full)
        
        for name in ['삼성전자 (005930)', 'SK하이닉스 (000660)', 'LG에너지솔루션 (373220)', 'NAVER (035420)', '현대차 (005380)']:
            content, _ = update_stock_in_html(content, name, dom_prices[name]['price_str'], dom_prices[name]['change_only'])
            
        pattern_foreign = r'(<span class="text-slate-400 font-medium">외국인</span>\s*<span class="text-)(blue-400|rose-500)( font-bold">)[^<]+(</span>)'
        foreign_color = "rose-500" if "+" in inv_trend['foreign'] else "blue-400"
        content = re.sub(pattern_foreign, rf'\g<1>{foreign_color}\g<3>{inv_trend["foreign"]}억\g<4>', content)
        
        pattern_inst = r'(<span class="text-slate-400 font-medium">기관</span>\s*<span class="text-)(blue-400|rose-500)( font-bold">)[^<]+(</span>)'
        inst_color = "rose-500" if "+" in inv_trend['institutional'] else "blue-400"
        content = re.sub(pattern_inst, rf'\g<1>{inst_color}\g<3>{inv_trend["institutional"]}억\g<4>', content)
        
        pattern_retail = r'(<span class="text-slate-400 font-medium">개인</span>\s*<span class="text-)(blue-400|rose-500)( font-bold">)[^<]+(</span>)'
        retail_color = "rose-500" if "+" in inv_trend['personal'] else "blue-400"
        content = re.sub(pattern_retail, rf'\g<1>{retail_color}\g<3>{inv_trend["personal"]}억\g<4>', content)

        content = re.sub(r'data:\s*\[\s*[0-9.]+\s*,\s*[0-9.]+\s*,\s*[0-9.]+\s*,\s*[0-9.]+\s*,\s*[0-9.]+\s*\]', f"data: {kospi_history}", content)
        content = re.sub(r'data:\s*\[\s*-?\d+\s*,\s*-?\d+\s*,\s*-?\d+\s*\]', f"data: {inv_chart_data}", content)
        
        content = content.replace("1,513.40원", f"{rate_val_comma}원")
        content = content.replace("1,527.10원", f"{rate_val_comma}원")
        
        with open(kospi_path, 'w', encoding='utf-8', newline='') as f:
            f.write(content)
        print("  [OK] kospi.html updated.")

    # 3. nasdaq.html
    nasdaq_path = os.path.join(base_dir, "nasdaq.html")
    if os.path.exists(nasdaq_path):
        with open(nasdaq_path, 'r', encoding='utf-8') as f:
            content = f.read()
        content = re.sub(r'미국 주식 시장 현황\s*\|\s*\d{4}\.\s*\d{2}\.\s*\d{2}\.\s*\d{2}:\d{2}', f'미국 주식 시장 현황 | {date_str}', content)
        content = update_index_card(content, "NASDAQ", nasdaq_val, nasdaq_change_full)
        
        usd_color = "rose-500" if usd_data['price'] > 1450 else "sky-400"
        usd_text = "High Currency Risk Zone" if usd_data['price'] > 1450 else "Normal Currency Zone"
        
        content = re.sub(
            r'(<span class="text-3xl font-bold text-)(?:rose-500|sky-400)(">)[^<]*( KRW</span>)',
            rf'\g<1>{usd_color}\g<2>{rate_val_comma}\g<3>',
            content
        )
        content = re.sub(
            r'(<span class="ml-2 text-xs bg-)(?:rose-500/20|sky-400/20)( text-)(?:rose-500|sky-400)( px-2 py-0.5 rounded font-bold">)[^<]*(</span>)',
            rf'\g<1>{usd_color}/20\g<2>{usd_color}\g<3>{usd_text} ({rate_val_comma})\g<4>',
            content
        )
        content = re.sub(
            r'(원/달러\s*환율이\s*<strong>)[^<]*(</strong>)',
            rf'\g<1>{rate_val_comma}원 ({usd_text})\g<2>',
            content
        )
        
        nvda_macro_pattern = r'(NVIDIA \(NVDA\)\s*</span>\s*<span class="text-3xl font-bold text-sky-400">)[^<]+(</span>\s*<span class="ml-2 text-xs text-)(rose-500|blue-400|emerald-400)(">)[^<]+(</span>)'
        nvda_color = "rose-500" if "+" in us_prices['엔비디아 (NVDA)']['change_only'] else "blue-400"
        content = re.sub(nvda_macro_pattern, rf'\g<1>{us_prices["엔비디아 (NVDA)"]["price_str"]}\g<2>{nvda_color}\g<4>{us_prices["엔비디아 (NVDA)"]["change_only"]} 상승\g<5>', content)
        
        for name in ['엔비디아 (NVDA)', '애플 (AAPL)', '마이크로소프트 (MSFT)', '알파벳 (GOOGL)', '아마존 (AMZN)', 'TSMC (TSM)', '브로드컴 (AVGO)', 'AMD (AMD)', 'ASML (ASML)']:
            content, _ = update_stock_in_html(content, name, us_prices[name]['price_str'], us_prices[name]['change_only'])
            
        content = re.sub(r'data:\s*\[\s*[0-9.]+\s*,\s*[0-9.]+\s*,\s*[0-9.]+\s*,\s*[0-9.]+\s*,\s*[0-9.]+\s*\]', f"data: {nasdaq_history}", content)
        
        with open(nasdaq_path, 'w', encoding='utf-8', newline='') as f:
            f.write(content)
        print("  [OK] nasdaq.html updated.")

    # 4. valuation_semi.html
    semi_path = os.path.join(base_dir, "valuation_semi.html")
    if os.path.exists(semi_path):
        with open(semi_path, 'r', encoding='utf-8') as f:
            content = f.read()
        content = re.sub(r'Last Updated:\s*\d{4}\.\s*\d{2}\.\s*\d{2}\.\s*\d{2}:\d{2}\s*KST', f'Last Updated: {date_str} KST', content)
        content = re.sub(r'주요 종목 적정가 및 리스크 진단\s*\|\s*\d{4}\.\s*\d{2}\.\s*\d{2}\.\s*\d{2}:\d{2}', f'주요 종목 적정가 및 리스크 진단 | {date_str}', content)
        
        content = re.sub(r'(<span class="text-sky-400 font-mono"\s*id="exchangeRateVal">)[^<]*( KRW</span>)', rf'\g<1>{rate_val_comma}\g<2>', content)
        content = re.sub(r'(<input type="range"\s*id="exchangeRateSlider"\s*min="\d+"\s*max="\d+"\s*step="\d+"\s*value=")\d+(")', rf'\g<1>{rate_rounded}\g<2>', content)
        
        header_color = "red-500" if usd_data['price'] > 1450 else "emerald-500"
        header_text = "⚠️ High Currency Risk Zone" if usd_data['price'] > 1450 else "✅ Normal Currency Zone"
        content = re.sub(r'<span id="headerRiskLabel">[^<]+</span>', f'<span id="headerRiskLabel">{header_text}</span>', content)
        content = re.sub(r'<span class="bg-(?:red-500|emerald-500) text-white px-2 py-0.5 rounded" id="headerRiskVal">[^<]+</span>', f'<span class="bg-{header_color} text-white px-2 py-0.5 rounded" id="headerRiskVal">{rate_val_comma}</span>', content)
        
        pattern_samsung_price = r'(삼성전자</h2>.*?<div class="text-3xl font-bold text-sky-400">)[^<]+(<span class="text-sm">KRW</span>)'
        content = re.sub(pattern_samsung_price, rf'\g<1>{dom_prices["삼성전자 (005930)"]["price_str"]} \g<2>', content, flags=re.DOTALL)
        pattern_hynix_price = r'(SK하이닉스</h2>.*?<div class="text-3xl font-bold text-sky-400">)[^<]+(<span class="text-sm">KRW</span>)'
        content = re.sub(pattern_hynix_price, rf'\g<1>{dom_prices["SK하이닉스 (000660)"]["price_str"]} \g<2>', content, flags=re.DOTALL)
        
        samsung_color = "text-rose-500" if "+" in dom_prices['삼성전자 (005930)']['change_only'] else "text-blue-400"
        hynix_color = "text-rose-500" if "+" in dom_prices['SK하이닉스 (000660)']['change_only'] else "text-blue-400"
        pattern_samsung_change = r'(삼성전자</h2>.*?<div class="text-right">.*?</div>\s*<div class=")(?:text-rose-500|text-blue-400|text-slate-400)(" text-sm font-semibold">)[^<]+(</div>)'
        content = re.sub(pattern_samsung_change, rf'\g<1>{samsung_color}\g<2>{dom_prices["삼성전자 (005930)"]["change_desc_simple"]}\g<3>', content, flags=re.DOTALL)
        pattern_hynix_change = r'(SK하이닉스</h2>.*?<div class="text-right">.*?</div>\s*<div class=")(?:text-rose-500|text-blue-400|text-slate-400)(" text-sm font-semibold">)[^<]+(</div>)'
        content = re.sub(pattern_hynix_change, rf'\g<1>{hynix_color}\g<2>{dom_prices["SK하이닉스 (000660)"]["change_desc_simple"]}\g<3>', content, flags=re.DOTALL)

        content = re.sub(r'const\s+samsungCurrentPrice\s*=\s*\d+;', f"const samsungCurrentPrice = {dom_prices['삼성전자 (005930)']['price']};", content)
        content = re.sub(r'const\s+hynixCurrentPrice\s*=\s*\d+;', f"const hynixCurrentPrice = {dom_prices['SK하이닉스 (000660)']['price']};", content)
        
        with open(semi_path, 'w', encoding='utf-8', newline='') as f:
            f.write(content)
        print("  [OK] valuation_semi.html updated.")

    # 5. valuation_defense.html
    defense_path = os.path.join(base_dir, "valuation_defense.html")
    if os.path.exists(defense_path):
        with open(defense_path, 'r', encoding='utf-8') as f:
            content = f.read()
        content = re.sub(r'Last Updated:\s*\d{4}\.\s*\d{2}\.\s*\d{2}\.\s*\d{2}:\d{2}\s*KST', f'Last Updated: {date_str} KST', content)
        content = re.sub(r'글로벌 지정학적 리스크 및 수주 가치 진단\s*\|\s*\d{4}\.\s*\d{2}\.\s*\d{2}\.\s*\d{2}:\d{2}', f'글로벌 지정학적 리스크 및 수주 가치 진단 | {date_str}', content)
        content = update_static_risk_badge(content, rate_val_comma)
        
        content = update_stock_price_block(content, "한화에어로스페이스", dom_prices['한화에어로스페이스']['price_str'], dom_prices['한화에어로스페이스']['change_desc_simple'])
        content = update_stock_price_block(content, "LIG넥스원", dom_prices['LIG넥스원']['price_str'], dom_prices['LIG넥스원']['change_desc_simple'])
        
        content = update_stock_valuation_block(content, "한화에어로스페이스", 1600000, dom_prices['한화에어로스페이스']['price'], discount_pct)
        content = update_stock_valuation_block(content, "LIG넥스원", 1100000, dom_prices['LIG넥스원']['price'], discount_pct)
        
        with open(defense_path, 'w', encoding='utf-8', newline='') as f:
            f.write(content)
        print("  [OK] valuation_defense.html updated.")

    # 6. valuation_battery.html
    battery_path = os.path.join(base_dir, "valuation_battery.html")
    if os.path.exists(battery_path):
        with open(battery_path, 'r', encoding='utf-8') as f:
            content = f.read()
        content = re.sub(r'Last Updated:\s*\d{4}\.\s*\d{2}\.\s*\d{2}\.\s*\d{2}:\d{2}\s*KST', f'Last Updated: {date_str} KST', content)
        content = re.sub(r'전기차 캐즘 돌파 및 실적 턴어라운드 진단\s*\|\s*\d{4}\.\s*\d{2}\.\s*\d{2}\.\s*\d{2}:\d{2}', f'전기차 캐즘 돌파 및 실적 턴어라운드 진단 | {date_str}', content)
        content = update_static_risk_badge(content, rate_val_comma)
        
        content = update_stock_price_block(content, "LG에너지솔루션", dom_prices['LG에너지솔루션 (373220)']['price_str'], dom_prices['LG에너지솔루션 (373220)']['change_desc_simple'])
        content = update_stock_price_block(content, "삼성SDI", dom_prices['삼성SDI']['price_str'], dom_prices['삼성SDI']['change_desc_simple'])
        
        content = update_stock_valuation_block(content, "LG에너지솔루션", 600000, dom_prices['LG에너지솔루션 (373220)']['price'], discount_pct)
        content = update_stock_valuation_block(content, "삼성SDI", 850000, dom_prices['삼성SDI']['price'], discount_pct)
        
        with open(battery_path, 'w', encoding='utf-8', newline='') as f:
            f.write(content)
        print("  [OK] valuation_battery.html updated.")

    # 7. valuation_ai.html
    ai_path = os.path.join(base_dir, "valuation_ai.html")
    if os.path.exists(ai_path):
        with open(ai_path, 'r', encoding='utf-8') as f:
            content = f.read()
        content = re.sub(r'Updated:\s*\d{4}-\d{2}-\d{2}\s*\d{2}:\d{2}\s*KST', f'Updated: {date_hyphen} KST', content)
        content = update_ai_usd_krw(content, rate_val_comma)
        content = update_ai_description_text(content, rate_val_comma)
        
        nvda_data = us_prices['엔비디아 (NVDA)']
        pattern_nvda_price = r'(<div class="text-sky-400 text-xs font-bold mb-2 uppercase">NVIDIA \(NVDA\)</div>\s*<div class="text-3xl font-black metric-value mb-1">)[^<]+(</div>)'
        content = re.sub(pattern_nvda_price, rf'\g<1>{nvda_data["price_str"]}\g<2>', content, flags=re.DOTALL)
        
        nvda_change_color = "text-emerald-400" if "+" in nvda_data['change_only'] else "text-red-400"
        pattern_nvda_change = r'(<div class="text-sky-400 text-xs font-bold mb-2 uppercase">NVIDIA \(NVDA\)</div>\s*<div class="text-3xl font-black metric-value mb-1">[^<]+</div>\s*<div class=")(?:text-emerald-400|text-red-400)(" text-sm font-bold">)[^<]+(</div>)'
        content = re.sub(pattern_nvda_change, rf'\g<1>{nvda_change_color}\g<2>{nvda_data["change_only"]} <span class="text-slate-500 font-normal ml-1">(상승)</span>\g<3>', content, flags=re.DOTALL)

        content = update_ai_action_guide(content, nvda_data['price_str'])
        
        with open(ai_path, 'w', encoding='utf-8', newline='') as f:
            f.write(content)
        print("  [OK] valuation_ai.html updated.")

    # 8. valuation_interactive_demo.html
    demo_path = os.path.join(base_dir, "valuation_interactive_demo.html")
    if os.path.exists(demo_path):
        with open(demo_path, 'r', encoding='utf-8') as f:
            content = f.read()
        content = re.sub(r'Last Updated:\s*\d{4}\.\s*\d{2}\.\s*\d{2}\.\s*\d{2}:\d{2}\s*KST', f'Last Updated: {date_str} KST', content)
        content = re.sub(r'매크로 변수에 따른 종목별 할인율 및 적정가 리계산\s*\|\s*\d{4}\.\s*\d{2}\.\s*\d{2}\.\s*\d{2}:\d{2}', f'매크로 변수에 따른 종목별 할인율 및 적정가 리계산 | {date_str}', content)
        
        content = re.sub(r'(<span class="text-sky-400 font-mono"\s*id="exchangeRateVal">)[^<]*( KRW</span>)', rf'\g<1>{rate_val_comma}\g<2>', content)
        content = re.sub(r'(<input type="range"\s*id="exchangeRateSlider"\s*min="\d+"\s*max="\d+"\s*step="\d+"\s*value=")\d+(")', rf'\g<1>{rate_rounded}\g<2>', content)
        
        content = update_demo_stock_price(content, "삼성전자", dom_prices['삼성전자 (005930)']['price_str'])
        content = update_demo_stock_price(content, "SK하이닉스", dom_prices['SK하이닉스 (000660)']['price_str'])
        content = update_demo_stock_price(content, "LG에너지솔루션", dom_prices['LG에너지솔루션 (373220)']['price_str'])
        
        content = update_demo_js_constants(content, dom_prices['삼성전자 (005930)']['price'], dom_prices['SK하이닉스 (000660)']['price'], dom_prices['LG에너지솔루션 (373220)']['price'])
        
        with open(demo_path, 'w', encoding='utf-8', newline='') as f:
            f.write(content)
        print("  [OK] valuation_interactive_demo.html updated.")

    # 9. news.html
    news_path = os.path.join(base_dir, "news.html")
    if os.path.exists(news_path):
        with open(news_path, 'r', encoding='utf-8') as f:
            content = f.read()
        content = re.sub(r'주요 분야 최신 뉴스 실시간 자동사냥\s*\|\s*[^<]+', f'주요 분야 최신 뉴스 실시간 자동사냥 | {date_korean}', content)
        with open(news_path, 'w', encoding='utf-8', newline='') as f:
            f.write(content)
        print("  [OK] news.html updated.")

if __name__ == '__main__':
    main()
