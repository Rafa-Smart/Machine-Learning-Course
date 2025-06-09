data_angka = [7,4,3,8,5,5,4,3,5,2,4,5,6,5,1,]
print(f"data angka = {data_angka}")

# 1. menghitung data
# jasi kita ingin menghitung bahwa data ini ada di list sampai berapa kali 
jumlah_data_4 = data_angka.count(4)
# maksudnya adalah kita menghitung ada berapa angka 3 dan 4 didalam list
jumlah_data_3 = data_angka.count(3)

print(f"jumlah data 4 dalam list --> {jumlah_data_4}")
print(f"jumlah data 3 dalam list --> {jumlah_data_3}")

# 2. mencari posisi data
data = ["rafa","putri","ghina"]
cari_data = data.index('ghina')
print(f"posisi index dari ghina adalah --> {cari_data}")

# 3. mengurutkan list
print(f"data angka sebelum di urutkan --> \n{data_angka}")
data_angka.sort()
print(f"ini adalah data angka yang sudah di urukan --> \n{data_angka}")

print(f"data sebelum di urutkan --> \n{data}")
data.sort()
print(f"ini adalah data yang sudah di urukan --> \n{data}")
# ini akan diurutkan berdasarkan abjad

# 4. membalik urutan list
print(f"data angka sebelum di dibalik --> \n{data_angka}")
data_angka.reverse()
print(f"ini adalah data angka yang sudah di dibalik --> \n{data_angka}")
# tetapi syarat nya kita harus sort dulu sebelum di reverse