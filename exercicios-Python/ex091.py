from random import randint
from time import sleep
from operator import itemgetter
valores = {'jogador1': randint(1, 6),
           'jogador2': randint(1, 6),
           'jogador3': randint(1, 6),
           'jogador4': randint(1, 4)}
ranking = {}
print('Valorer sorteados: ')
for k, v in valores.items():
    print(f'O {k} tirou {v}')
    sleep(1)
ranking = sorted(valores.items(), key=itemgetter(1), reverse=True)
print('=' * 50)
print(' >>> Ranking dos jogadores <<< ')
for i, valor in enumerate(ranking):
    print(f'    {i+1}º lugar: {valor[0]} com {valor[1]}.')
    sleep(1)
