lista = list()
lista.append(int(input('Digite um numero: ')))
seq = str(input('Quer continuar? [S/N] ')).strip().lower()
while True:
    if seq == 's':
        lista.append(int(input('Digite um numero: ')))
        seq = str(input('Quer continuar? [S/N] ')).strip().lower()
    elif seq == 'n':
        break
    else:
        print('Opção invalida. Tente novamente.')
        seq = str(input('Quer continuar? [S/N] ')).strip().lower()
lista.sort(reverse=True)
print(f'A lista tem {len(lista)} elementos.')
print(f'Os valores em ordem decrescente {lista}.')
if 5 in lista:
    print('Nesta lista contem o numero 5')
else:
    print('Nesta lista não contem o numero 5')
