x=int(input("Masukkan jumlah barang: "))
print("1. Pensil harganya 100/buah.")
print("2. Kertas harganya 200/buah.")
print("3. Pulpen harganya 250/buah.")
kode1=int(input("Masukkan kode barang [1, 2, 3]: "))
print("1. Satuan lusin (x 12).")
print("2. Satuan kodi (x 20).")
print("3. Satuan box (x 50).")
kode2=int(input("Masukkan kode satuan [1, 2, 3]: "))
if kode1>3:
    print("Anda salah memasukkan kode.")
else:
    if kode1==1:
        harga=100
    elif kode1==2:
        harga=200
    elif kode1==3:
        harga=250
    if kode2==1:
        satuan=12
    elif kode2==2:
        satuan=20
    elif kode2==3:
        satuan=50
print("Total bayar kode: ",kode1," adalah ")
print("(",x," x ",harga,") x ",satuan," Rp",(x*harga)*satuan)