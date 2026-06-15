# -*- coding: utf-8 -*-
import os
import re
import sys
import subprocess

def main():
    base_dir = r"C:\Users\S\Desktop\AI\Gemini\Stock"
    
    # 1. Fetch news
    print("\n--- Step 1: Fetching News via Node.js ---")
    try:
        # Run node fetch_news.cjs
        news_script = os.path.join(base_dir, "scripts", "fetch_news.cjs")
        print(f"Running: node {news_script}")
        subprocess.run(["node", news_script], check=True)
        print("[OK] News fetched and news.html generated successfully.")
    except Exception as e:
        print(f"[ERROR] Failed to fetch news: {e}")
        sys.exit(1)
        
    # 2. Update portal data to 20260615
    print("\n--- Step 2: Updating Portal Data (Indices, Prices, Valuations) ---")
    try:
        update_script = os.path.join(base_dir, "scripts", "update_portal_data_20260615.py")
        print(f"Running: python {update_script}")
        subprocess.run(["python", update_script], check=True)
        print("[OK] Portal data updated successfully.")
    except Exception as e:
        print(f"[ERROR] Failed to update portal data: {e}")
        sys.exit(1)
        
    # 3. Synchronize timestamps to the exact execution time
    now_str = "2026-06-15 12:00"
    now_dot_str = "2026. 06. 15. 12:00"
    now_korean_str = "2026년 6월 15일 12:00"
    
    print(f"\n--- Step 3: Syncing all HTML Timestamps to {now_str} (UTF-8 No BOM) ---")
    html_files = [f for f in os.listdir(base_dir) if f.endswith('.html')]
    for file_name in html_files:
        file_path = os.path.join(base_dir, file_name)
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
                
            # Perform regex replacements for timestamps
            # Pattern: yyyy. mm. dd. hh:mm
            content = re.sub(r'\d{4}\.\s*\d{2}\.\s*\d{2}\.\s*\d{2}:\d{2}', now_dot_str, content)
            # Pattern: yyyy-mm-dd hh:mm(:ss)?
            content = re.sub(r'\d{4}-\d{2}-\d{2}\s*\d{2}:\d{2}(:\d{2})?', now_str, content)
            # Pattern: Last Portal Update: yyyy-mm-dd hh:mm
            content = re.sub(r'Last Portal Update:\s*\d{4}-\d{2}-\d{2}\s*\d{2}:\d{2}', f'Last Portal Update: {now_str}', content)
            # Pattern: SYSTEM UPDATED: yyyy-mm-dd hh:mm
            content = re.sub(r'SYSTEM\s*UPDATED:\s*\d{4}-\d{2}-\d{2}\s*\d{2}:\d{2}', f'SYSTEM UPDATED: {now_str}', content)
            # Pattern: Last Updated: yyyy. mm. dd. hh:mm
            content = re.sub(r'Last\s*Updated:\s*\d{4}\.\s*\d{2}\.\s*\d{2}\.\s*\d{2}:\d{2}', f'Last Updated: {now_dot_str}', content)
            # Pattern: 실시간 자동사냥 | 2026년 ...
            content = re.sub(r'실시간\s*자동사냥\s*\|\s*\d{4}년\s*\d{1,2}월\s*\d{1,2}일\s*\d{1,2}:\d{2}', f'실시간 자동사냥 | {now_korean_str}', content)
            
            # Write back in UTF-8 without BOM
            with open(file_path, 'w', encoding='utf-8', newline='') as f:
                f.write(content)
            print(f"  [OK] Synced timestamps in {file_name}")
        except Exception as e:
            print(f"  [ERROR] Failed to sync timestamps in {file_name}: {e}")
            sys.exit(1)
            
    # 4. Revalidate
    print("\n--- Step 4: Running validation script ---")
    try:
        val_script = os.path.join(base_dir, "scripts", "revalidate_portal.py")
        print(f"Running: python {val_script}")
        subprocess.run(["python", val_script], check=True)
        print("[OK] Portal validation passed successfully.")
    except subprocess.CalledProcessError as e:
        print("[ERROR] Portal validation failed.")
        sys.exit(1)

if __name__ == "__main__":
    main()
