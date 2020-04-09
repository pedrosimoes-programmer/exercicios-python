from datetime import date
ano = int(input('Qual ano você quer analisar? Coloque 0 se quiser analisar o ano atual: '))
if ano == 0:
    ano = date.today().year
#anovalor = ano / 4
#anovalordois = ano / 400
# forma ruim ------->   if anovalor.is_integer() == True or anovalordois.is_integer() == True:

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano de {} é BISSEXTO!'.format(ano))
else:
    print('O ano de {} não é BISSEXTO!'.format(ano))
