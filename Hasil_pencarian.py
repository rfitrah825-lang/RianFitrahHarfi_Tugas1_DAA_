
from buku import Buku

class HasilPencarian:
    def __init__(self, hasil_buku, jumlah_perbandingan, waktu_rata_rata_ms):
        self.hasil_buku = hasil_buku
        self.jumlah_perbandingan = jumlah_perbandingan
        self.waktu_rata_rata_ms = waktu_rata_rata_ms

    def tampilkan(self):
        if self.hasil_buku is None:
            print("Buku tidak ditemukan.")
        else:
            print("Buku ditemukan:", self.hasil_buku)

        print("Jumlah perbandingan:", self.jumlah_perbandingan)
        print("Waktu pencarian:", self.waktu_rata_rata_ms, "ms")
