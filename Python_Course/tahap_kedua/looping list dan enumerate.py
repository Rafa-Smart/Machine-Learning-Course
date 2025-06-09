# looping dari list

kumpulan_angka = [4,5,6,7,3,5,2,4,6,9,6]
for angka in kumpulan_angka:
# maksudnya angka ini adalah angka yang ada di variable dari kumpulan_angka
    print(f"angka = {angka}")
print(20*"=")

peserta = ["ujang","jamal","otong","udin"]
for nama in peserta:
    print(f"nama = {nama}")

# for loop and range 
# ini adalah cara biasa
kumpulan_angka = [10,5,3,7,9,2]
panjang = len(kumpulan_angka)
for i in range(panjang):
    print(f"angka {i}")

print(20*"=")

# pake while
kumpulan_angka = [10,5,3,7,9,2]
panjang = len(kumpulan_angka)
i = 0 
while i < panjang:
    print(f"angka p = {kumpulan_angka[i]}")
    i += 1


# nah ini kan cara untuk ngelooping nya panjang caranya maka
# ada yang lebih singkat yaitu list comprehesion

print(20*"=")
data = ["rafa",1,2,3,"putri"]
[print(f"angka = {i}") for i in data]

print(20*"=")
# cara dengan enumerate
# yaitu mengambil index dan enumeratenya

data_list = ["rafa",1,2,3,"putri"]
for index,data in enumerate(data_list):
    print(f"index = {index}, data = {data}")
    # jadi kita dapat index dan datanya sekaligus


# mengkuadratkan angka didalam list di  
# variablenya langsung 

angka = [4,6,8,4,7,6]
angka_kuadrat = [i**2 for i in angka]
print(f"ini adalah angka kuadratnya {angka_kuadrat}")