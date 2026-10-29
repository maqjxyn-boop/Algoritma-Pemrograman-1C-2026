penuh = 0

for i in range(1, 11):
    print("\nMahasiswa ke-", i)

    nama = input("Nama: ")
    ipk = float(input("IPK: "))

    if ipk < 3.00:
        print(nama, "tidak memenuhi syarat.")
        continue

    penghasilan = int(input("Penghasilan orang tua: "))

    if penghasilan <= 3000000:
        print(nama, "mendapat beasiswa penuh.")
        penuh += 1
    elif penghasilan <= 5000000:
        print(nama, "mendapat beasiswa sebagian.")
    else:
        print(nama, "tidak mendapat beasiswa.")

    if penuh == 3:
        print("Kuota beasiswa penuh sudah terpenuhi.")
        break