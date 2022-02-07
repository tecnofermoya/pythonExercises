previo = 0
actual = 1
siguiente = previo + actual
num = int(input('Introduce el número de elementos de la serie: '))
print(previo, end=', ')
print(actual, end=', ')
print(siguiente, end=', ')

for i in range(1, num-2):
    previo = actual
    actual = siguiente
    siguiente = previo + actual
    if i == num-3:
        print(siguiente, end=' ')
    else:
        print(siguiente, end=', ')
