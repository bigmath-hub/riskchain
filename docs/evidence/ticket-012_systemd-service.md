# Ticket 012 - Systemd Service

## Command
```bash
systemctl --user start riskchain-watcher.service && systemctl --user status riskchain-watcher.service --no-pager
systemctl --user stop riskchain-watcher.service && systemctl --user status riskchain-watcher.service --no-pager
journalctl --user -u riskchain-watcher.service -n 80 --no-pager
# Limitation: user service depends on user session; next: loginctl enable-linger
```

## Output (normal)
```text
riskchain-watcher.service - Systemd Service v0 (run 24/7 on Linux)
     Loaded: loaded (/home/<USER>/.config/systemd/user/riskchain-watcher.service; disabled; preset: enabled)
     Active: active (running) since Fri 2026-01-30 18:25:39 +03; 14ms ago
   Main PID: 27712 (python)
      Tasks: 1 (limit: 18943)
     Memory: 2.3M (peak: 2.3M)
        CPU: 8ms
     CGroup: /user.slice/user-1000.slice/user@1000.service/app.slice/riskchain-watcher.service
             └─27712 /home/<USER>/work/riskchain-portifolio/.venv/bin/python -u src/watcher…
```

## Journal snippet
```text
Jan 30 18:20:52 <HOST> python[26696]: cycle_n=11
Jan 30 18:20:52 <HOST> python[26696]: latest_block=24348544
Jan 30 18:20:52 <HOST> python[26696]: cursor_before=468
Jan 30 18:20:52 <HOST> python[26696]: start_block=469
Jan 30 18:20:52 <HOST> python[26696]: end_block=471
Jan 30 18:20:52 <HOST> python[26696]: cursor_after=471
Jan 30 18:20:52 <HOST> python[26696]: processed_block_count=3
Jan 30 18:20:52 <HOST> python[26696]: sleep_seconds=3
Jan 30 18:20:55 <HOST> python[26696]: cycle_n=12
Jan 30 18:20:55 <HOST> python[26696]: latest_block=24348544
Jan 30 18:20:55 <HOST> python[26696]: cursor_before=471
Jan 30 18:20:55 <HOST> python[26696]: start_block=472
Jan 30 18:20:55 <HOST> python[26696]: end_block=474
Jan 30 18:20:55 <HOST> python[26696]: cursor_after=474
Jan 30 18:20:55 <HOST> python[26696]: processed_block_count=3
Jan 30 18:20:55 <HOST> python[26696]: sleep_seconds=3
Jan 30 18:20:59 <HOST> python[26696]: cycle_n=13
Jan 30 18:20:59 <HOST> python[26696]: latest_block=24348544
Jan 30 18:20:59 <HOST> python[26696]: cursor_before=474
Jan 30 18:20:59 <HOST> python[26696]: start_block=475
Jan 30 18:20:59 <HOST> python[26696]: end_block=477
Jan 30 18:20:59 <HOST> python[26696]: cursor_after=477
Jan 30 18:20:59 <HOST> python[26696]: processed_block_count=3
Jan 30 18:20:59 <HOST> python[26696]: sleep_seconds=3
```

## Stop snippet
```text
○ riskchain-watcher.service - Systemd Service v0 (run 24/7 on Linux)
     Loaded: loaded (/home/<USER>/.config/systemd/user/riskchain-watcher.service; disabled; 
preset: enabled)             
Active: inactive (dead)
Jan 30 18:37:59 <HOST> python[29039]: latest_block=24348629
Jan 30 18:37:59 <HOST> python[29039]: cursor_before=1020
Jan 30 18:37:59 <HOST> python[29039]: start_block=1021
Jan 30 18:37:59 <HOST> python[29039]: end_block=1023
Jan 30 18:37:59 <HOST> python[29039]: cursor_after=1023
Jan 30 18:37:59 <HOST> python[29039]: processed_block_count=3
Jan 30 18:37:59 <HOST> python[29039]: sleep_seconds=3
Jan 30 18:38:00 <HOST> systemd[1457]: Stopping riskchain-watcher.service - S…)...
Jan 30 18:38:00 <HOST> systemd[1457]: Stopped riskchain-watcher.service - Sy…ux).
Jan 30 18:38:00 <HOST> systemd[1457]: riskchain-watcher.service: Consumed 1.…ime.
Hint: Some lines were ellipsized, use -l to show in full.
```
