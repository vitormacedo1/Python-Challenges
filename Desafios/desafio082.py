lista = list()
pares = list()
impar = list()
lista.append(int(input('Digite um valor: ')))
seq = str(input('Quer continuar? [S/N] '))
while True:
    if seq == 's':
        lista.append(int(input('Digite um valor: ')))
        seq = str(input('Quer continuar? [S/N] '))
    elif seq == 'n':
        break
    else:
        print('Opção inválida. Tente Novamente.')
        seq = str(input('Quer continuar? [S/N] '))
lista.sort()
pares.sort()
impar.sort
print('=-' * 40)
print(f'A lista completa é {lista}')
for i, v in enumerate(lista):
    if v % 2 == 0:
        pares.append(v)
    else:
        impar.append(v)
print(f'A lista de pares é {pares}')
print(f'A lista de impares é {impar}')
