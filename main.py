from services.expense_manager import ExpenseManager

manager = ExpenseManager()

data = manager.tampilkan_pengeluaran()

print("DAFTAR PENGELUARAN COSTLENS")
print("===========================")

for pengeluaran in data:
    print("ID:", pengeluaran["id"])
    print("Nama:", pengeluaran["nama"])
    print("Kategori:", pengeluaran["kategori"])
    print("Tanggal:", pengeluaran["tanggal"])
    print("Total:", pengeluaran["total"])
    print("---------------------------")