temp = []
principal = []
maior = menor = 0
while True:
    temp.append(str(input("Digite o seu nome: ")))
    temp.append(float(input("Qual o seu peso? ")))
    if len(principal) == 0:
        maior = menor = temp[1]
    else:
        if temp[1] > maior:
            maior = temp[1]
        if temp[1] < menor:
            menor = temp[1] # Ou pode usar max() é min()
    principal.append(temp[:])
    temp.clear()
    resposta = str(input("Deseja continuar?[S/N] ")).upper()
    if resposta in 'N':
        break
print("-=-"*30)
print(f"Os dados foram {principal}")
print(f"Foram armazenadas {len(principal)}")
print(f"O maior peso é {maior:.1f}Kg, de ", end='')
for p in principal:
    if p[1] == maior:
        print(f"{p[0]}...", end=' ')
print()
print(f"O menor peso é {menor:.1f}Kg, de ", end='')
for p in principal:
    if p[1] == menor:
        print(f"{p[0]}...", end=' ')