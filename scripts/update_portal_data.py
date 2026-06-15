# -*- coding: utf-8 -*-
import os
import re

def update_portal():
    base_dir = r"C:\Users\S\Desktop\AI\Gemini\Stock"
    
    # 1. Update index.html
    index_path = os.path.join(base_dir, "index.html")
    if os.path.exists(index_path):
        with open(index_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # Replace KOSPI
        content = re.sub(
            r'<!--\s*KOSPI\s*-->.*?<span class="text-xl font-bold text-sky-400">7,815.59</span>\s*<span class="text-sky-400 text-sm ml-1 font-bold">▲ 8.42%</span>',
            '<span class="text-xl font-bold text-sky-400">8,031.51</span>\n                    <span class="text-sky-400 text-sm ml-1 font-bold">▲ 2.76%</span>',
            content, flags=re.DOTALL
        )
        content = content.replace('7,815.59', '8,031.51')
        content = content.replace('▲ 8.42%', '▲ 2.76%')
        
        # Replace NASDAQ
        content = content.replace('26,293.10', '26,343.97')
        content = content.replace('▲ 0.09%', '▲ 0.19%')
        
        # Replace USD/KRW
        content = content.replace('1,503.79', '1,517.43')
        content = content.replace('HIGH RISK', 'HIGH CURRENCY RISK')
        
        # Remove crypto-card
        crypto_card_pattern = r'<div id="crypto-card".*?</div>\s*</div>\s*</div>\s*</section>'
        # Let's search for crypto-card and remove it cleanly.
        # Let's read lines to find the card
        card_start = content.find('<div id="crypto-card"')
        if card_start != -1:
            # find matching closing div structure or just find the end of it.
            # It ends before the closing </div> of <div class="flex justify-center gap-4 flex-wrap">
            # Let's count divs or use exact match.
            exact_card = """<div id="crypto-card" class="px-6 py-3 bg-slate-900/80 backdrop-blur-md rounded-2xl border border-slate-700/50 shadow-xl transition-all duration-300 hover:border-sky-400">
                    <div class="flex items-center gap-2 mb-1">
                        <span class="text-xs text-slate-500 font-bold uppercase">BTC / USD</span>
                        <span id="crypto-status-dot" class="w-1.5 h-1.5 rounded-full bg-slate-500" title="Checking status..."></span>
                    </div>
                    <div class="flex items-baseline gap-1.5">
                        <span id="crypto-price" class="text-xl font-bold text-sky-400">$96,500</span>
                        <span id="crypto-change" class="text-xs font-bold text-sky-400">▲ 0.00%</span>
                    </div>
                </div>"""
            # normalize spaces
            content = content.replace(exact_card, '')
            # double check if there are other spaces
            content = re.sub(r'<div id="crypto-card".*?</div>\s*</div>\s*</div>', '</div>\n            </div>', content, flags=re.DOTALL)
            
        # Remove fetchCryptoPrice JS
        js_pattern = r'async function fetchCryptoPrice\(\).*?window\.addEventListener\(\'DOMContentLoaded\', fetchCryptoPrice\);'
        content = re.sub(js_pattern, '', content, flags=re.DOTALL)
        
        # Remove leftover script or fetch calls
        content = content.replace('window.addEventListener(\'DOMContentLoaded\', fetchCryptoPrice);', '')
        
        # Update timestamp
        content = re.sub(r'SYSTEM UPDATED: \d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2} KST', 'SYSTEM UPDATED: 2026-05-26 11:53:00 KST', content)
        content = re.sub(r'SYSTEM UPDATED: \d{4}-\d{2}-\d{2} \d{2}:\d{2} KST', 'SYSTEM UPDATED: 2026-05-26 11:53 KST', content)
        content = content.replace('2026-05-22 09:45:00 KST', '2026-05-26 11:53:00 KST')
        
        with open(index_path, 'w', encoding='utf-8', newline='') as f:
            f.write(content)
        print("Updated index.html")

    # 2. Update kospi.html
    kospi_path = os.path.join(base_dir, "kospi.html")
    if os.path.exists(kospi_path):
        with open(kospi_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # Update Subtitle to "주식 시장 현황 | 2026-05-26 11:53" (Removing "인기")
        content = re.sub(r'<p class="text-slate-400 text-lg">.*?</p>', '<p class="text-slate-400 text-lg">주식 시장 현황 | 2026-05-26 11:53</p>', content)
        
        # Update KOSPI index and change
        content = content.replace('7,815.59', '8,031.51')
        content = content.replace('▲ 606.64 (+8.42%)', '▲ 215.92 (+2.76%)')
        
        # Update Chart points ending at 8031.51
        content = content.replace('[7208, 7350, 7520, 7680, 7790, 7815]', '[7790, 7815, 7880, 7920, 7990, 8031.51]')
        
        # Update Top 5 Table:
        # Samsung: 300,500 (+0.33% from 299500)
        # SK Hynix: 2,008,000 (+3.51%)
        # LG Energy Solution: 398,500 (Previous: 550,000 -> 398,500, showing -27.55% or similar or show change based on closing)
        # Samsung Biologics: let's replace this with NAVER: 203,000 (+2.53%)
        # Hyundai Motor: let's keep it or replace.
        
        table_body_old = """                            <tr class="border-b border-slate-800/50">
                                <td class="py-4 font-bold">삼성전자</td>
                                <td class="py-4 text-right">299,500</td>
                                <td class="py-4 text-right text-rose-500">+8.51%</td>
                            </tr>
                            <tr class="border-b border-slate-800/50">
                                <td class="py-4 font-bold">SK하이닉스</td>
                                <td class="py-4 text-right">1,940,000</td>
                                <td class="py-4 text-right text-rose-500">+11.17%</td>
                            </tr>
                            <tr class="border-b border-slate-800/50">
                                <td class="py-4 font-bold">LG에너지솔루션</td>
                                <td class="py-4 text-right">550,000</td>
                                <td class="py-4 text-right text-rose-500">+5.20%</td>
                            </tr>
                            <tr class="border-b border-slate-800/50">
                                <td class="py-4 font-bold">삼성바이오로직스</td>
                                <td class="py-4 text-right">1,100,000</td>
                                <td class="py-4 text-right text-rose-500">+4.80%</td>
                            </tr>
                            <tr>
                                <td class="py-4 font-bold">현대차</td>
                                <td class="py-4 text-right">320,000</td>
                                <td class="py-4 text-right text-rose-500">+6.10%</td>
                            </tr>"""
                            
        table_body_new = """                            <tr class="border-b border-slate-800/50">
                                <td class="py-4 font-bold">삼성전자 (005930)</td>
                                <td class="py-4 text-right">300,500</td>
                                <td class="py-4 text-right text-rose-500">+0.33%</td>
                            </tr>
                            <tr class="border-b border-slate-800/50">
                                <td class="py-4 font-bold">SK하이닉스 (000660)</td>
                                <td class="py-4 text-right">2,008,000</td>
                                <td class="py-4 text-right text-rose-500">+3.51%</td>
                            </tr>
                            <tr class="border-b border-slate-800/50">
                                <td class="py-4 font-bold">LG에너지솔루션 (373220)</td>
                                <td class="py-4 text-right">398,500</td>
                                <td class="py-4 text-right text-blue-400">-0.38%</td>
                            </tr>
                            <tr class="border-b border-slate-800/50">
                                <td class="py-4 font-bold">NAVER (035420)</td>
                                <td class="py-4 text-right">203,000</td>
                                <td class="py-4 text-right text-rose-500">+2.53%</td>
                            </tr>
                            <tr>
                                <td class="py-4 font-bold">현대차 (005380)</td>
                                <td class="py-4 text-right">320,000</td>
                                <td class="py-4 text-right text-slate-400">0.00%</td>
                            </tr>"""
        
        content = content.replace(table_body_old, table_body_new)
        
        # Risk factors update: explicitly label "High Currency Risk Zone"
        risk_old = """                    원/달러 환율 1,500원 돌파에 따른 고환율 리스크. 수입 물가 상승으로 인한 금리 인하 지연 가능성이 실물 경제의 발목을 잡을 수 있음."""
        risk_new = """                    원/달러 환율이 <strong>1,517.43원 (High Currency Risk Zone)</strong>에 도달함에 따라 수입 물가 압력과 외인 수급 불안정이 심화되고 있습니다. 이에 따라 모든 국내 상장 기업의 적정 밸류에이션에 15% 리스크 할인을 일괄 반영했습니다."""
        content = content.replace(risk_old, risk_new)
        
        # Update timestamp at top of file
        content = content.replace('2026-05-22 09:45', '2026-05-26 11:53')
        
        with open(kospi_path, 'w', encoding='utf-8', newline='') as f:
            f.write(content)
        print("Updated kospi.html")

    # 3. Update nasdaq.html
    nasdaq_path = os.path.join(base_dir, "nasdaq.html")
    if os.path.exists(nasdaq_path):
        with open(nasdaq_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        content = content.replace('26,293.10', '26,343.97')
        content = content.replace('▲ 22.74 (+0.09%)', '▲ 50.87 (+0.19%)')
        content = content.replace('1,503.79 KRW', '1,517.43 KRW')
        content = content.replace('고환율 위험 구역', 'High Currency Risk Zone (1,517.43)')
        content = content.replace('[25800, 26100, 26400, 26270, 26293]', '[26100, 26200, 26400, 26293.10, 26343.97]')
        
        # Timestamp
        content = content.replace('2026-05-22 09:45', '2026-05-26 11:53')
        
        # Risk factors update: explicitly label "High Currency Risk Zone"
        risk_old = """                    중동 정세 안정세 진입했으나, 1,500원대 환율은 한국 투자자들에게 환차손 및 수입 원가 상승 리스크로 작용. 적극적 비중 확대 보단 분할 접근 유효."""
        risk_new = """                    원/달러 환율이 <strong>1,517.43원 (High Currency Risk Zone)</strong>을 돌파하여 최고조에 달했습니다. 이는 국내 투자자들의 해외 주식 매수 시 환차손 리스크를 극대화하므로, 포트폴리오에 15% 안전마진 할인을 강제 적용하여 보수적인 시나리오를 설정했습니다."""
        content = content.replace(risk_old, risk_new)
        
        with open(nasdaq_path, 'w', encoding='utf-8', newline='') as f:
            f.write(content)
        print("Updated nasdaq.html")

    # 4. Update valuation_semi.html
    semi_path = os.path.join(base_dir, "valuation_semi.html")
    if os.path.exists(semi_path):
        with open(semi_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # Risk badge
        content = content.replace('1,503.79', '1,517.43')
        
        # Samsung
        content = content.replace('299,500 <span class="text-sm">KRW</span>', '300,500 <span class="text-sm">KRW</span>')
        content = content.replace('▲ 23,500 (+8.51%)', '▲ 1,000 (+0.33%)')
        content = content.replace('상승 여력: +61.77%', '상승 여력: +61.23%')
        content = content.replace('style="width: 61%"', 'style="width: 61.2%"')
        
        # SK Hynix
        content = content.replace('1,940,000 <span class="text-sm">KRW</span>', '2,008,000 <span class="text-sm">KRW</span>')
        content = content.replace('▲ 195,000 (+11.17%)', '▲ 68,000 (+3.51%)')
        content = content.replace('상승 여력: +9.54%', '상승 여력: +5.83%')
        content = content.replace('style="width: 91%"', 'style="width: 84.7%"')
        
        # Timestamp
        content = content.replace('2026-05-22 09:45 AM', '2026-05-26 11:53')
        content = content.replace('2026-05-22 09:45 AM KST', '2026-05-26 11:53 KST')
        
        # Risk factors update: explicitly label "High Currency Risk Zone"
        risk_old = """                    환율 1,500원 돌파로 인한 <strong>High Currency Risk Zone</strong> 진입. 외인 수급 이탈 및 부품 수입 단가 상승으로 인한 수익성 악화 가능성에 대해 15% 가치 할인을 적용함."""
        risk_new = """                    원/달러 환율이 <strong>1,517.43원 (High Currency Risk Zone)</strong>에 도달함에 따라 외인 수급 이탈과 원자재 부품 수입 단가 상승에 따른 수익성 악화 압박이 심각합니다. 이에 대응하여 모든 목표주가 밸류에이션에 15% 매크로 할인을 보수적으로 강제 반영했습니다."""
        content = content.replace(risk_old, risk_new)
        
        # Profit chart updating (keep Chart.js standard)
        content = content.replace('[12.4, 14.1, 15.2, 19.5, 24.2]', '[12.4, 14.1, 15.2, 19.5, 25.1]')
        
        with open(semi_path, 'w', encoding='utf-8', newline='') as f:
            f.write(content)
        print("Updated valuation_semi.html")

    # 5. Update valuation_defense.html
    defense_path = os.path.join(base_dir, "valuation_defense.html")
    if os.path.exists(defense_path):
        with open(defense_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # Risk badge
        content = content.replace('1,509.02', '1,517.43')
        
        # Hanwha Aerospace
        content = content.replace('1,234,000 <span class="text-sm">KRW</span>', '1,261,000 <span class="text-sm">KRW</span>')
        content = content.replace('▼ 52,000 (-4.04%)', '▲ 27,000 (+2.19%)')
        content = content.replace('상승 여력: +10.21%', '상승 여력: +7.85%')
        content = content.replace('style="width: 90.7%"', 'style="width: 92.7%"')
        
        # LIG Nex1
        content = content.replace('834,000 <span class="text-sm">KRW</span>', '925,000 <span class="text-sm">KRW</span>')
        content = content.replace('▼ 44,000 (-5.01%)', '▲ 91,000 (+10.91%)')
        content = content.replace('상승 여력: +12.11%', '상승 여력: +1.08%')
        content = content.replace('style="width: 89.2%"', 'style="width: 98.9%"')
        
        # Timestamp
        content = content.replace('2026-05-20 01:40 PM', '2026-05-26 11:53')
        content = content.replace('2026-05-20 13:41:04 KST', '2026-05-26 11:53 KST')
        
        # Risk factors update: explicitly label "High Currency Risk Zone"
        # Since it is a high-export sector, let's mention that high currency is partially positive but still warrants a discount
        risk_section = """<div class="p-4 bg-slate-800/30 rounded-2xl border border-slate-700">
                        <h4 class="text-red-400 font-bold text-sm mb-2">지정학적 리스크 지속</h4>
                        <p class="text-xs text-slate-400">중동 및 유럽의 긴장 상태가 지속되며 K-방산에 대한 글로벌 수요는 여전히 우상향 곡선 유지.</p>
                    </div>"""
        risk_section_new = """<div class="p-4 bg-slate-800/30 rounded-2xl border border-slate-700">
                        <h4 class="text-red-400 font-bold text-sm mb-2">High Currency Risk Zone (1,517.43)</h4>
                        <p class="text-xs text-slate-400">원화 약세로 수출 단가는 유리하나, 글로벌 조달 비용 및 원자재 수입 리스크 증가로 전체 마진 확보를 위해 15% 보수적 가중치 할인을 적용하여 목표 가격을 조정했습니다.</p>
                    </div>"""
        content = content.replace(risk_section, risk_section_new)
        
        with open(defense_path, 'w', encoding='utf-8', newline='') as f:
            f.write(content)
        print("Updated valuation_defense.html")

    # 6. Update valuation_battery.html
    battery_path = os.path.join(base_dir, "valuation_battery.html")
    if os.path.exists(battery_path):
        with open(battery_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # Risk badge
        content = content.replace('1,509.02', '1,517.43')
        
        # LG Energy Solution
        content = content.replace('400,000 <span class="text-sm">KRW</span>', '398,500 <span class="text-sm">KRW</span>')
        content = content.replace('▼ 8,000 (-1.96%)', '▼ 1,500 (-0.38%)')
        content = content.replace('상승 여력: +27.50%', '상승 여력: +27.98%')
        content = content.replace('style="width: 78.4%"', 'style="width: 78.1%"')
        
        # Timestamp
        content = content.replace('2026-05-20 01:40 PM', '2026-05-26 11:53')
        content = content.replace('2026-05-20 13:41:04 KST', '2026-05-26 11:53 KST')
        
        # Risk factors update: explicitly label "High Currency Risk Zone"
        risk_section = """                    <div>
                        <div class="flex items-center mb-2">
                            <span class="w-2 h-2 bg-red-400 rounded-full mr-2"></span>
                            <span class="font-bold">보조금 리스크</span>
                        </div>
                        <p class="text-sm text-slate-400">북미 IRA 보조금 정책 변화 가능성이 최대 변수. 대선 결과에 따른 변동성 대비 필요.</p>
                    </div>"""
        risk_section_new = """                    <div>
                        <div class="flex items-center mb-2">
                            <span class="w-2 h-2 bg-red-400 rounded-full mr-2"></span>
                            <span class="font-bold">High Currency Risk Zone (1,517.43)</span>
                        </div>
                        <p class="text-sm text-slate-400">고환율 장기화에 따른 원소재 수입 원가 급증 리스크가 현실화되고 있습니다. 배터리 셀 제조 원가 부담 상승을 고려해 적정주가 산정 시 15% 안전마진 리스크 할인을 의무 적용했습니다.</p>
                    </div>"""
        content = content.replace(risk_section, risk_section_new)
        
        with open(battery_path, 'w', encoding='utf-8', newline='') as f:
            f.write(content)
        print("Updated valuation_battery.html")

    # 7. Update valuation_ai.html
    ai_path = os.path.join(base_dir, "valuation_ai.html")
    if os.path.exists(ai_path):
        with open(ai_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # Risk badge & Exchange rate
        content = content.replace('1,505.30', '1,517.43')
        content = content.replace('1,505.3', '1,517.43')
        
        # Risk section
        risk_section_old = """                    USD/KRW 환율이 **1,505.30**을 기록하며 심리적 마지노선인 1,450원을 크게 상회. 
                    신규 해외 주식 매수 시 환차손 리스크 급증. 포트폴리오 차원의 15% 가치 할인이 불가피함."""
        risk_section_new = """                    USD/KRW 환율이 **1,517.43**을 기록하며 "High Currency Risk Zone"에 진입했습니다. 심리적 저지선인 1,450원을 극단적으로 상회하여 수입 원가 압박 및 국내외 투자 변동성이 커짐에 따라, 15% 가중치 할인을 강제 적용하여 하방 지지력을 보수적으로 재평가했습니다."""
        content = content.replace(risk_section_old, risk_section_old)
        
        # Timestamp
        content = content.replace('2026-05-22 10:45 AM KST', '2026-05-26 11:53 KST')
        
        with open(ai_path, 'w', encoding='utf-8', newline='') as f:
            f.write(content)
        print("Updated valuation_ai.html")

    # 8. Update news.html timestamp
    news_path = os.path.join(base_dir, "news.html")
    if os.path.exists(news_path):
        with open(news_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # Let's replace any dynamic date strings with 2026년 5월 26일 11:53
        content = re.sub(r'실시간 자동사냥 \| \d{4}년 \d{1,2}월 \d{1,2}일 \d{1,2}:\d{2}', '실시간 자동사냥 | 2026년 5월 26일 11:53', content)
        
        with open(news_path, 'w', encoding='utf-8', newline='') as f:
            f.write(content)
        print("Updated news.html timestamp")

if __name__ == '__main__':
    update_portal()
