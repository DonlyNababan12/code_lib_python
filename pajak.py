nilai_pembelian = float(input("Masukkan nilai pembelian: "))

pajak = 0.11 * nilai_pembelian
total_bayar = nilai_pembelian + pajak

print(f"Total yang harus dibayar setelah pajak: {total_bayar}")