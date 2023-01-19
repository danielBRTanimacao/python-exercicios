'''numeros = []
pares = []
impares = []
while True:
    n = int(input("Digite um valor: "))
    if n not in numeros:
        numeros.append(n)
    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(numeros)
    per = str(input("deseja continuar?[S/N] ")).strip().upper()[0]
    if per in 'N':
        break
print("-="*20)
print(f'Os valores que você digitou na lista são {numeros}')
print(f"Os valores pares são {pares}")
print(f"Os valores impares são {impares}")'''
numeros = [] #MANEIRA QUE O GUANABARA FEZ
pares = []
impares = []
while True:
    numeros.append(int(input("Digite um valor: ")))
    per = str(input("deseja continuar?[S/N] ")).strip().upper()[0]
    if per in 'N':
        break
for i, v in enumerate(numeros):
    if v % 2 == 0:
        pares.append(v)
    elif v % 2 == 1:
        impares.append(v)
print("-="*20)
print(f'Os valores que você digitou na lista são {numeros}')
print(f"Os valores pares são {pares}")
print(f"Os valores impares são {impares}")