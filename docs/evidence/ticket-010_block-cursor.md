# Ticket 010 - Block Cursor v0

## Goal
Prove the watcher resumes from the last processed block.

## DB
SQLite meta table stores last_processed_block


## Command
```bash
python src/watcher_cursor_v0.py && python src/watcher_cursor_v0.py
```

## Output
```text
#Run 1
cursor_before= 0
latest_block= 24326712
start_block= 1
end_block= 3
block_number= 1
block_number= 2
block_number= 3
cursor_after= 3

#Run 2
cursor_before= 3
latest_block= 24326712
start_block= 4
end_block= 6
block_number= 4
block_number= 5
block_number= 6
cursor_after= 6
```

