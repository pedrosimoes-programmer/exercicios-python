#Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
#Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
#A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.
print('\33[36;7m-\33[m' * 35)
print('\33[31;1;mPrograma para Empréstimo Bancário\33[m')
print('\33[36;7m-\33[m' * 35)
valorcasa = float(input('\33[32mQual o valor da casa: R$\33[m'))
salario = float(input('\33[34mQual o seu salário: R$\33[m'))
anos = int(input('\33[30mEm quantos anos você pagará a casa:\33[m '))
presta = valorcasa / (anos * 12)

if presta > (salario * (30/100)):
    print('\33[37mEMPRÉSTIMO NEGADO!!!\33[m')
    print('Para pagar uma casa de R${}, as prestações mensais ficarão em: R${:.2f}, a serem pagas em {} anos'.format(
        valorcasa, presta, anos))
else:
    print('\33[35mEMPRÉSTIMO REALIZADO!!!\33[m')
    print('Para pagar uma casa de R${:.2f}, as prestações mensais ficarão em: R${:.2f}, a serem pagas em {} anos'.format
          (valorcasa, presta, anos))