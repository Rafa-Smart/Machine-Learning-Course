
print("\ttengah".expandtabs(10))
print("tengah".center(16,"*"))
# format_string_lengkap.py
# Penjelasan lengkap format string Python

# Struktur umum:
# {field_name:flags width .precision type}

# ini strukturnya {[field_name]:[flags][width][.precision][type]}


# ---------------------------------------------
# JENIS FORMAT TYPE
# ---------------------------------------------

# 1. Integer
print(f"Desimal: {255:d}")       # 255
print(f"Biner: {255:b}")          # 11111111
print(f"Oktal: {255:o}")         # 377
print(f"Heksadesimal (x): {255:x}") # ff
print(f"Heksadesimal (X): {255:X}") # FF
print(f"Locale format (n): {1000000:n}") # 1000000 (hasil tergantung lokal)
print(f"Ribuan dengan koma: {1000000:,}") # 1,000,000
print(f"Ribuan dengan underscore: {1000000:_}") # 1_000_000

# 2. Floating Point
print(f"Fixed-point: {1234.56789:f}")  # 1234.567890
print(f"Scientific (e): {1234.56789:e}")  # 1.234568e+03
print(f"Scientific (E): {1234.56789:E}")  # 1.234568E+03
print(f"General (g): {1234.56789:g}")     # 1234.57
print(f"General (G): {1234.56789:G}")     # 1234.57
print(f"Persentase: {0.12345:%}")         # 12.345000% // ini berati di kali dulu seratus baru di belakangnya di kasih %
print(f"Persentase dibatasi: {0.12345:.2%}") # 12.35%

# 3. Teks dan Objek
print(f"String biasa: {'halo':s}")     # halo
print(f"Repr objek: {123.456!r}")      # 123.456
print(f"ASCII objek: {'ñ':a}")         # '\xf1'

# ---------------------------------------------
# WIDTH dan PRECISION
# ---------------------------------------------
print(f"Lewat presisi: {123.4567:.2f}")    # 123.46
print(f"Lebar total: {123.4567:10.2f}")    # '    123.46'
print(f"String maksimal 3 karakter: {'Python':.3s}")  # 'Pyt'

# ---------------------------------------------
# ALIGNMENT & PADDING
# ---------------------------------------------
print(f"Rata kanan: {'Hi':>5}")       # '   Hi'
print(f"Rata kiri: {'Hi':<5}")        # 'Hi   '
print(f"Rata tengah: {'Hi':^5}")      # ' Hi  '
print(f"Padding karakter: {'Hi':*^10}")  # '****Hi****'

# Alignment angka dengan padding
print(f"Angka rata kanan: {123:>6}")  # '   123'
print(f"Angka padding nol: {123:06}") # '000123'
print(f"Tanda di awal & padding: {-42:=6}") # '-00042'

# ---------------------------------------------
# TANDA UNTUK ANGKA
# ---------------------------------------------
print(f"Tampilkan tanda: {42:+d}")     # +42
print(f"Hanya negatif: {42:-d}")       # 42
print(f"Spasi positif: {42: d}")       # ' 42'
print(f"Spasi negatif: {-42: d}")      # '-42'

# ---------------------------------------------
# CONTOH KOMPLEKS GABUNGAN
# ---------------------------------------------
angka = 1234.5678
print(f"Gabungan kompleks: {angka:*>+15,.2f}")  # '*+1,234.57'

# ---------------------------------------------
# FUNGSI format()
# ---------------------------------------------
print(format(angka, "10.2f"))         # '   1234.57'
print(format(angka, "*>+15,.2f"))     # '*+1,234.57'

# ---------------------------------------------
# GAYA LAMA DENGAN %
# ---------------------------------------------
print("Format lama: %.2f" % 3.14159)   # 3.14
print("Integer: %d" % 42)              # 42
print("Lebar dan presisi: %10.2f" % 3.14159)  # '      3.14'

# Semua format string di atas bisa digunakan dalam f-string, format(), dan format lama (%)
# Direkomendasikan gunakan f-string (sejak Python 3.6) karena paling mudah dibaca
