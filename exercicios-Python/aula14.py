r = 'S'
# while r == 'S':
#    n = int(input('Digite um valor: '))
#    r = str(input('Quer continuar? [S/N ')).upper()
# print('\33[31mAcabou!\33[m')

jogador = ''
lista = ''
while r == 'S':
    jogador = str(input('Digite o nome de um jogador de futebol: '))
    lista += jogador
    r = str(input('Quer continuar? [S/N] ')).upper()
print('Você digitou os seguintes jogadores: {}'.format(lista))
