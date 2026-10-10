total_belanja=int(input("masukkan total belanja: Rp"))

if  total_belanja % 100000 == 0:
    total_bayar = 0
    diskon = "gratis"

elif total_belanja % 50000 == 0:
    total_bayar = total_belanja * 50 // 100
    diskon = "50%"

elif total_belanja % 10000 == 0:
    total_bayar = total_belanja * 80 // 100
    diskon = "20%"

elif total_belanja >= 200000:
    total_bayar = total_belanja * 90 //100
    diskon = "10%"

else:
    total_bayar = total_belanja
    diskon = "tidak ada diskon"

status_point = "point bertambah" if total_bayar > 0 else "tidak ada point"

print("total belanja :", total_belanja)
print("diskon :", diskon)
print("total bayar :", total_bayar)
print("status point :", status_point)