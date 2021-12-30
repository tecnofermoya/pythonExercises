a = 'Hola'
b = 'mundo'
c = 87
d = 2.33145
print(a + ' ' + b)
print(f'-{a}-{b}-')
print('-{}-{}-'.format(a,b))
print('El resultado es: %s' % c)
print('El resultado es:', c)
print('El resultado es: {} min ({} seg)'.format(c, c*60))
print('La temperatura es {:.1f}ºC'.format(d))