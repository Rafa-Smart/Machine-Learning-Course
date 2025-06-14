# rotasi_kanan([1, 2, 3, 4, 5], 2)
# # Output: [4, 5, 1, 2, 3]
import os
os.system("cls")

a = [1,2,3,4,5]
a.insert(0,9)
print(a)

def rotasi_kanan(data, posisi):
    for i in range(posisi):
        a = data.pop()
        data.insert(0,a)
    print(data)

rotasi_kanan([1, 2, 3, 4, 5], 2)