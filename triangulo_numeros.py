altura = int(input('Altura del triángulo: '))

for i in range(1, (altura * 2) + 1, 2):
    for j in range(i, 0, -2):
        print(j, end=' ')
    print(' ')
