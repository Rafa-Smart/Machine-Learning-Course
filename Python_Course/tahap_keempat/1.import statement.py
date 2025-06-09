# import 

# import ini sangat penting yaitu adalah library yang sudah
# dibuat oleh orang programnya

# kegunaan import:

# 1.mengambil program dari file external .py
# atau menyambung program dari external
# jadi gini misal kita buat lagi file baru yang namanya adalah
# program 0.program_print.py 
# kemudian kita ingin panggil programnya dnegan cara import
import program_print
# liat outputnya

# 2.import dengan data
import variable_data
import putri
# lalu jika ingin mengaksesnya 
# jika :
# print(data) 
# maka ini akan error not defined
# jadi gini saat kita import maka data ini akan
# masuk ke variable_data jadi
# data ada di name space variable_data

# maka cara aksesnya adalah:
print(variable_data.data)
print(putri.wanita)

# 3.import dengan fungsi
import matematika
hasil = matematika.tambah(4,6)
