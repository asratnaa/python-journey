import os
def header():
    '''fungsi Header'''
    os.system("cls")
    # os.system("cls")
    print(f"{'PROGRAM MENGHITUNG LUAS':^40}")
    print(f"{'DAN KELILING PERSEGI PANJANG':^40}")
    print(f"{'-'*35}")

def input_user():
    lebar = int(input('masukan lebar = '))
    panjang = int(input('masukan panjang = '))
    return lebar,panjang

def hitung_luas(lebar,panjang):
    return lebar * panjang

def keliling(lebar,panjang):
    return 2*(panjang +lebar)

def display(message,value):
    '''fungsi display'''
    print(f"hasil perhitungan {message} = {value}")

#program utama
while True :
    header()
    lebar,panjang = input_user()
    luas = hitung_luas(lebar,panjang)
    keliling = keliling(lebar,panjang)
    display("luas", luas)
    display("keliling", keliling)

    isContinue = input("apakah lanjut (y/n)? ")
    if isContinue == "n":
        break

print('terima kasih')


