# teknik menduplikat list (yang salah)

a = ["rafa","aden","annisa"]
print(f"a = {a}")
# ini akan sama 
b = a 
print(f"b = {b}")

# kita akan merubah member dari a

a[1] = "putri"
b.sort()
print(f"a = {a}")
print(f"b = {b}")
# jadi apapun yang di rubah disalah satu variable
# maka variable lainnya pun akan ikut berubah

# addres dari kedua list
print(f"addres dari a = {hex(id(a))}")
print(f"addres dari b = {hex(id(b))}")
print(30*"=")
# nah maka kita harus mengkopy data dari a ke b
# agar saat kita mengubah data dari b, maka si a
# tidak akan berubah | dengan cara |

# menduplikat data dengan copy
print("membuat list c dengan a.copy")
c = a.copy()
print(f"ini adalah addres a = {hex(id(a))}")
print(f"ini adalah addres b = {hex(id(b))}")
print(f"ini adalah addres c = {hex(id(c))}")
# lihat addres c sudah berbeda dari addres a dan b

# jadi kita bisa lebih leluasa dalam merubah variable
# c tanpa merubah variable a
c[0] = "ghina"
print(f"ini adalah list a = {a}")
print(f"ini adalah list b = {b}")
print(f"ini adalah list c = {c}")
