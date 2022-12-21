diaAl = int(input("Quantos dias alugados: "))
kmRod = float(input("Quantos kilometros percorreu: "))
s = diaAl * 60 + kmRod * 0.15
print(f"O total a pagar e de R${s:.2f}")