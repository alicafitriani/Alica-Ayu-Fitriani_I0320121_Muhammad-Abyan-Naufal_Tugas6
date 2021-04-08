# Menghitung nilai rata-rata
banyak_nilai = int(input("Banyaknya nilai yang akan dihitung rata-rata : "))
data = []
i = 1
for i in range(banyak_nilai):
    nilai = float(input("nilai ke-{} :".format(i + 1)))
    data.append(float(nilai))
    i = 1 + i

rerata = sum(data)/banyak_nilai
print("Nilai rata-rata = ", rerata)