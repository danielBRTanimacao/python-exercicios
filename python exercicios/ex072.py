cont = ('zero', 'um', 'dois', 'tres', 'quatro')
while True: 
    num = int(input("Digite um número de 0 a 4: "))
    if 0 <= num <= 4:
        break
    print("Tente de novo...")
escolha = cont[num]
print(f"Você escolheu o número {num} ele escrito é {escolha}")