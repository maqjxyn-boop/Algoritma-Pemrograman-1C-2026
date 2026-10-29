jumlah = 0
total = 0
jarak_terjauh = 0
total_jarak = 0

while True:
    jarak = int(input("Masukkan jarak (0 untuk selesai): "))

    if jarak == 0:
        break

    if jarak < 0:
        print("Jarak tidak valid!")
        continue

    if jarak <= 5:
        tarif = 3000
    elif jarak <= 15:
        tarif = 3000 + (jarak - 5) * 1000
    else:
        tarif = 13000 + (jarak - 15) * 500

    jumlah += 1

    if jumlah % 5 == 0:
        tarif = tarif * 0.5
        print("Diskon 50%")

    total += tarif
    total_jarak += jarak

    if jarak > jarak_terjauh:
        jarak_terjauh = jarak

    print("Tarif: Rp", int(tarif))

print("Jumlah penumpang:", jumlah)
print("Total pendapatan: Rp", int(total))

if jumlah > 0:
    print("Jarak terjauh:", jarak_terjauh, "km")
    print("Rata-rata jarak:", total_jarak / jumlah, "km")
else:
    print("Belum ada penumpang.")