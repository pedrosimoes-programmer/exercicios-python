from datetime import date
#A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
#- Até 9 anos: MIRIM
#- Até 14 anos: INFANTIL
#- Até 19 anos: JÚNIOR
#- Até 25 anos: SÊNIOR
#- Acima de 25 anos: MASTER
print('\33[34mConfederação Nacional de Natação\33[m')
ano = int(input('\33[36mDigite o ano de nascimento do atleta: \33[m'))
idade = date.today().year - ano
if idade <= 9:
    print('O atleta com {} anos, encontra-se na categoria MIRIM!'.format(idade))
elif idade > 9 and idade <= 14:
    print('O atleta com {} anos, encontra-se na categoria INFANTIL!'.format(idade))
elif idade > 14 and idade <= 19:
    print('O atleta com {} anos, encontra-se na categoria JÚNIOR!'.format(idade))
elif idade > 19 and idade <= 25:
    print('O atleta com {} anos, encontra-se na categoria SÊNIOR!'.format(idade))
elif idade > 25:
    print('O atleta com {} anos, encontra-se na categoria MASTER!'.format(idade))
