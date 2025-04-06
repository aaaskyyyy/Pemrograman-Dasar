print("1. Perulangan for increment")
print("2. Perulangan while increment")
print("3. Perulangan for decrement")
print("4. Perulangan while decrement")
pilih=int(input("Masukkan pilihan Anda: "))
if pilih==1:
    for i in range (1,20,2):    #nilai untuk increment & decrement tidak bisa pecahanan
        print("Data for increment ke",i)
if pilih==2:
    i=1             #inisialisasi/nilai awal
    while i<=20:    #kondisi bernilai true
        print("Data while increment ke",i)
        i+=2        #i = i+2 disebut update, bisa bernilai increment/decrement
if pilih==3:
    for i in range (20,1,-2):    #nilai untuk increment & decrement tidak bisa pecahanan 
        print("Data for increment ke",i)
if pilih==4:
    i=20             #inisialisasi/nilai awal
    while i>=1:    #kondisi bernilai true
        print("Data while increment ke",i)
        i-=2        #i = i+2 disebut update, bisa bernilai increment/decrement