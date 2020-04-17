from random import randint
from time import sleep

def maior(* num):
    print('=' * 20)
    c = maior = 0
    while c < len(num):
        print(num[c], end='| ', flush=True)
        sleep(0.3)
        if c == 0 or num[c] > maior:
            maior = num[c]
        c+= 1
    print(f'O maior valor informado foi {maior}!')
    print(f'Foram informados {len(num)} valores ao todo.')

#Programa Principal
maior(randint(0, 9), randint(0, 9), randint(0, 9), randint(0, 9), randint(0, 9), randint(0, 9))
maior(randint(0, 9), randint(0, 9), randint(0, 9))
maior(randint(0, 9), randint(0, 9))
maior(randint(0,9))
maior()