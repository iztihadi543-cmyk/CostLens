import unittest
from services.pond_manager import (
    tambah_kolam,
    tampilkan_kolam,
    ubah_kolam,
    hapus_kolam
)


class TestPond(unittest.TestCase):

    def test_tambah_kolam(self):
        hasil = tambah_kolam(
            "Kolam Uji", 12, 1000, "Kolam terpal"
        )
        self.assertTrue(hasil)

    def test_tampilkan_kolam(self):
        hasil = tampilkan_kolam()
        self.assertIsInstance(hasil, list)

    def test_ubah_kolam(self):
        data = tampilkan_kolam()

        id_kolam = data[0]["id_kolam"]

        hasil = ubah_kolam(
            id_kolam, "Kolam Perubahan", 15, 1200,
            "Kolam sudah diperbarui"
        )

        self.assertTrue(hasil)

    def test_hapus_kolam(self):
        hasil = tambah_kolam(
            "Kolam Hapus", 10, 500, "Data pengujian"
        )

        data = tampilkan_kolam()
        id_kolam = data[-1]["id_kolam"]

        hasil = hapus_kolam(id_kolam)

        self.assertTrue(hasil)

    def test_nama_kolam_kosong(self):
        with self.assertRaises(ValueError):
            tambah_kolam("", 12, 1000)

    def test_luas_kolam_nol(self):
        with self.assertRaises(ValueError):
            tambah_kolam("Kolam Uji", 0, 1000)

    def test_kapasitas_kolam_nol(self):
        with self.assertRaises(ValueError):
            tambah_kolam("Kolam Uji", 12, 0)


if __name__ == "__main__":
    unittest.main()