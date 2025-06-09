# cpntinue, pass , break

# pass -> digunakan sebagai dummy atau ini tidak akan dieksekusi

# angka = 0
# while angka < 5:
#     angka += 1
#     if angka == 3:
#         print("putri aku sayang kamu")
#     print(angka)

# 1. pass
angka = 0
while angka < 5:
    angka += 1
    if angka == 3:
        pass # ini tidak akan melakukan apa apa 
    # pass ini ada tapi tidak akan diimplementasikan
    print(angka)

# 2. continue

sebuah_angka = 0

print(f"angka sekarang --> {sebuah_angka}")

while sebuah_angka < 5:
    sebuah_angka += 1
    print(f"ini adalah angka sekarang --> {sebuah_angka}")
    if sebuah_angka == 3:
        print("nice")
        
    print("hay bro")

print("nice")

while sebuah_angka < 5:
    sebuah_angka += 1
    print(f"ini adalah angka sekarang --> {sebuah_angka}") # aksi 1
    if sebuah_angka == 3:
        print("nice")
        continue # jadi saat kita menaruh continue disini maka 
    # continue ini akan membuat kita melewati aksi ke dua 
    print("hay bro") # aksi 2

print("nice")