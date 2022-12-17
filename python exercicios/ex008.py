d = float(input("Digite uma distancia em metros: "))
km = d / 1000
hm = d / 100
dam = d / 10
dm = d * 10
cm = d * 100
mm = d * 1000
print(f"A medida de {d} corresponde a \n{km}km \n{hm}hm \n{dam}dam \n{dm:.0f}dm \n{cm:.0f}cm \n{mm:.0f}mm")
