def dobrarValores(values):
    pos = 0
    while pos < len(values):
        values[pos] = values[pos] * 2
        pos += 1


#Programa Principal
valores = []
while True:
    v = int(input('Digite um valor (999 para parar): '))
    if v == 999:
        break
    valores.append(v)

resposta = str(input('Quer dobrar os valores da lista? [S/N]: ')).strip().upper()[0]
if resposta == 'S':
    dobrarValores(valores)
    print(f'\n{valores}')
elif resposta == 'N':
    print(f'\nOs valores foram {valores}')
