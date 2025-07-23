# seed_produk.py
import sqlite3

# Daftar produk tetap dengan harga 8000
produk_list = [
    # Chocolate Series
    ("coco rocky tiramisu", 8000, 0, "coklat"),
    ("coco banana", 8000, 0, "coklat"),
    ("coco classic", 8000, 0, "coklat"),
    ("coco halloween", 8000, 0, "coklat"),
    ("coco kulaku", 8000, 0, "coklat"),
    ("coco lumer", 8000, 0, "coklat"),
    ("coco maltino", 8000, 0, "coklat"),
    ("coco red florest", 8000, 0, "coklat"),
    ("coco trouble", 8000, 0, "coklat"),

    # Fruit Series
    ("alpukat", 8000, 0, "fruit"),
    ("mango", 8000, 0, "fruit"),
    ("lychee", 8000, 0, "fruit"),
    ("strawberry", 8000, 0, "fruit"),
    ("blueberry", 8000, 0, "fruit"),
    ("durian", 8000, 0, "fruit"),
    ("blewah", 8000, 0, "fruit"),
    ("nanas", 8000, 0, "fruit"),

    # Spesial Series
    ("brown sugar tiramisu", 8000, 0, "spesial"),
    ("brown sugar vanilla lagoan", 8000, 0, "spesial"),
    ("blody velvet", 8000, 0, "spesial"),
    ("brows sugar durian", 8000, 0, "spesial"),
    ("brown sugar klepon", 8000, 0, "spesial"),
    ("green velvet", 8000, 0, "spesial"),
    ("violet", 8000, 0, "spesial"),

    # Coffee Series
    ("coffe ala goklat", 8000, 0, "coffee"),
    ("coffe tiramisu", 8000, 0, "coffee"),
    ("coconut aren coffe", 8000, 0, "coffee"),
    ("capucino kulaku", 8000, 0, "coffee"),
    ("durian coffe", 8000, 0, "coffee"),
    ("coffe pandan", 8000, 0, "coffee"),

     # Gotea Series
    ("gotea honey", 6000, 0, "gotea"),
    ("gotea jasmine", 6000, 0, "gotea"),
    ("gotea special", 6000, 0, "gotea"),
    ("gotea black current", 7000, 0, "gotea"),
    ("gotea apple", 7000, 0, "gotea"),
    ("gotea mangga", 7000, 0, "gotea"),
    ("gotea lychee", 7000, 0, "gotea"),
    ("gotea lemon", 7000, 0, "gotea"),
    ("gotea peach", 7000, 0, "gotea"),
    ("gotea grape", 7000, 0, "gotea"),

    #Es Teh Jumbo
    ("EsTeh Jumbo", 3000, 0, "EsTeh"),
    ("EsTeh Jumbo Jeruk Nipis", 4000, 0, "EsTeh"),
]


conn = sqlite3.connect('database.db')
cur = conn.cursor()

for nama, harga, stok, kategori in produk_list:
    cur.execute("SELECT COUNT(*) FROM produk WHERE nama = ?", (nama,))
    if cur.fetchone()[0] == 0:
        cur.execute("INSERT INTO produk (nama, harga, stok, kategori) VALUES (?, ?, ?, ?)", (nama, harga, stok, kategori))
    else:
        cur.execute("UPDATE produk SET harga = ?, kategori = ? WHERE nama = ?", (harga, kategori, nama))


conn.commit()
conn.close()
print("✅ Produk tetap diisi / diperbarui dengan harga 8000.")
