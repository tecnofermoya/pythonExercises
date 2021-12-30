listaDesordenada = [2, 4, 8, 1, 0, 32, 67, 11, 4, 3]

def insertion_sort(lista):
    for i in range(1, len(lista)):
        print(i)
        while i > 0 and lista[i-1] > lista[i]:
            lista[i], lista[i-1] = lista[i-1], lista[i]
            i -= 1
            print(i)
    return lista

# print(len(listaDesordenada))
print(insertion_sort(listaDesordenada))        

