# perulangan / looping

# jadi looping ini akan bekerja jika kondisi nya true

# for kondisi:
#   aksi

# maksudnya adalah untuk semua i yang ada di rentang 5
# atau semua angka di 5 akan dikasih i
# for i in range(5); 



# 1. ini adalah for dengan list
nomor = [0,1,2,3,4] # ini adalah list
print(nomor)
# maksud di bawah ini adalah i ini adalah berada di dalam
# atau in variable nomor
# maka i ini akan berulang misal, i akan jadi 1 
# i akan jadi 2 , i akan jadi 3 ....
for i in nomor:
    print(f"i sekarang -> {i}")  
else:
    print("ini adalah akhir dari program")

# ini apalah penjelasan 
# for i in nomor:
# maksudnya adalah untuk i didalam variable nomor 
# print({i}) maka i akan mencetak angka pertama dari variable yaitu 0
# setelah itu karena masih true maka i akan mencetak ulang amgka ke dua yaitu 1
# dan seterusnya sampai nilai dari variable habis semua dicetak



# 2. ini for dengan range
for_range = range(1,5) # 5 ini ujung nya atau 5 nya tidak akan di tampilkan
for i in for_range:
    print(f"i sekarang -> {i}")  
else:
    print("ini adalah akhir dari program")

test = range(3)
for i in test:
    print("putri, kamu itu wanita cantik")


print(20*"=")

# 3 ini menggunakan string
data_str = 'saya ganteng abiiezz'
for huruf in data_str:
    print(huruf)
# yang ini maksud nya kita bisa melooping per huruf yang ada di variablenya
