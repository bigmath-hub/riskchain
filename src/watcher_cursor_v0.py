import os
import sqlite3
import requests
from dotenv import load_dotenv

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

if __name__ == "__main__":    
    load_dotenv()
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

    cursor_before = get_cursor_before(conn)
    print("cursor_before=", cursor_before)

    if not rpc_url:
        print("RPC_URL not set")
        raise SystemError(1)
    
    MAX_BLOCKS_PER_RUN = 3

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
    print("latest_block=", latest_block)
    
    start_block = cursor_before + 1
    end_block = min(
        latest_block, start_block + MAX_BLOCKS_PER_RUN - 1
    )
    print("start_block=", start_block)
    print("end_block=", end_block)

    cursor_after = cursor_before
    for bn in range(start_block, end_block + 1):
        print("block_number=", bn)
        set_cursor(conn, bn)
        conn.commit()
        cursor_after = bn
    print("cursor_after=", cursor_after)
