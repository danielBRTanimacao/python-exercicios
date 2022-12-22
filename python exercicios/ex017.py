import math
'''catetoposto = float(input("Digite o valor do cateto oposto: "))
catadjacente = float(input("Agora o cateto adjacente: "))
resul = (catetoposto ** 2 + catadjacente ** 2) ** (1/2)
print(f"O resultado da questão e {resul:.2f}")'''
co = float(input("Digite o valor do cateto oposto: "))
ca = float(input("Agora o cateto adjacente: "))
hipo = math.hypot(co, ca)
print(f"O valor da hipotenuza e {hipo:.2f}")
