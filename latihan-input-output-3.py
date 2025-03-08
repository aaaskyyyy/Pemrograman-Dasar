mk=input("Masukkan mata kuliah: ")
uts=int(input("Masukkan nilai UTS: "))
uas=int(input("Masukkan nilai UAS: "))
tugas=int(input("Masukkan nilai Tugas: "))
nilai=(uts+uas+tugas)/3
print("Mata kuliah %s "%mk) #%s artinya string
print("UTS = %d UAS = %d Tugas = %d "%(uts,uas,tugas)) #%d artinya desimal
print("Nilai akhir = (%d+%d+%d)/3=%f "%(uts,uas,tugas,nilai)) #%f artinya float