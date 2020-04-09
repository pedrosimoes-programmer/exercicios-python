# Fórmula da existência de triângulos: A soma dos dois lados SEMPRE tem que ser MAIOR que  a do terceiro
print('-=-' * 20)
print('Programa Analista de Triângulos')
print('-=-' * 20)
r1 = float(input('Digite o valor da primeira reta: '))
r2 = float(input('Digite o valor da segunda reta: '))
r3 = float(input('Digite o valor da segunda reta: '))
if r1 + r2 > r3:  # Forma certa: r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2
    print('O triângulo PODE existir!')
else:
    print('O triângulo NÃO PODE existir')
