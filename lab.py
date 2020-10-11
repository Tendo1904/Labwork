i = 0
j = 0
k = 0
a = 0
m = 0
l = 0
with open('steam_description_data.csv') as f:
	for line in f:
		w = line.split()
		i += len(line.split())	
		j += line.count('.') + line.count(',') + line.count(';')
		a += line.count('.') + line.count('!') + line.count('?')
		m += line.count('</')
		l += line.count(' ')
		for ch in line:
			k += len(ch)	

	print('Number of words ',i)
	print('Number of punctuation marks ',j)
	print('Amount of characters ',k)
	print('Amount of characters without spaces ',k-l)
	print('Amount of characters without p.m. ',k-j)
	print('Amount of sentences ',a-m)
	print('</ ',m)
	print('spaces ',l)
