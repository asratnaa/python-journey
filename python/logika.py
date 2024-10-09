# operasi logika atau boolean
# and , or , xor

print ('========================= not')
a = True
b = not a
print ('data a =', a)
print ('data a =', b)

print ('========================= and')
#kalau ada false pasti false
a = False 
b = False
c = a and b
print (a,'and',b,'=',c)
a = True
b = False
c = a and b
print (a,'and',b,'=',c)
a = False
b = True
c = a and b
print (a,'and',b,'=',c)
a = True
b = True
c = a and b
print (a,'and',b,'=',c)

print ('========================= or')
#kalau ada true pasti true
a = False 
b = True
c = a or b
print (a,'or',b,'=',c)

a = True 
b = False
c = a or b
print (a,'or',b,'=',c)

a = True 
b = True
c = a or b
print (a,'or',b,'=',c)

a = False
b = False
c = a or b
print (a,'or',b,'=',c)

print ('========================= xor')
#kalau true true false

a = False 
b = True
c = a ^ b
print (a,'xor',b,'=',c)

a = True 
b = True
c = a ^ b
print (a,'xor',b,'=',c)

a = True 
b = False
c = a ^ b
print (a,'xor',b,'=',c)

a = False
b = False
c = a ^ b
print (a,'xor',b,'=',c)

#latihan logika dan komparasi
#membuat rentang area dari angka

print ('# +++++++3---------10+++++++++')

inputUser = float(input ('masukan angka = '))
#memeriksa inputuser

isKurangDari = (inputUser < 3)
print ('kurang dari 3 = ', isKurangDari)

IsLebihDari = (inputUser > 10)
print ('lebih dari 10 = ', IsLebihDari)

iscorrect = (IsLebihDari and isKurangDari)
print ('kurang dari 3 atau lebih \n dari 10 = '  ,iscorrect)

print ('-------3+++++++++++++10-----------')
inputUser = float(input("masukan angka = "))
#periksa
isLebihDari = (inputUser > 3)
print ('lebih dari 3 = ',isLebihDari)

isKurangDari = (inputUser < 10)
print ('kurang dari 10 = ',isKurangDari)

iscorrect = (isKurangDari and isLebihDari)
print ('input user = ', iscorrect)


#latihan you can do it 
print(' ----0+++++5----8++++11----')
InputUser = float (input('masukan angka'))


KurangDari = (0 < InputUser < 5 )
print('lebih dari 0 kurang dari 5 = ', KurangDari)

LebihDari = (8 < InputUser < 11 )
print ('lebih dari 8 kurang dari 11 = ', LebihDari)

iscorrect = (KurangDari and LebihDari)
print ('inputuser = ', iscorrect)
