from random import randint
from time import sleep
c = 1
print('=' * 20, '=' * 20)
print('O computador pensou em um número, tente adivinhá-lo!')
print('=' * 20, '=' * 20)
n = randint(0, 10)
r = int(input('Digite o número que o computador pensou: '))
print('PROCESSANDO...')
sleep(0.5)
while r != n:
    if r < n:
        print('Mais, tente de novo!')
    else:
        print('Menos, tente de novo!')
    r = int(input('Digite o número que o computador pensou: '))
    print('PROCESSANDO...')
    sleep(0.5)
    c += 1
print('''Parabéns! O computador pensou no número {} e você acertou! 
Você precisou de {} tentativas para acertar!'''.format(n, c))
