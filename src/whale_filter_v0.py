import os
import sqlite3
import requests
from dotenv import load_dotenv

if __name__ == "__main__":
    load_dotenv()
    rpc_url = os.getenv("RPC_URL")
    min_value_wei = int(os.getenv('MIN_VALUE_WEI', "0"))
    db_path = os.getenv("DB_PATH", "riskchain.db")
    conn = sqlite3.connect(db_path)
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

    payload2 = {
        "jsonrpc": "2.0",
        "method": "eth_getBlockByNumber",
        "params": [hex_block, True],
        "id": 2
    }

    resp2 = requests.post(rpc_url, json=payload2, timeout=10)
    if resp2.status_code != 200:
        raise SystemExit(1)
    
    data2 = resp2.json()
    block = data2.get('result')
    if data2.get('error') or block is None:
        raise SystemExit(1)
    txs = block.get('transactions', [])
    tx_count = len(txs)    
    cur = conn.cursor()
    insert_sql = """
        INSERT INTO transactions(
        tx_hash,
        block_number,
        from_address,
        to_address,
        value_wei,
        timestamp_utc
        )
        VALUES (?,?,?,?,?,?)
    """
    block_number = int(block['number'], 16)
    timestamp_utc = str(int(block['timestamp'], 16))
    db_inserted_count = db_skipped_duplicates_count = 0
    flagged_count = 0
    sample_flagged = []
    for tx in txs:
        value_wei = int(tx['value'], 16)
        if value_wei < min_value_wei:
            continue
        flagged_count += 1
        tx_hash = tx['hash']
        if len(sample_flagged) < 3:
            sample_flagged.append(tx_hash)
        from_address = tx.get("from")
        to_address = tx.get("to")        
        row = (
            tx_hash,
            block_number,
            from_address,
            to_address,
            str(value_wei),
            timestamp_utc
        )
        try:
            cur.execute(insert_sql, row)
            db_inserted_count += 1
        except sqlite3.IntegrityError:
            db_skipped_duplicates_count += 1
    conn.commit()
    print(f"""
    block_number={block_number}
    tx_count={tx_count}
    flagged_count={flagged_count}
    db_inserted_count={db_inserted_count}
    db_skipped_duplicates_count={db_skipped_duplicates_count}
    """)        
    print(
    "sample_flagged_hashes=" + ",".join(sample_flagged)
    if sample_flagged else "sample_flagged_hashes=<empty>"    
    )
