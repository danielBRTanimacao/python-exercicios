import moeda

p = float(input("Digite o preço: R$"))
print(f"A metade de {moeda.moeda(p)} é {moeda.metade(p, True)}")
