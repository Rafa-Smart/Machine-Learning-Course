# operasi logika dan boolean 
# not, or, and, xor
# ini ch not
a = True
c = not a
print("data a =",a)
print('=======================')
print("data c =",c)
# jadi not adalah logika kebalikan jika nilai a = true (benar)
# lalu nilai a di not kan maka akan jadi kebalikan 
# jadi nilai c adalah false karena kebalikan dari a = true

print('=======================')
# ini adalah ch or
# huruf saat menulis false harus benar besar kecilnya
# jika salah satunya adalah true maka akan true
a = False
b = False
c = a or b
print(a,'or',b,'=',c)
b = False
a = True
c = a or b
print(a,'or',b,'=',c)
a = True
b = False
c = a or b
print(a,'or',b,'=',c)
a = True
b = True
c = a or b
print(a,'or',b,'=',c)

print('=======================')
# ini adalah and
# akan true jika dua duanya true
a = False
b = False
c = a and b
print(a,'and',b,'=',c)
b = False
a = True
c = a and b
print(a,'and',b,'=',c)
a = True
b = False
c = a and b
print(a,'and',b,'=',c)
a = True
b = True
c = a and b
print(a,'and',b,'=',c)
