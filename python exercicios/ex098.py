from time import sleep
def contador(inicio, fim, passo):
    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}:')
    sleep(1)
    if passo < 0:
        passo *= -1
    if passo == 0:
        passo =1
    if inicio > fim:
            fim = fim-passo
            passo = passo - passo*2
    for c in range(inicio, fim+1, passo):
        print(c, end='... ', flush=True)
        sleep(0.5)
    print('FIM!')
    print('-=' * 15)

print('-=' * 15)
contador(0,10,1)
contador(10, 0, 2)
print('Agora faça você! Personalize uma contagem!')
i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
print('-=' * 15)
contador(i, f, p)