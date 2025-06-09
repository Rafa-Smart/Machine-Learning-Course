# setiap hasil dari operasi komparasi adalah boolean
# >,<,>=,<=,==,!=,is,is not
# ch lebih besar dari
a = 4
b = 2
hasil = a > 3
print(a,'>' ,3,'=',hasil)
hasil = b > 3
print(b,'>' ,3,'=',hasil)
hasil = b > 2
print(b,'>' ,2,'=',hasil)
# ch kurang dari
print('======================')
hasil = a < 3
print(a,'<' ,3,'=',hasil)
hasil = b < 3
print(b,'<' ,3,'=',hasil)
hasil = b < 2
print(b,'<' ,2,'=',hasil)
print('======================')
# lebih besar sama dengan
hasil = a >= 3
print(a,'>=' ,3,'=',hasil)
hasil = b >= 3
print(b,'>=' ,3,'=',hasil)
hasil = b >= 2
print(b,'>=' ,2,'=',hasil)
# lebih kecil dari
print('======================')
hasil = a <= 3
print(a,'<=' ,3,'=',hasil)
hasil = b <= 3
print(b,'<=' ,3,'=',hasil)
hasil = b <= 2
print(b,'<=' ,2,'=',hasil)
# kalo yang = maka ini adalah asignment
# kalo == ini adalah membandingkan
 
#tidak sama dengan
print('======================')
hasil = a != 4
print(a,'!=',4,'=',hasil)
hasil = b != 4
print(b,'!=',4,'=',hasil)
# is adalah embanding kan memory / objek yaitu variable
x = 5
y = 5
print('nilai x =',x,'id = ',hex(id(x)))
print('nilai y =',y,'id = ',hex(id(x)))
hasil = x is y
# jadi si is ini  akan embanding kan nilai x dan y ini apakah
# sama 
print('x is y =',hasil)
# misal x = 5 jadi x adalah objek 
# dan 5 adalah literal
# dan is ini akan membandingan sebuah objek dengan id nya
 
#  is not adalah membandingkan nilai yang beda kebalikan is
x = 5
y = 5
print('nilai x =',x,'id = ',hex(id(x)))
print('nilai y =',y,'id = ',hex(id(x)))
hasil = x is not y
print('x is y =',hasil)
