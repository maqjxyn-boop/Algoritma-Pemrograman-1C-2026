pin = int(input("masukkan pin 3 digit: "))
jam = int(input("masukka jam kedatangan (0-23): "))

digit1 = pin // 100
digit2 = (pin // 10) % 10
digit3 = pin % 10
if pin % 5 == 0:
    if jam < 12:
        status = "garasi pagi terbuka"
    else:
        status = "garasi malam terbuka, lampu dinyalakan akan muncul"
elif pin % 2 == 0:
    if digit1 + digit3 == digit2:
        status = "garasi vip khusus bos"
    else:
        status = "kode genap ditolak, alarm berbunyi" 

else:
    status = "akses ditolak sepenuhnya"

cctv = "mode malam merekam" if jam > 18 else "mode siang standby"

print("digit pertama :", digit1)
print("digit kedua :", digit2)
print("digit ketiga :", digit3)
print("status garasi :", status)
print("status cctv :", cctv)
