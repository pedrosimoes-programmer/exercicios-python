#Retorno de Variáveis

def somar(a=0, b=0, c=0):
    s = a + b + c
    return s  #Usando o comando return, é possível retornar um valor a partir da função, e colocá-la numa variável, assim, usando-a da forma que desejar

r1 = somar(2, 4)
r2 = somar(3, 5, 4)
r3 = somar(8)
print(f'Os cálculos foram {r1}, {r2} e {r3}.')