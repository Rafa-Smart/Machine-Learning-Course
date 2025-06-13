# https://chatgpt.com/c/6848d54f-46ac-8009-9f13-17f6461ffe82

# bitwise adalah operasi yang dilakukan pada bit dari suatu bilangan
# Bitwise adalah operasi yang dilakukan langsung pada representasi biner dari bilangan. Python mengizinkan manipulasi bilangan bit-per-bit (binary digit) menggunakan operator bitwise.
# Setiap angka dalam komputer diubah ke bentuk biner (0 dan 1). Operator bitwise bekerja langsung pada bit-bit tersebut.


# AND	    Bitwise AND	    &	a & b	    1 jika kedua bit 1
# OR	    Bitwise OR	    |	`a	        b`
# XOR	    Bitwise XOR	    ^	a ^ b	    1 jika beda
# NOT	    Bitwise NOT	    ~	~a	        Inversi bit (flip 0↔1)
# SHIFT L	Left Shift	    <<	a << n	    Geser bit ke kiri
# SHIFT R	Right Shift	    >>	a >> n	    Geser bit ke kanan

a = 6
b = 3
print("a =", bin(a), "b =", bin(b))

c = a | b  # Bitwise OR
# a = 110
# b = 011
# c = 111 = 7 = 4 + 2 + 1
print("a | b =", bin(c), "=", c)
# dan seterusnya sama seperti itu

print("============")
# shift left
# Geser bit dari angka a ke kiri sebanyak n posisi. Setiap kali geser, nilainya dikali 2.
d = a << 2  # Geser 2 posisi ke kiri
# a itu kan 000000110 => jadi 00011000, jadi 0nya geser ke kiri sebanyak n posisi
# print("a << 2 =", bin(d), "=", d)  # 24 = 16 + 8
print("a << 2 =", format(d, "08b"), "=", d)  # 24 = 16 + 8 sama aja 00011000

print("ini tes aja")
# jadi dari pada pake format mending pake ini 
print(f"{d:08b}") # 00011000
# kesimpulan
# a << 1 = a * 2
# a << 2 = a * 4
# a << n = a * (2^n)

print("+++++++==")
# shift right
# geser bit dari angka a ke kanan sebanyak n posisi, bearti setiap bergeser akan di bagi 2

e = a >> 2
# a itu kan 000000110 => jadi 00000001, jadi 0nya geser ke kanan sebanyak n posisi
# print("a >> 2 =", bin(e), "=", e)  # 1 = 0 + 0 + 1
print("a >> 2 =", format(e, "08b"), "=", e)  # 1 = 0 + 0 + 1

# jadi fungsi format di python itu untuk mengubah bilangan biner ke format biner nilia menjadi string dengan format string tertentu
# Bagian	Arti
# 08b = 
# 0	Tambahkan leading zero jika panjangnya kurang
# 8	Panjang total hasil adalah 8 karakter
# b	Format biner (binary)
# 'b'	Biner	'1010'
# 'o'	Oktal	'12'
# 'x'	Heksadesimal kecil (a-f)	'a'
# 'X'	Heksadesimal besar (A-F)	'A'
# 'd'	Desimal	'10'
# 'f'	Float 6 digit desimal default	'10.000000'
# '.2f'	Float 2 digit desimal	'10.00'
# '>8'	Rata kanan 8 kolom	' 10'
# '<8'	Rata kiri 8 kolom	'10 '
# '^8'	Rata tengah 8 kolom	' 10 '
# '08b'	Biner 8 bit dengan leading zero	'00001010'