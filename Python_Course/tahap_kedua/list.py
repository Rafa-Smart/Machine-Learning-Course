# ----list----
# list adalah kumpulan data menggunakan []

# 1. kumpulan data number
data_angka = [1,2,3]
print(data_angka)

print(30*"=")

# 2. kumpulan data string
data_string = ["rafa","aden","putri"]
print(data_string)

print(30*"=")

# 3. kumpulan data boolean
data_bool = ["True","False","True"]
print(data_bool)

print(30*"=")

# 4. kumpulan data campuran
data_campuran = [1,"bala-bala",2,"cireng","rafa",True,"aden",False]
print(data_campuran)

# 5. cara alternaive bikin list

data_range = range(0,10,2)# ini maksudnya data 1 - 9
# maksud dari 2 ini adalah kita melewati atau melompat 2
print(data_range)

data_list = list(data_range)
# atau bisa juga seperti ini
# data_list = list((range(0,10)))
print(data_list)

# 5. cara buat list for loop, list comprehension
# data_list_pake_for = [i for i in range(0,10)]
# # maksudnya adalah kita memasukan i kedalam (i yang sudah ada di dalam range)
# print(data_list_pake_for**2)
# jika kita mengkuadratkan list didalam for maka tidak bisa 
# oleh karena itu kita memakai for
# ini ada contohnya di bawah


data_list_pake_for = [i**2 for i in range(0,10)]
print(data_list_pake_for)

# 6, buat list pake for pake if
list_pake_for_if = [i for i in range(0,10) if i!= 5]
# ini maksudnya kita menghilangkan 5
print(list_pake_for_if)

# contoh dibawah ini kita ingin menampilkan yang genap saja

list_pake_for_if = [i for i in range(0,10) if i % 2 == 0 ]
print(list_pake_for_if)

# contoh dibawah ini kita ingin menampilkan yang ganjil saja
list_pake_for_if = [i for i in range(0,10) if i % 2 !=0 ]
print(list_pake_for_if)

# contoh dibawah ini kita menampilkan angka ganjil saja
# degan kuadrat
list_pake_for_if = [i**2 for i in range(0,10) if i % 2 !=0 ]
print(list_pake_for_if)