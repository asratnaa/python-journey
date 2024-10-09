### LIST

## cara alternatif membuat list
data_range = range(0,10,2) # range(start,stop,step)
print (data_range)

# membuat list dengan for loop, list comprehension
data = [i for i in range (10,0,-2)]
print (data)

#dataganjil
data_for = [ i for i in range (12,0,-1) if i%2]
print(data_for)

#datagenap
genap =[i for i in range (1,12,1) if i%2 == 0] 
print (f'list data genap = {genap} ')

##### operasi list ####

nama = ['asri', 'ratna' , 'widya' ,'aisyah']
pertama = nama[0]
print(pertama)

ketiga = nama[-2]
print(f'nama terakhir = {ketiga}')

#jumlah list
jumlah = len(nama)
print(f' jumlah data = {jumlah}')

#insert
nama.insert (1, 'laila')
print(nama)

# menambah di akhir list
nama.append ('nana')
print(nama)

jumlah = len(nama)
print(f'jumlah saat ini = {jumlah}')

#Meremove data 
nama.remove ('asri')
print (nama)

#meremove daata akhir
nama.pop ()
print(nama)

#mengurutkan data 
nama.sort()
print (nama)

#membalik list
nama.reverse()
print (nama)

angka = [0,3,7,8,9,5,2,6,2,2,1,3,8]
print (angka)

jumlah = (f'jumlah angka 0 = {angka.count(8)}')
print (jumlah)

angka.sort()
print(angka)

angka.reverse()
print(angka)

#### copylist
a = ['kenzi','marina','narnia']
print (f' anggota a =\n {a}')
b = a.copy()

print (f'anggota b =\n {b}')
print (f'anddres a = {hex(id(a))}')
print (f'anddres b = {hex(id(b))}')

# coba ubah data 1
a[2]= 'vexana'
print (a)
print (b) #b tidak berubah 

### nested list
data_c = [1,2,3]
data_d = [5,8]

list_2d = (data_c,data_d,2,1)
print (list_2d)
print ('\n')
print (6*'=' + 'contoh penggunaan' + 6*'=') 
print ('\n')
murid_1 = ['lili',17,'wanita']
murid_2 = ['mino', 30 , 'pria']
murid_3 = ['selena', '26','wanita']

murid_mix = [murid_1,murid_2,murid_3]

print (murid_mix)
for murid in murid_mix :
    print (f'nama \t\t:{murid[0]}')
    print (f'umur \t\t:{murid[1]}')
    print(f'jenis kelamin\t:{murid[2]}\n')

murid_baru = murid_mix.copy()
print(murid_baru)
print ('\n')
murid_1[0] = 'legolas' ## salah karna jdi berubah semua
print(murid_baru)
print (murid_mix)

# mengambil data dari nested list
murid = murid_mix[0][0]
print(f'nama murid = {murid}') 

print('\n')
# kita gunakan deepcopy

print (5*'=' + 'kita gunakan deepcopy' + 5*'=')
from copy import deepcopy
murid_mix = [murid_1,murid_2,murid_3]
print(murid_mix)

print('\n')
murid_new = deepcopy(murid_mix)
print (murid_new)
murid_1[0] = 'hanabi' #setelah menggunakan deepcopy 
                        #berubah hanya di awal
print('\n')
print(murid_new) #tdk berubah
print (murid_mix)

murid_new[0][0] = 'kagura' #berubah yg kedua
print(murid_new)


