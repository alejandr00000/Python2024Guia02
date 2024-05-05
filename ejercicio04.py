'''
4.	Haga un programa que reciba un número mayor que 0 e imprima el valor de la suma de todos los naturales 
entre 1 y el número, incluyéndolos.
'''

cantidad = int(input('Ingrese un número positivo: '))
contador = 0
suma = 0

while contador <= cantidad:
    suma = suma + contador
    contador = contador + 1

print(suma)

#Si se quiere imprimir un mensaje mostrando la operatoria que se está realizando, se puede hacer lo siguiente
contador = 0
suma = 0
mensaje_suma = ''
while contador <= cantidad:
    suma = suma + contador
    mensaje_suma = mensaje_suma + str(contador)
    if (contador < cantidad):
        mensaje_suma = f'{mensaje_suma} + '
    
    contador = contador + 1

print(f'{mensaje_suma} = {suma}')

