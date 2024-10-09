# operasi manipulasi string

# 1. menyambungkan string

nama_depan = 'asri'
nama_tengah = 'ratna'
nama_belakang = 'aisyah'
nama_lengkap = nama_depan + ' '+ nama_tengah+ ' '+ nama_belakang 
print ('nama lengkap = ', nama_lengkap)

# menghitung panjang string
nama = len(nama_lengkap)
print ('jumlah nama ' + nama_lengkap + '=' + str(nama))

#operator untuk string

#apakah ada komponen char di string
nama = 'ratna'
status = nama in nama_lengkap
print ('apakah ada', nama ,'di nama lengkap = ', status)
print ('apakah ada' + ' ' + nama + ' ' +'di nama lengkap = ' + str(status))

#mengulang string
print (10*'ha')

#indexing
print('index ke- 10 =  ' + nama_lengkap[5])
print('index ke- 5:10 =  ' + nama_lengkap[5:10])
print('index ke- =  ' + nama_lengkap[5:13:2])

#item paling kecil
print ('nama paling kecil =' + min(nama_lengkap))
print ('nama paling besar = '+ max(nama_lengkap))


#operator dalam bentuk method

## merubah case dari string
#merubah semua upper cast

normal = 'Kamu Pasti Bisa'

print ('====lower===')
print ('lower = ' + str(normal.lower()))
print ('====upper===')
print ('upper = ' , normal.upper())

## pengecekan dengan ismethod

salam = 'hey bro'
apakah_lower = salam.islower()
print (salam + ' '+'apakah lower = '+ str(apakah_lower))
apakah_upper = salam.isupper()
print (salam,'apakah upper = ', apakah_upper)

#isalpha ----- untuk mengecek semuanya huruf 
#isdecimal ---- untuk mengecek angka saja
#isalnum ------ hruf dan angka
#isspace ------ spasi, tab ,new line \n
#istitle --- huruf depan kapital

judul = 'It Is Okey Not To Be Okay'
cek_judul = judul.istitle()
print (judul + ' '+ 'apakah\n sesuai= '+ ' '+ str(cek_judul))

password = 'Ratnacantik123'
cek_password = password.isalnum()
print (password+' '+'apakah sesuai = '+' '+str(cek_password))

#mengecek komponen startswith dan endswith
kata_depan = 'hari ini happy'.startswith('happy')
print ('kata depan diawali dengan happy = ' , kata_depan)
kata_belakang = 'hari ini happy'.endswith('happy')
print('kata belakang diakhiri \n dengan happy ='+' '+str(kata_belakang))

#penggabungan komponen , join, split

kata = ('hari','ini','happy')
gabungan = ','.join(kata)
print(gabungan)

gabungan = 'sangat'.join(kata)
print (gabungan)

pisah = gabungan.split('sangat')
print(pisah)

pisah = 'happy'.split('gabungan')
print(pisah)

#alokasi karakter rjust(), ljust() , center()

kanan = 'kanan'.rjust(10)
print(kanan)

center = 'kanan'.center(30)
print(center)

center = 'kanan'.center(30,'=')
print(center)

#contoh generic
##bolean
bolean = True
format = f"bolean ={bolean}"
print(format)

##string
string = 'ratna'
format = f'hello {string}'
print (format)

##angka
angka = 200
format = f'angka = {angka}'
print (format)

#bilangan bulat
angka = 5000
format = f'angka = {angka:d}'
print (format)

#bilangan ribuan
angka = 10000
format = f'angka = {angka:,}'
print(format)

#bilangan desimal
angka = 6.98
format = f'angka = {angka:.4f}'
print(format)

#menampilkan leading zero
angka = 55.99
format = f'bilangan = {angka:07.3f}'
print(format)

#menampilkan tanda + atau -
angka = - 10 
format = f'angka = {angka:.2f}'
print(format)

#menformat persen 
angka = 0.558
format =f'angka = {angka:.2%}'
print (format)

#melakukan operasi aritmatika dalam place holder
harga = 10000
jumlah =8
format =f'harga barang = Rp {harga*jumlah:,.2f}'
print (format)

#format angka lain (octal,binary, hexadecimal)

angka_octal = 255
angka_binary = 20
angka_hexadecimal = 90
format_octal = f'angka_octal = {oct(angka_octal)}'
format_binary= f'angka_binary = {bin(angka_binary)}'
format_hexa= f'angka_hexadecimal = {hex(angka_hexadecimal)}'

print(format_octal)
print(format_binary)
print(format_hexa)


print (5*'='+ 'width and multiline'+ 5*'=')
##width and multiline
ukuran_sepatu = 40
tinggi = 160
berat = 50 

#string
format = f'ukuran sepatu = {ukuran_sepatu} \ntinggi = {tinggi} \nberat = {berat}'
print(format)

#string multiline
format = f'''
ukuran sepatu = {ukuran_sepatu}
tinggi = {tinggi}
berat = {berat}
'''
print(format)

#mengatur lebar
format = f'''
ukuran sepatu = {ukuran_sepatu:>3}
tinggi        = {tinggi:>3}
berat         = {berat:>3}
'''
print(format)