# https://chatgpt.com/c/684b8f3f-31f4-8009-ade3-5641df78cfac
# 
import os
os.system("cls")

# jadi for loop di python itu untuk mengiterasi objek yang itereble (atau yang bsia di iterasi), cotohnya
# list, tuple, string, dictionary, set, dan lain-lain, atau objek itereble buatan sendiri

# range(stop)
# range(start, stop)
# range(start, stop, step)


# ada beberapa aturan yaitu
# for i in range(10, 0, 1):  # tidak jalan karena step-nya +1, tapi 10 > 0
#     print(i)

# range(1, 10, 0)  # akan error: ValueError: range() arg 3 must not be zero


for i in range(1, 10, 2):
    print(i)

# ohh jadi kalo misalkan range(1,10,2)
# maka artinya setiap perulangan itu ang awalnya 
# 1 maka akan ditambah dengan 2, dan seterusnya sampai ke 10 (tidka termasuk berati akan sampai 9 saja)

print("==========")

for i in range(10, 0, -1):
    print(i)

# artinya adalah setiap perulangna maka yang nilai awalnya adlah 10
# maka otomatis inya di perulangan pertama akan menjadi 10, lalu disetiap
# perulangna nilai inya akan dikurangi 1, dan begitu seterusnya dampai nilai akhirnya 0, dan tidak termasuk 0nya maka akan berhenti pada 1, nah kalo mau nilai 0nya terbawa maka harus 
# untuk nilai akhirnya itu adalah -1

# dan rnage ini akna menghaislkan sebuah objek [10,9,8,7,6,5,4,3,2,1] kalo stepnya -1
# dan range ini akan menghasilkan sebuah objek [1,2,3,4,5,6,7,8,9,10] kalo stepnya 1 (default)

# jadi sebenarnya range itu adalah sebuah class yang akan menghasilkan sebuah objek yang itereble

print("ini data range")
r = range(1, 10, 2)

print(r[0])       # 1
print(r[-1])      # 9
print(len(r))     # 5 (karena ada 1, 3, 5, 7, 9)
print(5 in r)     # True
print(list(r))    # [1, 3, 5, 7, 9]


# nah ini adalah metode slicing di python

print("========================")

# jadi [stepAwal:stepAkhir:Lewatan]

# ini penting nih, jadi kalo slicing itu, stepAkhirnya juga akan terambil

objekRange1 = range(1,11)
print(objekRange1)  # ini akan menghasilkan objek range(1, 11)
# jadi harus di konvesikan dulu ke list
print(list(objekRange1)) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# jadi ketika kita sclicing dari sbeuah objek range maka kita itu seperti membuat objek range baru yang sesuai dengna metode slicingnya, ocntoh

slicing1 = objekRange1[5:] # berati kita mengambil data range dari index ke 5 sampai akhir
print(list(slicing1)) # [6, 7, 8, 9, 10]

print("percobaan".center(10,"="))
print(f"mengambil index ke 5 sampai ke 7 \n{list(objekRange1[5:7])}") # [6, 7]
# disini index ke 0nya itu adalah 1
print(f"mengambil index ke 0 sampai ke 7 \n{list(objekRange1[:7])}") 
print(f"mengambil index ke 0 sampai ke 7 tapi di tambah 2 setiap perulangan \n{list(objekRange1[:7:2])}") 
print(f"mengambil index ke 0 sampai ke akhir (tanpa di setting (murni dari yg awal)) tapi di tambah 2 setiap perulangan \n{list(objekRange1[::3])}")  # [1, 4, 7, 10]

print("percobaan".center(10,"="))

print(f"id objek range asli {id(objekRange1)}")
print(f"id objek range slicing1 {id(slicing1)}")
# ini hasilnya akan berbeda karena ketika kita slicing maka akan menghaislkan objek range baru

print("========")

