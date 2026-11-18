# CostLens
### Catfish Farming Cost Management System

CostLens adalah aplikasi desktop berbasis Python yang dirancang untuk membantu pembudidaya ikan lele skala kecil dalam mencatat, mengelola, dan menganalisis pengeluaran operasional berdasarkan siklus budidaya.

Aplikasi ini bertujuan mempermudah pencatatan biaya seperti pembelian pakan, benih lele, obat-obatan, vitamin, listrik, air, dan kebutuhan operasional lainnya agar pengeluaran dapat dipantau dengan lebih terstruktur.

## Latar Belakang

Dalam kegiatan budidaya ikan lele, pencatatan biaya operasional sering dilakukan secara manual. Hal ini dapat menyebabkan data pengeluaran tersebar, sulit dicari, dan menyulitkan pembudidaya ketika ingin mengetahui total biaya dalam satu siklus budidaya.

CostLens dikembangkan sebagai solusi sederhana untuk membantu mengelola catatan pengeluaran, mengelompokkan biaya berdasarkan siklus budidaya, serta menyajikan informasi pengeluaran secara lebih terorganisasi.

## Fitur Utama

Fitur yang dikembangkan dalam CostLens meliputi:

- **Dashboard:** Menampilkan ringkasan pengeluaran dan jumlah transaksi.
- **Manajemen Kolam:** Mengelola informasi kolam budidaya.
- **Manajemen Siklus:** Mencatat dan mengelola siklus budidaya berdasarkan kolam.
- **Manajemen Pengeluaran:** Menambahkan, mengubah, dan menghapus catatan pengeluaran.
- **Pencarian Data:** Mencari transaksi berdasarkan ID, nama pengeluaran, atau kategori.
- **Pengurutan Data:** Mengurutkan transaksi berdasarkan tanggal, nama, kategori, atau total biaya.
- **Filter Data:** Menyaring pengeluaran berdasarkan kategori dan rentang tanggal atau nominal.
- **Ringkasan Biaya:** Menghitung total pengeluaran berdasarkan siklus budidaya.
- **Penyimpanan CSV:** Menyimpan dan membaca data agar tetap tersedia ketika aplikasi dijalankan kembali.

## Teknologi yang Digunakan

| Teknologi | Kegunaan |
|---|---|
| Python | Bahasa pemrograman utama |
| Tkinter | Pembuatan antarmuka desktop |
| CSV | Penyimpanan data |
| Unittest | Pengujian fungsi program |

CostLens dirancang sebagai aplikasi desktop yang dapat digunakan secara offline.

## Algoritma yang Digunakan

Beberapa algoritma dan konsep pemrograman yang diterapkan:

- **Linear Search:** Mencari data secara berurutan berdasarkan kata kunci.
- **Bubble Sort:** Mengurutkan data transaksi berdasarkan kriteria tertentu.
- **Lambda:** Membantu menentukan kriteria pengurutan data.
- **Args:** Mendukung perhitungan total dari beberapa nilai pengeluaran.
- **Kwargs:** Mendukung penyaringan data berdasarkan beberapa kriteria.

## Struktur Proyek

```text
CostLens/
│
├── main.py
├── README.md
├── .gitignore
│
├── data/
│   ├── ponds.csv
│   ├── cycles.csv
│   └── expenses.csv
│
├── services/
│   ├── __init__.py
│   ├── pond_manager.py
│   ├── cycle_manager.py
│   └── expense_manager.py
│
├── storage/
│   ├── __init__.py
│   └── file_handler.py
│
├── tests/
│   ├── __init__.py
│   ├── test_expense.py
│   ├── test_search.py
│   └── test_sort.py
│
├── ui/
│   ├── __init__.py
│   └── interface.py
│
└── utils/
    ├── __init__.py
    └── validation.py
```

## Format Penyimpanan Data

CostLens menggunakan tiga file CSV utama:

1. `ponds.csv` — Menyimpan informasi kolam.
2. `cycles.csv` — Menyimpan informasi siklus budidaya.
3. `expenses.csv` — Menyimpan catatan pengeluaran operasional.

Perhitungan total pengeluaran menggunakan rumus:

**Total Pengeluaran = Jumlah × Harga Satuan**

## Cara Menjalankan Aplikasi

Pastikan Python sudah terpasang pada komputer.

1. Buka folder proyek CostLens.
2. Buka terminal pada folder tersebut.
3. Jalankan perintah:

```bash
python main.py
```

## Menjalankan Pengujian

CostLens menggunakan modul `unittest` untuk menguji fungsi pengolahan data secara terpisah dari antarmuka aplikasi.

Untuk menjalankan seluruh pengujian:

```bash
python -m unittest discover -s tests -v
```

Untuk menguji validasi pengeluaran secara khusus:

```bash
python -m unittest tests.test_expense -v
```

## Tujuan Pengembangan

CostLens dikembangkan sebagai proyek pembelajaran Pemrograman Terstruktur dengan menerapkan pengelolaan data, pemrosesan tabel, algoritma pencarian dan pengurutan, pengolahan file, modularisasi program, penanganan kesalahan, serta pengujian unit.

---

**CostLens — Manage Costs, Understand Your Cultivation.**