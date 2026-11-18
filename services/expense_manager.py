"""
Modul untuk mengelola data pengeluaran CostLens.
"""

from storage.file_handler import read_csv, write_csv
from utils.validation import validasi_pengeluaran


class ExpenseManager:
    """
    Mengelola penambahan, pembacaan, dan penyimpanan data pengeluaran.
    """

    def __init__(self):
        self.data = read_csv("expenses.csv")

    def tambah_pengeluaran(
        self, id_siklus, nama, kategori, tanggal,
        jumlah, satuan, harga_satuan, keterangan=""
    ):
        """
        Menambahkan satu data pengeluaran baru.
        """

        validasi_pengeluaran(nama, tanggal, jumlah, harga_satuan)

        total = float(jumlah) * float(harga_satuan)

        data_baru = {
            "id": str(len(self.data) + 1),
            "id_siklus": id_siklus,
            "nama": nama,
            "kategori": kategori,
            "tanggal": tanggal,
            "jumlah": str(jumlah),
            "satuan": satuan,
            "harga_satuan": str(harga_satuan),
            "total": str(total),
            "keterangan": keterangan
        }

        self.data.append(data_baru)

        kolom = [
            "id", "id_siklus", "nama", "kategori", "tanggal",
            "jumlah", "satuan", "harga_satuan", "total", "keterangan"
        ]

        return write_csv("expenses.csv", kolom, self.data)