#  Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência.
#  No final, mostre uma listagem de preços, organizando os dados em forma tabular.
produtos = ('Processador', 2000, 'Placa Mãe', 1000, 'Fonte de Alimentação', 700, 'Memória RAM', 400, 'HDD', 250, 'SSD',
            250, 'Placa de Vídeo', 1400)
print('=' * 50)
print('{:^50}'.format('Listagem de preços'))
print('=' * 50)
for item in range(0, len(produtos)):
    if item % 2 == 0:
        print(f'{produtos[item]:.<40}', end='R$')
    else:
        print(f'{produtos[item]:>8.2f}')
