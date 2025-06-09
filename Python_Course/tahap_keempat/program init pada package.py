import ipa
import matematika

# jadi fungsi dari init adalah
# dieksekusi langsung saat kita import si package

hasil_tambah = matematika.basic.tambah(3,4,5,6,4,3)
print(f"ini adalah hasil pertambahan = {hasil_tambah}")


hasil_kali = matematika.basic.kali(2,3,4,5,6)
print(f"ini adalah hasil perkalian = {hasil_kali}")

pangkat_3 = matematika.scientific.pangkat(3)
print(f"ini adalah hasil perpangkatan 3 = {pangkat_3(5)}")


hasil_fisika = ipa.fisika.gaya(5,8)
print(f"ini adalah hasil gaya = {hasil_fisika}")

