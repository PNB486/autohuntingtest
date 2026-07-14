# -*- coding: utf-8 -*-
import os
import sys
import subprocess
import datetime

def run_command(cmd, cwd):
    print(f"Running: {' '.join(cmd) if isinstance(cmd, list) else cmd}")
    res = subprocess.run(cmd, cwd=cwd, shell=True, capture_output=True, text=True, encoding='utf-8', errors='replace')
    if res.returncode != 0:
        print(f"[ERROR] Command failed with return code {res.returncode}")
        print(f"Stdout:\n{res.stdout}")
        print(f"Stderr:\n{res.stderr}")
        return False, res.stdout, res.stderr
    return True, res.stdout, res.stderr

def main():
    if hasattr(sys.stdout, 'reconfigure'):
        sys.stdout.reconfigure(encoding='utf-8')
    if hasattr(sys.stderr, 'reconfigure'):
        sys.stderr.reconfigure(encoding='utf-8')
    
    base_dir = r"C:\Users\S\Desktop\AI\Gemini\Stock"
    os.environ["chcp"] = "65001"
    
    # Force shell encoding to UTF-8
    if sys.platform == 'win32':
        subprocess.run("chcp 65001", shell=True)

    print("========================================")
    print(f"[Soul's Auto-Hunt Engine] Starting update pipeline at {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("========================================")

    # 1. Sync with git remote
    print("\n[1/6] Aligning workspace with remote GitHub repository...")
    ok, stdout, stderr = run_command("git fetch origin main", base_dir)
    if not ok:
        print("[WARNING] git fetch failed, proceeding anyway...")
    
    ok, stdout, stderr = run_command("git reset --hard origin/main", base_dir)
    if not ok:
        print("[WARNING] git reset failed, proceeding anyway...")

    # 2. Fetch news
    print("\n[2/6] Hunting real-time news...")
    ok, stdout, stderr = run_command("node scripts/fetch_news.cjs", base_dir)
    if not ok:
        print("[ERROR] News fetching failed.")
        sys.exit(1)
    print(stdout)

    # 3. Auto-update market data
    print("\n[3/6] Updating Indices, Prices, and Valuations...")
    ok, stdout, stderr = run_command("python scripts/auto_update_market_data.py", base_dir)
    if not ok:
        print("[ERROR] Market data update failed.")
        sys.exit(1)
    print(stdout)

    # 4. Revalidate HTML files
    print("\n[4/6] Verifying portal integrity...")
    ok, stdout, stderr = run_command("python scripts/revalidate_portal.py", base_dir)
    if not ok:
        print("[ERROR] Portal validation failed.")
        sys.exit(1)
    print(stdout)

    # 5. Git Commit & Push (Force to keep single commit as per Rule 7)
    print("\n[5/6] Committing changes to git (single-commit mode)...")
    run_command("git add .", base_dir)
    ok, stdout, stderr = run_command('git commit --amend -m "Auto Hunt Portal Update"', base_dir)
    if not ok:
        # Fallback to standard commit if there's no commit to amend
        print("Amend failed. Attempting standard commit...")
        ok, stdout, stderr = run_command('git commit -m "Auto Hunt Portal Update"', base_dir)
    
    print("\n[6/6] Pushing to remote repository...")
    ok, stdout, stderr = run_command("git push origin main --force", base_dir)
    if not ok:
        print("[ERROR] Git push failed.")
        sys.exit(1)
    print(stdout)

    # Verify Git sync
    print("\n[Verification] Cross-checking Git Remote Sync...")
    _, local_hash, _ = run_command("git rev-parse HEAD", base_dir)
    local_hash = local_hash.strip()
    
    run_command("git fetch origin main", base_dir)
    _, remote_hash, _ = run_command("git rev-parse origin/main", base_dir)
    remote_hash = remote_hash.strip()

    if local_hash == remote_hash:
        print(f"[OK] Git Remote Sync Verified successfully!")
        print(f"Local & Remote Hash: {local_hash}")
    else:
        print(f"[ERROR] Git Sync Mismatch!")
        print(f"Local:  {local_hash}")
        print(f"Remote: {remote_hash}")
        sys.exit(1)

    print("\n========================================")
    print("Pipeline Execution Complete & Verified!")
    print("========================================")

if __name__ == '__main__':
    main()
