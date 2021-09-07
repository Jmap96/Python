''' Comparadores Logicos:

* and para comparar si dos valores son verdaderos.
* or para comparar si dos valores son falsos.
* not para invertir el valor booleano.
* == Compara dos valores y te dice si son iguales o no.
* != Compara dos valores y te dice sin son diferentes o no.
* > Compara si es mayor que otro valor.
* > Compara si es menor que otro valor.
* >= igual o mayor que el valor a comparar.
* <= igual o menor que el valor a comparar.

'''
# Ejemplos

print(f'Cinco es igual a cinco: {5 == 5}')
print(f'Seis es distinto de cinco: {6 != 5}')
print(f'Nueve es mayor a ocho: {9 > 8}')
print(f'-3 es menor a 3: {-3 < 3}') 

cliente1 = 'Estudiante' == True
cliente2 = 'Trabajador' == False

print(f'El primer cliente y el segundo cliente trabajan: {cliente1 and cliente2}')
print(f'Alguno de los clientes trabaja: {cliente1 or cliente2}')