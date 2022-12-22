import random
alun1 = input("Primeiro aluno: ")
alun2 = input("Segundo aluno: ")
alun3 = input("Terceiro aluno: ")
alun4 = input("Quarto aluno: ")
escolista = [alun1, alun2, alun3, alun4]
print(f"O aluno escolhido foi {random.choice(escolista)}")