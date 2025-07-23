import sqlite3

conn = sqlite3.connect('database.db')
cur = conn.cursor()

cur.execute('''
CREATE TABLE IF NOT EXISTS bahan (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nama TEXT NOT NULL,
    satuan TEXT
);
''')

cur.execute('''
CREATE TABLE IF NOT EXISTS pembelian (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    bahan_id INTEGER,
    jumlah REAL,
    harga_total INTEGER,
    tanggal TEXT DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (bahan_id) REFERENCES bahan(id)
);
''')

conn.commit()
conn.close()
print("✅ Tabel bahan & pembelian berhasil dibuat.")
