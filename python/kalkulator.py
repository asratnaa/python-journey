print('='*20)
print(5*'='+'kalkulator sederhana'+5*'=')

input_1 = float(input('masukan angka 1 = '))
masukan = (input('operator (x,/,+,- ) = '))
input_2 = float(input('masukan angka = '))


if (masukan) == ('+') :
    angka = (input_1 + input_2)
    print(f'hasilnya adalah = {angka}')
elif(masukan)== ('-') :
    angka = (input_1 - input_2)
    print (f'hasilnya adalah = {angka}')
elif(masukan) == ('x' ) or (masukan) == ('*') :
    angka = (input_1 * input_2)
    print (f'hasilnya adalah = {angka}')
elif(masukan) == ('/') :
    angka = (input_1 / input_2)
    print (f'hasilnya adalah = {angka}')
else :
    print ('haduh yang bener dong')