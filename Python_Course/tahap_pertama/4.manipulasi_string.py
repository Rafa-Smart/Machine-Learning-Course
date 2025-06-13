# String dalam Python adalah urutan karakter yang immutable (tidak bisa diubah setelah dibuat), tapi kamu bisa membuat string baru berdasarkan hasil operasi/manipulasi terhadap string sebelumnya.


# jadi kalo immutable itu artinya tipe datanya yang tidak bisa di ubah, tapi kalo misalkan kita ubah, maka itu artinya kita membuat yang baru contohnya int, float, str, tuple, frozenset
# kalo mutable itu artinya tipe data yang bisa diubah seteah di deklarasikan list, dict, set, bytearray

# mutabble berati datanya diubah tpai tidak mengganti alamat aslinya

a = 10
print(id(a))  # Alamat memori a
# jadi bakalan di timpa
a = a + 5
print(id(a))  # Alamat memori berubah!

print("contoh")
b = [1, 2, 3]
print(id(b))  # Alamat memori b
b.append(4)
print(id(b))  # Alamat memori tetap 

print("tpai ini aneh juga lihat, dan ini harus waspada")
a = [1, 2, 3]
b = a
b.append(4)
print(a)  # [1, 2, 3, 4] - a juga berubah!

print("=============================")
# 1. Deklarasi dan Akses Karakter
text = "Python"
print("Akses karakter pertama:", text[0])      # P
print("Akses karakter terakhir:", text[-1])    # n

# 2. Menggabungkan String
satu = "Belajar"
dua = "Python"
gabung = satu + " " + dua
print("Menggabungkan string:", gabung)

# 3. Mengulang String
ulang = "Hi " * 3
print("Mengulang string:", ulang)

# 4. Panjang String
panjang = len(text)
print("Panjang string 'Python':", panjang)

# 5. Slicing / Memotong String
print("Slice awal:", text[:3])        # Pyt
print("Slice akhir:", text[3:])       # hon
print("Slice tengah:", text[1:5])     # ytho

# 6. Perubahan Huruf
judul = "belajar python"
print("Uppercase:", judul.upper())
print("Lowercase:", judul.lower())
print("Capitalized:", judul.capitalize())
print("Title Case:", judul.title())

# 7. Menghapus Spasi
nama_kotor = "  adi setiawan  "
print("Tanpa spasi kiri-kanan:", nama_kotor.strip())
print("Tanpa spasi kiri:", nama_kotor.lstrip())
print("Tanpa spasi kanan:", nama_kotor.rstrip())

# 8. Pencarian dan Penggantian
kalimat = "saya suka python dan python menyenangkan"
print("Index kata 'python':", kalimat.find("python"))
print("Ganti 'python' dengan 'Java':", kalimat.replace("python", "Java"))

# 9. Pemeriksaan String
angka = "12345"
huruf = "Python"
kombinasi = "Python123"
print("Apakah angka?:", angka.isdigit())
print("Apakah huruf?:", huruf.isalpha())
print("Apakah alfanumerik?:", kombinasi.isalnum())

# 10. Split dan Join
data = "apel,jeruk,anggur"
list_buah = data.split(",")
print("Hasil split:", list_buah)
print("Join kembali:", " | ".join(list_buah))

# 11. Format String
nama = "Dina"
umur = 21
print(f"Nama saya {nama}, umur saya {umur} tahun")  # f-string
print("Nama saya {}, umur saya {} tahun".format(nama, umur))
# ini sama kayak di js, tapi js perlu util.format("nama:%s, umur:%d", nama, umur)


# 12
kalimat2 = "Saya sedang belajar string di Python"
# jadi kalo kita pake .split() itu sama saja seperti .split(" "), karena defaultnya adaalah itu
jumlah_kata = kalimat2.split(" ")
print("Jumlah kata:", jumlah_kata)

# 15. Studi Kasus: Validasi Email Sederhana
email = "example@gmail.com"
if "@" in email and email.endswith(".com"):
    print("Email valid")
else:
    print("Email tidak valid")


print("============")

# 16. Studi Kasus: Bersihkan dan Format Data Kontak
data_kontak = [
    "  jOhn doe , john@example.COM  ",
    "  jane smith , jane123@GMAIL.com  "
]

# keren nih, lebih mudah dari pada di js


for entry in data_kontak:
    nama_mentah, email_mentah = entry.strip().split(",") # disini berati nilai dari entry adalaj ["john", "email"]
    # emailDoang = email_mentah.index("@") // ini juga bisa
    emailDoang = email_mentah.replace(email_mentah[email_mentah.find("@"):],"@gmail.com") # ini juga bisa
    print(emailDoang)
    nama_bersih = nama_mentah.strip().title()
    email_bersih = email_mentah.strip().lower()
    print(f"Nama: {nama_bersih}, Email: {emailDoang}")


