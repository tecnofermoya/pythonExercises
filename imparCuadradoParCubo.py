''' Escribe un código que calcule el cuadrado de un número si este es impar,
o el cubo de un número si este es par. Por ejemplo, para 4 tu programa debe 
entregar 64 y para 3 debe entregar 9 '''

try:
    num = int(input('Introduce un número: '))
    if num % 2 == 0:
        print('El número %s es par' % num)
        num = num ** 3
        print('Salida: %s' % num)
    else:
        print('El número %s es impar' % num)
        num = num ** 2
        print('Salida: %s' % num)
except:
    print('Debes introducir un número')