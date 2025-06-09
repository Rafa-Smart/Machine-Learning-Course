data_0 = [1,2]
data_1 = [3,4]
data_2d = [data_0,data_1]
data_2d_copy = data_2d.copy()

print(f"data asli = {data_2d}") #nested list
print(f"data copy = {data_2d_copy}")

# mengambil data dari nested list
data = data_2d[0]
print(f'data pertama = {data}')
# hanya mengambil data pertama yang pertamanya
data = data_2d[0][0]
print(f'data pertama = {data}')

# addres semuanya
print(f'addres data asli = \n {hex(id(data_2d))}')
print(f'addres data copy = \n {hex(id(data_2d_copy))}')

print("addres dari member ke 1 =")
print(f'addres data asli = \n {hex(id(data_2d[0]))}')
print(f'addres data copy = \n {hex(id(data_2d_copy[0]))}')

# PEMBERITAHUAN!
# saat kita mengcopy maka yang data asli dan data copy 
# akan berbeda addres
# ---------------------------------------------
# jadi ini tuh saat kita mengcopy nested list maka yang terjadi adalah
# yang ke copy itu adalah luarnya saja namun isi dalamnya
# tetap sama addresnya

# jadi misal 
data_2d[0][1] = 3 # rubah data dalam list
data_2d = [data_0,data_1,10]
data_2d_copy = data_2d.copy()
data_2d[2] = 5 # rubah data bukan list

print(f"data asli = {data_2d}") #nested list
print(f"data copy = {data_2d_copy}")

# baca !!
# karena 10 disini yang kita ganti dengan 5 adalah data yang bukan
# list

# nah kesimpulannya adalah bahwa
# data yang berada dalam list = tidak bisa di copy (tidak bisa diubah addresnya)
# data yang bukan list = bisa di copy (berubah addresnya)
# dengan kata lainnya jika kita mengkopy data hanya memakai copy
# sebenarnya kia hanya mengcopy bagian dasarnya aja
# tetapi jika kita menggunakan deepcopy maka kita sudah mengcopy smpai
# bagian dalam nya juga



# nahh oleh sebab itu kita bakal pake 1 lagi namanya
# adalah deepcopy
# menggunakan import deepcopy

from copy import deepcopy
data_2d = [data_0,data_1,10]
data_2d_deepcopy = deepcopy(data_2d)
data_2d[0][1] = 5
print(f"ini adalah data asli dari nested list {data_2d}")
print(f"ini adalah data deepcopy dari nested list {data_2d_deepcopy}")