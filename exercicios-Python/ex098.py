from time import sleep


def contador(inicio, fim, passo):
    print('=' * 20)
    print(f'Contagem de {inicio} até {fim}, de {passo} em {passo}')
    print('=' * 20)
    if inicio > fim:
        for num in range(inicio, fim - passo, - passo):
            print(num, end=' ')
            #sleep(0.4)
    if fim > inicio:
        for num in range(inicio, fim + passo, passo):
            print(num, end=' ')
            #sleep(0.4)
    if passo == 0:
        for num in range(inicio, fim, 1):
            print(num, end=' ')
            #sleep(0.4)
    print('FIM')


#Programa Principal

contador(1, 10, 1)

contador(10, 0, 2)

print('=' * 20)
print('Personalize sua contagem!')
contador(int(input('Início: ')), int((input('Fim: '))), int(input('Passo: ')))
