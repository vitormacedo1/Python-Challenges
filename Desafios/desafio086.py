matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for c in range(0,3):
    for l in range(0,3):
        matriz[c][l] = int(input(f'Digite uma valor para posição [{c}][{l}]: '))
for l in range(0,3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()

