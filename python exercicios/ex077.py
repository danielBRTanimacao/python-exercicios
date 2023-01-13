palavras = 'APRENDER', 'PROGRAMAR', 'LINGUAGEM', 'PYTHON', 'CURSO'
for p in palavras:
    print(f"\nA palavra {p} temos", end=' ')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')
