import os
os.system("cls")

# jadi pass itu
# Menghindari error pada blok yang harus ada isinya secara sintaksis, seperti dalam if, for, def, atau class.
# Digunakan saat ingin menunda implementasi.
# Digunakan saat membuat kerangka awal program.



# contoh dari pass
nilai = 75
if nilai >= 80:
    print("A")
elif nilai >= 60:
    pass  # Belum tentukan nilai C
else:
    print("E")

# nh kalo continue

# continue adalah pernyataan kontrol dalam loop (for atau while) yang melewati sisa iterasi saat ini dan langsung ke iterasi berikutnya.
# 📎 Tujuan continue:
# Menghindari eksekusi baris tertentu jika kondisi tertentu terpenui.
# Digunakan untuk melewatkan sebagian kode dalam loop, tanpa menghentikan seluruh loop.
# 📌 Cara Kerja continue:
# Saat Python bertemu continue, ia tidak melanjutkan ke baris setelahnya dalam loop saat ini, tetapi lompat ke perulangan berikutnya.

# jadi continue itu akna melewati baris program jika kondisi tertentu terpenui


for i in range(1,20,1):
    if i % 2 == 0: # arena i ini adalah genap, dan ketika genap, 
        # maka akan di continue (akan dilewat dan langsung ke atas lagi), jadi print()yang ada dibawah nya tidak akan dijalankan
        continue
    print(f"ini bilangan ganjil saja {i}")

# contoh lagi
teks = "python"
for huruf in teks:
    if huruf == 'h': 
        # jadi ketika perulangannya bertemu dnega huruf h, maka
        # akan dilewat seluruh program dibawahnya), dan langusng ualng lagi ke perulangan awal, jadi si print()yang dibawahnya tidka akan deksekusi
        continue
    print(huruf)

# nilai = 75
# if nilai >= 80:
#     print("A")
# elif nilai >= 60:
#     continue  # ini ga bisa karena continue hanya bisa digunakan di loop
# else:
#     print("E")



# jadi kesimpulannya continue itu akna melewatkan seluruh program dibawahnya dan akan lanjut ke atas lagi
# dan kebalikan dari continue itu adalah break, karena benar benar tidak akan menjalankan seluruh program dibawahnya dan langsung selesai, karena kalo continue itu kan tidak akan menjalankan program dibawahnya dan languang kembali ke atas atau awal.

# jdai untuk mencari bilangan
for i in range(1,20,1):
    if i == 12:
        break
    print(f"ini bilangan {i}")