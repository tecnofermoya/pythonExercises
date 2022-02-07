while True:
    num = int(input('Introduce un número: '))
    factorial = 1
    for i in range(1, num+1):
        factorial *= i
    print(f'El factorial del número {num} es {factorial}')
    repetir = input('¿Deseas hacer otro cálculo (S/N): ')
    if repetir == 'N':
        break

