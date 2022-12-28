casa = float(input("Valor da casa: "))
sala = float(input("Salario do comprador: R$"))
anos = int(input("Digite em quantos anos ira pagar: "))
prestacao = casa / (anos * 12)
minimu = sala * 30  / 100
print(f"para pagar uma casa de R${casa:.2f} em {anos} anos a prestação sera de R${prestacao:.2f}")
if prestacao <= minimu:
    print("sua prestação foi concedida")
else:
    print("Sua prestação foi negada")