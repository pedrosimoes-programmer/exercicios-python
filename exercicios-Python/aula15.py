c = 0
while True:
    if c == 26981:
        break
    print(c)
    c += 1

# F Strings: print(f'O {nome} tem {idade} anos.')
nome = str(input('Digite seu nome: '))
idade = int(input('Digite sua idade: '))
sal = float(input('Digite seu salário: '))
print(f'O {nome} tem {idade} anos.')  # Python 3.6+
print('O {} tem {} anos.'.format(nome, idade))  # Python 3
print('O %s tem %d anos.' % (nome, idade))  # Python 2

print(f'O {nome} tem {idade} anos e ganha R${sal:.2f}')