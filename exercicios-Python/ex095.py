allPlayers = []
dadosJogador = {}
totPartidas = 0
gols = []

while True:
    print('=' * 30)
    dadosJogador['Nome'] = str(input('Nome do jogador: '))
    totPartidas = int(input(f'Quantas partidas o {dadosJogador["Nome"]} jogou? '))
    gols.clear()
    for c in range(1, totPartidas + 1):
        gols.append(int(input(f'Quantos gols {dadosJogador["Nome"]} marcou na {c}ª partida? ')))
        dadosJogador['Gols'] = gols[:]
    dadosJogador['Total'] = sum(gols)
    allPlayers.append(dadosJogador.copy())
    while True:
        r = str(input('Quer continuar? [S/N]: ')).upper().strip()[0]
        if r in 'SN':
            break
        print('ERRO! Digite apenas S ou N!')
    if r == 'N':
        break

print('=' * 50)
#Cabeçalho da Tabela
print('Cod ', end='')
for keys in dadosJogador.keys():
    print(f'{keys:<15}', end='')
print()
#Resultados da tabela
for k, v in enumerate(allPlayers):
    print(f'{k:>3} ', end='')
    for dado in v.values():
        print(f'{str(dado):<15}', end='')
    print()
print('=' * 30)
while True:
    codigo = int(input('Mostrar dados de qual jogador (código) (999 para parar): '))
    if codigo == 999:
        break
    if codigo >= len(allPlayers):
        print(f'Erro não há jogador com código {codigo}! Tente novamente.')
    else:
        print(f'Levantamento do jogador {allPlayers[codigo]["Nome"]}:')
        for partida, gol in enumerate(allPlayers[codigo]["Gols"]):
            print(f'    Na {partida+1}ª partida, {allPlayers[codigo]["Nome"]} marcou {gol} gols.')
    print('=' * 30)
print('     <<<  Obrigado, VOLTE SEMPRE!  >>>')