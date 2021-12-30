frutas = {'Plátano':1.35, 'Manzana':0.8, 'Pera':0.85, 'Naranja':0.7}
fruta = input('Elige una fruta: ')
if fruta in frutas:
    kilos = float(input('Número de kilos: '))
    precioTotal = kilos * frutas[fruta]
    print(f'El precio total es de {precioTotal:,.2f} €')
else:
    print('La fruta elegida no está en nuestra tienda')