import os
os.system("cls")

1. 
data = [1,2,3,4,5,6,7,8,9,10]
data[0:2] = [30, 22]  
print(data) # [30, 22, 3, 4, 5, 6, 7, 8, 9, 10]

# kita bisa menyalin data array dengan baik dengan cara ini

print(data[:]) # [30, 22, 3, 4, 5, 6, 7, 8, 9, 10]
print(data[::2]) # [30, 3, 5, 7, 9]

a = data
print(id(data)) #2265440542912 sama
print(id(a)) # 2265440542912 sama


# ada 2 cra mengcopy yaitu shallow copy dan deepcopy
import copy


# 1.shallow copy 
# nah karena sama maka ketika kita ubah si a, maka si data juga berubah, karena alamat memorinya sama, oleh karena itu
print("=======================")
# in namanya shallow copy yaitu
# Hanya menyalin referensi dari objek asli, bukan objek itu sendiri.
# Jika objek asli berisi objek lain (seperti list dalam list), salinan tersebut masih merujuk ke objek yang sama.

b = data[:]
print(id(data)) # 2166948782272 berbeda
print(id(b)) # 2166950686784 berbeda
print("============")

# dan bisa juga pake ini 
import copy

original = [[1, 2, 3], [4, 5, 6]]
shallow_copy = copy.copy(original)  # atau original.copy() untuk list

# Modifikasi di salinan memengaruhi asli
shallow_copy[0][0] = 99

print(original)     # Output: [[99, 2, 3], [4, 5, 6]] sama 
print(shallow_copy) # Output: [[99, 2, 3], [4, 5, 6]] sama

# jadi si shallow copy ini hanya mengcopy luarannya saja tpai yg nestednya tidak


# 2. cara mengcopy dengan deepcopy
print("===========")


# atau bisa jgua pake modul lain
c = copy.deepcopy(data)
print(id(data)) # 2018349965504 berbeda
print(id(c)) # 2018352891840

print("--------")

# atau bisa juga agar lebih jelas
import copy

original = [[1, 2, 3], [4, 5, 6]]
deep_copy = copy.deepcopy(original)

# Modifikasi di salinan TIDAK memengaruhi asli
deep_copy[0][0] = 99

print(original)   # Output: [[1, 2, 3], [4, 5, 6]]
print(deep_copy)  # Output: [[99, 2, 3], [4, 5, 6]]


print("menyisipkan dan menghapus list")
a = [1,2,3,4,5]
print(a)
b = a.pop(3) # berati mengeluarkan index ke 3, dan mereturn nilai dari index ke 3 yaitu 4, dan ditaro di variable b
print(a)
print(b)
a.insert(0, b)
print(a)
# jadi kita ambil 4 dan kita sisipkan di awal list 

print("mengurutkan data array")
print("========")

def urut(data):
    for i in range(len(data)):
        for j in range(len(data)-1):
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]
    print(f"setelah terurut {data}")

a = [45,76,4,2,3,1,5,2,7,9,6,3,2,46,7,8,9,5,3,10]
print(f"sebelum terurut {a}")
urut(a)
b = [3,6,4,45,33,5,6,7,83,63,45,4,34,5,6,6,1,2,3,4]
# atau bisa juga
print(f"sebelum terurut {b}")
b.sort()
print(f"setelah terurut {b}")
# print(f"sebelum terurut {b.sort()}") in ga bisa akrena sort itu return None, hanya mengubah data b saja jadi ga ada returnnya

# atau bisa juga mengembalikan data baru dan beda alamat menggunakna sorted()

a = [3,4,5,10,7,3,1,2,3,4,5,6,9]
b = sorted(a)
print(a, id(a)) # idnya beda
print(b, id(b))


print("zip in python")
# penting nih

nama = ['A', 'B']
nilai = [80, 90]
gabung = list(zip(nama, nilai))  # [('A', 80), ('B', 90)]

for grade, nilai in gabung:
    print(f"nilai anda {nilai} grade anda {grade}")
    # nilai anda 80 grade anda A
    # nilai anda 90 grade anda B

print("===========")
# contoh lain 
a = "abcdef"
b = list(range(1,5+1)) # karena range itu return objek maka kita casting ke list dahulu
c = list(range(6,10+1))
d = zip(a,b,c)
print(list(d)) # <zip object at 0x0000015D75D66C80 adalah alamat memori di mana objek ini disimpan (setiap eksekusi akan berbeda).

print("========")
zipped = zip([1, 2], ['a', 'b'])
list1 = list(zipped)  # [(1, 'a'), (2, 'b')]
list2 = list(zipped)  # [] (karena iterator sudah habis)

# contoh lagi
zip([1, 2, 3], ['a', 'b'])  # Hanya menghasilkan [(1, 'a'), (2, 'b')]
# Solusi: Gunakan itertools.zip_longest jika ingin menyesuaikan panjang.

# cara mnegunzip
zipped = [(1, 'a'), (2, 'b'), (3, 'c')]
print(zipped)
numbers, letters = zip(*zipped)  # Unzip

print(numbers)  # (1, 2, 3)
print(letters)  # ('a', 'b', 'c')

# jadi kenapa range(1,10), dan zip(), menghasilkan objek dan harus di casting dulu ?, karena ini adalah design dari pyhtonnya untuk meminimkan penggunaan memory, tapi bisa diakses jiga di butuhkan saja misal ketika di for loop, ini akn lazy maka akan di panggil menggunakna method next() (mirip di js)

# jadi kegunaan list itu adalah
# 1. Konversi Iterable ke List (Termasuk Lazy Objects)
# a. Mengubah range, zip, map, dll. menjadi List

# dan objek lazy atau
# (iterator lazy biasanya hanya bisa diiterasi sekali).

# Membuat list dengan 5 elemen None
default_list = list([None] * 5)  # [None, None, None, None, None]

# Alternatif (lebih cepat):
default_list = [None for _ in range(5)]


# conoth lain
data = [[10, 20], [30, 40], [5]]
maksimum = max([max(inner) for inner in data])
