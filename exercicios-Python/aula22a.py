def contador(i, f, p):
    #Quando abre-se 3 aspas duplas, temos uma Docstring, a partir daí o comando help(parâmetro) passa a funcionar com o que eu escrever
    """
    Realiza uma contagem, onde i == início da contagem, f == final da contagem e p == passo da contagem!
    """
    c = i
    while c <= f:
        print(f'{c}', end=' ')
        c += p
    print('FIM!')

def Multiplicar(a=1, b=1, c=1):  # Quando põe-se a=0, b=0, c=0, temos parâmetros opcionais, então caso eu não os chame, o programa não dará erro e ele passará a valer o que eu coloquei
    """
    Funcao que multiplica numeros! 
    a == Primeiro valor;
    b == Segundo valor;
    c == Terceiro valor;
    """
    multi = a * b * c
    print(f'O resultado da multiplicação é {multi}.')


#Interactive Help (Maneiras de Documentação no Python)
help(print)

help(input)
print(input.__doc__)
#NÃO NECESSARIAMENTE O HELP() e o __doc__ vão ter as mesmas coisas!

contador(2, 10, 2)
help(contador)

help(Multiplicar)

Multiplicar(5, 5, 5)
Multiplicar(3, 2)
Multiplicar(4)
Multiplicar()
Multiplicar(c = 4, a= 3)
