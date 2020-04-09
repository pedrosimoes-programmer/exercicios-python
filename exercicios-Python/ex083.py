#  Forma sem bugs
expressao = (str(input('Digite a expressão: ')))
pilhaParenteses = []
for v in expressao:
    if v == '(':
        pilhaParenteses.append('(')
    elif v == ')':
        if len(pilhaParenteses) > 0:
            pilhaParenteses.pop()
        else:
            pilhaParenteses.append(')')
            break
if len(pilhaParenteses) == 0:
    print(f'A expressão {expressao} está válida.')
else:
    print(f'A expressão {expressao} está inválida!')

#  Forma com bugs
#expressao = (str(input('Digite a expressão: ')))
#if expressao.count('(') == expressao.count(')'):
#    print('Sua expressão está válida.')
#else:
#    print('Sua expressão está inválida!')
