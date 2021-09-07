""" Primer programa: Conversor de monedas """

dolar_cop = 3875
dolar_clp = 767.05
cop = int(input('Cuantos pesos colombianos tienes: ')) # COP es el indicativo del pesos colombiano
clp = int(input('Cuantos pesos chilenos tienes: ')) #CLP es el indicativo del pesos chileno

dolares_cop = cop / dolar_cop
dolares_cop = round(dolares_cop, 2)
dolares_clp = clp / dolar_clp
dolares_clp = round(dolares_clp, 2)

print(f'Tienes ${cop} pesos colombianos que su valor en dolares US es: ${dolares_cop}')
print(f'Tienes ${clp} pesos chilenos que su valor en dolares US es: ${dolares_clp}')
 

"""Operacion Contraria"""

usd = int(input('Cuantos dolares tienes: '))
cop1 = 0.00026

cop_dolares = usd / cop1
cop_dolares = round(cop_dolares, 2)
print(f'Tienes ${usd} Dolares US que equivalen ${cop_dolares} pesos colombianos')