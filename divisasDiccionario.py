divisas = {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}
seleccion = input('Introduce una divisa: ')
if seleccion in divisas:
    print(f'La divisa seleccionada es {divisas[seleccion]}')
else:
    print(f'La divisa {seleccion} no se encuentra en el diccionario')