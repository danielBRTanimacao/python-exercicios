def notas(*n, sit=False):
    """
    -> A função notas mostra as condições de um aluno
    : parametro n recebe varia notas
    : parametro sit retorna a situação do aluno
    : return retorn um dicionario r
    """
    r = {}
    r["Total"] = len(n)
    r["maior"] = max(n)
    r['menor'] = min(n)
    r['media'] = sum(n) / len(n)
    if sit == True:
        if r['media'] >= 7:
            r['situação'] = 'Boa'
        elif r['media'] >= 5:
            r['situação'] = 'Razoavel'
        else:
            r['situação'] = 'Pessimo'
    return r


#programa principal
resp = notas(4, 5, 6, sit=True)
print(resp)
