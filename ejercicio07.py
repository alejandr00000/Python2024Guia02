'''
7.	Pida números positivos al usuario hasta que ingrese un número negativo. El programa debe imprimir 
una lista con todos los números ingresados y la suma de todos los números que ingresó (incluyendo el 
número negativo).
'''

lista_numeros = []
numero = 0
suma = 0
print('Este programa calculará suma de los números que usted ingrese, siempre que sean mayores o iguales a cero.\nCuando ingrese un número negativo, el programa terminará de ejecutarse.')

while numero >= 0:
    numero = float(input('Ingrese un número: '))
    lista_numeros.append(numero)
    suma = suma + numero

print(f'La lista de números es {lista_numeros}.\nLa suma de los números es de {suma}')

