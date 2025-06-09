print(20*"=")
# 1. menyambung string (concatenate)
nama_pertama = "putri"
nama_tengah = "maulidia"
nama_akhir = "yusuf"

nama_lengkap = nama_pertama +" "+ nama_tengah +" "+ nama_akhir
print(nama_lengkap)

# 2. menghitung panjang dari string
panjang = len(nama_lengkap)
print("panjang dari nama putri adalah" + nama_lengkap + " " + "=",str)

# 3. operator untuk string
# mengecek apakah ada komponen string di string
d = "d"
status = d in nama_lengkap
print(d + " " + "string ada di" + nama_lengkap + "=" + str(status))

# jika kita cari huruf besar akan false karena kata kunci
# in juga membaca huruf upper (besar) atau lower(kecil)
d = "D"
status = d in nama_lengkap
print(d + " " + "string ada di" + nama_lengkap + "=" + str(status))

# atau kita ingin menggunakan sebaliknya yaitu
# mengecek apakah "d" ini tidak ada di nama_lengkap
d = "D"
status = d not in nama_lengkap
print(d + " " + "string ada di" + nama_lengkap + "=" + str(status))
nama = "rafa khadafi"
nama = "rafa" in nama
print(nama)
# mengulang string
print(10*"wk")

# indexing yaitu mengambil data dari string
print("index ke-0 : "  + nama_lengkap[0])
print("index ke-0 : "  + nama_lengkap[6])
print("index ke-(-1) : "  + nama_lengkap[-1]) #jika  (-) maka ngambil
print('index range dari 0 - 5 : ' + nama_lengkap[0:5])
print("index 2,4,6,8,10 : " + nama_lengkap[0:10:2])
# [0:10:2] nah 2 ini adalah berapa jauh lompatannya jadi 2 4 6 8
# nya lewat belakang
# index mulai dari 0


# item paling kecil
print("paling kecil : " + min(nama_lengkap))
# item paling besar
print("paling besar : " + max(nama_lengkap))
# maksudnya nilai paling kecil atau besar adalah mengambil nilai
# dari setiap 1 karakter string misal karakter (a)
# dengan menggunakan ascii_code contoh
ascii_code = ord("y") # ini lagi ambil kode dari y
print("kode dari strng adalah " + str(ascii_code))
# ini kenapa pake str karena kita ingin mengambil / mengubah
# karakter (y) ini ke dalam bentuk string yaitu 
# string dari (y) adalah 32 
# ord  adalah untuk mengambil unic code (kode) dari setiap 
# karakter string
data = 117
print("karakter untuk ascii code dari 117 adalah " + chr(data))
# ini kenapa pake char / chr karena kita mengambil atau mengubah
# nilai 117 ke dalam bentuk string yaitu 117 string nya adalah u
# menjadi satu karakter 

# 4. operator dalam bentuk method
data = "rafa khadafi"
jumlah = data.count("a")# disini kita hitung jumlah a pada onjek data
print("jumlah a pada data : " + str(jumlah) )
# data adalah objek yang ingin kita manipulai dan dengan 
# dan kita ingin memanipulasi dengan menghitung dengan cara 
# menempelkan hal / operator pengubah ke si objek yaitu si data
# menggunakan . / dot maka count ini akan nempel kepada si objek
# dan akan memanipulasi objek