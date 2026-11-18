from storage.file_handler import read_csv, write_csv


def tampilkan_kolam():
    """
    Mengambil seluruh data kolam dari file CSV.
    """

    data = read_csv("ponds.csv")

    return data


def tambah_kolam(nama_kolam, luas, kapasitas, keterangan=""):
    """
    Menambahkan data kolam baru ke file CSV.
    """

    if nama_kolam == "":
        raise ValueError("Nama kolam tidak boleh kosong.")

    if float(luas) <= 0:
        raise ValueError("Luas kolam harus lebih dari 0.")

    if int(kapasitas) <= 0:
        raise ValueError("Kapasitas kolam harus lebih dari 0.")

    data = read_csv("ponds.csv")

    data_baru = {
        "id_kolam": "KLM" + str(len(data) + 1).zfill(3),
        "nama_kolam": nama_kolam,
        "luas": str(luas),
        "kapasitas": str(kapasitas),
        "keterangan": keterangan
    }

    data.append(data_baru)

    kolom = [
        "id_kolam",
        "nama_kolam",
        "luas",
        "kapasitas",
        "keterangan"
    ]

    return write_csv("ponds.csv", kolom, data)
def ubah_kolam(id_kolam, nama_kolam, luas, kapasitas, keterangan=""):
    """
    Mengubah informasi kolam berdasarkan ID kolam.
    """

    if nama_kolam == "":
        raise ValueError("Nama kolam tidak boleh kosong.")

    if float(luas) <= 0:
        raise ValueError("Luas kolam harus lebih dari 0.")

    if int(kapasitas) <= 0:
        raise ValueError("Kapasitas kolam harus lebih dari 0.")

    data = read_csv("ponds.csv")
    ditemukan = False

    for kolam in data:
        if kolam["id_kolam"] == id_kolam:
            kolam["nama_kolam"] = nama_kolam
            kolam["luas"] = str(luas)
            kolam["kapasitas"] = str(kapasitas)
            kolam["keterangan"] = keterangan
            ditemukan = True

    if ditemukan:
        kolom = [
            "id_kolam", "nama_kolam", "luas",
            "kapasitas", "keterangan"
        ]

        return write_csv("ponds.csv", kolom, data)

    return False
def hapus_kolam(id_kolam):
    """
    Menghapus kolam jika belum memiliki riwayat siklus.
    """

    data_kolam = read_csv("ponds.csv")
    data_siklus = read_csv("cycles.csv")

    for siklus in data_siklus:
        if siklus["id_kolam"] == id_kolam:
            raise ValueError(
                "Kolam tidak dapat dihapus karena memiliki riwayat siklus."
            )

    data_baru = []
    ditemukan = False

    for kolam in data_kolam:
        if kolam["id_kolam"] == id_kolam:
            ditemukan = True
        else:
            data_baru.append(kolam)

    if ditemukan:
        kolom = [
            "id_kolam", "nama_kolam", "luas",
            "kapasitas", "keterangan"
        ]

        return write_csv("ponds.csv", kolom, data_baru)

    return False