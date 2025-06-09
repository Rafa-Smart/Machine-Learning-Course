# nested list adalah list di dalam list


# jadi kita akan membuat list didalam list
# artinya komponen komponen list nya adalah list
# itu sendiri.


data_0 = [1,2]
data_1 = [3,4]
data_list_biasa = [1,2,3,4]
print(f"ini data list biasa = \n{data_list_biasa}")
data_2d = [data_0,data_1]
print(f"ini adalah data list dengan nested = \n{data_2d}")
data_2d = [data_0,data_1,data_list_biasa,6,7]
print(f"ini adalah nested list campuran = \n{data_2d}")

# gunanya menggunakan ini adalah biasanya 
# jika kita menggunakan data yang berseri

# contoh penggunaan
data_peserta_0 = ["raden",25,"laki-laki"]
data_peserta_1 = ["annisa",20,"wanita"]
data_peserta_2 = ["mamah dedeh",56,"wanita"]

list_peserta = [data_peserta_0,data_peserta_1,data_peserta_2]
print(f'ini adalah list peserta = \n {list_peserta}')

# contoh kita akan mengeluarkan data nya

for i in list_peserta:
    print(f"nama\t = {i[0]}")
    print(f"umur\t = {i[1]}")
    print(f"kelamin\t = {i[2]}\n")

# namun masalahnya beberapa operasi tidak bisa digunakan
# untuk nested list salah satunya adalah untuk memory
# atau referens
# cara penyelesaiannya adalah ini

list_copy = list_peserta.copy()
print(f"peserta = \n {list_copy}")
# hasilnya sama
# tapi jika kita ganti nih
data_peserta_0[0] = "ucup"
print(f'ini adalah list yang sebelumnya = \n {list_peserta}')
print(f"ini adalah list yang diganti =\n {list_copy}")

# nah hasilnya di dua dua variable akan berubah
# nah ini akan dibahas dalam episode selanjutnya