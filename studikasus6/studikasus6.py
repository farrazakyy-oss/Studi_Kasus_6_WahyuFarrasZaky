import json

path = r"C:\Users\acer\OneDrive\Documents\DDP\studikasus6\inventaris.json"
with open(path, "r", encoding="utf-8") as f:
    data = json.load(f)

while True:
    print("\nSistem Manajemen Inventaris")
    print("1. Tampilkan data barang")
    print("2. Tambah barang baru")
    print("3. Keluar")
    pilihan = input("Pilih menu (1-3): ")

    if pilihan == "1":
        print("\nDaftar Barang")
        for barang in data:
            print(barang["kode"], "|", barang["nama"], "|", barang["stok"], "|", barang["harga"])

    elif pilihan == "2":
        data_baru = {
            "kode": input("Kode barang: "),
            "nama": input("Nama barang: "),
            "stok": int(input("Stok barang: ")),
            "harga": int(input("Harga barang: "))
        }
        data.append(data_baru)

        with open(path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)
        print("Barang baru berhasil ditambahkan.")

    elif pilihan == "3":
        print("Keluar dari program.")
        break

    else:
        print("Pilihan tidak valid, coba lagi.")

