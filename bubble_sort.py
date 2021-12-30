nums = [2, 5, 66, 4, 1, 0, 45, 23, 3]
print(len(nums))
print(range(len(nums) - 1))

def bubble_sort(lista):
    for _ in range(len(lista) - 1):
        for j in range(len(lista) - 1):
            if lista[j] > lista[j+1]:
                # aux = lista[j]
                # lista[j] = lista[j+1] 
                # lista[j+1] = aux
                lista[j], lista[j+1] = lista[j+1], lista[j]
    return lista

print(bubble_sort(nums))