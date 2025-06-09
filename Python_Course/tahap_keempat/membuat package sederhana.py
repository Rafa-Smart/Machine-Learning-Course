# import time
# t_start = time.time()
from sains import fisika
# bisa juga yang diatas atau yang dibawah
import sains.matematika

# atau bisa juga gini kalo mau yang lebih spesifik
from sains.fisika import gaya as force


# jadi gini penjelasannya
# sains adalah nama folder / packagenya 
# .matematika adalah nama modul / nama file dari package sains
hasil_tambah = sains.matematika.tambah(1,2,3,4,5,6)
# sains adalah nama folder / packagenya 
# .matematika adalah nama modul / nama file dari package sains
# .tambah adalah nama modul atau fungsi / def dari sebuah file
print(f"hasil tambah dari package adalah = {hasil_tambah}")

# t_end = time.time()
# print(f"ini adalah waktu eksekusi dari programnya = {t_end - t_start}")

gaya = fisika.gaya(90,10)
print(f"gaya adalah = {gaya}")

# ini jika pake yang 
# from sains.fisika import gaya as force

gaya = force(90,10)
print(f"gaya adalah = {gaya}")