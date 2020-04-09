lanches = ['Hambúrguer', 'Refrigerante', 'Sorvete', 'Pudim']
num = [0, 5, 3, 1]
print(lanches)
lanches[3] = 'Maçã'
print(lanches)
lanches.append(len(lanches))  # Adiciona um elemento na última posição
print(lanches)
lanches.insert(1, 'Batata Frita')  # Adiciona um elemento na posição que eu quiser
print(lanches)
print(lanches[3])
print(f'Esse menu tem {len(lanches) - 1} elementos')
num.sort()  # Organiza os elementos em ordem do menor ao maior
print(num)
num.sort(reverse=True)  # Organiza os elementos em ordem do maior ao menor
print(num)
if 7 in num:  # Teste para eliminar um elemento
    num.remove(7)
else:
    print('Não há o número 7 na lista!')
print(num)
lanches.pop()
print(lanches)