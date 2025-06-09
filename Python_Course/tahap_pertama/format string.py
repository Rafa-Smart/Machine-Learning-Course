# 1. string
# contoh generic
# ini adalh contoh yang ribet
nama = "rafa"
str = "hello " + nama
print(str)

# ini yang simple
nama = "rafa"
# maksud dari f ini adalah format
format_str = f"hello {nama}"
print(format_str)

# 3. boolean
boolean = True
format_str = f"boolean : {boolean}"
print(format_str)

# 2. angka

angka = 2005.5
format_str = f"angka : {angka}"
print(format_str)

# 4. bilangan bulat 
angka = 15.5
format_str = f"bilangan bulat : {angka:.2f}"
# d disini untuk menampilkan bahwa si angka ini adalah biangan bulat
print(format_str)

# 5. bilangan ribuan
angka = 2000
# cara bikin ada koma di depan 2 
print(f"ribuan : {angka:,}")

# 5. jutaan 
angka = 2000000
# cara bikin ada koma di depan 2 
# akan otomatis berkoma
print(f"jutaan : {angka:,}")

# 6. bilangan desimal
angka = 2005.54321
format_str = f"angka desimal : {angka:.2f}"
# fungsi titik nya adalah untuk membedakan dari angka
# 2000. nah disini berhenti jadi titik ini untuk 
# mengoprasikan bilangan dibelakang titik itu maksudnya
print(format_str)

# 7. menampilkan leading zero 
angka = 2000.54321
print(f"desimal nya:{angka:9.2f}")
# maksud dari 9 ini adalah totalnya 9 angka dari depan
# 2000.5432 ini ada 9 angka dari depan
# dan jika lebih maka akan ada temoat yang kosong
angka = 2000.54321
print(f"desimal nya:{angka:08.2f}")
# kita juga bisa menambah kan nilai didepannya 
# menggunakan ini 

# 8. menampilkan tanda + dan -
angka_minus = -15
angka_plus = 10 
print(f"minus : {angka_minus}\nplus : {angka_plus:+d}")
# dikasih d atau apa saja tergantung angka, karena ini 
# angka bulat maka memakai d

# 9. memformat persen
persentase = 0.045
print(f"persen : {persentase:.2%}")

# 10. melakukan operasi aaritmatika didalam kurung kurawal
harga = 10.567
jumlah = 5 
hasil = harga*jumlah
print(f"hasilnya Rp.{hasil:.2f}")

# 11.format angka lain (binary, octal, hexadecimal)
angka = 255
binary = f"binary = {bin(angka)}"
octal = f"octal = {oct(angka)}"
hexadecimal = f"hexadecimal = {hex(angka)}"
print(binary)
print(octal)
print(hexadecimal)