import unittest
from services.expense_manager import ExpenseManager
from utils.validation import validasi_pengeluaran


class TestExpense(unittest.TestCase):

    # Pengujian validasi
    def test_data_valid(self):
        hasil = validasi_pengeluaran(
            "Pakan Lele", "2026-11-18", 10, 15000
        )
        self.assertTrue(hasil)

    def test_nama_kosong(self):
        with self.assertRaises(ValueError):
            validasi_pengeluaran("", "2026-11-18", 10, 15000)

    def test_tanggal_kosong(self):
        with self.assertRaises(ValueError):
            validasi_pengeluaran("Pakan Lele", "", 10, 15000)

    def test_jumlah_nol(self):
        with self.assertRaises(ValueError):
            validasi_pengeluaran("Pakan Lele", "2026-11-18", 0, 15000)

    def test_harga_negatif(self):
        with self.assertRaises(ValueError):
            validasi_pengeluaran("Pakan Lele", "2026-11-18", 10, -15000)

    # Pengujian filter kategori
    def test_filter_kategori(self):
        manager = ExpenseManager()

        manager.data = [
            {"kategori": "Pakan", "id_siklus": "S001", "total": "150000"},
            {"kategori": "Obat", "id_siklus": "S001", "total": "50000"}
        ]

        hasil = manager.filter_pengeluaran(kategori="Pakan")

        self.assertEqual(len(hasil), 1)
        self.assertEqual(hasil[0]["kategori"], "Pakan")

    # Pengujian filter siklus
    def test_filter_siklus(self):
        manager = ExpenseManager()

        manager.data = [
            {"kategori": "Pakan", "id_siklus": "S001", "total": "150000"},
            {"kategori": "Obat", "id_siklus": "S002", "total": "50000"}
        ]

        hasil = manager.filter_pengeluaran(id_siklus="S001")

        self.assertEqual(len(hasil), 1)

    # Pengujian filter rentang total
    def test_filter_rentang_total(self):
        manager = ExpenseManager()

        manager.data = [
            {"kategori": "Pakan", "id_siklus": "S001", "total": "150000"},
            {"kategori": "Obat", "id_siklus": "S001", "total": "50000"},
            {"kategori": "Benih", "id_siklus": "S001", "total": "250000"}
        ]

        hasil = manager.filter_pengeluaran(
            min_total=50000,
            max_total=200000
        )

        self.assertEqual(len(hasil), 2)


if __name__ == "__main__":
    unittest.main()