from cgi import print_arguments


n = input("Digite algo: ")
print(f"O tipo primitivo desse valor e {type(n)}")
print(f"So tem espaços? {n.isspace()}")
print(f"É um número? {n.isnumeric()}")
print(f"É alfabetico? {n.isalpha()}")
print(f"É alfanúmerico? {n.isalnum()}")
print(f"Esta em maiusculo? {n.isupper()}")
print(f"Esta em minusculo? {n.islower()}")
print(f"Esta capitalizado? {n.istitle()}")