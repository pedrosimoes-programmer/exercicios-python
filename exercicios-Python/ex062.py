print('Gerador de PA')
print('=' * 20)
c = 0
pt = int(input('Primeiro termo da PA: '))
r = int(input('Razão da PA: '))
novosTermos = 10  # No começo, simulo que vale 10, pois o programa começa mostrando 10 termos
total = 0  # Total de termos a serem mostrados
while novosTermos != 0:
    total += novosTermos  # O total é = aos novosTermos, que começa, valendo 10, pois se não, o while não rodaria
    while c < total:
        print(pt, end=' -> ')
        pt += r
        c += 1
    print('PAUSA')
    novosTermos = int(input('Quantos termos você quer ver a mais? [0 para PARAR] '))  # O While começa de novo, com os nT do usuário
print('Progressão Aritmética finalizada com {} termos'.format(total))  # Mostra quantos o total de termos mostrados
