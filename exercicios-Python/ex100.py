from random import randint

numeros = []


def sorteia(* num):
    for num in range(0, 5):
        numeros.append(randint(0, 9))


def somaPar(numerosLista):
    cont = 0
    somaPares = 0
    while cont <= len(numerosLista):  # Poderia ser < 5, pois a lista contém 5 números
        if numerosLista[cont] % 2 == 0:
            somaPares += numerosLista[cont]
    print(f'A soma dos números pares sorteados foi: {somaPares}.')

sorteia()
somaPar(numeros)
