# operator asigment
print ('====tambah=====')
a = 5
print ('nilai a = ', a)
a += 5
print ('nilai a + 5 = ', a)

print ('====perkalian=====')
a = 5
print ('nilai a = ', a)
a *= 5
print ('nilai a * 5 = ', a)

print ('====pangkat=====')
a = 5
print ('nilai a = ', a)
a **= 5
print ('nilai a**5 = ', a)

# and
print ('====AND=====')
a = True
print ('nilai a = ', a)
a &= False
print ('nilai a& true = ', a)

# and
print ('====OR=====')
a = True
print ('nilai a = ', a)
a |= False
print ('nilai a| true = ', a)

#geser geser
print ('====>>=====')
a = 0b01000
print ('nilai a = ', '=', format (a,'05b'))
print ('nilai a = ', '=',a)
a >>= 2
print ('nilai a>>=2 ','=', a)