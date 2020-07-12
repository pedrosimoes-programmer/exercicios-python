def aumentar(n=0, taxa=0, formatado=True):
    res = n + (n * (taxa / 100))
    if formatado == True:
        return moeda(res)
    else:
        return res


def diminuir(n=0, taxa=0, formatado=True):
    res = n - (n * (taxa / 100))
    return res if formatado == False else moeda(n)


def dobro(n=0, formatado=True):
    res = n * 2
    return res if formatado == False else moeda(n)


def metade(n=0, formatado=True):
    res = n / 2
    return res if formatado == False else moeda(n)

def moeda(n=0, moeda='R$'):
    return f'{moeda}{n:.2f}'.replace('.', ',')
