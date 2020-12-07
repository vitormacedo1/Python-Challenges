lista = list()
lista.append(int(input('Digite um valor: ')))
print('Valor computado com sucesso...')
while True:
    cont = str(input('Quer continur? [S/N] ')).strip().lower()
    if cont == 's':
        lista.append(int(input('Digite um valor: ')))
        print('Valor computado com sucesso...')
    elif cont == 'n':
        break
    else:
        print('Opção solicitada inválida. Tente novamente.')
print('Operação cancelado com sucesso.')
print(f'A lista registrada foi {lista}')