def menampilkanNama():
    print("Nama saya adalah Rafa Khadafi")
    print("Saya sedang belajar Python")

menampilkanNama()
# jadi sebenernya python itu bisa di compile juga ke bytecode selain kalo kita mau liat langsung
# lewat library dis
# tapi kita juga bisa buat langusng lewat terminal, dan akan menghasilkan sebuah folder __pycache__
# yang berisi file .pyc / kode byte dari kode kita

# caranya adalah dnegna mengetikan python -m _py_compile nama_file.py
# PS C:\Machine-Learning> cd Python_Course
# PS C:\Machine-Learning\Python_Course> cd tahap_pertama
# PS C:\Machine-Learning\Python_Course\tahap_pertama> python -m py_compile 2.compile_program.py  
# PS C:\Machine-Learning\Python_Course\tahap_pertama> cd ..
# PS C:\Machine-Learning\Python_Course> cd tahap_pertama
# PS C:\Machine-Learning\Python_Course\tahap_pertama> cd __pycache__
# PS C:\Machine-Learning\Python_Course\tahap_pertama\__pycache__> python .\2.compile_program.cpython-313.pyc
# Nama saya adalah Rafa Khadafi
# Saya sedang belajar Python
# PS C:\Machine-Learning\Python_Course\tahap_pertama\__pycache__> 

# jadi kalo mau langsng terisi nama filenya, kamu tinggal tuis dulu sedikit nama filenya, terus tekan tab


# fungsinya adalah ketik kamu mempunyai kode python yang memerlukan kecepatan exekusi yang cepat, maka kamu harus mengubah dulu ke bytecode, baru melakukan exekusi, agar lebih cepat