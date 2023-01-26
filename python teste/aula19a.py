'''pessoas = {'nome': 'Bababui', 'idade': '90', 'sexo': 'Masculino'}
del pessoas['sexo']
pessoas['peso'] = 98.5
for k, v in pessoas.items(): tambem a o key() e values()
    print(f"{k} = {v}")
#Agora usando em listas
brasil = []
estado1 = {'uf': 'Brasilia', 'sigla': 'BR'}
estado2 = {'uf': 'Pernambuco', 'sigla': 'PE'}
brasil.append(estado1)
brasil.append(estado2)
print(brasil)'''
estado = dict()
brasil = list()
for c in range(0,3):
    estado['uf'] = str(input("Digite o nome do estado: "))
    estado['sigla'] = str(input("Digite a sigla: "))
    brasil.append(estado.copy()) #e a mesma coisa de [:] para copiar nos dicionarios
for e in brasil:
    for k, v in e.items(): #k são as chaves e v e o valor
        print(k, v)
