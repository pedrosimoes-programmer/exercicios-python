def aumentar(n=0, taxa=0, formatado=True):
    '''
    --> Calcula o aumento de determinado preço, retornando o resultado
    com ou sem formatação, relativo à taxa informada.
    :param n: o preço que se quer ajustar
    :param taxa: a taxa de aumento referente ao preço (porcentagem; %)
    :param formatado: saída de valores formatada ou não?
    :return: o valor reajustado, com ou seu formatação
    '''
    res = n + (n * (taxa / 100))
    if formatado == True:
        return moeda(res)
    else:
        return res


def diminuir(n=0, taxa=0, formatado=True):
    '''
    --> Calcula a redução de determinado preço, retornando o resultado
    com ou sem formatação, relativo à taxa informada.
    :param n: o preço que se quer ajustar
    :param taxa: a taxa de redução referente ao preço (porcentagem; %)
    :param formatado: saída de valores formatada ou não?
    :return: o valor reajustado, com ou seu formatação
    '''
    res = n - (n * (taxa / 100))
    return res if formatado == False else moeda(res)


def dobro(n=0, formatado=True):
    '''
    --> Calcula o dobro de determinado preço, retornando o resultado
    com ou sem formatação.
    :param n: o preço que se quer dobrar
    :param formatado: saída de valores formatada ou não?
    :return: o valor reajustado ao dobro, com ou seu formatação
    '''
    res = n * 2
    return res if formatado == False else moeda(res)


def metade(n=0, formatado=True):
    '''
    --> Calcula a metade de determinado preço, retornando o resultado com ou
    sem formatação
    :param n: o preço a ser ajustado pela metade
    :param formatado: saída de valores será formatada ou não?
    :return: o valor pela metade, com ou sem formatação
    '''
    res = n / 2
    return res if formatado == False else moeda(res)

def moeda(n=0, moeda='R$'):
    '''
    --> Realiza a formatação do valor informado para valor monetário
    :param n: preço a ser formatado
    :param moeda: tipo de moeda usado na formatação (R$, U$, etc)
    :return: valor formatado em valor monetário
    '''
    return f'{moeda}{n:.2f}'.replace('.', ',')


def titulo(msg):
    '''
    --> Realiza a formatação de uma mensagem para um título
    :param msg: mensagem informada para formatação
    :return: mensagem formatada como título
    '''
    tam = len(msg) + 4
    print('=' * tam)
    print(f'  {msg}')
    print('=' * tam)

def resumo(n=0, taxaAumento=0, taxaRedução=0):
    '''
    --> Faz o resumo de um determinado preço com: o preço analisado; seu dobro; sua metade;
    seu aumento a uma taxa; sua redução a uma taxa;
    :param n: preço informado
    :param taxaAumento: taxa de aumento do preço (porcentagem; %)
    :param taxaRedução: taxa de redução do preço (porcentagem; %)
    :return:
    '''
    msg = 'Resumo do valor'
    titulo(msg) # .center(quantos_caracteres_para_centralizar 30) <-- para centralizar o texto
    print(f'Preço analisado:    \t{moeda(n)}')  # \t para tabulação
    print(f'Dobro do preço:     \t{dobro(n)}')
    print(f'Metade do preço:    \t{metade(n)}')
    print(f'{taxaAumento}% de aumento:     \t{aumentar(n, taxaAumento)}')
    print(f'{taxaRedução}% de aumento:     \t{diminuir(n, taxaRedução)}')
    print('=' * 19)
