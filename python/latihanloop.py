print ('awal for')

sisi = 10

count = 1
for i in range (3) :
    print ('*' * count)
    count += 1
print ('akhir for')

print("awal while")
count = 1
while True:
	if (count%2):
		# Print jika ganjil
		print("*"*count)
		count += 1
	else:
		# akan kembali ke atas jika ganjil
		count += 1
		continue

	# akan break jika count melebihi sisi
	if count > sisi:
		break

print("akhier while")