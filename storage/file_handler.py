
"""
Modul untuk membaca dan menyimpan data CostLens menggunakan file CSV.
"""

import csv


def read_csv(filename):
    """
    Membaca data dari file CSV dan mengembalikannya dalam bentuk list dictionary.
    """
    file_path = "data/" + filename

    try:
        with open(file_path, mode="r", newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            return list(reader)

    except FileNotFoundError:
        print(f"File {filename} tidak ditemukan.")
        return []

    except (csv.Error, UnicodeDecodeError) as error:
        print(f"Terjadi kesalahan saat membaca {filename}: {error}")
        return []


def write_csv(filename, fieldnames, data):
    """
    Menyimpan data ke file CSV menggunakan nama kolom yang ditentukan.
    """
    file_path = "data/" + filename

    try:
        with open(file_path, mode="w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)

            writer.writeheader()
            writer.writerows(data)

        return True

    except OSError as error:
        print(f"Terjadi kesalahan saat menyimpan {filename}: {error}")
        return False
