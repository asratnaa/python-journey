def fungsi(*args):
    nama = args[0]
    tinggi = args[1]
    berat = args[2]
    print(f"{nama} punya tinggi {tinggi} dan berat {berat}")

fungsi("dudung",120,120)

def tambah(*data) :
    output = 0
    for angka in data :
     output += angka
    return output

hasil = tambah(1,2,4)
print(f'hasil tambah = {hasil}')

def fungsi(**kwargs):
    '''fungsi kwargs'''
    nama = kwargs["nama"]
    tinggi = kwargs["tinggi"]
    berat = kwargs["berat"]
    print(f"{nama} punya tinggi {tinggi} dan berat {berat}")

fungsi(nama="ucup",tinggi=183,berat=79)

def operasi_mtk (*args,**kwargs):
   output = 0
   if kwargs["option"] == "tambah":
      for angka in args:    
        output += angka

   elif kwargs['option'] == 'kali' :
      output = 1
      for angka in args :
        output *= angka
   else:
      print('selesai')
    return output
   
hasil = operasi_mtk(1,1,option = 'tambah')
print(hasil)

def math(*args,**kwargs):
    output = 0
    if kwargs["option"] == "tambah":
        for angka in args:
            output +=angka
    elif kwargs["option"] == "kali":
        output = 1
        for angka in args:
            output *= angka
    else:
        print("tidak ada operasi")

    return output

hasil = math(1,2,3,4,option="tambah")

print(f"hasil jumlah {hasil}")

hasil = math(1,2,3,4,option="kali")
print(f"hasil kali {hasil}")

