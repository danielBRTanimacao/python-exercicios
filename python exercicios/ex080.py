lista = []
for c in range(0, 5):
    n = int(input("Digite um valor: "))
    if c == 0 or n > lista[-1]:
        lista.append(n)
        print("O valor foi adicionado no final da lista")
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                print(f"O valor foi adicionado na posição {pos} da lista")
                break
            pos += 1
print("-="*20)
print(f"Os valores digitados foram {lista}")