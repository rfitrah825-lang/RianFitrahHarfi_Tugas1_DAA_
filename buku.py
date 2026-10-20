"""Model input untuk merepresentasikan satu data buku."""


class Buku:
    """Menyimpan ID, judul, dan penulis sebuah buku."""

    def __init__(self, book_id, title, authors):
        self.book_id = self._sebagai_teks(book_id, "Tidak diketahui")
        self.title = self._sebagai_teks(title, "Judul tidak diketahui")
        self.authors = self._sebagai_teks(authors, "Tidak diketahui")

    @staticmethod
    def _sebagai_teks(nilai, nilai_default):
        """Mengubah nilai atribut menjadi teks yang aman ditampilkan."""
        if nilai is None:
            return nilai_default

        teks = str(nilai).strip()
        if teks == "" or teks.casefold() == "nan" or teks.casefold() == "none":
            return nilai_default

        return teks

    def __str__(self):
        return f"{self.title} — {self.authors} (ID: {self.book_id})"
