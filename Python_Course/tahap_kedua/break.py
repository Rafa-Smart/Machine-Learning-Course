# break itu biasanya digunakan untuk mencari data, maka apabila
# data sudah ditemukan maka ini akan berhenti atau break karena 
# data yng kita cari sudah didapatkan

# atau kita biasanya memaai break ini saat kita menggunakan
# looping yang terus menerus atau tak hingga
# data = int(input("hitung sampai = "))
# angka = 0
# # bisa gini atau while true:
# while True :
#     angka += 1
#     print(f"count = {angka}")
#     if angka == data:
#         print("nice")
#         break
#     print("oke mantap")
# print("oke cukup")

# for i in range(1,6):
#     for j in range(1, i +1):
#         print(j, end=" ")
#     print()


# for i in range(1,6):
#     print(f"*"*i)
# n = 6
# for i in range(n,0,-1):
#     print("*"*i)
n = 6
for i in range(1,n+1):
    print(f" "*(n-i),end="")
    print("*"*(2*i-1))

# print()
# for i in range(1,n+1):
#     print(" "*i,end='')
#     print("*"*(n-i))
# # for i in range(n,0,-1):
# #     print(f" "*(n-i),end="")
# #     print("*"*(2*i-1))

# n = 6  # Anda bisa mengganti nilai n sesuai kebutuhan

for i in range(1, n + 1):
    print(" " * (i - 1), end="")  # Mencetak spasi
    print("*" * (2 * (n - i + 1) - 1)) 