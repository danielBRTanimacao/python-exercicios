listanum = []
for c in range(0, 5):
    listanum.append(int(input(f"Digite um valor na posição {c}: ")))
'''
    if c == 0:
        mai = men = listanum[0]
    else:
        if listanum[c] > mai:
            mai = listanum[c]   PODE USAR ESSA FORMA DE DESCOBRIR O MAIOR E MENOR TAMBEM
        if listanum[c] < men:
            men = listanum[c]
'''
mai = max(listanum)
men = min(listanum)
print("-="*30)
print(f"Você digitou os valores {listanum}")
print(f"O maior valor é {mai} nas posições ", end='')
for p, v in enumerate(listanum): #Lembrar do enumerate
    if v == mai:
        print(f"{p}... ", end='')
print()
print(f"O menor valor e {men} na posição ", end='')
for p, v in enumerate(listanum):
    if v == men:
        print(f"{p}... ", end='')
print()
