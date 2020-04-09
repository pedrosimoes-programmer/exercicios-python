def area(l, c):
    areaTerreno = l * c
    print(f'A área de um terreno {l}x{c} é {areaTerreno}m²')


#Programa Principal
print('     PROGRAMA CONTROLADOR DE TERRENOS')
area(float(input('Largura (m): ')), float(input('Comprimento (m): ')))
