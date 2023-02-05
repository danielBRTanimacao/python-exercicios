def area(l, c):
    a = l * c
    print(f"A area de um terreno {l}x{c} é de {a}m2")


print(" Controles de terreno ")
print("-"*15)
lar = float(input("Largura (m): "))
comp = float(input("Comprimento (m): "))
area(lar, comp)
