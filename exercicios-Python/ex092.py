from datetime import date
print('<   CADASTRAMENTO DE FUNCIONÁRIOS   >')
pessoa = {'nome': str(input('Nome: ')),
          'idade': date.today().year - int(input('Ano de nascimento: ')),
          'carteiraTrabalho': int(input('Carteira de Trabalho (0 caso não tenha): '))}
if pessoa['carteiraTrabalho'] != 0:
    pessoa['anoContratação'] = int(input('Ano de contratação: '))
    pessoa['salário'] = float(input('Salário: R$'))
    pessoa['aposentadoria'] = pessoa['idade'] + ((pessoa['anoContratação'] + 35) - date.today().year)
print('=' * 50)
for k, v in pessoa.items():
    print(f'{k} tem o valor {v}')
