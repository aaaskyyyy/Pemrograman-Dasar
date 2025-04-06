print("1. Perulangan for")
print("2. Perulangan while")
print("3. Keluar")
pilih = int(input("Masukkan pilihan Anda: "))
if pilih == 1:
    print("PERULANGAN for -> Harga Pertalite Rp 10.000/liter")
    print("Jumlah Liter         Total Harga Pertalite")
    for i in range(1,16,2):
        print("   ", i, "                   ", i*10000)
elif pilih == 2:
    print("PERULANGAN while -> Harga Solar subsidi Rp 6.800/liter")
    print("Jumlah Liter         Total Harga Solar")
    i = 20
    while i>0:
        print("    ", i,"                   ", i*6800)
        i-=2
elif pilih == 3: 
    exit()