'''
5.	Pida ocho nombres al usuario y los agregue a la lista de un curso. Al final debe imprimir la lista y 
un mensaje indicando la cantidad de estudiantes que hay en el curso.
'''
lista_curso = []
contador = 0

while contador < 8:
    nombre = input(f'Ingrese el nombre del alumno número {contador + 1}: ')
    print(lista_curso)
    contador += 1

tamaño_curso = len(lista_curso)
print(f'La lista del curso es: {lista_curso}.\nLa cantidad de alumnos es {tamaño_curso}')

