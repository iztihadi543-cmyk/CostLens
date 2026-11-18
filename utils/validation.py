"""
Modul untuk memvalidasi data yang dimasukkan ke CostLens.
"""


def validasi_pengeluaran(nama, tanggal, jumlah, harga_satuan):
    """
    Memeriksa kelengkapan dan kebenaran data pengeluaran.
    """

    if nama == "":
        raise ValueError("Nama pengeluaran tidak boleh kosong.")

    if tanggal == "":
        raise ValueError("Tanggal pengeluaran harus diisi.")

    if float(jumlah) <= 0:
        raise ValueError("Jumlah harus lebih dari 0.")

    if float(harga_satuan) < 0:
        raise ValueError("Harga satuan tidak boleh negatif.")

    return True