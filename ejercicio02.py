'''
2.	Pida un mensaje al usuario y la cantidad de veces que quiera mostrarlo en pantalla. Luego, debe hacerlo.
'''

mensaje = input('Ingrese el mensaje que desee mostrar en pantalla: ')
cantidad = int(input('Ingrese la cantidad de veces que desee mostrar el mensaje: '))
contador = 0

while contador < cantidad:
    print(f'{contador + 1}. {mensaje}')
    contador = contador + 1

