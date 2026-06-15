# -*- coding: utf-8 -*-
import subprocess
import os
import sys

def main():
    base_dir = r"C:\Users\S\Desktop\AI\Gemini\Stock"
    
    # 1. Fetch news
    print("\n--- Step 1: Fetching News via Node.js ---")
    try:
        news_script = os.path.join(base_dir, "scripts", "fetch_news.cjs")
        print(f"Running: node {news_script}")
        subprocess.run(["node", news_script], check=True)
        print("[OK] News fetched and news.html generated successfully.")
    except Exception as e:
        print(f"[ERROR] Failed to fetch news: {e}")
        sys.exit(1)
        
    # 2. Update data to 15:00 KST
    print("\n--- Step 2: Updating Portal Data to 15:00 KST ---")
    try:
        update_script = os.path.join(base_dir, "scripts", "update_portal_data_20260615_1500.py")
        print(f"Running: python {update_script}")
        subprocess.run(["python", update_script], check=True)
        print("[OK] Portal data updated successfully.")
    except Exception as e:
        print(f"[ERROR] Failed to update portal data: {e}")
        sys.exit(1)
        
    # 3. Revalidate
    print("\n--- Step 3: Running Validation ---")
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
