from random import sample
n1 = input("Primeiro aluno: ")
n2 = input("Segundo aluno: ")
n3 = input("Terceiro aluno: ")
n4 = input("Quarto aluno: ")
lista = [n1, n2, n3, n4]
escordem = sample(lista, 4)
print(f"Os que irão apresentar o trabalho primeiro são \n{escordem}")