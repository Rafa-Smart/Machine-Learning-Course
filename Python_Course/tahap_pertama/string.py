# srting adalah kumpulan karakter
data = "ini adalah string"
print(data)
print(f"ini adalah type datanya :",type(data))
# 1 cara buat string 
# - dengan singel quote '...'
data = 'menggunakan singel quote'
print(data)
# - dengan double quote "..."
data = "menggunakan double quote"
print(data)
print('"hallo apa kabar')
# 2 cara buat string 
# - dengan backslash \
# contoh kita membuat ' menjadi string
print('ini adalah hari jum\'at')
print('g\'day,is\'it?')
# -cara menanbahkan backslash yaitu dengan \\
print("c:\\user\\ucup")
# tab
print("ucup\totong")
# new line
print("baris pertama\nbaris kedua")
print("baris pertama\rbaris kedua")
print("baris pertama\n\rbaris kedua")
# 3 cara buat string literal
print('c:\new folder')#salah hasilnya malah enter
print('c:\\new folder')#ini bisa tapi ada lagi
# raw string
print(r'c:\new folder')
# dengan menggunakan raw string maka akan membuat 
# apapun yang dibalik kutip akan dianggap string

# multiline literal string
print("""
nama : rafa 
kelas : 10 pplg 2""")
# ini maksudnya adalah apapun yang kita masukan 
# kedalam """ maka akan dianggap seperti 
# enternya dan lain lain


# multiline literal string dan raw
print(r"""nama : rafa 
kelas : 10 pplg 2
      website : www.rafa.com/newid
""")