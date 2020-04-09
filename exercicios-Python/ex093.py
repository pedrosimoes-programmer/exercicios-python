dadosJogador = dict()
dadosJogador['Nome'] = str(input('Nome do jogador: '))
dadosJogador['Partidas'] = int(input(f'Total de partidas de {dadosJogador["Nome"]}: '))
gols = []
#totGols = 0
for c in range(1, dadosJogador['Partidas'] + 1):
    gols.append(int(input(f'Quantos gols {dadosJogador["Nome"]} fez na {c}ª partida? ')))
    dadosJogador['Gols'] = gols[:]
# Forma 1 para fazer o total de gols ->  for gols in dadosJogador['Gols']:
    #totGols += gols
# Forma 2 abaixo, usando o metódo sum
dadosJogador['Total'] = sum(gols)
print('=' * 50)
print(dadosJogador)
print('=' * 30)
for k, v in dadosJogador.items():
    print(f'O campo {k} tem valor {v}.')
print('=' * 20)
print(f'O jogador {dadosJogador["Nome"]} jogou {dadosJogador["Partidas"]} partidas.')
for indice, valor in enumerate(dadosJogador['Gols']):
    print(f'    => Na {indice+1}ª partida, fez {valor} gols.')
print(f'Foi um total de {dadosJogador["Total"]} gols.')
