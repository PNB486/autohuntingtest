import os

def fix_encoding(file_path):
    try:
        # Read the file with various encodings to find the right one
        with open(file_path, 'rb') as f:
            content = f.read()
        
        # Try decoding as UTF-8
        try:
            text = content.decode('utf-8')
        except UnicodeDecodeError:
            # If UTF-8 fails, try cp949 (Korean Windows)
            text = content.decode('cp949')
        
        # Write back as UTF-8 No BOM
        with open(file_path, 'w', encoding='utf-8', newline='') as f:
            f.write(text)
        print(f"Fixed encoding for {file_path}")
    except Exception as e:
        print(f"Failed to fix {file_path}: {e}")

html_files = [f for f in os.listdir('.') if f.endswith('.html')]
for file in html_files:
    fix_encoding(file)
