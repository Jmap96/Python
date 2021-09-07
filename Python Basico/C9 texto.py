''' metodo: Los métodos son acciones o funciones que puede realizar un objeto '''

nombre = input("Cual es tu nombre: ")

mayusculas = nombre.upper() # devuelve los caracteres en mayusculas
minisculas = nombre.lower() # devuelve los caracteres en minisculas
mayuscula_inicial = nombre.capitalize() # devuelve la primera letra en mayusculas
espacios = nombre.strip() # elimina espacios basura
remplazar = nombre.replace('o', 'a') # remplazar caracteres
len(nombre) # cuenta la cantidad de caracteres


""" Slices """

nombre[0] # buscar por indice
nombre[0:3] # desde el inicio hasta el indice
nombre[:3 ] # desde el inicio hasta el indice
nombre[3:] # desde el indice hasta el final

numeros = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
numeros[0:15:2] # desde el indice hasta el indice con saltos
nombre[::-1] # trae al reves el objecto