import os

def fix_encoding(file_path):
    try:
        # Try reading as UTF-8
        with open(file_path, 'rb') as f:
            content = f.read()
        
        # Try to decode as EUC-KR if it fails UTF-8 or contains garbled text
        try:
            decoded_content = content.decode('utf-8')
            # Check if it looks like garbled text (heuristic: high density of weird chars)
            if '??' in decoded_content and ('삼성' not in decoded_content and '주식' not in decoded_content):
                 # Might be mis-decoded
                 pass
        except UnicodeDecodeError:
            try:
                decoded_content = content.decode('euc-kr')
            except UnicodeDecodeError:
                # Fallback to latin-1 or similar if needed, but let's stick to these for now
                return

        # Write back as UTF-8 (No BOM)
        with open(file_path, 'w', encoding='utf-8', newline='') as f:
            f.write(decoded_content)
        print(f"Fixed encoding for: {file_path}")
    except Exception as e:
        print(f"Failed to fix {file_path}: {e}")

directory = r'C:\Users\S\Desktop\AI\Gemini\Stock'
for filename in os.listdir(directory):
    if filename.endswith('.html'):
        fix_encoding(os.path.join(directory, filename))
