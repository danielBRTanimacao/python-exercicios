num = int(input("Digite um nuemero inteiro qualquer: "))
print('''Escolha uma das bases para converção
[1] converter para BINARIO
[2] converter para OCTAL
[3] para HEXADECIMAL''')
op = int(input('Qual e sua opção: '))
if op == 1:
    print(f"{num} convertido paara BINARIO e {bin(num)[2:]}")
elif op == 2:
    print(f"{num} convertido para OCTAL e {oct(num)[2:]}")
elif op == 3:
    print(f"{num} convertido para HEXADECIMAL e {hex(num)[2:]}")
else:
    print("Esse número não esta na lista por favor tente de novo")