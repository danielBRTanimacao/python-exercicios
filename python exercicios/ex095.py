time = []
jogador = {}
partida = []
while True:
    jogador.clear()
    jogador['nome'] = str(input('Nome: '))
    tot = int(input(f"Quantas partidas {jogador['nome']} jogou? "))
    partida.clear()
    for c in range(0, tot):
        partida.append(int(input(f"    Quantos gols na partida {c}: ")))
    jogador['gols'] = partida[:]
    jogador['total'] = sum(partida)
    time.append(jogador.copy())
    while True:
        per = str(input("Quer continuar? [S/N] ")).strip().upper()[0]
        if per in 'SN':
            break
        print('ERRO! Tente usar apenas S ou N')
    if per == 'N':
        break
print('-=-'*30)
for i in jogador.keys():
    print(f"{i:<15}", end='')
for k, v in enumerate(time):
    print(f"{k:>4}", end='')
    for d in v.values():
        print(f"{str(d):<15}", end='')
    print()
print("---"*30)
while True:
    busca = int(input('Mostrar dados de qual jogador? 999 para: '))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'Não existe nenhum jogador com codigo {busca}')
    else:
        print(f"Levantamento do jogador {time[busca]['nome']}:")
        for i, g in enumerate(time[busca]['gols']):
            print(f'    No jogo {i} fez {g} gols')
    print("-"*40)
print("<< Volte sempre >>")