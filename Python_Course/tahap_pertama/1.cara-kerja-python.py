# python itu adalah bahasa pemrograman yang interpreter artinya
# ✅ Python adalah bahasa interpreted, tapi sebelum dieksekusi, Python tetap melakukan kompilasi ringan ke bytecode (bukan native machine code).

# 1. Kode Sumber Python (file .py)
#       ↓
# 2. kode di parsing dulu, jadi ngecek kurung dll
# 3. Dikompilasi ke Bytecode (.pyc) oleh Python Compiler
#       ↓
# 4. Bytecode dijalankan oleh Python Virtual Machine (PVM)
#       ↓
# 5. Output muncul di layar


# kalo mau liat byte kode dari python bisa pake
import dis
import dis
def cek_genap(n):
    if n % 2 == 0:
      return "Genap"
    else:
       return "Ganjil"

dis.dis(cek_genap(5))