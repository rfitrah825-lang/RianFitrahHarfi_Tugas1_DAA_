
import pandas as pd
import time


# ==========================================
# 1. MEMBACA DATASET
# ==========================================

DATASET_FILE = "google_books_dataset.csv"


def baca_dataset():
    df = pd.read_csv(DATASET_FILE)

    # Judul kosong tidak dapat digunakan untuk pencarian.
    df = df.dropna(subset=["title"]).copy()
    df["title"] = df["title"].astype(str)

    # Data disimpan sebagai list berisi dictionary.
    buku = df.to_dict(orient="records")

    return buku


def normalisasi(teks):
    # Agar pencarian tidak membedakan huruf besar dan kecil.
    return str(teks).strip().casefold()


# ==========================================
# 2. LINEAR SEARCH
# ==========================================

def linear_search(data, target):
    jumlah_perbandingan = 0
    target = normalisasi(target)

    for buku in data:
        judul = normalisasi(buku["title"])

        jumlah_perbandingan += 1

        if judul == target:
            return buku, jumlah_perbandingan

    return None, jumlah_perbandingan


# ==========================================
# 3. BINARY SEARCH
# ==========================================

def binary_search(data_terurut, target):
    kiri = 0
    kanan = len(data_terurut) - 1
    jumlah_perbandingan = 0
    target = normalisasi(target)

    while kiri <= kanan:
        tengah = (kiri + kanan) // 2
        judul_tengah = normalisasi(
            data_terurut[tengah]["title"]
        )

        # Membandingkan judul dengan target.
        jumlah_perbandingan += 1

        if judul_tengah == target:
            return data_terurut[tengah], jumlah_perbandingan

        jumlah_perbandingan += 1

        if judul_tengah < target:
            kiri = tengah + 1
        else:
            kanan = tengah - 1

    return None, jumlah_perbandingan


# ==========================================
# 4. MENAMPILKAN INFORMASI BUKU
# ==========================================

def tampilkan_buku(buku):
    if buku is None:
        print("Buku tidak ditemukan.")
        return

    print("Buku ditemukan!")
    print("ID          :", buku.get("book_id", "-"))
    print("Judul       :", buku.get("title", "-"))
    print("Penulis     :", buku.get("authors", "-"))
    print("Penerbit    :", buku.get("publisher", "-"))
    print("Kategori    :", buku.get("categories", "-"))
    print("Tahun terbit :", buku.get("published_date", "-"))
    print("Rating      :", buku.get("average_rating", "-"))


# ==========================================
# 5. PENGUJIAN WORST-CASE
# ==========================================

def uji_performa(data):
    ukuran_input = [100, 1000, 10000]

    # Target sengaja dibuat tidak ada di dataset.
    # Ini menguji kasus terburuk pencarian tidak berhasil.
    target = "\x00judul_yang_tidak_ada"

    print("\n" + "=" * 92)
    print("HASIL PENGUJIAN WORST-CASE")
    print("=" * 92)

    print(
        f"{'Algoritma':<16}"
        f"{'n':>8}"
        f"{'Perbandingan':>18}"
        f"{'Waktu (ms)':>18}"
        f"{'Hasil':>20}"
    )
    print("-" * 92)

    for n in ukuran_input:
        # Menggunakan n buku pertama.
        subset = data[:n]

        # Binary Search harus menggunakan data terurut.
        subset_terurut = sorted(
            subset,
            key=lambda buku: normalisasi(buku["title"])
        )

        # Mengukur waktu Linear Search.
        mulai = time.perf_counter()
        hasil_linear, banding_linear = linear_search(
            subset, target
        )
        waktu_linear = (time.perf_counter() - mulai) * 1000

        # Mengukur waktu Binary Search.
        # Pengurutan dilakukan sebelum pengukuran.
        mulai = time.perf_counter()
        hasil_binary, banding_binary = binary_search(
            subset_terurut, target
        )
        waktu_binary = (time.perf_counter() - mulai) * 1000

        print(
            f"{'Linear Search':<16}"
            f"{n:>8}"
            f"{banding_linear:>18}"
            f"{waktu_linear:>18.6f}"
            f"{'Tidak ditemukan':>20}"
        )

        print(
            f"{'Binary Search':<16}"
            f"{n:>8}"
            f"{banding_binary:>18}"
            f"{waktu_binary:>18.6f}"
            f"{'Tidak ditemukan':>20}"
        )

        print("-" * 92)


# ==========================================
# 6. PENCARIAN JUDUL OLEH PENGGUNA
# ==========================================

def cari_buku(data):
    print("\n" + "=" * 50)
    print("PENCARIAN BUKU")
    print("=" * 50)

    target = input(
        "Masukkan judul buku yang ingin dicari: "
    ).strip()

    if target == "":
        print("Judul tidak boleh kosong.")
        return

    # Linear Search menggunakan urutan data asli.
    mulai = time.perf_counter()
    hasil_linear, banding_linear = linear_search(
        data, target
    )
    waktu_linear = (time.perf_counter() - mulai) * 1000

    # Data diurutkan berdasarkan judul sebelum Binary Search.
    data_terurut = sorted(
        data,
        key=lambda buku: normalisasi(buku["title"])
    )

    mulai = time.perf_counter()
    hasil_binary, banding_binary = binary_search(
        data_terurut, target
    )
    waktu_binary = (time.perf_counter() - mulai) * 1000

    print("\n--- HASIL LINEAR SEARCH ---")
    tampilkan_buku(hasil_linear)
    print("Jumlah perbandingan:", banding_linear)
    print(f"Waktu pencarian    : {waktu_linear:.6f} ms")

    print("\n--- HASIL BINARY SEARCH ---")
    tampilkan_buku(hasil_binary)
    print("Jumlah perbandingan:", banding_binary)
    print(f"Waktu pencarian    : {waktu_binary:.6f} ms")


# ==========================================
# 7. PROGRAM UTAMA
# ==========================================

def main():
    try:
        data = baca_dataset()

        print("=" * 50)
        print("ANALISIS LINEAR SEARCH DAN BINARY SEARCH")
        print("=" * 50)
        print("Dataset berhasil dibaca.")
        print("Jumlah buku:", len(data))

        # Menjalankan pengujian ukuran input.
        if len(data) < 10000:
            print(
                "\nPeringatan: jumlah data kurang dari "
                "10.000. Pengujian akan menggunakan "
                "ukuran yang tersedia."
            )

        ukuran_tersedia = [
            n for n in [100, 1000, 10000]
            if n <= len(data)
        ]

        if len(ukuran_tersedia) < 3:
            print(
                "Tidak semua ukuran input dapat diuji "
                "karena jumlah data terbatas."
            )

        uji_performa(data)

        # Memungkinkan pengguna mencari buku sendiri.
        cari_buku(data)

    except FileNotFoundError:
        print(
            f"File {DATASET_FILE} tidak ditemukan. "
            "Pastikan file CSV berada satu folder "
            "dengan main.py."
        )

    except KeyError as error:
        print(
            "Kolom dataset tidak ditemukan:",
            error
        )
        print(
            "Pastikan dataset memiliki kolom "
            "'title' dan 'book_id'."
        )


if __name__ == "__main__":
    main()
