"""
Pengujian algoritma Bubble Sort pada CostLens.
"""

import unittest
from services.expense_manager import ExpenseManager


class TestPengurutan(unittest.TestCase):

    def setUp(self):
        self.manager = ExpenseManager()

        self.manager.data = [
            {
                "id": "1",
                "nama": "Vitamin",
                "kategori": "Obat",
                "tanggal": "2026-11-18",
                "total": "50000"
            },
            {
                "id": "2",
                "nama": "Pakan",
                "kategori": "Pakan",
                "tanggal": "2026-11-16",
                "total": "150000"
            },
            {
                "id": "3",
                "nama": "Benih",
                "kategori": "Benih",
                "tanggal": "2026-11-17",
                "total": "200000"
            }
        ]

    def test_urut_total_terkecil(self):
        hasil = self.manager.urutkan_pengeluaran("total", "asc")

        self.assertEqual(
            [data["total"] for data in hasil],
            ["50000", "150000", "200000"]
        )

    def test_urut_total_terbesar(self):
        hasil = self.manager.urutkan_pengeluaran("total", "desc")

        self.assertEqual(
            [data["total"] for data in hasil],
            ["200000", "150000", "50000"]
        )

    def test_urut_nama(self):
        hasil = self.manager.urutkan_pengeluaran("nama", "asc")

        self.assertEqual(
            [data["nama"] for data in hasil],
            ["Benih", "Pakan", "Vitamin"]
        )

    def test_urut_tanggal(self):
        hasil = self.manager.urutkan_pengeluaran("tanggal", "asc")

        self.assertEqual(
            [data["tanggal"] for data in hasil],
            ["2026-11-16", "2026-11-17", "2026-11-18"]
        )


if __name__ == "__main__":
    unittest.main()