import os
import sys

# Common mojibake patterns to detect (UTF-8 bytes read as CP949)
MOJIBAKE_PATTERNS = [
    "?먮룞?щ깷", # 자동사냥
    "?ы꽭",     # 포털
    "諛섎룄泥?",   # 반도체
    "援?궡利앹떆", # 국내증시
    "?댁쇅利앹떆", # 해외증시
    "諛⑹궛",     # 방산
    "?댁감?꾩?",   # 이차전지
    "?뺣쭩",     # 탐욕
    "留ㅻℓ",     # 매매
    "二쇱슂",     # 주요
    "理쒖떊",     # 최신
    "?ㅼ떆媛?",   # 실시간
    "遺꾩빞",     # 분야
]

def validate_file(file_path):
    print(f"Validating {file_path}...")
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # 1. Check for meta charset="UTF-8"
        if '<meta charset="UTF-8">' not in content.upper() and '<meta charset="UTF-8">' not in content:
             # Some might use <meta charset="utf-8">
             if 'CHARSET="UTF-8"' not in content.upper():
                print(f"  [ERROR] Missing meta charset tag in {file_path}")
                return False
        
        # 2. Check for mojibake patterns
        for pattern in MOJIBAKE_PATTERNS:
            if pattern in content:
                print(f"  [ERROR] Mojibake detected in {file_path}: Found '{pattern}'")
                return False
        
        # 3. Check for mandatory background color
        if '#020617' not in content:
            print(f"  [ERROR] Mandatory background color (#020617) not found in {file_path}")
            return False

        # 4. Check for gradient shorthand issue (Should use background-image for .hero-gradient)
        if '.hero-gradient' in content and 'background:' in content and 'radial-gradient' in content:
            # This is a simple check; a more robust one would use regex or a parser
            if 'background-image:' not in content and 'background:' in content:
                 print(f"  [WARNING] .hero-gradient might be using 'background' shorthand instead of 'background-image' in {file_path}")
                 # Only error if we are sure it's the wrong usage
                 if 'background: radial-gradient' in content:
                    print(f"  [ERROR] .hero-gradient uses 'background' shorthand which resets background-color. Use 'background-image' instead.")
                    return False
        
        print(f"  [OK] {file_path} is valid.")
        return True
    except Exception as e:
        print(f"  [ERROR] Failed to read {file_path}: {e}")
        return False

def main():
    directory = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    html_files = [f for f in os.listdir(directory) if f.endswith('.html')]
    
    if not html_files:
        print("No HTML files found to validate.")
        return
    
    all_valid = True
    for file in html_files:
        if not validate_file(os.path.join(directory, file)):
            all_valid = False
            
    if all_valid:
        print("\nAll HTML files passed validation.")
        sys.exit(0)
    else:
        print("\nValidation failed! Please fix encoding issues.")
        sys.exit(1)

if __name__ == "__main__":
    main()
