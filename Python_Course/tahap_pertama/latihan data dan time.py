# date and time
import datetime as dt
import os
os.system("cls")
# dengan menggunakan from datetime ini akan dapat menyngkat
# pemanggilan modul yang asalnya harus gini
# dt.datetime.today() jadi seperti ini
# dt.today

# dt adalah nama pendek dari datetime
# jadi artinya kita import datetime sebagai dt
# kita juga bisa mengganti panggilan singkatan dari datetime
# selain dt misal hj / klk / apa saja bebas

hari_ini = dt.date.today()
print(hari_ini)
print(f"hari ini adalah hari = {hari_ini:%A}")
# jika kita menggunakan a kecil maka akan didingkat
# tapi jika kita menggunakan A besar maka akan full jawabanya tidak disingkat
lahir = dt.date(2009,5,12)
print(f"hari saat aku lahir adalah hari = {lahir:%A}")
print(lahir)

print(20*"=")
print("SILAHKAN\nMASUKAN TAHUN, BULAN, TANGGAL\n")
tahun = int(input("tahun lahir mu =\t"))
bulan = int(input("bulan lahir mu =\t"))
tanggal = int(input("tanggal lahir mu =\t"))

tanggal_lahir = dt.date(tahun,bulan,tanggal)
print(f"ini adalah tanggal anda = {tanggal_lahir}")
print(f"harinya adalah = {tanggal_lahir:%A}")

# ini hitung umur
saat_ini = dt.date.today()
print(f"hari ini adalah = {saat_ini}")
umur_hari =saat_ini - tanggal_lahir
umur_tahun = umur_hari.days // 365
# maksud dari days adalah memberikan tota hari 
umur_bulan_sisa = (umur_hari.days % 365) // 30
umur_hari_sisa = (umur_bulan_sisa % 30) // 1
print(30*"=")
print(umur_hari)
print(f"umur tahun kamu sekarang adalah = {umur_tahun} tahun\n {umur_bulan_sisa}bulan\n {umur_hari_sisa}hari")



# Hari dalam Minggu

# %a : Nama hari dalam bentuk singkat (contoh: Mon, Tue, Wed)
# %A : Nama hari dalam bentuk panjang (contoh: Monday, Tuesday, Wednesday)
# Bulan dalam Tahun

# %b : Nama bulan dalam bentuk singkat (contoh: Jan, Feb, Mar)
# %B : Nama bulan dalam bentuk panjang (contoh: January, February, March)
# Tanggal dan Waktu

# %d : Hari dalam bulan (01-31)
# %m : Bulan (01-12)
# %y : Tahun tanpa century (00-99)
# %Y : Tahun dengan century (1900-2099)
# %H : Jam (00-23)
# %I : Jam dalam format 12 jam (01-12)
# %M : Menit (00-59)
# %S : Detik (00-59)
# %f : Mikrodetik (000000-999999)
# Waktu Khusus

# %p : AM atau PM (format 12 jam)
# %z : Offset dari UTC (contoh: +0100)
# %Z : Zona waktu (contoh: UTC, EST)
# Format Lain

# %j : Hari dalam tahun (001-366)
# %U : Minggu dalam tahun, minggu pertama dimulai pada minggu pertama bulan Januari (00-53)
# %W : Minggu dalam tahun, minggu pertama dimulai pada Senin pertama bulan Januari (00-53)