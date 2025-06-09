# operasi 

# 1. cara mengambil data dari list

# index 0(-3) | 1(-2) | 2(-1)
data = ["rafa","aden","putri"]
data_0 = data[0]
print(F"data pertama (index 0) --> {data_0}")

data_terakhir = data[-1]
print(f"data terakhir (index -1) --> {data_terakhir}")
# ini misal kita tidak tahu data paling terakhirnya berapa maka
# kita bisa pake -1
print(25*"=")
# 2. cara mengambil info jumlah data dalam list
hitung_data = len(data[0])
print(f"panjang data di (index 0) --> {hitung_data}")

# ini menghitung data keseluruhan yang ada dalam list
hitung_data = len(data)
print(f"jumlah data dalam list --> {hitung_data}")
# ini kenapa outputnya adalah 3 karena kita punya 3 data 
# yang dipisahkan mengguankan koma (,)

print(25*"=")

# 3. menambahkan item pada list sesuai posisi
print(f"data sebelum ditambah --> \n {data}")
data.insert(1,"ghina")
# kita menambahkan ghina di index ke 1 
# setelah si rafa (index ke 0)
print(f"ini adalah data yang sudah ditambah --> \n {data}")

# 4. menambah data langsung di akhir 
data.append("nazwa")
print(f"ini menambah data di akhir --> \n {data}")

# 5. menggabung kan 2 list
# jadi kita butuh data baru

data_baru = ["steak", "ramen", "kebab"]
data.extend(data_baru)
print(f"ini adalah data tambahan --> \n {data}")

# 5. merubah data
# kita ingin mengubah data di index ke 2 yang asalnya aden jadi khadafi
data[2] = "khadafi"
print(f"ini data setelah di rubah --> \n {data}")

# 6. menghapus data dalam list
data.remove("khadafi")
# data.remove("jamal") ini akan error karena data memang
# sudah tidak ada dalam list
print(f"ini data setelah dihapus -->\n {data}")

# 7. menghapus data peling belakang 
data.pop()
print(f"setelah di pop --> \n{data}")

# 8. atau kita juga bisa melihat data yang dihapus menggunakan pop
data_hapus = data.pop(4)
print(f"ini adalah data yang dihapus oleh pop --> \n {data_hapus}")