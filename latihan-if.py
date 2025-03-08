x=int(input ("Masukkan nilai x: ")) #python fleksibel jd terserah mau menggunakan tanda "" atau '' asalkan konsisten
if x>0: #titik dua (:) artinya "maka" #kondisional if yang bernilai true
    print('Nilai  x = ',x,' bilangan positif') #indent (menjorok) sangat penting di python, jika salah indent maka codingan akan error
elif x==0: #singkatan dari else if
    print('Nilai  x = ',x,' bilangan netral')
else:
    print('Nilai  x = ',x,' bilangan negatif')