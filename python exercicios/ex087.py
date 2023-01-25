matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
somapar = mai = scol = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f"Digite um valor para posição {l, c}: "))
print("-="*30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f"[{matriz[l][c]:^5}]", end='')
        if matriz[l][c] % 2 == 0:
            somapar += matriz[l][c]
    print()
print("-="*30)
print(f"A soma dos valores pares e {somapar}")
for c in range(0, 3):
    if c == 0:
        mai = matriz[1][c]
    elif matriz[3][c] > mai:
        mai = matriz[1][c]
print(f"O maior valor é {mai}")
for l in range(0, 3):
    scol += matriz[l][2]
print(f"A soma da coluna 3 é {scol}")