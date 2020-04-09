#Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
#- à vista dinheiro/cheque: 10% de desconto
#- à vista no cartão: 5% de desconto
#- em até 2x no cartão: preço formal
#- 3x ou mais no cartão: 20% de juros
print('-' * 20, 'Lojas Pedro', '-' * 20)
preço = float(input('Digite o valor a ser pago pelas compras: R$'))
formapagamento = int(input('''1 para: à vista dinheiro/cheque
2 para: à vista no cartão
3 para: até 2x no cartão
4 para: 3x ou mais no cartão
Digite a forma como deseja realizar o pagamento: '''))
if formapagamento == 1:
    desconto = preço - (preço * 0.1)
    print('\33[31mA forma de pagamento escolhida foi à vista dinheiro/cheque.')
    print('O valor com o desconto ficou: R${:.2f}\33[m'.format(desconto))
elif formapagamento == 2:
    desconto = preço - (preço * 0.05)
    print('\33[35mA forma de pagamento escolhida foi à vista no cartão.')
    print('O valor com o desconto ficou: R${:.2f}\33[m'.format(desconto))
elif formapagamento == 3:
    parcelas = preço / 2
    print('\33[33mA forma de pagamento escolhida foi em até 2x no cartão.')
    print('Sua compra será parcelada em 2x de R${:.2f} sem JUROS'.format(parcelas))
    print('O preço total ficou R${:.2f}\33[m'.format(preço))
elif formapagamento == 4:
    totalparcelas = int(input('Quantas parcelas: '))
    juros = preço + (preço * 0.2)
    parcela = juros / totalparcelas
    print('\33[32mA forma de pagamento escolhida foi em 3x ou mais no cartão.')
    print('Sua compra será parcelada em {}x de R${:.2f} com 20% de JUROS'.format(totalparcelas, parcela))
    print('O preço total ficou R${:.2f}\33[m'.format(juros))
else:
    print('\33[36mOPÇÃO INVÁLIDA! Tente novamente!\33[m')
