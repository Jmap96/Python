""" Que es una variable: Una variable es una “caja” o lugar en 
donde puedo guardar objetos: números, texto, etc.  

* Para mostar el valor en consola se usa la funcion print()"""

# Ejemplo

x =  5 + 5
y = 'Hola Mundo'

print(x)

""" Es recomendable usar nombres propios para el identificador o 
nombre de mi variable. esta debe seguir ciertos lineamientos: 
** No puede comenzar con un número 
** Debe estar en minúsculas. 
** Las palabras dentro del mismo se separan con guión bajo"""

# Ejemplo

saludo = 'Hola Mundo'
print(saludo)

""" Los operadores matematicos en python son: 

+ : Suma
- : Resta
/ : Division
// : Division Entera
% : Residuo o Resto
** : Potencia

Para usar los operadores de raiz y logaritmo se utiliza la liberaria math.
la cual se invoca utilizando la siguinte linea de codigo <import math> """

# Ejemplos

suma = 5 + 5 
resta = 5 - 3
multiplicacion = 5 * 6
division = 36 / 5
division_entera = 36 // 5
residuo = 36 % 5
potencia = 3 ** 2

import math

raiz = math.sqrt(9)
logaritmo = math.log(9)

print(f' El valor de la suma es : {suma}\n El valor de la resta es: {resta}\n El valor de la multiplicacion es: {multiplicacion}')
print(f' El valor de la division es: {division}\n El valor de la division entera: {division_entera}')
print(f' El valor del residuo es: {residuo}\n El valor de la potencia es: {potencia}')
print(f' El valor de la raiz: {raiz}\n El valor logaritmo es: {logaritmo}')
 