# oke ini adalah isi dari class range
class range:
    def __init__(self, start, stop=None, step=1):

        # nah disini kita cek kalo misalkan
        # si range nya itu di settingnya range(10),
        # maka stopnyakan otomatis 0 dan stepnya juga sudah defaulnya 1,
        # maka stopnya jadi si 10 dan startnya jadi 0
        # jadi range(0,10,1)
        if stop is None:
            stop = start
            start = 0

        if step == 0:
            raise ValueError("range() arg 3 must not be zero")

        self.start = start
        self.stop = stop
        self.step = step
        self._length = self._calculate_length()

    def _calculate_length(self):
        # ini adlaah jika salah maka akan return 0
        if (self.step > 0 and self.start >= self.stop) or (self.step < 0 and self.start <= self.stop):
            return 0
        return ((abs(self.stop - self.start) + abs(self.step) - 1) // abs(self.step))

    def __len__(self):
        return self._length

    def __getitem__(self, index):
        if isinstance(index, slice):
            return self._slice(index)
        if index < 0:
            index += len(self)
        if index < 0 or index >= len(self):
            raise IndexError("range object index out of range")
        return self.start + index * self.step

    def _slice(self, s):
        start, stop, step = s.indices(len(self))
        new_start = self[start]
        new_stop = self[stop] if stop < len(self) else self.stop
        new_step = self.step * step
        # nih lihat kao kita slicing itu akan menghaislkan objek range baru
        return range(new_start, new_stop, new_step)

    def __iter__(self):
        i = 0
        while i < len(self):
            yield self[i]
            i += 1

    def __contains__(self, item):
        if self.step > 0:
            if item < self.start or item >= self.stop:
                return False
        else:
            if item > self.start or item <= self.stop:
                return False
        return (item - self.start) % self.step == 0



# kalo kita pake __namavariable__, maka akan dipanggil langsung oleh si pythonnya, ketika kamu melakukan sesuatu
# misal __len__, nah fungis ini akan langusng di panggil ketika kita mengakses len pada objek instancenya mi

# nih 
# Nama	Fungsi
# __init__	        Dipanggil saat objek dibuat (constructor)
# __str__	        Mengatur tampilan objek saat dicetak dengan print()
# __repr__	        Representasi resmi objek untuk debugging
# __len__	        Mengembalikan panjang objek (dipanggil oleh len(obj))
# __getitem__	    Mengatur akses seperti obj[index]
# __setitem__	    Mengatur penugasan seperti obj[index] = value
# __iter__	        Menjadikan objek bisa diiterasi dalam for
# __next__	        Untuk pengulangan manual dengan next()
# __contains__	    Untuk in, misal: 3 in obj
# __name__	        Digunakan untuk mengetahui nama modul/file Python
# __main__	        Nama khusus saat script dijalankan langsung (bukan diimpor)



# Nama dengan pola __nama__ adalah "reserved" → Python sudah menetapkannya dengan fungsi khusus.

# Jadi jangan membuat sendiri nama seperti __data__ atau __mycode__ kecuali tahu fungsinya, karena bisa bentrok dengan sistem Python.



# ➡️ Fungsi itu akan masuk ke class object (bukan ke objek instancenya langsung).

# 🔹 Penjelasan:
# Misal:
# class Person:
#     def greet(self):
#         print("Hello!")

# p = Person()
# Fungsi greet disimpan di dalam class Person, bukan di objek p.

# Saat kamu memanggil p.greet(), Python akan mencari ke class-nya (Person) dan menjalankan greet() dengan argumen self mengarah ke p.

# 🔍 Ilustrasi (di balik layar):
# Python akan melakukan semacam pencarian seperti ini:
# p.greet() ⟶ Person.greet(p)

# karena mengakses Person.greet(p = (yang sebenarnya adlaha self) lihat di class person)


# 📚 Di Mana Letaknya Secara Teknis?
# Fungsi-fungsi class disimpan di:

# Person.__dict__  # berisi semua metode/fungsi/atribut class


# print(Person.__dict__)
# # Akan menampilkan bahwa 'greet' ada di class, bukan di instance



# print(p.__dict__)
# # Tidak ada 'greet' di sini karena hanya berisi data (atribut) spesifik instance