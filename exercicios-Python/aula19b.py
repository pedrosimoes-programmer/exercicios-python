pessoa = dict()
pessoa['nome'] = str(input('Nome: '))
pessoa['idade'] = int(input('Idade: '))
pessoa['sexo'] = str(input('Sexo: '))[0]
del pessoa['sexo']
print(pessoa)