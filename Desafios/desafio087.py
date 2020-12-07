matriz = [[], [], []]
par = []
somap = somat = 0
tres = []
linha = []
for c in range(0, 3):
    for l in range(0, 3):
        num = int(input(f'Digite um valor para a posição [{c}][{l}]: '))
        matriz[c].append(num)
        if num % 2 == 0:
            par.append(num)
        if l == 2:
            tres.append(num)
        if c == 1:
            linha.append(num)
for soma in par:
    somap += soma
for soma1 in tres:
    somat += soma1
print('-=' * 15)
for c in range(0, 3):
    for l in range(0, 3):
        print(f'[{matriz[c][l]:^5}]', end='')
    print()
print('-=' * 15)
print(f'A soma dos valores pares é: {somap}')
print(f'A soma da terceira coluna é: {somat}')
print(f'O maior numero da segunda linha é: {max(linha)}')
