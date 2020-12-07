word = ('aprender', 'curso', 'python', 'grátis',
        'amarelo', 'camila',' pitanga', 'bambam',
        'churros', 'de', 'carne')
for w in word:
    print(f'\nNa palavra {w.upper()} temos as vogais: ', end='')
    for letra in w:
        if letra.lower() in 'aáãâeéêíîioóõúu':
            print(letra, end='.')