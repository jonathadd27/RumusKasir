#Sourcecode
#----------------------
#Inputan
nama = str(input("Masukan Nama Barang   : "))
harga = int(input("Masukan Harga Barang  : "))
jumlah = int(input("Masukan Jumlah Barang : "))

#RumusKair
hitungbayar = harga*jumlah

#MenghitungRumus
if hitungbayar > 100000 :
    potongan = hitungbayar * 0.10
    discount = hitungbayar - potongan
else :
    print("Total Jumlah Bayar \t\t\t : ", hitungbayar)

print("\n")
print("===================================================")
print("")
print("\t\t\t Hitung Barang")
print("\n")
print("====================================================")
print("Nama Barang         : ", nama)
print("Harga Barang        : ", harga)
print("Jumlah Barang       : ", jumlah)
print("Hitung Bayar        : ", hitungbayar)
print("Total Jumlah Bayar  : ", discount)