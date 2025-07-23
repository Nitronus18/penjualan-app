# init_db.py
import sqlite3

conn = sqlite3.connect('database.db')
cur = conn.cursor()

cur.execute('''
CREATE TABLE IF NOT EXISTS produk (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nama TEXT NOT NULL,
    harga INTEGER NOT NULL,
    stok INTEGER NOT NULL
);
''')

# Tambahkan kolom kategori jika belum ada
cur.execute('ALTER TABLE produk ADD COLUMN kategori TEXT')

cur.execute('''
CREATE TABLE IF NOT EXISTS penjualan (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    produk_id INTEGER,
    jumlah INTEGER,
    tanggal TEXT DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (produk_id) REFERENCES produk(id)
);
''')

conn.commit()
conn.close()
