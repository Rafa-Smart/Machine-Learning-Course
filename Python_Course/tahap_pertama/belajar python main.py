print("hello")
print("world")
print("hello world")

# ini adalah komen
a = 10 
print(a)
# harus sesuai urutan
# artinya memasukan value 10 ke variable a
# variable adalah temat menyimpan data
panjang = 19
print("nilai panjang = ", panjang)
# artinya sebuah variable boleh lebih dari 1 huruf namun
# tidak boleh beda kata
# atau pke spasi tapi pake 
# saat menggunakan variable jangan angka dulu (10_juta)
x = 5
print("nilai x = ", x)
a = 7
# contoh lagi inderect 
b = a
print("nilai b = ", b)

# tipe data (int)
data_int = 1
print("data = " ,data_int)
print("bertipe = ",type(data_int))

# tipe data dengan koma (float)
data_float = 1.5
print("data =", data_float)
print("bertipe = ",type(data_float))

# tipe data kumpulan  karater string
data_str = "rafa"
print("data =", data_str)
print("bertipe = ",type(data_str))

# tipe data biner true/false(boolean)
data_bool= True
print("data =", data_bool)
print("bertipe = ",type(data_bool))
# tipe data khusus

# bilangan complex
data_complex = complex(5,7)
print("data =", data_complex)
print("bertipe = ",type(data_complex))

# kita bisa mengimport tipe data dari bahasa c
# karena kita butuh 
from ctypes import c_double, c_char, c_long
data_c_double= c_double(3.99)
print("data =", data_c_double )
print("bertipe = ", type(data_c_double))

# casting yaitu merubah satu tipe data ke tipe data yang lain
data_int = 9
print("data = ", data_int, ",type =",type (data_int))
data_float = float(data_int)
print("data = ", data_float, ",type =",type (data_float))
data_str = str(data_int)
print("data = ", data_str, ",type =",type (data_str))
# data bool akan false jika 0 dan akan true jika selain 0
data_bool = bool(data_int)
print("data = ", data_bool, ",type =",type (data_bool))
