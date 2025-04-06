nilai=int(input("Masukkan nilai: "))
pangkat=int(input("Masukkan pangkat: "))+1
pangkatan=1
for i in range(1, pangkat):
    print(nilai, end=("")) #end= agar data ditampilkan ke samping, bukan ke bawah
    if i < pangkat-1:
        print (end=(" x "))
    pangkatan=pangkatan*nilai
print(" =",pangkatan)