lista = ('Lápis', 1.5,
         'Caneta', 2.5,
         'Borracha', 3)
print('=' * 36)
print(f'{"LOJA DAS LOJAS":^36}')
print('=' * 36)
for c in range(0, len(lista)):
    if c % 2 == 0:
        print(f'{lista[c]:.<30}', end='')
    else:
        print(f'R${lista[c]:>3.2f}')