# Studi_Kasus_6_WahyuFarrasZaky

## Penjelasan Kode Program

program ini adalah sistem inventaris sederhana, data barang disimpan di json agar tidak hilang saat program ditutup.

<img width="637" height="97" alt="Screenshot 2026-10-07 224439" src="https://github.com/user-attachments/assets/57da0397-ccc0-4769-ac68-48b0a2fffdb2" />

baris 1 import json agar program bisa berjalan

baris 3 adalah letak file json

baris 4 berfungsi untuk membuka file dalam mode "r" atau read

baris 5 mengubah isi file json menjadi list python dan menyimpannya di variabel data, isinya list berisi dictionary

<img width="402" height="117" alt="Screenshot 2026-10-07 224459" src="https://github.com/user-attachments/assets/c4993cc0-88c8-4773-a3b5-1bee01d5bd2b" />

kode untuk tampilan menu saat menjalankan program, while True digunakan sebagai pengulangan

<img width="836" height="82" alt="Screenshot 2026-10-07 224511" src="https://github.com/user-attachments/assets/89a97ac5-31e9-40d8-ae69-c014b29f3fff" />

if pilihan == 1 memastikan apakah user memilih 1

for barang in data mengulang untuk setiap dictionary di list data

baris 17 mencetak isi barang berdasarkan key nya

<img width="500" height="237" alt="Screenshot 2026-10-07 230430" src="https://github.com/user-attachments/assets/2be1657f-e0c1-47a2-89af-063467088534" />

elif pilihan == 2 berjalan jika user memilih 2

baris 20-25 membuat dictionary data_baru yang berisi satu barang.

data.append(data_baru) menambah barang baru ke akhir list data

baris 29 membuka file dalam mode "w" atau write

json.dump(data, f, indent=4) menulis data ke file json

<img width="450" height="118" alt="Screenshot 2026-10-07 224544" src="https://github.com/user-attachments/assets/acd06cd0-5973-47fb-957c-b9d62066c643" />

baris 32-34 berfungsi untuk menghentikan program, jika user memilih 3, program mencetak pesan dan menjalankan break. Break menghentikan while True jadi program berhenti.

else bertugas untuk memastikan bahwa pilihan user harus dari 1-3, jadi jika user memilih angka selain 1-3, maka program akan mencetak pesan lalu while mengulang program dan menunya muncul kembali.

## Output Program

<img width="388" height="167" alt="Screenshot 2026-10-07 224613" src="https://github.com/user-attachments/assets/b1a1ef5a-818a-423e-aa0d-ea6a8c4ce753" />

ini adalah output jika user memilih pilihan 1, program akan menampilkan data yang telah ditambahkan user dari json.

<img width="290" height="185" alt="Screenshot 2026-10-07 224600" src="https://github.com/user-attachments/assets/db111f30-436f-4a39-96d1-a603ad47449c" />

tampilan jika user memilih pilihan 2, pertama user diminta untuk menginput kode, nama, stok dan harga sebelum data barang yang baru bisa dimasukkan kedalam json.

<img width="352" height="132" alt="Screenshot 2026-10-07 224622" src="https://github.com/user-attachments/assets/b145a46c-bfe8-42de-8990-b601fa78fe67" />

tampilan jika user memilih 3, program akan otomatis berhenti.

<img width="416" height="277" alt="Screenshot 2026-10-07 231920" src="https://github.com/user-attachments/assets/c717fe99-5645-44b6-9a57-1bfa62d55e58" />

adapula tampilan isi file json sebagai penyimpanan data program.
