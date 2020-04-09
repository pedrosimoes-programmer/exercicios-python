for c in range(1, 51):
    if c % 2 == 0:
        print(c)
#forma 2

for c in range(2, 51, 2): # gasta menos processador, ou seja, menos trabalho
    print(c, end='  ')
