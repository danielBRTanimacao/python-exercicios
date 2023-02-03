from datetime import datetime
dados = {}
dados['nome'] = str(input("Nome: "))
nasc = int(input("Ano de nascimento: "))
dados['idade'] = datetime.now().year - nasc
dados['ctps'] = int(input("Carteira de trabalho (0 se não tem): "))
if dados['ctps'] != 0:
    dados['contratação'] = int(input("Ano de contratação: "))
    dados['salario'] = float(input("Salario: "))
    dados['aposentadoria'] = dados['idade'] + ((dados['contratação'] + 35) - datetime.now().year)
for k, v in dados.items():
    print(f"{k} tem o valor {v}")
