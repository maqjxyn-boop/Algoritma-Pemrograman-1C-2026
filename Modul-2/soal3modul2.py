suhu = float(input("masukkan suhu reaktor: "))
tekanan = float(input("masukkan tekananreaktor: "))

if suhu > 1000:
    if tekanan > 50:
        status = "meltdown segera evakuasi"
    else:
        status = "bahaya suhu:segera turunkan daya"
elif suhu > 500:
    if tekanan > 30:
        status = "tekanan tidak stabil"
    else:
        status = "operasi reaktor normal"

else:
    status = "reaktor belum cukup panas"

pompa = "pompa maksimal" if suhu > 800 else "pompa normal"

print("suhu reaktor", suhu, "C")
print("tekanan gas", tekanan, "bar")
print("status bahaya", status)
print("status pompa", pompa)
