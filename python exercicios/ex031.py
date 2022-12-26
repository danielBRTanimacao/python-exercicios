v = float(input("Qual a distancia da sua viagem: "))
vm = v * 0.50
vl = v * 0.45
print(f"Você está preste a começar uma viagem de {v:.0f}KM")
if v <= 200:
    print(f"E o preço da sua viagem sera de R${vm:.2f}")
else:
    print(f"E o preço da sua viagem sera de R${vl:.2f}")