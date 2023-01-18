numeros = []
while True:
    n = int(input("Digite um valor: "))
    if n not in numeros:
        numeros.append(n)
    else:
        print("Esse número ja existe e sera deletado")
    per = str(input("Deseja continuar?[S/N] ")).lower().strip()[0]
    if per not in 'sn':
        while True:
            per = str(input("Deseja continuar?[S/N] ")).lower().strip()[0]
            if per in 'sn':
                break
    if per in 'n':
        break
print("-="*15)
numeros.sort()
print(f"Os valores digitados foram {numeros}")
