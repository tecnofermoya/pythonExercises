lista = [1, 2, 3, 15]

def agregaNumero():
    num = int(input('Introduce un número: '))
    lista.append(num)
    print(lista)

while input('¿Deseas agregar otro número (S/N)?: ').lower() == 's':
    agregaNumero()

def ordenaLista():
    for i in len(lista):
        if lista[i] % 2 == 0:
            listaPares.append(lista[i])
        else:
            listaImpares.append(lista[i])
    print(listaPares.sorted())
    print(listaImpares.sorted())

ordenaLista()


