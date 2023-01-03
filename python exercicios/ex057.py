'''c = 1
while c != 'M' and c != 'F':
    c = str(input("Informe seu sexo [M/F]: ")).upper()
    if c == 'M':
        print("Sexo M registrdo com sucesso")
    if c == 'F':
        print("Sexo F registrado com sucesso")
    if c != 'M' and c!= 'F':
        print("Por favor tente de novo")
print("Acabou")'''

#ou
sexo = str(input("Informe o seu sexo [M/F]: ")).strip().upper()[0] #do upper pegar apenas a primeira letra
while sexo not in 'MF': #enquanto sexo não estiver em M e F
    sexo = str(input("Dados invalidos. Por favor informe seu sexo de novo: ")).strip().upper()[0]
