import os
import sqlite3
import requests
from dotenv import load_dotenv
from datetime import datetime, timezone


if __name__ == "__main__":
    load_dotenv()
    rpc_url = os.getenv("RPC_URL")
    db_path = os.getenv("DB_PATH", "riskchain.db")    
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    print(f"db_path={db_path} ok")
    
    cursor.execute(
        '''
        SELECT value FROM meta WHERE key="last_processed_block";
        '''
    )   
    # Fetch the result
    cursor_row = cursor.fetchone()

    cursor.execute(
        '''
        SELECT value FROM meta WHERE key="last_run_utc";
        '''
    )            
    # Fetch the result
    last_run_row = cursor.fetchone()

    cursor_value = int(cursor_row[0]) if cursor_row else 0
    last_run_utc = last_run_row[0] if last_run_row else "MISSING"
    

    print(f"cursor_value={cursor_value}")
    print(f"last_run_utc={last_run_utc}")

    threshold = 180    

    if last_run_utc == 'MISSING':
        fresh = 'NEVER'
        age_seconds = 'NA'
    else:
        last_dt = datetime.fromisoformat(last_run_utc.replace("Z", "+00:00"))
        age_seconds = int((datetime.now(timezone.utc) - last_dt).total_seconds())
        fresh = 'OK' if age_seconds <= threshold else 'STALE'    
    
    print(f"age_seconds={age_seconds} fresh={fresh}")
    
    if not rpc_url:
        print("latest_block = 'SKIP'")

    else:
        payload = {
            "jsonrpc": "2.0",
            "id": 1,
            "method": "eth_blockNumber",
            "params": []
        }
        r = requests.post(rpc_url, json=payload, timeout=10)
        latest_block = int(r.json()['result'], 16)
        print(f"latest_block={latest_block}")

