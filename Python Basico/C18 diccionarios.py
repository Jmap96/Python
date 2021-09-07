""" Diccionarios 

Son una estructura de datos mutable las cuales almacenan diferentes tipos de valores sin darle importancia a su orden. 
Identifican a cada elemento por una clave (Key). Se escriben entre {}.

"""

def run():
    mi_diccionario = {
        'llave1': 'a',
        'llave2': 'b',
        'llave3':'c',
        'llave4':'d',

    }

    poblacion_paises = {
        'Argentina': 44938712,
        'Brasil': 210147125,
        'Colombia': 50372424
    }
    
    print(poblacion_paises['Argentina']) # te imprime el valor de la llave

    # for pais in poblacion_paises.keys(): # Recorre las llaves del diccionario
    #     print(pais)

    # for poblacion in poblacion_paises.values(): # Recorre los valores asignados a las llaves
    #     print(poblacion)

    for pais, poblacion in poblacion_paises.items():
        print(f'El pais {pais} tiene una poblacion aproximada de: {poblacion}')

if __name__ == '__main__':
    run()   