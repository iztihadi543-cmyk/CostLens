import unittest
from services.expense_manager import ExpenseManager


class TestPencarian(unittest.TestCase):

    def setUp(self):
        self.manager = ExpenseManager()

        self.manager.data = [
            {
                "id": "1",
                "id_siklus": "S001",
                "nama": "Pakan Lele",
                "kategori": "Pakan",
                "tanggal": "2026-11-18",
                "jumlah": "10",
                "satuan": "kg",
                "harga_satuan": "15000",
                "total": "150000",
                "keterangan": ""
            },
            {
                "id": "2",
                "id_siklus": "S001",
                "nama": "Vitamin Lele",
                "kategori": "Obat",
                "tanggal": "2026-11-18",
                "jumlah": "2",
                "satuan": "botol",
                "harga_satuan": "25000",
                "total": "50000",
                "keterangan": ""
            }
        ]

    def test_cari_berdasarkan_nama(self):
        hasil = self.manager.cari_pengeluaran("pakan")
        self.assertEqual(len(hasil), 1)

    def test_cari_berdasarkan_kategori(self):
        hasil = self.manager.cari_pengeluaran("obat")
        self.assertEqual(len(hasil), 1)

    def test_cari_berdasarkan_id(self):
        hasil = self.manager.cari_pengeluaran("2")
        self.assertEqual(len(hasil), 1)

    def test_data_tidak_ditemukan(self):
        hasil = self.manager.cari_pengeluaran("solar")
        self.assertEqual(len(hasil), 0)


if __name__ == "__main__":
    unittest.main()