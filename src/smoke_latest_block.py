import os
import requests
  
if __name__ == "__main__":
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
        print(f"latest_block={block_num}")
    except (KeyError, ValueError, TypeError) as e:
        print("Parse error")
        raise SystemExit(1) from e
