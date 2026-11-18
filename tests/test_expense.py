"""
Pengujian fungsi validasi pengeluaran.
"""

import unittest
from utils.validation import validasi_pengeluaran


class TestValidasiPengeluaran(unittest.TestCase):

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


if __name__ == "__main__":
    unittest.main()