pessoa = {}
galera = list()
soma = media = 0
while True:
    pessoa.clear()
    pessoa['nome'] = str(input("Nome: "))
    while True:
        pessoa['sexo'] = str(input("Sexo [M/F]: ")).upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print("ERRO, tente de novo, digite apenas M ou F")
    pessoa['idade'] = int(input("Idade: "))
    soma += pessoa['idade']
    galera.append(pessoa.copy())
    while True:
        per = str(input("Deseja continuar? [S/N]: ")).strip().upper()[0]
        if per in 'SN':
            break
        print("Erro responda com S ou N")
    if per == 'N':
        break
print("-=-"*30)
print(f"Ao todo temos {len(galera)} pessoas contratadas")
media = soma / len(galera)
print(f"A media de idade e {media:5.2f} anos")
print("As mulheres cadastradas foram ", end='')
for p in galera:
    if p['sexo'] == 'F':
        print(f"{p['nome']} ", end='')
print()