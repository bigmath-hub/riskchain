- **Date**: 2026-01-22
- **Machine:** Linux Mint

- **Commands:** 
```bash
pwd && python3 --version && which python && pip --version && python src/smoke_latest_block.py
```

- **output:**
```bash
/home/matheus/work/riskchain-portifolio
Python 3.12.3
/home/matheus/work/riskchain-portifolio/.venv/bin/python
pip 25.3 from /home/matheus/work/riskchain-portifolio/.venv/lib/python3.12/site-packages/pip 
(python 3.12)                                                                                DEBUG: O servidor respondeu: {'jsonrpc': '2.0', 'id': 1, 'result': '0x172abb1'}
latest_block=24292273
```

**Result:** PASS (local run succeeded)
**Git commit:** 77d7472
