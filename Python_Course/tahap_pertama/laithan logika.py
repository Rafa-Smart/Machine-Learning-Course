# jika user mamasukan nilai diantara 3 dan 10 maka false
# ini adalah kasus gabungngan
inputuser = float(input("masukan angka yang bernilai\n kurang dari 3\n atau\n lebih besar dari 10\n:"))
iskurangdari = (inputuser < 3)
islebihdari = (inputuser > 10)
print("kurang dari 3 =",iskurangdari)
print("lebih dari 10",islebihdari)

iscorrect = iskurangdari or islebihdari
print("angka yang anda masukan",iscorrect)
print("\n",10*"=","\n")
# jika user memasukan nilai diantara 3 dan 10 maka true
# ini adalh irisan karena kita mengiris diantara 2 buah daerah
inputuser = float(input("masukan angka yang bernilai\n lebih besar dari 3\n dan\n kurang  dari 10\n:"))
iskurangdari = (inputuser > 3)
print("lebih besar dari 3",islebihdari)
islebihdari = (inputuser < 10)
print("kurang dari 10",islebihdari)
benar = iskurangdari and islebihdari
print("hasailnya :",benar)
print("\n",10*"=","\n")
input = float(input("masukan angka kurang dari 5, dan 11\n dan lebih dari 0 dan 8 \n:"))
kurangdari = (input < 5)
kurangdari = (input < 11)
lebihdari = (input > 0)
lebihdari = (input > 8)
print(kurangdari or lebihdari)

# or itu ditambah
# and itu dikali