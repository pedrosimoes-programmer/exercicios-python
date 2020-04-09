nome = input('\33[31mDigite seu nome: \33[m')
sal = float(input('\33[0;33mDigite o seu salário: \33[m'))
if sal >= 1500.0:
    newsal = sal + (sal * 15/100)
else:
    newsal = sal + (sal * 30/100)
print('\33[34mParabéns {}, o seu novo salário é: {:.2f}!'.format(nome, newsal))
