# Ticket 009 - Whale Filter v0 (threshold + persist to SQLite)

## Command
```bash
python src/whale_filter_v0.py
python src/whale_filter_v0.py
```

## Output
```text
block_number=24313116
tx_count=521
flagged_count=7
db_inserted_count=7
db_skipped_duplicates_count=0
sample_flagged_hashes=0xab571be8ed90d0ec3f78d63bffab75a9cd6acd3d5b04812a95b96214cc18c1b6,
0xf70f93a0ee2d094355d4f4eb26c94996fa237c8d6e24ae849ff89d99cd95a767,
0x9291d006beefaa6efaae627bed8818b2b3a3b101015e34d054e9a1f32eaaf450

block_number=24313116
tx_count=521
flagged_count=7
db_inserted_count=0
db_skipped_duplicates_count=7
sample_flagged_hashes=0xab571be8ed90d0ec3f78d63bffab75a9cd6acd3d5b04812a95b96214cc18c1b6,
0xf70f93a0ee2d094355d4f4eb26c94996fa237c8d6e24ae849ff89d99cd95a767,
0x9291d006beefaa6efaae627bed8818b2b3a3b101015e34d054e9a1f32eaaf450
```
