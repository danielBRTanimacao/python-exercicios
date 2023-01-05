primeiro = int(input("primeiro termo: "))
razão = int(input("Digite a razão: "))
termo = primeiro
cont = 1
while cont <= 10:
    print(f"{termo} -> ", end='')
    termo += razão
    cont += 1
print("Fim")