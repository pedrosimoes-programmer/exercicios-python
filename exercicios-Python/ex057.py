# Faça um programa que leia o sexo de uma pessoa,
# mas só aceite os valores 'M' ou 'F'. Caso esteja errado, peça a digitação novamente até ter um valor correto.
sexo = ''
sexo = str(input('Digite o seu sexo [M/F]: ')).strip().upper()[0]  # Tira os espaços/Tudo maiúsculo/Pega a 1ª letra
while sexo not in 'MmFf':
    sexo = str(input('Erro! Digite o seu sexo novamente [M/F]: ')).upper().strip()[0]
print('Sexo {} recebido com sucesso'.format(sexo))
