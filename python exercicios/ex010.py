real = float(input("Quanto de dinheiro você tem na carteira? R$"))
# COM VARIAVEL
dolar = real / 5.15
euro = real / 5.12
print(f"Com R${real} você pode comprar US${dolar:.2f}")
print(f"E com R${real} você pode comprar EU${euro:.2f}")