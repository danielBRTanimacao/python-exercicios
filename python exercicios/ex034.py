sala = float(input("Digite o valor do seu salario atual: "))
cal =  (10/100) * 1250 + 1250
cal2 =  (15/100) * 1250 + 1250
if sala > 1250:
    print(f"Você recebeu um aumento de 10% agora seu salario e de R${cal:.2f}")
else:
    print(f"Você recebeu um aumento de 15% agora seu salario e de R${cal2:.2f}")