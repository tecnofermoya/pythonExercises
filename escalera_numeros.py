'''
Escribe un programa cuya salida sea
2
2, 4
2, 4, 8
2, 4, 8, 16
y así hasta 1024, es decir,
2, 4, 8, 16, 32, 64, 128, 256, 512, 1024
'''

for i in range(1, 11):
	for j in range(1, i+1):
		if j == i:
			print(2**j, end='')
		else:
			print(2**j, end=', ')
	print('')
