'''valor = list()
for cont in range(0, 5):
    valor.append(int(input('Digite um valor: ')))
for c, v in enumerate(valor):
    print(f'Na posição {c}, tem o valor {v}.')
print('Cheiguei no final da lista')'''
a = [2, 3, 4, 2, 8]
b = a[:] # recebe todos os valores assim quando se muda um não muda o outro
b[2] = 8
print(f'Lista A: {a}')
print(f'Lista B: {b}')