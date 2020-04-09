#forma 1
valor = int(input('Digite um número qualquer: '))
if valor % 2 == 0:
    print('O número é PAR!')
else:
    print('O número é ÍMPAR!')

#forma 2
valor = int(input('Digite um número qualquer: '))
nvalor = valor / 2
if nvalor.is_integer() == True:
    print('O seu número é PAR!')
else:
    print('O seu número é ÍMPAR')
