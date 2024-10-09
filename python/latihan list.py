murid = ['austus','angela','vale','connie']
murid.sort()
print (murid)

murid.reverse()
print (murid)

jumlah = len(murid)
print(f'jumlah murid = {jumlah}')

index = murid.index('angela')
print (f'index angela = {index}') #setelah di reverse

murid.insert(1,'lapulapu')
print(murid)

murid.remove('vale')
print(murid)

murid.append('lunox') #nambah paling belakang
print (murid)

murid.pop() #hapus paling belakang
print (murid)

#mengambil data
data = murid[-2]
print (f'nama murid = {data}')

jumlah = len(murid)
print(f'jumlah murid = {jumlah}')

data = murid[1]
print (f'nama murid = {data}')

#merubah data 
murid[1] = 'kagura'
print(murid)

#buat list
list =[i for i in range (0,12,3)]
print(list)

kumpulan = [8,10,5,9,0]
print (kumpulan)

#gabungkan list
kumpulan.extend(list)
print (kumpulan)
kumpulan.sort()
print(kumpulan)

#count
angka = [10,9,8,0,6,4,4,4,4,5,5,10,10,10]
jumlah = angka.count(10)
print (f'jumlah angka 10 = {jumlah}')

angka.sort()
print(angka)


nama_1=['jo',25 ,'lk']
nama_2=['dit',27,'lk']
nama_3=['hana',30,'pr']

namamix = (nama_1,nama_2,nama_3)
print (namamix)
print('\n')

for nama in namamix:
    print(f'nama    = {nama[0]}')
    print(f'kelamin = {nama[2]}')

nama_1=['jo',25 ,'lk']
nama_2=['dit',27,'lk']
namamix = (nama_1,nama_2,nama_3)
print (namamix)

from copy import deepcopy
namamix2 = (nama_2,nama_1)
print (namamix2)

print('looping for')
for nama in namamix2:
    print(f'nama = {nama[0]}')
print('\n')

[print (f'nama = {i}') for i in nama] #gk bisa

#for loop and range
angka = [10,4,5,8]
panjang = len(angka)
i= 0


for i in range (panjang) :
    print (f'angka = {angka[i]}')


#while

kumpulan_angka = [10,5,4,2,6,5]

panjang = len(kumpulan_angka)
i = 0

while i < panjang :
      print (f'angka = {kumpulan_angka[i]}')
      i+=1

# list comprehension
print("\nList Comprehension")
data = ["ucup",1,2,3,"otong"] 

[print (f'data = {i}') for i in data]

kumpulan_angka = [10,5,4,2,6,5]
[print(f'angka = {i}') for i in kumpulan_angka ]

# enumerate
print("\nEnumerate")
data_list = ["ucup",1,2,3,"otong"]

for index, data in enumerate(data_list) :
     print (f'data = {data}', f'index = {index}' )