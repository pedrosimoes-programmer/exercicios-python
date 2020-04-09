while True:
    print(('=' * 20))
    n = int(input('De qual valor você quer ver uma  [VALOR NEGATIVO para PARAR]: '))
    print(('=' * 20))
    if n <= -1:
        break
    for c in range(1, 11):
        print(f'{n} x {c} = {n*c}')

    print('=' * 20)
print('Programa encerrado com sucesso. Volte sempre!')