def voto(anoNascimento):
    from datetime import date
    valor = date.today().year - anoNascimento
    return valor


#Programa Principal
print('=' * 30)
ano = int(input('Em qual ano você nasceu? '))
idade = voto(ano)
if idade >= 16 and idade < 18 or idade >= 70:
    print(f'Com {idade} anos, o voto é OPCIONAL!')
if idade >= 18 and idade < 70:
    print(f'Com {idade} anos, o voto é OBRIGATÓRIO!')
if idade < 16:
    print(f'Com {idade} anos, NÃO VOTA!')
