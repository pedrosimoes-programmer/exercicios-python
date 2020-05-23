#ESCOPO DE VARIÁVEIS:

#Escopo = Local onde a variável existe, ou onde ela não vai mais existir

#Escopo Global = quando a variável funciona em qualquer parte do programa
#Escopo Local = quando a variável só funciona em uma área, quando declarada em uma função, por exemplo

#Caso use o método global
def teste(b):
    global a  #Caso eu use o comando global, ele modificará a variável global, e não criará uma variável local!
    a = 6
    b += 4
    c = 2
    print(f'A local vale {a}')
    print(f'B local vale {b}')
    print(f'C local vale {c}')

a = 5
print(f'A global vale {a} (ANTES DE EXECUTAR A FUNÇÃO)')

teste(a)
print(f'A global, agora, vale {a} (DEPOIS DE EXECUTAR A FUNÇÃO)')