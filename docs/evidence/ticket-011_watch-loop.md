# Ticket 011 - Watch Loop v0

## Goal
Make the watcher run in a loop with a sleep interval and keep going after temporary RPC errors.

## Command
```bash
python src/watcher_loop_v0.py
RPC_URL="http://127.0.0.1:1" python src/watcher_loop_v0.py
```

## Output (normal)
```text
cycle_n=1
latest_block=24334929
cursor_before=177
start_block=178
end_block=180
cursor_after=180
processed_blocks_count=3

sleep_seconds=3

cycle_n=2
latest_block=24334929
cursor_before=180
start_block=181
end_block=183
cursor_after=183
processed_blocks_count=3
```

## Output (forced error)
```text
cycle_n=1 rpc_error=1 err_type=ConnectionError err_msg=HTTPConnectionPool(host='127.0.0.1', port=1): Max retries exceeded with url: / (Caused by NewConnectionError("HTTPConnection(host='127.0.0.1', port=1): Failed to establish a new connection: [Errno 111] Connection refused")) will_retry=1                                                                                 
sleep_seconds=3

cycle_n=2 rpc_error=1 err_type=ConnectionError err_msg=HTTPConnectionPool(host='127.0.0.1', port=1): Max retries exceeded with url: / (Caused by NewConnectionError("HTTPConnection(host='127.0.0.1', port=1): Failed to establish a new connection: [Errno 111] Connection refused")) will_retry=1                                                                                 
sleep_seconds=3       
```

