valores = []
r = 'S'
c = 0
provisorio = []
while True:
    provisorio.append(int(input('Digite um valor para ser adicionado à lista: ')))
    if c == 0:
        print('Valor adicionado com sucesso à lista.')
        valores.append(provisorio[c])
    else:
        if provisorio[c] in valores:
            print('Valor duplicado. Não será adicionado.')
        else:
            print('Valor adicionado com sucesso à lista.')
            valores.append(provisorio[c])
    c += 1
    r = input('Quer continuar [S/N]: ').strip().upper()[0]
    if r == 'N':
        break
print('-=' * 50)
valores.sort()
print(f'Você digitou os valores {valores}')
