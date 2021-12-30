#------------- DATOS DE EJEMPLO PARA PROBAR --------------
# alumnos = ['Fernando', 'Isabel', 'Federico', 'Noelia', 'Pedro Miguel','Juan Miguel','Pepe','Esteban']
# notas = [9.4, 6.7, 9.39, 3.4, 6.7, 9.45, 8.7, 5.4]
#------------- DECLARACIÓN DE VARIABLES ------------------
alumnos = []
notas = []
notaMax = 0.0
alumnoMax = ''
continuar = True

#------------- INTRODUCCIÓN DE DATOS ---------------------
while continuar:

    try:
        print('-----------------------------------------------------------------')
        alumno = input('Introduce un alumno: ')
        nota = float(input('Introduce su calificación en el examen: '))
        if nota >= 0 and nota <= 10:
            alumnos.append(alumno)
            notas.append(nota)
            cont = input('Gestionar más alumnos/as? [S/N] ')
            if cont not in ['S','s']:
                continuar = False
        else:
            print('-----------------------------------------------------------------')
            print('Debes introducir una calificación correcta. Empecemos de nuevo...')

    except:
        print('Debes introducir valores válidos')

#------------- IMRIMIMOS AMBAS LISTAS COMO CONTROL FUNCIONAMIENTO ---------------------    
print(alumnos)
print(notas)

#------------- OBTENCIÓN DE LA CALIFICACIÓN MÁS ALTA ----------------------------------
for i in range(0,len(notas)):
    if notas[i] > notaMax:
        notaMax = notas[i]
        alumnoMax = alumnos[i]

#------------- RESULTADOS EN PANTALLA -------------------------------------------------
print('{} es el/la alumno/a que consiguió la nota más alta con {}'.format(alumnoMax,notaMax))
