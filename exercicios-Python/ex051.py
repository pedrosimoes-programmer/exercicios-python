print('=' * 20, '10 PRIMEIROS TERMOS DE UMA PA'.title(), '=' * 20)
pt = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a razão dessa PA: '))

for c in range(1, 11):
    print(pt, end=' -> ')
    pt += r
print('ACABOU')
