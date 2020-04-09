#Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e
# a quantidade de dias pelos quais ele foi alugado.
# Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.
km = float(input('Digite o número de Km percorridos: '))
dias = float(input('Por quantos dias ele foi alugado? '))
total = (60*dias) + (0.15*km)
print('O preço a pagar pelo carro é: R${} '.format(total))