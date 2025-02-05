#list untuk menyimpan nilai
angka_list = []
#meminta pengguna mengisi 10 input dengan angka
for i in range(10):
    angka = float(input(f"Masukkan angka ke-{i+1}: "))
    angka_list.append(angka)
#menghitung rata rata
rerata = sum(angka_list) / len(angka_list)
#menampilkan hasil rata rata
print(f"Rata-rata dari angka yang dimasukkan adalah: {rerata}")