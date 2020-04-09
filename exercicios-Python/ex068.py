from random import randint
c = 0
while True:
    print('-=' * 20)
    print('\33[36mPAR OU ÍMPAR\33[m')
    print('-=' * 20)
    n = int(input('Digite um número: '))
    escolha = str(input('Você quer par ou ímpar? [P/I]: ')).strip().upper()[0]
    while escolha not in 'PI':
        escolha = str(input('Você quer par ou ímpar? [P/I]: ')).strip().upper()[0]
    computador = randint(0, 10)
    if (n + computador) % 2 == 0:
        if escolha in 'P':
            print(f'Você ganhou! O computador jogou {computador} e você jogou {n}, TOTAL {n + computador} DEU PAR!')
            print('Vamos novamente...')
            c += 1
        else:
            print(f'GAME OVER! O computador jogou {computador} e você jogou {n}! Total {n + computador} DEU PAR '
                  f'\nVocê ganhou {c} vezes!')
            break
    elif (n + computador) % 2 != 0:
        if escolha in 'I':
            print(f'Você ganhou! O computador jogou {computador} e você jogou {n}, TOTAL {n + computador} DEU ÍMPAR')
            print('Vamos novamente...')
            c += 1
        else:
            print(f'GAME OVER! O computador jogou {computador} e você jogou {n}, TOTAL {n + computador} DEU ÍMPAR!'
                  f' \nVocê ganhou {c} vezes!')
            break
