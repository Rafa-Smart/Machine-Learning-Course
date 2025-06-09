# width and multiline

# data
data_nama = "putri maulidia yusuf"
data_umur = 15
data_tinggi = 167
data_nomor_sepatu = 43

# string standar
data_str = f"""nama : {data_nama}\numur : {data_umur}
tinggi : {data_tinggi}\nnomor sepatu : {data_nomor_sepatu}"""
print(data_str)
print("data string".center(20,"="))

# string multiline
data_str = f"""
nama   : {data_nama}
umur   : {data_umur}
tinggi : {data_tinggi}
no sepatu : {data_nomor_sepatu}
"""
print(data_str)

# mengatur rata kiri atau kanan
data_str = f"""
nama   : {data_nama:>5}
umur   : {data_umur:>5}
tinggi : {data_tinggi:>5}
no sepatu : {data_nomor_sepatu}
"""
# jadi maksudnya :>5 itu adalah siapa pun yang 
# karakter hurufnya kurang dari 5 maka akan rata ke kanan
print(data_str)
