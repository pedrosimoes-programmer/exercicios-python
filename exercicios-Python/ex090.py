aluno = dict()
aluno['nome'] = str(input('Nome do aluno: '))
aluno['média'] = float(input(f'Média de {aluno["nome"]}: '))
if aluno['média'] >= 7.0:
    aluno['situação'] = 'Aprovado'
elif aluno['média'] >= 5:
    aluno['situação'] = 'em Recuperação'
elif aluno['média'] < 5:
    aluno['situação'] = 'Reprovado'
print('=' * 50)
# Forma 1: print(f'O aluno {aluno["nome"]} tirou {aluno["média"]} e está {aluno["situação"]}.')
# Forma 2:
for k, v in aluno.items():
    print(f'{k} é igual a \33[31m{v}\33[m')
