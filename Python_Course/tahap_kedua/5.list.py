import os 
os.system("cls")

# https://chatgpt.com/c/684d019a-8f48-8009-8f3f-f2fc5202331a



# jadi list itu adalah sebuah class
# jadi bisa 
 
s = list("halo") 
print(s) # ['h', 'a', 'l', 'o']

# fungsi bawaan
# len(list) → Panjang list
# sum(list) → Menjumlah isi list angka
# min(list), max(list) → Nilai terkecil/besar
# sorted(list) → Mengurutkan list


# method
# Metode	Fungsi
# append(x)	        Menambah item ke akhir list
# extend(iter)	    Menambahkan semua item dari iterable
# insert(i,x)	    Menyisipkan x pada index ke-i
# remove(x)	        Menghapus item pertama yang nilainya x
# pop([i])	        Menghapus item pada index i (default terakhir) dan mengembalikan nilainya
# clear()	        Menghapus seluruh isi list
# index(x)	        Mengembalikan index dari elemen pertama yang bernilai x
# count(x)	        Menghitung berapa kali x muncul
# reverse()	        Membalik urutan list
# sort()	        Mengurutkan isi list (bisa dengan kriteria custom)



# cara mudah untuk membaut list dengn cepat
# List dari angka genap
genap = [i for i in range(10) if i % 2 == 0]

# Pangkat dua
kuadrat = [x**2 for x in range(5)]


# contoh lagi 

[1, 2] + [3]  # [1, 2, 3]
[1] * 3       # [1, 1, 1]
2 in [1, 2]   # True


# contoh membuat list dengna 

print(f"genap {[i for i in range(1,11) if i % 2 == 0]}") # genap [2, 4, 6, 8, 10]
print("===============")

print(f"data sebelum = \n{[ i for i in range(1,11)]}\ndata setelah hapus 5\n{[j for j in [x for x in range(1,11)] if j != 5]}") 


print("===============")
print(f"data -> {[f"mangga {i}" for i in range(1,10+1)]}")