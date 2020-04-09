import emoji
from time import sleep
print('\33[31m=' * 20, 'Contagem Regressiva para os Fogos de Artíficio', '=' * 20, '\33[m')

for c in range(10, -1, -1):
    print(c)
    sleep(1)
print(emoji.emojize('\33[34mOs fogos estão explodindo :fireworks:\33[m', use_aliases= True))
print('\33[35mBUM, BUM, BUM, BUM, BUM, BUM, BUM, POOW!!!\33[m')