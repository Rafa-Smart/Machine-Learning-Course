# 1. merubah case dari string
# upper / besar
nama = "rafa khadafi"
nama = nama.upper()
print("normal : " + nama)
# lower / kecil
alay = "AKU KECE ABIEZZ"
alay = alay.lower()
print("lower: " + alay )

# 2. pengecekan menggunakan isx method
# contoh untuk pengecekan lower case
salam = "hay bro"
# lalu kita mau ngecek apakah hey bro ini lower case semua apa
# enggak
apakah_lower = salam.islower()
print(salam + " " + str(apakah_lower))
# ini kenapa ditambah str karena 
# Menggabungkan string dengan hasil boolean yang diubah menjadi string
# karena saat variable apakah_lower kita is kan maka 
# hasil ini pasti akan boolean mangkanya
# saat di print kita ubah dulu tipedata di apakah_lower yang
# tadinya adalah bool menjadi str

print(20*"=")
# contoh pengecekan upper
apakah_upper = salam.isupper()
print(salam + " " + str(apakah_upper))

# 3. isalpha9 untuk mengecek apakah semuanya adalah huruf dan tidak kosong

# 4. isalnum() untuk mengecek apakah ada huruf dan angka
# biasanya kegunaan isalnum ini untuk mengecek password yang meggunakan huruf dan angka
print(20*"=")
kamu = "rafa12"
hasil = kamu.isalnum()
print(kamu + " " + str(hasil))

# 5. isdecimal() untuk mengecek angka saja
# 6. isspasi() untuk mengecek apakah ada huruf kosong seperti spasi,tab,newline
# 7 istitle( untuk mengecek apakah semua huruf awalnya dimulai dengan huruf besar)

# 8. mengecek komponen starswith() endswith()
# cara dibawah ini bida bikin mudah
cek_start = "rafa khadafi".startswith("rafa")
print("start = " + str(cek_start))
# ini untuk mengecek apakah string ini startnya menggunakan 
# kata atau string rafa

# 8. penggabungan komponen join() split()

# maksudnya adalah join adalah emnggabungkan 
# dan spilit adalah memisahkan
pisah = ['aku','sayang','kamu']
gabungan = ','.join(pisah)
print(pisah)
print(gabungan)
# maksud dari ',' ini adalah kita ingin menggabungkan kata aku sayang kamu 
# dengan menggunakan , jadi aku,sayang,kamu 
# kita bisa juga dengan menggunakan spasi
gabungan = ' '.join(pisah)
print(gabungan)

gabungan = ' ehm '.join(pisah)
print(gabungan)

print(20*"=")
# 9. memisahkan data
gabungan = "kamuehmsayangehmaku"
print(gabungan)
# contoh menggunakan split
gabungan = "kamuehmsayangehmaku".split('ehm')
print(gabungan)

# 10. alokasi karakter rjust(), ljust ,center()
print(20*"=" + "data" + 20*"=")

kanan = "data".rjust(10)
print("'"+kanan+"'")

kiri = "data".ljust(10)
print("'"+kiri+"'")

tengah = "data".center(10)
print("'"+tengah+"'")

# bisa juga begini
tengah = "data".center(20,"-")
print("'"+tengah+"'")
print("====================")
# 11. kebalikannya yaitu strip()
# atau maksudnya adalah menghilangkan
tengah = tengah.strip("-")
print("'"+tengah+"'")