# list -> array, mengakses dengan 
# menggunakan index

data_list = ['ucup','otong','dudung']

print(data_list[0])

# dictionary (dict) -> associative array
# identifier -> key

data_dictionary = {
    'key':'value',
	'cp':'ucup',
	'tg':'otong',
	'dg':'dudung',
	'nmbr':100,
}

print (data_dictionary)

print(data_dictionary['cp'])

# cek key ada engga
key = 'cp'
checkkey = key in data_dictionary
print(f' apakah ada key cp = {checkkey}')

#panjang dictionary
lendict = len (data_dictionary)
print(f' panjang dictionary = {lendict}')

#mengakses value (read) dengan get

print(data_dictionary.get('cp'))
print(data_dictionary.get('kiss','data tidak ditemukan'))

# mengupdate data
data_dictionary['cp'] = 'irwan'
print (data_dictionary)

data_dictionary['iwn'] = 'irwan'
print (data_dictionary)

#menggunakan update
data_dictionary.update ({'iwn' : 'nurul'})
print (data_dictionary)

data_dictionary.update ({'ir' : 'irwan'})
print (data_dictionary)

#mendelete
del data_dictionary['iwn']
print (data_dictionary)