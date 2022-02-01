altura = int(input('Altura del triángulo: '))

for i in range(1, altura+1):
    for j in range(1, i+1):
        if j % 2 != 0:
            print(j, end=' ')
    print(' ')
