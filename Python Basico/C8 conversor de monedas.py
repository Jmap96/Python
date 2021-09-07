""" Mejorando Conversor de Monedas Usando Funciones """

def conversor(tipo_pesos, valor_dolar):
    exc = int(input(f'Cuantos pesos {tipo_pesos} tienes: '))
    dolares = cop / valor_dolar
    dolares = round(dolares_cop, 2)
    print(f'Tienes ${exc} pesos colombianos que su valor en dolares US es: ${dolares}')

menu = ''' Bienvenido al conversor de monedas  🪙💰

--- Seleciona algun numero para hacer la operacion ---

1 - Pesos Colombianos
2 - pesos Chilenos
3 - Pesos Mexicanos
4 - Pesos Argentinos

--- Elige alguna de las cuatro opciones ---
                Gracias
'''
opcion = int(input(menu))

if opcion == 1:
    conversor('Colombianos', 3875 )
elif opcion == 2:
    conversor('Chilenos', 767.5 )
elif opcion == 3:
    conversor('Mexicanos', 19.92 )
elif opcion == 4:
    conversor('Argentinos', 97.87 )
else:
    print('Has elegido una opcion incorreta')

