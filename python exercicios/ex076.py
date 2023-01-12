listagem = ('lapis', 1.70, 'batata', 4.0, 'lapiseira', 0.5, 'caderno', 22.0)
print("--"*20)
print(f"{'LISTA DE PREÇOS':^40}")
print("--"*20)
for itens in range(0, len(listagem)):
    if itens % 2 == 0:
        print(f"{listagem[itens]:.<30}", end='')
    else:
        print(f"R${listagem[itens]:>8.2f}")
print("--"*20)
