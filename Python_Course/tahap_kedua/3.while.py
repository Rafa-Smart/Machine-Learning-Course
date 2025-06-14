import os
os.system("cls")

# i = 0
# while i < 10:
#     i+=1
#     print("*"*i)

# segitiga biasa

i = 0
tinggi = 10
tinggi2 = 10
while tinggi > i:
    tinggi-=1
    print(" "*tinggi,end="")
    j=0
    while j < (tinggi2 - tinggi)*2-1 :
        j+=1
        print("*",end="")
    print()





i2 = 0
tinggi2 = 10
tinggi22 = 10
while i2 < tinggi2:
    i2+=1
    print(" "*i2,end="")
    j2=0
    while j2 < (tinggi22-i2) * 2 - 1 :
        j2+=1
        print("*",end="")
    print()