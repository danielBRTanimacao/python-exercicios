primeiro = int(input("primeiro termo: "))
razão = int(input("Digite a razão: "))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while cont <= total:
        print(f"{termo} -> ", end='')
        termo += razão
        cont += 1
    print("Pausa")
    mais = int(input("Quantos termos você que mostrar a mais? "))
print("Acabou")

