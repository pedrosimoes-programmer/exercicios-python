def ficha(* nomeJogador, gols ):   
    print(f'O jogador {nomeJogador} fez {gols} gol(s) no campeonato!')
    

#Programa Principal

jogador = str(input('Informe o nome do jogador: '))
totGols = int(input(f'Informe quantos gols o jogador fez: '))   
ficha(jogador, totGols)
