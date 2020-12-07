lista = list()
for c in range(0, 5):
    lista.append(int(input(f'Digite um valor na posição {c}: ')))
print(f'A lista digitada foi {lista}')
print(f'O maior valor digitado foi {max(lista)} na(s) posições:', end='')
for i, v in enumerate(lista):
    if v == max(lista):
        print(f'{i}...', end='')
print(f'\nO menor numero digitado foi {min(lista)} na(s) posições:', end='')
for i, v in enumerate(lista):
    if v == min(lista):
        print(f'{i}...', end='')