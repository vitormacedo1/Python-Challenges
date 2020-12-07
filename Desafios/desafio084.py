lista = list()
dado = list()
peso = list()
cont = 0
while True:
    lista.append(str(input('Nome: ')).capitalize())
    lista.append(int(input('Peso: ')))
    stop = str(input('Quer continua? [S/N] ')).strip().lower()
    dado.append(lista[:])
    peso.append(lista[1])
    lista.clear()
    cont += 1
    if stop in 'sn':
        if stop == 'n':
            break
    else:
        print('Erro. Tente novamente!')
        stop = str(input('Quer continua? [S/N] ')).strip().lower()
print(f'Foram cadastradas {cont} pessoas')
print(f'O maior peso cadastrado foi {max(peso):.2f}Kg. Peso de ', end='')
for c in dado:
    if c[1] == max(peso):
        print(f'{c[0]}', end=' ')
print(f'\nO menor peso foi {min(peso)}Kg. Peso de ', end='')
for n in dado:
    if n[1] == min(peso):
        print(f'{n[0]}', end=' ')