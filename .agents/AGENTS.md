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
