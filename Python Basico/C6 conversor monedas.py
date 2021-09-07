"""Mejorando Conversor de Monedas"""

menu = ''' Bienvenido al conversor de monedas  🪙💰

--- Seleciona algun numero para hacer la operacion ---

1 - Pesos Colombianos
2 - pesos Chilenos
3 - Pesos Mexicanos
4 - Pesos Argentinos

--- Elige alguna de las cuatro opciones ---
                Gracias
'''

dolar_cop = 3875
dolar_clp = 767.05
dolar_mxn = 19.92
dolar_ars = 97.87

opcion = int(input(menu))

if opcion == 1:
    cop = int(input('Cuantos pesos colombianos tienes: '))
    dolares_cop = cop / dolar_cop
    dolares_cop = round(dolares_cop, 2)
    print(f'Tienes ${cop} pesos colombianos que su valor en dolares US es: ${dolares_cop}')
elif opcion == 2:
    clp = int(input('Cuantos pesos chilenos tienes: '))
    dolares_clp = clp / dolar_clp
    dolares_clp = round(dolares_clp, 2)
    print(f'Tienes ${clp} pesos chilenos que su valor en dolares US es: ${dolares_clp}')
elif opcion == 3:
    mxn = int(input('Cuantos pesos mexicanos tienes: '))
    dolares_mxn = mxn / dolar_mxn
    dolares_mxn = round(dolares_mxn, 2)
    print(f'Tienes ${mxn} pesos mexicanos que su valor en dolares US es: ${dolares_mxn}')
elif opcion == 4:
    ars = int(input('Cuantos pesos argentinos tienes: '))
    dolares_ars = ars / dolar_ars
    dolares_ars = round(dolares_ars, 2)
    print(f'Tienes ${ars} pesos argentinos que su valor en dolares US es: ${dolares_ars}')
    
else: 
    print('Has elegido una opcion incorreta')