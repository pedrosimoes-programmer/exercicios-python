def aumentar(n=0, taxa=0, formatado=True):
    res = n + (n * (taxa / 100))
    if formatado == True:
        return moeda(res)
    else:
        return res


def diminuir(n=0, taxa=0, formatado=True):
    res = n - (n * (taxa / 100))
    return res if formatado == False else moeda(res)


def dobro(n=0, formatado=True):
    res = n * 2
    return res if formatado == False else moeda(res)


def metade(n=0, formatado=True):
    res = n / 2
    return res if formatado == False else moeda(res)

def moeda(n=0, moeda='R$'):
    return f'{moeda}{n:.2f}'.replace('.', ',')


def titulo(msg):
    tam = len(msg) + 4
    print('=' * tam)
    print(f'  {msg}')
    print('=' * tam)

def resumo(n=0, taxaAumento=0, taxaRedução=0):
    msg = 'Resumo do valor'
    titulo(msg) # .center(quantos_caracteres_para_centralizar 30) <-- para centralizar o texto 
    print(f'Preço analisado:    \t{moeda(n)}')  # \t para tabulação
    print(f'Dobro do preço:     \t{dobro(n)}')
    print(f'Metade do preço:    \t{metade(n)}')
    print(f'{taxaAumento}% de aumento:     \t{aumentar(n, taxaAumento)}')
    print(f'{taxaRedução}% de aumento:     \t{diminuir(n, taxaRedução)}')
    print('=' * 19)
