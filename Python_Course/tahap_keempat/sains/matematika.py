'''modul tambah'''
def tambah(*args):
    hasil = 0 
    for data in args:
        hasil += data
    return hasil

'''modul kali'''
def kali(*args):
    hasil = 1
    for data in args:
        hasil *= data
    return hasil

'''modul pangkat'''
def pangkat(n:int):
    return lambda angka:angka**n
