from datetime import date
#import datetime
# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade,
# se ele ainda vai se alistar ao serviço militar
#, se é a hora exata de se alistar ou se já passou do tempo do alistamento.
#Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
anonascimento = int(input('Digite o seu ano de nascimento: '))
idade = date.today().year - anonascimento
if idade < 18:
    print('Quem nasceu em {}, tem {} anos'.format(anonascimento, idade))
    print('Você ainda se alistará ao serviço militar!')
    print('Faltam {} anos para você se alistar!'.format(18 - idade))
elif idade > 18:
    print('Quem nasceu em {}, tem {} anos'.format(anonascimento, idade))
    print('Você já passou do prazo para se alistar!')
    print('Seu prazo para alistamento foi há {} ano(s) atrás!'.format(idade - 18))
elif idade == 18:
    print('Quem nasceu em {}, tem {} anos'.format(anonascimento, idade))
    print('Esse é seu ano de alistamento militar, {}!'.format(date.today().year))

