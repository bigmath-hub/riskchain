import os
import sqlite3
import requests
from dotenv import load_dotenv
from time import sleep

# TODO: Watch loop v0
# - repeat N rounds
# - print receipt per round
# - sleep t seconds
# - on error: print and continue

def get_cursor_before(conn):
    cursor = conn.cursor()    
    cursor.execute(
        '''
        SELECT value FROM meta WHERE key="last_processed_block";
        '''
    )        
    
    # Fetch the result
    result = cursor.fetchone()    
    
    if result is None:
        return 0
            
    return int(result[0])

def set_cursor(conn, bn):
    cursor = conn.cursor()
    # The "excluded." prefix refers to the value that would have 
    # been inserted had there been no conflict.
    upsert_query = '''
    INSERT INTO meta (key, value) VALUES (?, ?)
    ON CONFLICT(key)
    DO UPDATE SET                
        value = excluded.value;
    '''
    # Execute and commit the transaction
    try:
        cursor.execute(
            upsert_query, ("last_processed_block", str(bn))
        )        
    except sqlite3.Error as e:
        raise ValueError(f"An error occurred: {e}")
    
def run_once(conn, rpc_url, max_blocks_per_run):
    cursor_before = get_cursor_before(conn)    
    
    if not rpc_url:
        print("RPC_URL not set")
        raise SystemError(1)
    
    payload = {
        "jsonrpc": "2.0",
        "method": "eth_blockNumber",
        "params": [],
        "id": 1
    }

    resp = requests.post(rpc_url, json=payload, timeout=10)
    if resp.status_code != 200:
        raise SystemExit(1)    
    
    data = resp.json()    
    hex_block = data.get("result")
    latest_block = int(hex_block, 16)    
    
    start_block = cursor_before + 1
    end_block = min(
        latest_block, start_block + max_blocks_per_run - 1
    )       

    cursor_after = cursor_before
    for bn in range(start_block, end_block + 1):        
        set_cursor(conn, bn)
        conn.commit()
        cursor_after = bn    
    
    processed_blocks_count = (
        end_block - start_block + 1 if start_block <= end_block else 0
    )

    final_return = {
        'latest_block': latest_block,
        'cursor_before': cursor_before,
        'start_block': start_block,
        'end_block': end_block,
        'cursor_after': cursor_after,
        'processed_blocks_count': processed_blocks_count
    }

    return final_return

if __name__ == "__main__":
    load_dotenv()
    SLEEP_SECONDS = int(os.getenv("SLEEP_SECONDS", "3"))
    MAX_CYCLES = 3    
    MAX_BLOCKS_PER_RUN = int(os.getenv("MAX_BLOCKS_PER_RUN", "3"))    
    rpc_url = os.getenv("RPC_URL")
    db_path = os.getenv("DB_PATH", "riskchain.db")
    conn = sqlite3.connect(db_path)
    
    meta = (
        '''
        CREATE TABLE IF NOT EXISTS meta (
        key TEXT PRIMARY KEY, 
        value TEXT NOT NULL);
    '''
    )
    
    conn.execute(meta)
    conn.commit()    

    for cycle_n in range(1, MAX_CYCLES + 1):
        try:
            audit = run_once(conn, rpc_url, MAX_BLOCKS_PER_RUN)
            print(f"""
cycle_n={cycle_n}
latest_block={audit['latest_block']}
cursor_before={audit['cursor_before']}
start_block={audit['start_block']}
end_block={audit['end_block']}
cursor_after={audit['cursor_after']}
processed_block_count={audit['processed_blocks_count']}
""")
        except Exception as e:
            print(f"""                
cycle_n={cycle_n} 
rpc_error=1 
err_type={type(e).__name__} 
err_msg={e} will_retry=1                
            """)
        if cycle_n < MAX_CYCLES:
            print(f"sleep_seconds={SLEEP_SECONDS}")
            sleep(SLEEP_SECONDS)
