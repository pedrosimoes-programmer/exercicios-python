#Crie um programa que faça o computador jogar Jokenpô com você.
from random import randint
import time
jogada = int(input('''Suas opções de jogada:
[0] PEDRA
[1] TESOURA
[2] PAPEL
Qual é sua jogada: '''))
computador = randint(0, 2)

print('JO')
time.sleep(1)
print('KEN')
time.sleep(1)
print('PÔ')

if jogada == 0 and computador == 0:
    print('O computador jogou PEDRA')
    print('O jogador jogou PEDRA')
    print('EMPATE')
elif jogada == 0 and computador == 1:
    print('O computador jogou TESOURA')
    print('O jogador jogou PEDRA')
    print('O jogador VENCEU!')
elif jogada == 0 and computador == 2:
    print('O computador jogou PAPEL')
    print('O jogador jogou PEDRA')
    print('O computador VENCEU')
elif jogada == 1 and computador == 0:
    print('O computador jogou PEDRA')
    print('O jogador jogou TESOURA')
    print('O computador VENCEU')
elif jogada == 1 and computador == 1:
    print('O computador jogou TESOURA')
    print('O jogador jogou TESOURA')
    print('EMPATE')
elif jogada == 1 and computador == 2:
    print('O computador jogou PAPEL')
    print('O jogador jogou TESOURA')
    print('O jogador VENCEU!')
elif jogada == 2 and computador == 0:
    print('O computador jogou PEDRA')
    print('O jogador jogou PAPEL')
    print('O jogador VENCEU!')
elif jogada == 2 and computador == 1:
    print('O computador jogou TESOURA')
    print('O jogador jogou PAPEL')
    print('O computador VENCEU')
elif jogada == 2 and computador == 2:
    print('O computador jogou PAPEL')
    print('O jogador jogou PAPEL')
    print('EMPATE')
else:
    print('Você digitou algo errado, tente novamente')
