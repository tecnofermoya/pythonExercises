nombre = input('Introduce tu nombre: ')
edad = int(input('Introduce tu edad: '))
ciudad = input('Introduce tu ciudad: ')
telefono = int(input('Introduce tu teléfono: '))
datos = {'nombre':nombre, 'edad':edad, 'ciudad':ciudad, 'telefono': telefono}
print(f'{datos['nombre']} tienes {datos['edad']} años, vives en {datos['ciudad']} y tu número de teléfono es {datos['telefono']}')
