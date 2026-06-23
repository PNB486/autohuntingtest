# Soul Insight Portal (Auto Hunting Project) Rules

## 1. 정규식 패턴 및 슬라이더 업데이트 규칙 (중요)
- HTML 파일의 환율(`exchangeRateSlider`), 지정학적 리스크(`geoRiskSlider`) 등의 범위 슬라이더 값을 교체할 때 **탐욕적 정규식(greedy regex)** 사용을 절대 금지합니다.
- **오류 예시**: `re.sub(r'value="[0-9]+"', f'value="{rate_rounded}"', content)` 와 같이 교체하면 문서 전체의 모든 슬라이더 `value` 속성들이 동일하게 변경되어 치명적인 버그가 발생합니다.
- **해결책**: 항상 태그의 ID 및 고유 특성(예: `id="exchangeRateSlider"`)을 구체적으로 식별하는 타겟 정규식을 사용하여 업데이트 하십시오.
  - 예시: `re.sub(r'(<input type="range"\s*id="exchangeRateSlider"\s*min="\d+"\s*max="\d+"\s*step="\d+"\s*value=")\d+(")', ...)`

## 2. 환율 레이블 단위 중복 방지 규칙
- 환율 레이블 값을 치환할 때 캡처 그룹 매칭 범위에 단위(`KRW`)가 포함되어 있는지 정확하게 식별해야 합니다.
- 캡처 그룹 치환 시 단위가 중복 생성되어 `1,530.38 KRW KRW` 와 같이 표기되지 않도록 정합성을 유지해야 합니다.
  - 예시: `re.sub(r'(<span class="text-sky-400 font-mono"\s*id="exchangeRateVal">)[^<]*( KRW</span>)', rf'\g<1>{rate_val_comma}\g<2>', content)` (여기서 `\g<2>`에 공백과 `KRW` 단위가 이미 포함되어 있으므로 치환문에 `KRW`를 중복해서 삽입하지 않음)

## 3. 리포트 인코딩 및 검증 무결성 규칙
- 모든 HTML 리포트와 스크립트는 **UTF-8 (No BOM)** 규격으로 저장되어야 합니다.
- 코드 또는 데이터를 수정한 후에는 **반드시** `chcp 65001` 환경에서 `python scripts/revalidate_portal.py`를 실행하여 인코딩 오류(모지바케), Chart.js 반응형 컨테이너 구조 및 CDN 일관성 등을 자가 검증해야 합니다.

## 4. Git 단일 커밋 및 강제 동기화 (Force Push)
- 로컬 변경사항을 Git에 업로드할 때에는 단일 커밋 이력을 관리하기 위해 반드시 아래 명령어로 원격 저장소에 반영하고 커밋 해시 정렬을 교차 검증해야 합니다.
  ```powershell
  git add .
  git commit --amend -m "Auto Hunt Portal Update"
  git push origin main --force
  ```
  
## 5. 국내 금융 데이터 수집처 규칙 (Naver Finance API 사용 필수)
- 코스피(KOSPI) 지수, 투자자별 수급 동향, 국내 개별 종목(삼성전자, SK하이닉스, LG에너지솔루션, NAVER, 현대차, 한화에어로스페이스, LIG넥스원, 삼성SDI 등)의 가격 데이터 수집 시, Yahoo Finance API 대신 **네이버 금융 모바일 API**를 사용해야 합니다.
- **Naver API 엔드포인트**:
  - 실시간 지수/종가: `https://m.stock.naver.com/api/index/{지수명}/basic` (KOSPI 등)
  - 실시간 종목 시세: `https://m.stock.naver.com/api/stock/{종목코드}/basic`
  - 역사적 가격 추이: `https://m.stock.naver.com/api/index/{지수명}/price?pageSize={개수}&page=1`
- 국내 장 운영 시간(09:00 ~ 15:30 KST) 중 Yahoo Finance의 국내 주가 데이터는 지연 또는 전날 종가 고정 오류가 발생하므로 실시간성 유지를 위해 네이버 금융 모바일 API 조회가 필수적입니다.

## 6. KOSPI 지수 이원화 차트 구현 규칙 (당일 시간별 & 5일 요일별)
- `kospi.html`의 KOSPI 차트는 사용자가 **당일 (시간별)**과 **5일 (요일별)** 뷰를 탭으로 전환할 수 있는 이원화 구조를 유지해야 합니다.
  - **당일 (시간별)**: 당일 네이버 금융 API에서 추출한 `시가(Open)`, `장중 최저가(Low)`, `장중 최고가(High)`, `현재가(Current)`를 결합해 `[open, low, high, price]` 형태의 실시간 4포인트 차트로 구성합니다.
  - **5일 (요일별)**: 네이버 금융 역사적 API에서 가져온 최근 5거래일의 종가와 실제 요일 이름(예: `['Thu', 'Fri', 'Mon', 'Tue', 'Wed']`)을 결합하여 구성합니다.
- `scripts/auto_update_market_data.py`는 `kospi.html` 내부의 `intradayData`, `dailyLabels`, `dailyData` JS 변수 그룹을 정규식을 사용해 안전하게 업데이트해야 합니다.
- **지수 카드 텍스트 업데이트 규칙 (중요)**: `kospi.html` 및 `nasdaq.html` 등 대시보드 지수 카드의 지수 및 등락률 텍스트를 업데이트하는 `update_index_card` 함수는 탭 전환 버튼 유무 등 카드 헤더 구조가 파일마다 다를 수 있으므로, 헤더 `<h3>` 태그부터 실제 수치가 노출되는 `span` 태그까지 유연하게 매칭할 수 있는 정규식 패턴(예: `.*?` 와 `re.escape`)을 사용하여 업데이트해야 하며 업데이트 성공 여부를 항상 검증해야 합니다.
