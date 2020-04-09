#forma simples
nome = input('Qual é seu nome: ').upper()
if nome == 'PEDRO':
    print('Nome esplêndido!')
else:
    print('Nome normal')
print('Bom dia, {}'.format(nome.title()))

#forma composta
nome = input('Qual é seu nome: ').upper()
if 'PEDRO DE OLIVEIRA SIMÕES' in nome:
    print('O melhor nome do mundo')
else:
    print('Outro nome normal')
print('Bom dia, {}'.format(nome.title()))