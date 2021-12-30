num1 = int(input('Primer número entero positivo: '))
num2 = int(input('Segundo número entero positivo: '))
listaPares = []
listaImpares = []

for i in range(num1,num2+1):
    if i % 2 == 0:
        listaPares.append(i)
    else:
        listaImpares.append(i)

print(f'Números pares: {listaPares}')
print(f'Números impares: {listaImpares}')
