frase = input('Digite uma frase: ').strip()
print(f"A letra A aparece {frase.lower().count('A')}")
print(f'A primeira letra A aparece na prosição {frase.lower().find("A")}')
print(f"A ultima letra A aparece na posição {frase.lower().rfind('A'[-1])}")