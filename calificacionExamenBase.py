''' Un examen tiene un número de preguntas determinado por el usuario.
Todas las preguntas tienen el mismo valor. La puntuación total del examen,
sobre un máximo de 10 puntos, se calcula de la siguiente manera: cada 3
respuestas malas se descuenta 1 buena y cada 3 respuestas omitidas equivalen
a una mala '''

preguntas = int(input('Número de preguntas del examen: '))

malas = int(input('Respuestas malas: '))

omitidas = int(input('Respuestas omitidas: '))

correctas = preguntas - malas - omitidas
print('Correctas: %s' % correctas)

malas = malas + omitidas // 3
malas = malas // 3
print('Descontar: %s' % malas)

correctas -= malas
print('Total correctas: %s' % correctas)

calificacion = (10 / preguntas) * correctas
print('Calificación: %s' % calificacion)
