def fatorial(n, mostrarConta):
    """
     Funcao que calcula o valor do fatorial de um numero, onde:
     param: n = valor inicial
     param: show = valor logico que mostra ou nao o calculo do fatorial
     return: valor do fatorial = param : f
    """
    f = 1
    if mostrarConta == 'S':
        for c in range(n, 0, -1):
            print(f'{c}', end='')
            if c == 1:
                print(' = ', end='')
            else:
                print(' x ', end='')
            f *= c
    else:
        for c in range(n, 0, -1):
            f *= c

    return f
    

#Programa Principal
valor = int(input('Qual o valor do fatorial a ser calculado: '))
show = str(input('Você quer ver o processo de fatorial? [Sim/Não]: ')).upper().strip()[0]
print(fatorial(valor, show))
r = str(input('Você quer ver as DocStrings da função? [Sim/Não]: ')).upper().strip()[0]
if r == 'S':
    help(fatorial)