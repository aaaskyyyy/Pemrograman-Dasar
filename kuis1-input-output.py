hari = int(input("Masukan jumlah hari kerja "))
gajiOperator = hari*7500
gajiManajer = (hari*9000)-(hari*9000*0.1)
print("Uang Harian Operator Rp 7500")
print("Uang Harian Manajer  Rp 9000 potong pajak 10%")
print("Total Gaji Operator ", hari , " hari x 7500 Rupiah = ", gajiOperator)
print("Total Gaji Manajer (", hari, " hari x 9000)-(", hari, " x 9000 x 0.1) = ", gajiManajer, " rupiah")