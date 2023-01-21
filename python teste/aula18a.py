'''pessoas = [['Bababui', 10], ['Bico Seco', 16]]
print(pessoas[0][1])
teste = []
teste.append('bababui')
teste.append(18)
galera = []
galera.append(teste[:]) #Cria uma lista onde a variavel e nova
teste[0] = 'Bob'
teste[1] = 90
galera.append(teste[:])
print(galera)
galera = [['bob', 10], ['buiu', 32], ['moco', 43]]
print(galera[2][0
galera = [['bob', 10], ['buiu', 32], ['moco', 43]]
for c in galera:
    print(f"{c[0]} Tem {c[1]} de idade")'''
galera = []
dados = []
totm = totmen = 0
for c in range(0, 3):
    galera.append(str(input("Digite seu nome: ")))
    galera.append(int(input("Digite sua idade: ")))
    dados.append(galera[:])
    galera.clear()
for p in dados:
    if p[1] >= 21:
        print(f"{p[0]} é maior de idade")
        totm += 1
    else:
        print(f"{p[0]}é menor de idade")
        totmen += 1
print("O total de maior idade e {}")