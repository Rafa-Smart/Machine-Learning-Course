# informasi 
# saat di looping , jika for sudah beres hingga
# perulangan terakhhir misal 5 perulangan nya sudah 
# sampai di 5 maka si looping ini akan beres atau
# lanjut ke else

# while = ketika

# while kodisi: (nah kondisi ini adalah murni boolean)
    # aksi

# angka = 10 
# while angka > 5:
#     print("rafa kece")
# jika program ini kita jalankan maka 'rafa kece' akan 
# terus di cetak sampai kapanpun karena
# logikanya adalah true maksudnya jadi while ini akan
# terus mencetak program jika logika yang di pakai adalah true


angka = 0
while angka < 5:
    angka += 1
# jadi maksud dari angka += 1 ini adalah saat while bekerja 
# ia akan terus mencetak, nah bagaimana cara kita untuk menstopnya
# caranya adalah di setiap while mencetak angka, maka kita 
# tambahkan 1 sampai logikanya akan false jika variable
# ini > (lebih dari) 5 jika sudah sampai 5 maka akan berhenti
# jadi nanti akan gini saat while cetak 0, maka 0 ini akan
# ditambah 1 dan seterusnya 0 + 1 = 1, 1 + 1 = 2,2 + 1 = 3 dan seterusnya 
    print(f"ini adalah {angka}")



no = 0
while no < 5:
    no += 1
    print("putri I love you")
    if no == 3:
        print("wajah mu begitu menawan")
        continue
    print("aku sayang kamu putri")
print("kamu sangat cantik")