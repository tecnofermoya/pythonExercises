num = int(input('Introduce un número: '))
contador = 0

for i in range(2, num + 1):
    if num % i == 0:
        contador += 1

if contador == 1:
    print(f'El número {num} es primo')
else:
    print(f'El número {num} no es primo')
