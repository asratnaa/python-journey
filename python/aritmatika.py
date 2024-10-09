
a = 10 
b = 3 

#operasi tambah
hasil = a + b
print(a,'+', b,'=',hasil)

#operasi kurang
hasil = a - b
print(a,'-', b,'=',hasil)

#operasi kali
hasil = a * b
print(a,'*', b,'=',hasil)

#operasi bagi
hasil = a / b
print(a,'/', b,'=',hasil)

#operasi pangkat/ eksponen
hasil = a ** b
print(a,'**', b,'=',hasil)

#operasi modulus
hasil = a % b
print(a,'%', b,'=',hasil)

#operasi floor division (pembulatan kebawah)
hasil = a // b
print(a,'//', b,'=',hasil)

#prioritas operasi

x = 3
y = 4
z = 5

hasil =(x + y) * z
print ('(',x,'+',y,')','*', z , '=', hasil )

hasil = (x / z) * y 
print ('(',x,'/',z,')','*',y ,'=', hasil)


#latihan konversi satuan temperatur
#konversi celcius ke satuan lain

celcius = float(input("masukan suhu celcius : "))
print("nilai celcius = ", celcius)

fahrenheit = (9/5 * celcius) + 32
print("suhu dalam fahrenheit adalah" , fahrenheit)

reamur = (4/5 * celcius)
print ("suhu dalam reamur = ", reamur)

kelvin = ( celcius + 273)
print ("suhu dalam kelvin =", kelvin)


#operasi komparasi
#setiap hasil dari operasi adalah boilan

a = 5
b = 8 
#lebih besar dari 
print ("========================== lebih besar dari")
hasil = (a > b)
print("apakah a lebih besar dari b = ",hasil)

#lebih kecil dari sama dengan
print ("========================== lebih kecil dari sama dengan")
hasil = (a <= b)
print("apakah a lebih kecil sama dengan b = ",hasil)

#sama dengan =
print ("========================== sama dengan")
hasil = (a == b)
print("apakah a sama dengan b = ",hasil)



#is dan is not
#is sebagai object identity
x = 5 
y = 6
print ('nilai x =', x , 'id = ', hex (id(x)))
print ( 'nilai y = ', y ,'id = ' , hex(id(y)))
print (x ,'is', y, hasil)
print (x, '==','10' , hasil)