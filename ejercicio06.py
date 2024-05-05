'''
6.	Pida dos números a y b, para luego sumarlos e imprimir el resultado. Sin embargo, los números deben 
ser mayores que 0. El programa debe pedir los números hasta que el usuario los ingrese correctamente.
'''

numero01 = float(input('Ingrese el primer número. No puede ser negativo: '))

while numero01 < 0:
    numero01 = float(input('El número no puede ser negativo.\nIngrese el primer número: '))

numero02 = float(input('Ingrese el segundo número No puede ser negativo: '))

while numero02 < 0:
    numero02 = float(input('El número no puede ser negativo.\nIngrese el segundo número: '))

suma = numero01 + numero02
print(f'{numero01} + {numero02} = {suma}')