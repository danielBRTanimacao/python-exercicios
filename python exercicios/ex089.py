ficha = []
while True:
    nome = str(input("Nome: "))
    nota1 = float(input("Nota 1: "))
    nota2 = float(input("Nota 2: "))
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], media])
    resp = str(input("Deseja continuar?[S/N] ")).upper()[0]
    if resp in 'Nn':
        break
print("-="*20)
print(f"{'N°':<5}{'NOME':<10}{'MEDIA':>8}")
print('-'*28)
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<9}{a[2]:>7.1f}')
while True:
    print("-"*30)
    opcao = int(input("Mostrar notas de qual aluno? [999 interrompe] "))
    if opcao == 999:
        print("FINALIZANDO...")
        break
    if opcao <= len(ficha) - 1:
        print(f"A nota do aluno {ficha[opcao][0]} é {ficha[opcao][1]}")
print("VOLTE SEMPRE...")