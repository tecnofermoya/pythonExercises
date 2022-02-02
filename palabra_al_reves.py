palabra = input('Introduce una palabra: ')

for i in range(len(palabra)-1, -1, -1):
    print(palabra[i], end='')
