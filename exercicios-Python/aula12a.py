profissao = input('Qual a sua profissão: ')
if profissao.title() == 'Professor':
    print('Que bela profissão!')
    materia = input('Que matéria você ensina: '.title())
    if materia.title() == 'Geografia':
        print('Que bela matéria!')
    else:
        print('Odeio a matéria de {}!'.format(materia))
elif profissao.title() == 'Empresário':
    print('Uma excelente profissão!')
    salario = int(input('Qual seu salário: R$'))
    if salario >= 15000:
        print('Você ganha bastante! Parabéns!')
    else:
        print('Você ganha relativamente bem!')
        opcao = input('Quer um aumento? ')
        if opcao.title() == 'Sim' or 'Yes' or 'Sí':
            aumento = salario + (salario * 15/100)
            print('Parabéns, você recebeu um aumento de 15%, agora seu novo salário é: {}'.format(aumento))
        else:
            print('Você é um idiota! Agora não adianta mais chorar!')
elif profissao.title() == 'Geógrafo':
    print('Uma profissão difícil de ser encontrada no Brasil. Parabéns!')
else:
    print('Você tem uma profissão normal, {}!'.format(profissao.title()))
