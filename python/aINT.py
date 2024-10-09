def fizzbuzz (angka):
    for i in range(1,angka+1):
        if i%3 == 0:
            if i%5 == 0 :
                print('FizzBuzz')
            else:
                print('Fizz')
        elif i%5 == 0:
            print('Buzz')
        else:
            print(i)    

fizzbuzz(1)            

def HurufVokal(huruf):
    for i in huruf :
        if i in 'aiueoAIUEO':
            print(i)
HurufVokal('Indonesia')

def GantiHuruf(angka):
    daftar = {'a':'1','i':'2','u':'3','e':'4','o':'5','A':'1','I':'2','U':'3','E':'4','O':'5'}
    hasil = ""
    for i in angka:
        if i in daftar:
            hasil+= daftar[i]
        else:
            hasil+= i    
    print(hasil)

GantiHuruf('interview')

def balikkata(kata):
    return kata [::-1]
    
print(balikkata('hallo'))

def balikan(kata):
    new= ''.join(reversed(kata))
    print(new)
balikan('ratna')    

def ganjilgenap(tebak):
    jumlah = len(tebak)
    if jumlah %2== 0:
        print('Genap')
    else:
        print('ganjil')
        
ganjilgenap('kamar')            

def bilanganmenurun(tes):
    angka=[]
    for i in range(tes,0,-1):
        angka.append(i) 

    print (angka)    

bilanganmenurun(4)   

def bilangangenap(tes):
    angka=[]
    for i in range(tes,0,-1):
        if i%2 == 0 :
            angka.append(i) 

    print (angka)    

bilangangenap(4)  

def ganjilX(sample):
    deret = []
    for i in range(0,sample):
        if i%2 !=0:
            deret.append(i)

    for i in range(len(deret)):
        index = deret.index(deret[i])
        if index%2 == 0 :
            deret[i]='x'
    print(deret)     

ganjilX(9)        

def Kapital(kk):
    new = kk.upper()
    print(new)

Kapital('nama')

def kapital(sample):
    hasil = ''
    for i in sample:
        if i in 'aiueo':
            hasil += i.upper()
        else:
            hasil += i

    print(hasil)           

kapital('jakarta')

def huruf(sample):
    data = ''
    for i in sample:
        if i in 'aiueo':
            data += i.upper()
        else:
            data += i   
    print(data)     
huruf('memasak')        
    
def index(sample):
    kata=''
    for i in sample:
        if i in 'aiueo':
            kata +=i.upper()
        else:
            kata+= i    

    result = list(kata)
    for i in range(len(result)) :
        if i%2 == 0 :
            result[i] = result[i].upper()
    final_result = ''.join(result)
    print(final_result)                   

index('mimisan')    

           
            
               
#     print(hasil)     
# index('minum')        
    

def leap(year):
        if year% 4 == 0:
            if year%100 == 0:
                if year%400 == 0:
                    print('leap')
                else:
                    print('not leap')   
            else:
                print('leap')      
        else:
            print('not leap')           
leap(1900)                

for i in range(2,8):
    if i > 1 :
        for n in range(2,i):
            if i%n == 0 :
                break
        else:
            print(i)