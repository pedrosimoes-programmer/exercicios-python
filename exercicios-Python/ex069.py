print('-=' * 20, 'CADASTRO DE USUÁRIOS', '-=' * 20)
r = ''
mais18 = homens = mulheresMenos20 = 0
while True:
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]:')).strip().upper()[0]
    while sexo not in 'M/F':
        sexo = str(input('Sexo [M/F]:')).strip().upper()[0]
    if idade > 18:
        mais18 += 1
    if sexo == 'M':
        homens += 1
    if sexo == 'F' and idade < 20:
        mulheresMenos20 += 1
    r = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    while r not in 'S/N':
        r = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if r == 'N':
        break
print(f'''Ao todo, temos {homens} homens, {mais18} pessoas acima de 18 anos e 
{mulheresMenos20} mulheres abaixo de 20 anos''')