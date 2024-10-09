# copy dictionary

teman_teman = {
	"cup":"ucup surucup",
	"tong":"otong surotong",
	"dung":"dudung surudung",
	"sep":"asep si kasyep",
	"cuy":"ucuy surucuy"
}

friend = teman_teman.copy()
print (friend)

friend['cup'] = 'ucup ajah'
print (friend)

# pop dictionary (berdasarkan key)
dataAsep = friend.pop('sep')
print(dataAsep)
print(f"friends = {friend}\n") #asep ilang

print('\n')
# popitem dictionary (yang terakhir ajah)
data = friend.popitem()
print(data)
print(f"friends = {friend}\n") ### ucuy ilang
print (f'teman_teman = {teman_teman}')