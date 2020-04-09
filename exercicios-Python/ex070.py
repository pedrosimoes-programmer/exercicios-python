print('-' * 20, 'CAIXA: LOJAS MERLIM', '-' * 20)
total = produtos1000 = preçoBarato = c = 0
produtoBarato = ' '
while True:
    produto = str(input('Digite o nome do produto: '))
    preço = float(input('Digite o preço do produto: '))
    c += 1
    total += preço
    if preço > 1000:
        produtos1000 += 1
    if c == 1 or preço < preçoBarato:
        preçoBarato = preço
        produtoBarato = produto
    resposta = str(input('Quer continuar [S/N]: ')).upper().strip()[0]
    while resposta not in 'S/N':
        resposta = str(input('Quer continuar [S/N]: ')).upper().strip()[0]
    if resposta == 'N':
        break
print('{:-^40}'.format(' FIM DA COMPRA '))
print(f'Foram comprados {c} produtos.') if c > 1 else print(f'Foi comprado {c} produto.')
print(f'O total gasto na compra foi R${total:.2f}.')
print(f'No total, {produtos1000} produtos custam mais que R$1000,00.') \
    if produtos1000 > 1 or produtos1000 == 0 else print(f'No total, {produtos1000} produto custa mais que R$1000,00.')
print(f'O produto mais barato foi {produtoBarato} e seu preço foi R${preçoBarato:.2f}.')
print('{:-^40}'.format(' PROGRAMA FINALIZADO '))  # - < Põe traços, 40 < pula 40 caracteres, ^ < centraliza a frase
