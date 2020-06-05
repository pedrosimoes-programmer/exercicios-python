def ficha(nomeJogador='<desconhecido', gols=0):   
    print(f'O jogador {nomeJogador} fez {gols} gol(s) no campeonato!')

#Programa Principal

jogador = str(input('Informe o nome do jogador: '))
totGols = str(input('Informe quantos gols o jogador fez: '))   
if totGols.isnumeric():
    totGols = int(totGols)
else:
    totGols = '0'
if jogador.strip() == '':
    ficha(gols=totGols)
else:
    ficha(jogador, totGols)
