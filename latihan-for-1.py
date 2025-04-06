awal=int(input("Masukkan nilai awal: "))
akhir=int(input("Masukkan nilai akhir: "))+1
jumlah=0
for i in range(awal,akhir): #menampilkan rentang nilai dari 0 sampai 4 
    print(i, end=(" "))
    jumlah=jumlah+i
print()
print("Jumlah total adalah ",jumlah)