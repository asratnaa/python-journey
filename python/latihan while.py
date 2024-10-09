#angka = 6
#print (angka)
#while angka <= 7 :
#    angka += 1
#    print (angka)
#    if (angka) == 8 :
#        print ('end')
#print ('selesai')

#angka = 20
#print (angka)
#while angka >= 6 :
#    angka -= 2
#    print (angka)
#    if angka == 8 :
#        print ('nah ketemu')
#        continue
#print ('end')

#angka = 20
#print (angka)
#while angka >= 6 :
#    angka -= 2
#    print (angka)
#    if angka == 8 :
#        print ('udah bro cape')
#        break
#print ('end')

######## while tidak bisa digabung dengan FOR ########

#for i in range(5,0,-1) :
#    print (' '*(5-i),end='')
#    for x in range(i) :
#        print ('+',end='')
#    print() ### pelajarin ini 

sisi = 10
angka = 1
while True :
    if (angka%2):
        print ('*'*angka)
        angka += 1
    else :
        angka += 1
        continue
    if angka > sisi :
        break
#print()

print (5*'=' + 'FOR' + 5*'=' )

angka = 1

for i in range(9) :
    print ('+' * angka) 
    angka += 1
print ('akhir')

