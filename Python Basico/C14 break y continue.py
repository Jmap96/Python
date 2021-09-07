# def run():
#     for contador in range(1001):
#         if contador % 2 != 0:
#             continue # lee la linea de codigo salta las excepciones y continua la operacion 
#         print(contador)

# def run():
#     for contador in range (1001):
#         print(contador)
#         if contador == 568:
#             break # rompe el codigo al llegar a la linea asignada


def run():
    texto = input('Agrega una frase: ')
    for letra in texto:
        if letra == 'o':
            continue
        print(letra)

if __name__ == '__main__':
    run()