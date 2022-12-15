n1 = float(input("Digite sua primeira nota: "))
n2 = float(input("Digite a segunda: "))
m = (n1 + n2) / 2
print(f"Sua media e {m:.1f}")
if m >= 6:
    print("Sua media foi boa parabens!")
else:
    print("Vix essa media ai ta uma cagada!")