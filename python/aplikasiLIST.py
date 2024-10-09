#program buku 
list_buku = []
while True:
    judul = input(f'masukan judul = ')
    penulis = input(f'masukan nama penulis = ')
    daftar_buku = [judul,penulis]
    list_buku.append(daftar_buku)

    for index, buku in enumerate(list_buku):
        print(f'index {index+1} | {buku[0]} | {buku[1]})')

    isSelesai = input (f'apakah lanjut ? Yes OR No : ') 
    if isSelesai == 'No' :
        break
print ('terima kasih sudah membaca ')