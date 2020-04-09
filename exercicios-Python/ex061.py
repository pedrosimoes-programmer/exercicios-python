c = 0
pt = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a razão dessa PA: '))
while c < 10:
    print(pt, end=' -> ')
    pt += r
    c += 1
print('FIM')
