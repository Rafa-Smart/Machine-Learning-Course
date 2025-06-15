import os
os.system("cls")
# # segitiga biasa
# for i in range(0,11,1):
#     print("*"*i)

# print("=========")
# # segitiga terbalik biasa
# for i in range(11,0,-1):
#     print("*"*i)


# print("=============")


# # segitiga sempurna
# tinggi = 11
# for i in range(tinggi):
#     print(" "*(tinggi-i),end="")
#     for j in range(2*i-1):
#         print("*",end="")
#     print()

# print("========================")


# # cara saya
# for i in range(tinggi):
#     print(" "*(tinggi - (tinggi - i)),end="")
#     for j in range(tinggi*2-(2*i)-1):
#         print("*",end="")
#     print()

# print("==================")
# jumlah_baris = 11

# for i in range(jumlah_baris - 1, 0, -1):
#     spasi = jumlah_baris - i
#     print(" " * spasi, end="")
#     for j in range(2 * i - 1):
#         print("*", end="")
#     print()

jumlah_perkalian = int(input("\nMasukkan jumlah perkalian: "))



for i in range(jumlah_perkalian+1):
        print(f" {i} X {jumlah_perkalian} = {i*jumlah_perkalian}")
