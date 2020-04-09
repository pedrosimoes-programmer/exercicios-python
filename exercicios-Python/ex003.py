cores = {'azul': '\33[34m', 'brancosublinhado': '\33[4;30m', 'limpador': '\33[m', 'vermelho': '\33[31m'}
n1= int(input('Digite um número '))
n2 = int(input('Digite outro número '))
soma = n1 + n2
print('A soma entre {}{}{} e {}{}{} vale {}{}'.format(cores['azul'], n1, cores['limpador'], cores['brancosublinhado'], n2, cores['limpador'], cores['vermelho'], soma))
