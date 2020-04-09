#Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
#- EQUILÁTERO: todos os lados iguais
#- ISÓSCELES: dois lados iguais, um diferente
#- ESCALENO: todos os lados diferentes
print('-' * 20, 'Programa Analisador de Triângulos', '-' * 20)
seg1 = float(input('Digite o valor do primeiro segmento: '))
seg2 = float(input('Digite o valor do segundo segmento: '))
seg3 = float(input('Digite o valor do terceiro segmento: '))
if seg1 < seg2 + seg3 and seg2 < seg1 + seg3 and seg3 < seg1 + seg2:
    if seg1 == seg2 and seg3: # outra possibilidade --> seg1 == seg2 == seg3:
        print('Os segmentos PODEM formar um triângulo do tipo EQUILÁTERO!')
    elif seg1 != seg2 != seg3 != seg1:
        print('Os segmentos acima PODEM formar um triângulo do tipo ESCALENO!')
    else:
        print('Os segmentos acima PODEM formar um triângulo do tipo ISÓSCELES!')
else:
    print('Os segmentos NÃO PODEM formar um triângulo!')
