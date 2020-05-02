from random import randint
from time import sleep


def sorteia(num):
    print(f'Sorteando os 5 valores: ', end='')
    for num in range(0, 5):
        n = randint(1, 10)
        numeros.append(n)
        print(f'{n}', end=' ', flush=True)
        sleep(0.3)
    print('\nFIM DO SORTEIO!')


def somaPar(numLista):
    somapares = 0
    for numero in numLista:  # Poderia ser < 5, pois a lista contém 5 números
        if numero % 2 == 0:
            somapares += numero
    print(f'A soma dos números pares sorteados foi: {somapares}.')


numeros = []
sorteia(numeros)
somaPar(numeros)
