# ini adalah data base sederhana
print(30*"=")
print("PROGRAM DAFTAR BUKU".center(20))
print(30*"=")

list_buku = []
while True:
    print("masukan data buku")
    judul_input = str(input("masukan judul buku = "))
    penulis_input = str(input("masukan nama penulis = "))


    buku_baru = [judul_input,penulis_input]
    list_buku.append(buku_baru)
    # jadi ini adalah kode dimana ketika user menginput judul
    # dan penulis, maka data nya akan ada di variable buku baru
    # setelah itu data di buku baru ini akan ditambahkan ke variable
    # list buku yang masih kosong
    print(20*"=")
    print("no. | judul | penulis")
    for index,buku in enumerate (list_buku):
        print(f"{index + 1} |{buku[0]} | {buku[1]}")

    print(20*"=")
    islanjut = str(input("apakah ingin melanjutkan ? (y/n)"))
    if islanjut == "n":
        break
print("TERIMA KASIH")