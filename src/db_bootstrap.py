import sqlite3

# Save datebase -> module constant (reusable)
DB_PATH = "data/riskchain.db"

def main():
    with sqlite3.connect(DB_PATH) as conn:
        print(f"connected={DB_PATH}")
        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS transactions (
                tx_hash TEXT UNIQUE,
                block_number INTEGER,
                from_address TEXT,
                to_address TEXT,
                value_wei INTEGER,
                timestamp_utc TEXT
            );            
            """
        )
        conn.execute(
            """
            INSERT OR IGNORE INTO transactions (
                tx_hash, 
                block_number, 
                from_address,
                to_address,
                value_wei,
                timestamp_utc
            )            
            VALUES (
                '0xSAMPLE_TX_HASH',
                1,
                '0xFROM',
                '0xTO',
                123,
                '2026-01-22T00:00:00Z'
            );
            """
        )
        count = conn.execute(
            """
            SELECT COUNT(*) FROM transactions;
            """
        ).fetchone()[0]
        cols = conn.execute("""
                PRAGMA table_info(transactions)
                """).fetchall()
        print(f"cols={len(cols)}")
        print(f"rows={count}")

if __name__ == "__main__":
    main()
