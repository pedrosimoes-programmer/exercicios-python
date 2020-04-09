def soma(* valores):
    s = 0
    for num in valores:
        s += num
    print(f'Somandos os valores {valores}, a soma é: {s}')


#Programa Principal
soma(0, 3, 45, 6)
soma(4, 7, 3)
soma(4)
soma(4, 3)