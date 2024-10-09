#pengenalan fungsi

def perkenalan():
    print("hello world")
    print("Kepada Ucup Surucup")
    print("Dan juga kepada Otong Surotong")

perkenalan()


def tambah(a,b):
    hasil = a + b
    print (f'{a} + {b} = {hasil}')
    kali = a * b
    print (f'{a} * {b} = {kali}')
    modulus = a%b
    print (f'{a} % {b} = {modulus}')

tambah (8,8)

def kuadrat (input_angka) :
    output = input_angka **2
    return output 

y = kuadrat(5)
print(f' hasil y = {y}')
x = kuadrat(1)
print(f' hasil x = {x}')
z = 10 + kuadrat(10)
print(f' hasil z = {z}')

def tambah (a,b):
    return a+b

x = tambah(9,0)
print(x)

def operasi_matematika(angka_1,angka_2):
    tambah = angka_1 + angka_2
    kurang = angka_1 - angka_2
    kali = angka_1 * angka_2
    bagi = angka_1 / angka_2

    return tambah,kurang,kali,bagi

k,l,m,n = operasi_matematika(9,5)

print(f"Hasil tambah = {k}")
print(f"Hasil kurang = {l}")
print(f"Hasil kali = {m}")
print(f"Hasil bagi = {n}")

#### FUNGSI DENGAN ARGUMENT

def say_hello(nama = 'ganteng') :
    print(f'hallo {nama}')

say_hello('ratna')
say_hello()

#contoh 2
def sapa_dia(nama, pesan = "Apa kabar?"):
    '''fungsi dengan satu input biasa, dan satu default argument'''
    print(f"hai {nama}, {pesan}")

sapa_dia("Dudung","Hai Ganteeeng")
sapa_dia("Otong")

def hitung_pangkat(angka, pangkat=2):
    hasil = angka**pangkat
    return hasil

print(hitung_pangkat(3,4))

hasil = hitung_pangkat(pangkat=3, angka=5)
print(hasil)
coba = hitung_pangkat (2,4)
print(coba)

def fungsi(input1=1,input2=2,input3=3,input4=4):
    hasil = input1 + input2 + input3 + input4
    return hasil

print(fungsi())
print(fungsi(input3=10))

''' Type hints untuk fungsi '''

# bentuk standar fungsi yang udah kita pelajari

# studi kasus
def fungsi(parameter):
    hasil = parameter**2
    print(hasil)

fungsi(9)
#fungsi("Ucup")..... fungsi supaya tidak salah memasukan 
#                     jenis data yang akan di inpu
#fungsi(True)

def pangkat(angka:int):
    output = angka**3
    return output

x = pangkat(7)
print(x)

def display(argument:str):
    print(argument)

display('ratna')
    