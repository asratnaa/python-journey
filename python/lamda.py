pangkat = lambda num,pow : num**pow
print (pangkat(2,4))

jumlah = lambda num,pow : num+pow
print (jumlah(3,8))

jumlah = lambda num : num+2
print (jumlah(3))

#sorting list biasa
nama = ['ratna','widyain','aisyah']
nama.sort(key=len)
print(f' sort biasa = {nama}')

#fungsi 

def panjang_nama(m):
    return len(m)
nama.sort(key=panjang_nama)
print(f"sorted list by panjang = {nama}")


#sorting lambda
nama = ['ratna','widya','aisyah']
nama.sort(key = lambda nama :len(nama))
print (nama)

# filter
data_angka = [1,2,3,4,5,6,7,8,9,10,11,12]
data_angka.sort()
print (data_angka)


#fungsi
angka = [i for i in range (4,9)]
def kurangdari5 (angka) :
    return angka < 5
data_angka_baru = list(filter(kurangdari5,angka))
data_lambda = list(filter(lambda x : x > 5, angka))
print(data_angka_baru)
print(data_lambda)


#FUNGSI lambda
data = [i for i in range (0,12)]
ganjil =(list (filter(lambda x : (x%2 == 0 ),data)))
print(ganjil)

genap =(list (filter(lambda x : (x%2 != 0 ),data)))
print(genap)

kuadrat =(list (filter(lambda x : (x%5== 0 ),data)))
print(kuadrat)


# anonymous function
# currying <- Haskell Curry 
def pangkat(n):
    return lambda angka:angka**n

pangkat2 = pangkat(2)
print(f"pangkat2 = {pangkat2(5)}")

pangkat3 = pangkat(3)
print(pangkat3(2))