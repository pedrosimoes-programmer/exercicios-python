def escreva(txt):
    print('~' * (len(txt) + 4))
    print(f'  {txt}')
    print('~' * (len(txt) + 4))


#Programa Principal
while True:
    escreva(str(input('Digite um texto: ')))
    r = str(input('Quer continuar? [S/N]: ')).upper().strip()[0]
    if r == 'N':
        break
#escreva('Olá, Mundo!')
