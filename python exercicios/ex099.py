
def linha():
    print('-=' * 30)


def maior(*num):
    from time import sleep
    linha()
    i = 0
    print("Analisando os valores recebidos...")
    for n in num:
        sleep(.25)
        print(f'{n} ',end='')
        i += 1
    print(f'Foram infomados {i} valores.')
    if len(num) == 0:
        print(f'O maior valor informado foi 0.')
    else:
        print(f'O maior valor informado foi {max(num)}.')


maior(2,9,4,5,7,1)
maior(4,7,0)
maior(1,2)
maior(6)
maior()