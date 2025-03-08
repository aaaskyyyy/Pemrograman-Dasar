uts=int(input("Masukkan nilai UTS: "))
uas=int(input("Masukkan nilai UAS: "))
tugas=int(input("Masukkan nilai Tugas: "))
nilai=(uts+uas+tugas)/3 #operator aritmatik + - * / %
print("Hasil nilai akhir: ",nilai)
if nilai >=85 and nilai <=100: #operator comparison > < >= <= != ==
    print("Nilai ",nilai," adalah A")
else:
    if nilai >=65 and nilai <85: #operator logika and, or, not
        print("Nilai ",nilai," adalah B")
    elif nilai >=50 and nilai <65:
        print("Nilai ",nilai," adalah C")
    else:
        print("Nilai tidak lulus")
        print("Mengulang lagi tahun depan")