import csv
from pathlib import Path
from collections import Counter
from datetime import datetime

def main():
    CSV_PATH = Path("docs/forensics/seed-data.csv")
    
    tx_hashes = set()
    addresses = set()
    labels = Counter()    
    missing_source_count = 0
    rows_total = 0
    min_dt = None
    max_dt = None

    with CSV_PATH.open(mode='r', encoding='utf-8') as csvfile:
        csv_reader = csv.DictReader(csvfile)
        for row in csv_reader:
            rows_total += 1

            f = (row.get("from_address") or "").strip().lower()
            t = (row.get("to_address") or "").strip().lower()            
            h = (row.get("tx_hash") or "").strip().lower()                        
            label = (row.get("label") or "").strip().lower()            
            m = (row.get("source") or "").strip().lower()                                    
            
            s = (row.get("date_utc") or "").strip()
            if s:            
                if s.endswith("Z"):                
                    s = s[:-1] + "+00:00"
                dt = datetime.fromisoformat(s)
                if (min_dt is None) or (dt < min_dt):
                    min_dt = dt
                if (max_dt is None) or (dt > max_dt):
                    max_dt = dt

            if h:                
                tx_hashes.add(h)
            if f:
                addresses.add(f)
            if t:
                addresses.add(t)
            if label:
                labels[label] += 1                        
            if not m:
                missing_source_count += 1          
    
    
    labels_top_5 = labels.most_common(5)
    print(f"rows_total={rows_total}")
    print(f"unique_tx_hashes={len(tx_hashes)}")    
    print(f"unique_addresses={len(addresses)}")    
    print("labels_top5:")
    for name, cnt in labels_top_5:
        print(f"label={name} count={cnt}")
    print(f"missing_source_count={missing_source_count}")
    print(f"earliest_date_utc={min_dt.isoformat() if min_dt else 'NA'}")
    print(f"latest_date_utc={max_dt.isoformat() if max_dt else 'NA'}")

if __name__ == "__main__":
    main()
