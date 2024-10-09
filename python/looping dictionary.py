teman_teman = {
	"cup":"ucup surucup",
	"tong":"otong surotong",
	"dung":"dudung surudung",
	"sep":"asep si kasyep",
	"cuy":"ucuy surucuy"
}

# looping first try (yang keluar adalah keynya)
for teman in teman_teman:
    print (teman)

# operator untuk mengambil item / iterables
print('\n')
#key = teman_teman.keys()
#print(key) #### bisa tanpa ini 

for key in teman_teman.keys():
    print(key)

print('\n')
#value = teman_teman.values()
#print(value) 

for value in teman_teman.values():
   print(value)

print('\n')

#item = teman_teman.items()
#print(item)
for item in teman_teman.items():
    print(item)


for key, value in teman_teman.items() :
    print (f'key ={key}, value = {value}')