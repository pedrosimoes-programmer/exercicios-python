for c in range(1, 7):
    print(2 * c)

print('')

for c in range(6, 0, -1): #-1 é a forma que o for realizará a contagem, ou seja, contando de -1 em -1
    print(c)

print('')

for c in range(0, 12, 2): # 2 é a forma que ele vai fazer a contagem, ou seja, de 2 em 2
    print(c)

print('')

i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))

for c in range(i, f+1, p):
    print(c)

print('')

s = 0
for c in range(0, 4):
    n = int(input('Digite um valor: '))
    s += n
print('A soma de todos os valores foi: {}'.format(s))
