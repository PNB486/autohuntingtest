import subprocess
import re
import os
import webbrowser
import sys

def generate_report():
    print("시장 데이터를 분석 중입니다. (약 10~30초 소요)")
    
    try:
        # Windows 환경에서 subprocess 실행 시 인코딩 문제 방지를 위해 shell=True 추가
        result = subprocess.run(
            ['gemini', '-q', '오늘 코스피 시장 분석해서 HTML 코드만 출력해줘. market-analyst 스킬을 반드시 사용해.'],
            capture_output=True,
            text=True,
            encoding='utf-8',
            shell=True
        )
        
        if result.returncode != 0:
            print(f"오류가 발생했습니다: {result.stderr}")
            return
            
        output = result.stdout
        
        # ```html ... ``` 블록 추출
        match = re.search(r'```html\n(.*?)\n```', output, re.DOTALL | re.IGNORECASE)
        if not match:
            # html 태그가 없는 코드 블록도 시도
            match = re.search(r'```\n(.*?)\n```', output, re.DOTALL)
            
        html_content = match.group(1) if match else output
        
        # HTML 코드가 제대로 들어왔는지 기본 검증
        if "<html" not in html_content.lower():
            print("HTML 형식의 응답을 받지 못했습니다. 아래는 원본 응답입니다:")
            print(output[:500] + "...")
            return
            
        file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'Latest_Market_Report.html')
        
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(html_content)
            
        print(f"리포트 생성이 완료되었습니다: {file_path}")
        
        # 웹 브라우저에서 자동 실행
        webbrowser.open('file://' + os.path.realpath(file_path))
        
    except Exception as e:
        print(f"스크립트 실행 중 예외가 발생했습니다: {e}")

if __name__ == "__main__":
    generate_report()
