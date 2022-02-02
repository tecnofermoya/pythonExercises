frase = input('Introduce una frase: ')
letra = input('Introduce una letra: ')
contador = 0

for i in range(0, len(frase)):
    if frase[i].lower() == letra.lower():
        contador += 1

print(f'La letra "{letra}" aparece {contador} veces en la frase.')
