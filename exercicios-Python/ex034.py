salario = float(input('Digite o valor do seu salário: R$'))
if salario > 1250:
    aumento = salario + (salario*10/100)
    print('O seu antigo salário era R${:.2f} e o novo é: R${:.2f}'.format(salario, aumento))
else:
    aumento = salario + (salario*15/100)
    print('O seu antigo salário era R${:.2f} e o novo é: R${:.2f}'.format(salario, aumento))
