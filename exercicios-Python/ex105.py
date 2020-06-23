def notas(*notes, sit=False):
    #DOC STRING 
    """
    -> Função para analisar notas e situações de diversos alunos;
    :param notes = uma ou mais notas recebidas (aceita várias);
    :param sit = valor opcional que indica se deve ou não adicionar a situação;
    :return: dicionários com várias informações sobre as notas dos alunos;
    
    """
    dicionario = {}
    dicionario['notas'] = notes #(RETIRAR AO FINAL DA FUNÇÃO!)
    maiorNota = menorNota = cont = 0
    dicionario['total'] = len(dicionario['notas'])
    while cont < len(dicionario['notas']): # VERIFICAÇÃO DE MAIOR E MENOR NOTAS (VER ERRO NO FOR (ENUMERATE))
        if cont == 0:
            maiorNota = menorNota = dicionario['notas'][cont]
        else:
            if dicionario['notas'][cont] > maiorNota:
                maiorNota = dicionario['notas'][cont]
            if dicionario['notas'][cont] < menorNota:
                menorNota = dicionario['notas'][cont]
        cont += 1
    dicionario['maior'] = maiorNota  # PODERIA TER USADO O MÉTODO MAX(notes)
    dicionario['menor'] = menorNota  # PODERIA TER USADO O MÉTODO MIN(notes)
    somaNotas = sum(dicionario['notas'])
    dicionario['média'] = somaNotas / dicionario['total']
    if sit == True:     #OPCIONAL (RETIRAR CASO NÃO HOUVER AO FINAL DA FUNÇÃO!)
        if dicionario['média'] < 6:
            dicionario['situacao'] = 'RUIM'
        if dicionario['média'] >= 5 and dicionario['média'] < 7:
            dicionario['situacao'] = 'RAZOÁVEl'
        if dicionario['média'] > 7:
            dicionario['situacao'] = 'BOA'
    return(dicionario)


# Programa principal
resp = notas(1.5, 2.5, 10, 10, sit=True)
print(resp)
help(notas)
