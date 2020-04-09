# FORMA SEM USAR LISTAS COMPOSTA, ou seja, LISTAS DENTRO DE LISTAS
from random import randint
from time import sleep

print('=' * 50)
print('GERADOR DE PALPITES NA MEGA SENA')
print('=' * 50)
provisorio = 0
numeros = []
jogos = int(input('Quantos jogos você quer gerar? '))
print('=' * 30)
print('=' * 3, '\33[36mGerando os Jogos\33[m', '=' * 3)
for i in range(0, jogos):
    print(f'Jogo {i + 1}: ', end=' ')
    for c in range(0, 6):
        provisorio = randint(1, 60)
        if provisorio in numeros:
            provisorio = randint(0, 60)
        if c == 0 or provisorio not in numeros:
            numeros.append(provisorio)
        numeros.sort()
    print(numeros)
    sleep(1)
    numeros.clear()
print('=' * 20, 'Boa Sorte', '=' * 20)

# FORMA USANDO LISTAS COMPOSTAS

quantidadeJogos = numero = 0
games = list()
copiaJogos = []
quantidade = int(input('Quantos jogos você quer gerar? '))
while quantidadeJogos <= quantidade:
    cont = 0
    while True:
        numero = randint(1, 60)
        if numero not in copiaJogos:
            copiaJogos.append(numero)
            cont += 1
        if cont >= 6:
            break
        copiaJogos.sort()
        games.append(copiaJogos[:])
        copiaJogos.clear()
        quantidadeJogos += 1
print(f'Os jogos sorteados foram {games}')
# INCOMPLETO
