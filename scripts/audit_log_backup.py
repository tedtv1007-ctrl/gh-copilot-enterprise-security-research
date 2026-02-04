import requests
import json
import os
import gzip
from datetime import datetime, timedelta

# 配置區域
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
ENTERPRISE_SLUG = os.getenv("GITHUB_ENT_SLUG")
STATE_FILE = "last_timestamp.txt"
BACKUP_DIR = "./backups"

def fetch_audit_logs(after_ts=None):
    """
    透過 GitHub API 獲取 Audit Logs
    """
    url = f"https://api.github.com/enterprises/{ENTERPRISE_SLUG}/audit-log"
    params = {"per_page": 100}
    if after_ts:
        params["phrase"] = f"created:>={after_ts}"
    
    headers = {
        "Authorization": f"token {GITHUB_TOKEN}",
        "Accept": "application/vnd.github+json"
    }
    
    response = requests.get(url, headers=headers, params=params)
    response.raise_for_status()
    return response.json()

def save_and_compress(logs):
    """
    存儲並壓縮日誌
    """
    if not logs:
        print("沒有新日誌需要備份。")
        return
    
    if not os.path.exists(BACKUP_DIR):
        os.makedirs(BACKUP_DIR)
        
    filename = f"audit_log_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json.gz"
    filepath = os.path.join(BACKUP_DIR, filename)
    
    content = json.dumps(logs, indent=2).encode('utf-8')
    with gzip.open(filepath, 'wb') as f:
        f.write(content)
        
    print(f"備份成功: {filepath}")

def main():
    # 讀取上次備份的時間點實現增量備份
    last_ts = None
    if os.path.exists(STATE_FILE):
        with open(STATE_FILE, "r") as f:
            last_ts = f.read().strip()
    else:
        # 預設拉取過去 24 小時
        last_ts = (datetime.now() - timedelta(days=1)).isoformat()

    try:
        logs = fetch_audit_logs(last_ts)
        save_and_compress(logs)
        
        # 更新最後一次拉取的時間 (簡化邏輯：使用當前時間)
        with open(STATE_FILE, "w") as f:
            f.write(datetime.now().isoformat())
            
    except Exception as e:
        print(f"備份過程中出錯: {e}")

if __name__ == "__main__":
    main()
