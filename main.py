from storage.file_handler import read_csv, write_csv

# Menguji pembacaan data kolam
data_kolam = read_csv("ponds.csv")
print("Data kolam:", data_kolam)

# Menguji penyimpanan data kolam
kolom = ["id_kolam", "nama_kolam", "luas", "kapasitas", "keterangan"]

data_baru = [
    {
        "id_kolam": "KLM001",
        "nama_kolam": "Kolam A",
        "luas": "12",
        "kapasitas": "1000",
        "keterangan": "Kolam terpal"
    }
]

hasil = write_csv("ponds.csv", kolom, data_baru)
print("Penyimpanan berhasil:", hasil)

# Membaca kembali data yang sudah disimpan
data_kolam = read_csv("ponds.csv")
print("Data setelah disimpan:", data_kolam)
