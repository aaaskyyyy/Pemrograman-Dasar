for i in range(5, 0, -1):      # loop dari 5 ke 1 (mundur)
    for j in range(1, i + 1):  # loop dari 1 ke i
        print(j, end=' ')       # cetak tanpa pindah baris
    print()                    # pindah ke baris baru setelah inner loop selesai
