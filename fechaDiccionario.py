meses = {
    '01':'enero',
    '02':'febrero',
    '03':'marzo',
    '04':'abril',
    '05':'mayo',
    '06':'junio',
    '07':'julio',
    '08':'agosto',
    '09':'septiembre',
    '10':'octubre',
    '11':'noviembre',
    '12':'diciembre',
    }

fechaActual = input('Introduce la fecha actual en formato dd/mm/aaaa: ')
fechaActual = fechaActual.split('/')
dia = fechaActual[0]
mes = fechaActual[1]
anno = fechaActual[2]
print(f'Hoy es {dia} de {meses[mes]} de {anno}')