'''
Cree un programa que reciba el nombre de un país y lo busque en una lista. Al final, debe mostrar en pantalla
un mensaje indicando si el nombre está en la lista o no
'''

paises = ['Argentina', 'Chile', 'Brasil', 'Bolivia', 'Colombia', 'Uruguay']
pais_buscado = input('Ingrese un país para ser buscado en una lista: ').capitalize()
contador = 0

while contador < len(paises):
    if (paises[contador] == pais_buscado):
        print(f'El país {pais_buscado} está en la lista')
        break #Esta línea de código se encarga de terminar el ciclo while sin de deba llegar al final
    else:
        contador = contador + 1

print(contador)
if (contador == len(paises)):
    print(f'El país {pais_buscado} no está en la lista')