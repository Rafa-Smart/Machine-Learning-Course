# latihan bikin segitiga

# 1. ini adalah for

# sisi = 10
# # ini adalah dummy
# count = 1
# for i in range(sisi):
#     print("*"*count)
#     count += 1

# 2. ini adalah while

 
print(10*"="+"BIASA"+10*"=")

data = 10

hitung = 0
while True:
    print("*"*hitung)
    hitung += 1
    if hitung > data:
        break
print("sudah")

print(30*"=")

# 3. hanya ganjil saja 
data = 10
print(10*"="+"GANJIL"+10*"=")

hitung = 0
while True:
    # akan kembali keatas perulangannya jika ganjil
    if  hitung  % 2 :
        print("*"*hitung)
        hitung += 1
    else:
        # maksud dari else ini adalah jika hasil nya genap maka akan
        # cuma ditmabahkan 1 saja tanpa dieksekusi apapun
        hitung += 1
        continue
    # dan ini akan mencetak jika genap

    # ini akan break hitung melebihi data
    if hitung > data:
        break
print("yang ini hanya ganjil saja ")

print(10*"="+"GENAP"+10*"=")
no = 10
dummy = 1
while True:
    if  dummy % 2 == 0 and dummy != 0:
        print("*"*dummy)
    dummy += 1
    if  dummy > no:
        break

print("ini adalah contoh segitiga sama kaki ganjil")
data = 10
spasi = int(data/2)
hitung = 0
while True:
    if  hitung  % 2 :
        print(" "*spasi,"*"*hitung)
        hitung += 1
        spasi -= 1
    else:
        hitung += 1
        continue
    if hitung > data:
        break



print(10*"="+"buat segitiga sama kaki genap"+10*"=")
sisi = 10
spasi = int(sisi/2)
dummy = 0
while True:
    if  dummy % 2 == 0 and dummy != 0:
        print(" "*spasi,"*"*dummy)
        dummy += 1
        spasi -= 1
    else:
        dummy += 1

    if  dummy > sisi:
        break



print(20*"=")

no_hp = 15
misal = 0

while True:
    if misal % 2 :
        print("*"*misal)
        misal += 1
    else:
        misal += 1 
        continue
    if misal > no_hp:
        break
print("ini adalah segitiga biasa")

print(20*"*")

no_hp_2 = 16
misal_2 = 0
spasi_2 = int(no_hp_2/2)
while True:
    if misal_2 % 2 == 0 and misal_2 != 0:
        print(" "*spasi_2,"*"*misal_2)
        misal_2 += 1
        spasi_2 -= 1
    else:
        misal_2 += 1
        continue
    if misal_2 > no_hp_2:
        break
print("ini adalah segitiga sama kaki (genap)")


print(20*"*")

a = 10
b = 0
c = int(a/2) 
while True:
    if a % 2 :
        print(" "*c,"*"*a)
        a -= 1
        c += 1
    else:
        a -= 1
        continue
    if b > a:
        break
print("ini adalah segitiga terbalik")

# Inisialisasi:

# data diatur ke 10. Ini adalah nilai batas yang akan digunakan untuk menghentikan perulangan.
# hitung diatur ke 0. Ini adalah variabel yang akan kita gunakan dalam perulangan untuk menentukan apakah kita akan mencetak atau tidak.
# Perulangan (while True):

# while True adalah perulangan tanpa henti yang hanya akan berhenti jika kita menggunakan break.
# Di dalam perulangan:

# Jika hitung % 2 benar (ganjil):
# hitung % 2 adalah operasi modulus yang memeriksa sisa bagi dari hitung ketika dibagi 2. Jika hitung ganjil, hasilnya adalah 1 (benar). Jika genap, hasilnya adalah 0 (salah).
# Jika hitung ganjil, maka print("*"*hitung) akan mencetak string yang terdiri dari hitung jumlah bintang (*).
# Kemudian hitung bertambah 1.
# Jika hitung genap:
# else akan dipicu. Dalam kasus ini, hanya hitung yang akan ditambah 1, dan continue akan mengarahkan kembali ke atas perulangan tanpa melakukan tindakan tambahan.
# Pengecekan if hitung > data:
# Setelah memproses jika hitung ganjil, kita memeriksa apakah hitung sudah lebih besar dari data (10). Jika ya, maka break akan menghentikan perulangan.
# Kapan perulangan berhenti?

# Ketika hitung melebihi data (10), maka perulangan akan berhenti karena perintah break dieksekusi.
# Mari kita lihat langkah demi langkah eksekusi:

# Iterasi 1:

# hitung = 0 (genap)
# hitung bertambah 1, jadi hitung menjadi 1.
# continue mengarah kembali ke atas perulangan.
# Iterasi 2:

# hitung = 1 (ganjil)
# Mencetak * (1 bintang)
# hitung bertambah 1, jadi hitung menjadi 2.
# Mengecek apakah hitung > 10 (tidak, jadi melanjutkan perulangan).
# Iterasi 3:

# hitung = 2 (genap)
# hitung bertambah 1, jadi hitung menjadi 3.
# continue mengarah kembali ke atas perulangan.
# Iterasi 4:

# hitung = 3 (ganjil)
# Mencetak *** (3 bintang)
# hitung bertambah 1, jadi hitung menjadi 4.
# Mengecek apakah hitung > 10 (tidak, jadi melanjutkan perulangan).
# Iterasi 5:

# hitung = 4 (genap)
# hitung bertambah 1, jadi hitung menjadi 5.
# continue mengarah kembali ke atas perulangan.
# Iterasi 6:

# hitung = 5 (ganjil)
# Mencetak ***** (5 bintang)
# hitung bertambah 1, jadi hitung menjadi 6.
# Mengecek apakah hitung > 10 (tidak, jadi melanjutkan perulangan).
# Iterasi 7:

# hitung = 6 (genap)
# hitung bertambah 1, jadi hitung menjadi 7.
# continue mengarah kembali ke atas perulangan.
# Iterasi 8:

# hitung = 7 (ganjil)
# Mencetak ******* (7 bintang)
# hitung bertambah 1, jadi hitung menjadi 8.
# Mengecek apakah hitung > 10 (tidak, jadi melanjutkan perulangan).
# Iterasi 9:

# hitung = 8 (genap)
# hitung bertambah 1, jadi hitung menjadi 9.
# continue mengarah kembali ke atas perulangan.
# Iterasi 10:

# hitung = 9 (ganjil)
# Mencetak ********* (9 bintang)
# hitung bertambah 1, jadi hitung menjadi 10.
# Mengecek apakah hitung > 10 (tidak, jadi melanjutkan perulangan).
# Iterasi 11:

# hitung = 10 (genap)
# hitung bertambah 1, jadi hitung menjadi 11.
# continue mengarah kembali ke atas perulangan.
# Pada pengecekan if hitung > data, hitung adalah 11, yang lebih besar dari 10, sehingga break dieksekusi.
# Perulangan berhenti dan program selesai.

# Kesimpulan:
# Program ini mencetak barisan bintang dengan panjang ganjil (1, 3, 5, 7, 9) dan berhenti ketika panjang bintang melebihi batas yang ditentukan (data), yaitu 10.