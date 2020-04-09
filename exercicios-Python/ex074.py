from random import randint
n = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
print(f'Os valores sorteados foram {n}')
for c in range(0, len(n)):
    if c == 0:
        menor = maior = n[c]
    if menor > n[c]:
        menor = n[c]
    if maior < n[c]:
        maior = n[c]
print(f'O maior valor sorteado foi {maior}')  #Forma 1
print(f'O menor valor sorteado foi {menor}')  #Forma 1

print(f'O menor valor sorteado foi {min(n)}')  #Forma 2
print(f'O maior valor sorteado foi {max(n)}')  #Forma 2
