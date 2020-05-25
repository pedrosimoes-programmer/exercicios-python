def voto(anoNascimento):
    from datetime import date
    idade = date.today().year - anoNascimento
    if idade < 16:
        return(f'Com {idade} anos: NÃO VOTA!')
    elif 16 <= idade < 18 or idade > 65:
        return(f'Com {idade} anos: VOTO OPCIONAL!')
    else:
        return(f'Com {idade} anos: VOTO OBRIGATÓRIO!')        


#Programa Principal
print('=' * 30)
ano = int(input('Em qual ano você nasceu? '))
print(voto(ano))
