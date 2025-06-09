# if and else

# if : kondisi : aksi;
# program selanjutnya


# 1. program if inline
nama = input("siapa nama anda ? ")
if nama == "putri" :
     print("kamu cantikk ")
     print(f"terima kasih {nama}")

print(35*"=")
# 2. program if indentation
if nama == "Rafa":
     print(f"kamu ganteng {nama}")
     print(f"kamu juga keren {nama}")
print(f"terima kasih {nama}")
# yang ada atau masih di tab setelah nulis if maka itu adalah
# masih termasuk bagian dari if
# kalo mau keluar dari kondisi if tinggal di backspase

print(35*"=")
# 3. else statement
if nama == "putri":
     print(f'hai {nama} cantik')
else:
     print("kamu bukan doi !!")
print("ini adalah akhir program")