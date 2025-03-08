lama = int(input("Masukkan lama sewa mobil "))
print("1. Sewa Mobil Avanza Rp 200/hari (dalam ribuan)")
print("2. Sewa Mobil Xenia Rp 300/hari (dalam ribuan)")
print("3. Sewa Mobil APV Rp 150/hari (dalam ribuan)")
kode = int(input("Masukkan kode sewa [1,2,3] "))
supir = int(input("Pakai supir atau tidak, biaya tambahan Rp 100 pilih(1/2) (ya/tidak) "))

if supir == 1:
    if kode == 1:
        print("Mobil yang disewa pakai supir, hitung (", lama, " x 200) + 100 = ", (lama*200)+100)
    if kode == 2:
        print("Mobil yang disewa pakai supir, hitung (", lama, " x 300) + 100 = ", (lama*300)+100)
    if kode == 3:
        print("Mobil yang disewa pakai supir, hitung (", lama, " x 150) + 100 = ", (lama*200)+100)
        
if supir == 2:
    if kode == 1:
        print("Mobil yang disewa tidak pakai supir, hitung (", lama, " x 200) = ", (lama*200))
    if kode == 2:
        print("Mobil yang disewa tidak pakai supir, hitung (", lama, " x 300) = ", (lama*300))
    if kode == 3:
        print("Mobil yang disewa tidak pakai supir, hitung (", lama, " x 150) = ", (lama*200))