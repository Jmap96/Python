''' range en Python es un tipo que se utiliza para representar una secuencia inmutable de números. 
    Uno de sus principales usos es junto a la sentencia for, para definir un bucle sobre el que se 
    itera un número determinado de veces '''

# Ejemplo diferencia entre el while y el for
contador = 0
LIMITE = 501
while contador < LIMITE:
    print(contador)
    contador += 1


for contador in range (1000):
    print(contador)

