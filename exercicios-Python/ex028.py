from random import randrange, randint
from time import sleep
#forma 1
#n = randrange(5) #Faz o PC 'pensar' em um número entre 0 e 5

#forma 2
n = randint(0, 5) #Faz o PC 'pensar' em um número entre 0 e 5
print('-=-' * 20)
print('O computador pensou em um número entre 0 e 5, tente adivinhá-lo!')
print('-=-' * 20)
alternativa = int(input('Digite o número: ')) #O que o PC pensou
print('PROCESSANDO......')
sleep(3) #Faz o PC 'dormir' durante o tempo colocado no parênteses
if alternativa == n:
    print('Parabéns, você ganhou o jogo!') #GANHOU
else:
    print('Você perdeu o jogo, o computador pensou no número {} e não no número {}'.format(n, alternativa)) #PERDEU
