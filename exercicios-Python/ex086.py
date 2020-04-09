#  Versão GAMBIARRA PEDRO
matriz = []
coluna = linha = 0
for c in range(0, 9):
    matriz.append(int(input(f'Digite um valor para a posição [{coluna}, {linha}]: ')))
    linha += 1
    if linha > 2:
        linha = 0
        coluna += 1
print('=' * 50)
print(f'[{matriz[0]}] [{matriz[1]}] [{matriz[2]}]'
      f'\n[{matriz[3]}] [{matriz[4]}] [{matriz[5]}]'
      f'\n[{matriz[6]}] [{matriz[7]}] [{matriz[8]}]')

#  Versão FUNCIONAL GUANABARA
matriz2 = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for colun in range(0, 3):
    for line in range(0, 3):
        matriz2[colun][line] = int(input(f'Digite um valor para a posição [{colun}, {line}]: '))
print('=' * 50)
for colun in range(0, 3):
    for line in range(0, 3):
        print(f'[{matriz2[colun][line]:^5}]', end='')
    print()

