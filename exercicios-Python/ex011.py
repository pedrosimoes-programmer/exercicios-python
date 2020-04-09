#cada litro de tinta pinta 2m²
lparede = float(input('\33[7;33mDigite a largura da parede (em metros): '))
aparede = float(input('Digite a altura da parede (em metros): \33[m'))
area = lparede * aparede
print('\33[4;35mA área da sua parede é: {} m².'.format(area), end=' ''\33[m')
print('\33[4;35mPara pintar sua parede, serão necessários {} L de tinta'.format(area/2))
