# https://chatgpt.com/c/684ed22e-5d54-8009-bc22-fe7c093f7ca0

import os
os.system("cls")

# set adalah kumpulan elemen yang tidak berurutan, tidak bisa diindeks, dan tidak memiliki elemen duplikat.
# Mirip dengan himpunan dalam matematika.

data = {1,1,1,1,2,3,4,5}
print(data) # {1, 2, 3, 4, 5} // tidak bsia duplikat

# Hashable = Hanya elemen yang immutable bisa dimasukkan // yg tidak bisa di ubah
# constohnya adalah string, integer, float, boolean, tuple, dan lain-lain.

# 1. cara membuat set
data = set([1,2,3,4,3,2,1]) # {1, 2, 3, 4}
print(data)

data = set("Rafa Khadafi")
print(data) # {'K', 'h', 'R', 'i', 'd', 'f', 'a', ' '} ga urutan


print("=============")
s = {1, 2}
print(s)  # {1, 2}
s.add(3)
print(s)  # {1, 2, 3}
s.remove(2)  # Akan error jika elemen tidak ada
print(s)  # {1, 3}
s.discard(10)    # Tidak error walaupun elemen tidak ada
s.pop()          # Menghapus elemen acak
print(s)  # {3}
s.clear()  
print(s)  # {}
print("=============")

# 2. operasi himpunan pada set


# 1. union / gabungan  jadi meggabungkan 2 set  tanpa duplikat

a = {1,2,3}
b = {4,5,6}
print(a | b) # bis pake ini atau itu {1, 2, 3, 4, 5, 6}
print(a.union(b)) # {1, 2, 3, 4, 5, 6}


print("=============")

# 3. Intersection (Irisan)
# Intersection adalah operasi himpunan yang digunakan untuk mengambil elemen yang sama (elemen yang terdapat di semua set yang dibandingkan).

a = {12,3,4,5,2}
b = {12,3,4,5,2,6,2}
c = {12,3,4,5,2,1,2,3}
d = {12,3,4,5,2,8,9,0}
e = a.intersection(b,c,d)
print(e) # {2, 3, 4, 5, 12}
print(a & b) # {2, 3, 4, 5, 12}

teman_aldi = {"Budi", "Citra", "Doni", "Eva"}
teman_bela = {"Citra", "Eva", "Gilang", "Hari"}

teman_bersama = teman_aldi & teman_bela
print("Teman bersama mereka adalah:", teman_bersama)
# Output: {'Citra', 'Eva'}


print("============")
# 4. difference / selisih atau perbedaan
# Difference (selisih) adalah operasi himpunan untuk mengambil elemen yang hanya ada di set pertama, tetapi tidak ada di set kedua (atau lebih).

a = {1, 2, 3}
b = {2, 3, 4}
c = a - b
print(c) # {1} // karena di himpunan a hanya ada 1 yang berbeda dengan himpunan lain

x = {1, 2, 3, 4, 5}
y = {2, 4}
z = {3}

hasil = x.difference(y, z)
print(hasil)  # Output: {1, 5}

print("============")

# 5. syimmetryc difference

# Symmetric Difference adalah operasi himpunan yang mengambil semua elemen yang tidak sama — yaitu:
# Elemen yang hanya ada di satu set saja, bukan di keduanya.

# jdai ngambil yang bedanya aja / atau untuk mencari elemen unik dari kedua set atau himpunan sama kayak pake set


a = {1, 2, 3}
b = {3, 4, 5}

hasil = a.difference(b)

print(f"hasil difference {hasil}")  # Output: {1}

a = {1, 2, 3}
b = {3, 4, 5}

hasil = a.symmetric_difference(b)
hasil2 = a ^ b
print(f"hasil symmetric_difference {hasil2}")  # Output: {1, 2, 4, 5}
print(f"hasil symmetric_difference {hasil}")  # Output: {1, 2, 4, 5}



# bedanya dengan difference biasa adalah kalo yang biasa itu hanya mengambil yang beda dari satu setnya saja yaitu yang di cek

# tapi aklo yang simetrik ini mengambil yang beda dari seluruh himpunannya

print("============")






# difference

# Fungsi: Mengembalikan set baru yang berisi perbedaan antara dua set (elemen yang ada di set pertama tapi tidak ada di set kedua)
# Sifat: Non-mutating (tidak mengubah set asli)
# Return value: Set baru
# Sintaks: set1.difference(set2)

# difference_update

# Fungsi: Memodifikasi set asli dengan menghapus elemen yang ada di set lain
# Sifat: Mutating (mengubah set asli)
# Return value: None (karena mengubah set asli)
# Sintaks: set1.difference_update(set2)



# pelajari lagi yang ada di chat gpt nya 
# https://chatgpt.com/c/684ed570-0140-8009-b765-0f5569125d5e