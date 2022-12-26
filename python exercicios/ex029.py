vel = float(input("Digite a velocidade atual do carro: "))
if vel > 80:
    print("Multado vc passou do limite permitido que e de 80KM/h")
    multa = (vel - 80) * 7
    print(f"Vc pagara um multa de R${multa:.2f}")
else:
    print("Dirija com cuidado tenha um bom dia!")