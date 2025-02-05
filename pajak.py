#input nilai harga barang
nilai_pembelian = float(input("Masukkan nilai pembelian: "))
#bersarnya pajak dan menghitung pajak yang harus dibayar
pajak = 0.11 * nilai_pembelian
total_bayar = nilai_pembelian + pajak
#menampilkan hasil yang harus dibayar
print(f"Total yang harus dibayar setelah pajak: {total_bayar}")