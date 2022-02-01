password = input('Nueva contraseña: ')
check_password = ''

while check_password != password:
    check_password = input('Repite la contraseña: ')

print('Contraseña correcta')
