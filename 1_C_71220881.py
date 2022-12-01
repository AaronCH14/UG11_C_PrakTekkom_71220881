print ("Operasi Matematika")
print ("1. Jumlah [+]")
print ("2. kurang [-]")
print ("3. kali   [*]")
print ("4. bagi   [/]")
print ("-----------------------------")
Operasi = int(input("Pilih Operasi 1/2/3/4:"))
Bilangan1 = int(input("Masukkan Bilangan Pertama : "))
Bilangan2 = int(input("Masukkan Bilangan Kedua : "))

def hitung_penjumlah(Operasi,Bilangan1,Bilangan2):
    penjumlahan = Bilangan1+Bilangan2
    return penjumlahan
def hitung_pengurangan(Operasi,Bilangan1,Bilangan2):
    pengurangan = Bilangan1-Bilangan2
    return pengurangan
def hitung_perkalian(Operasi,Bilangan1,Bilangan2):
    perkalian= Bilangan1*Bilangan2
    return perkalian
def hitung_pembagian(Operasi,Bilangan1,Bilangan2):
    pembagian = Bilangan1/Bilangan2
    return pembagian

if Operasi== 1 :
   hasil = Bilangan1+Bilangan2
elif Operasi == 2 :
    hasil = Bilangan1-Bilangan2
elif Operasi == 3 :
    hasil = Bilangan1*Bilangan2
elif Operasi == 4 :
    hasil = Bilangan1/Bilangan2
    
print ("Hasil : %d" %hasil)
