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

    def hitung_total(self, *jumlah_pengeluaran):
        """
        Menghitung total dari beberapa nilai pengeluaran.
        """

        total = 0

        for jumlah in jumlah_pengeluaran:
            total += float(jumlah)

        return total

    def hitung_total_siklus(self, id_siklus):
        """
        Menghitung seluruh pengeluaran berdasarkan ID siklus.
        """

        total = 0

        for pengeluaran in self.data:
            if pengeluaran["id_siklus"] == id_siklus:
                total += float(pengeluaran["total"])

        return total

    def tampilkan_pengeluaran(self):
        """
        Mengembalikan seluruh data pengeluaran.
        """

        return self.data

    def cari_pengeluaran(self, keyword):
        """
        Mencari pengeluaran berdasarkan ID, nama, atau kategori
        menggunakan algoritma Linear Search.
        """

        hasil = []

        keyword = keyword.lower()

        for pengeluaran in self.data:
            if (keyword in pengeluaran["id"].lower()
                or keyword in pengeluaran["nama"].lower()
                or keyword in pengeluaran["kategori"].lower()):

                hasil.append(pengeluaran)

        return hasil

    def urutkan_pengeluaran(self, berdasarkan, urutan="asc"):
        """
        Mengurutkan data menggunakan Bubble Sort dan lambda.
        """

        data = self.data.copy()

        if berdasarkan == "total":
            kunci = lambda item: float(item[berdasarkan])
        else:
            kunci = lambda item: item[berdasarkan].lower()

        for i in range(len(data)):
            for j in range(0, len(data) - i - 1):

                nilai_1 = kunci(data[j])
                nilai_2 = kunci(data[j + 1])

                if urutan == "asc":
                    kondisi = nilai_1 > nilai_2
                else:
                    kondisi = nilai_1 < nilai_2

                if kondisi:
                    data[j], data[j + 1] = data[j + 1], data[j]

        return data