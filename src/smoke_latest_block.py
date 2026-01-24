import os
import requests
from dotenv import load_dotenv
  
if __name__ == "__main__":
    load_dotenv()
    rpc_url = os.getenv('RPC_URL')
    if not rpc_url:
        print("RPC_URL not set")
        raise SystemExit(1)    
    
    payload = {
        "jsonrpc": "2.0",        
        "method": "eth_blockNumber",
        "params": [],
        "id": 1
    }
    
    resp = requests.post(rpc_url, json=payload, timeout=10)

    if resp.status_code != 200:
        print("RPC call failed")
        raise SystemExit(1)
    
    data = resp.json()
    
    try:        
        hex_block = data['result']    
        block_num = int(hex_block, 16)
        payload2 = {
        "jsonrpc": "2.0",
        "method": "eth_getBlockByNumber",
        "params":[hex_block, False]
        }
        data2 = requests.post(rpc_url, json=payload2, timeout=10).json()
        if data2.get('error') or data2.get('result') is None:
            print("RPC2 failed")
            raise SystemExit(1)
        block = data2["result"]
        if int(block['number'], 16) != block_num:
            raise SystemExit(1)
        ts = int(block['timestamp'], 16)   
        print(f"latest_block={block_num}")
        print(f"block_hash={block['hash']}")
        print(f"block_size={len(block["transactions"])}")
        print(f"block_timestamp={ts}")
        print("block_fetch_ok=1")
    except (KeyError, ValueError, TypeError) as e:
        print("Parse error")
        raise SystemExit(1) from e
