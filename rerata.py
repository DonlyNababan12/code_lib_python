angka_list = []

for i in range(10):
    angka = float(input(f"Masukkan angka ke-{i+1}: "))
    angka_list.append(angka)

rerata = sum(angka_list) / len(angka_list)

print(f"Rata-rata dari angka yang dimasukkan adalah: {rerata}")