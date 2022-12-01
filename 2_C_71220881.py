print ("Pemeriksa Kelipatan 9")
Kel9 = int(input("Masukkan Kelipatan 9 Yang Ingin Diperiksa :"))

def kelipatan_9(Kel9):
    hasil = Kel9 % 9
    return hasil


if kelipatan_9(Kel9)==0:
    print ("Benar")
else :
    print ("Salah")
