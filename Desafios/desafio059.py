num = 0
n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
while num != 4:
    print('O que deseja fazer?')
    print('[ 0 ] Somar \n[ 1 ] Multiplicar \n[ 2 ] Maior \n[ 3 ] Novos Numeros \n[ 4 ] Sair ')
    num = int(input('Digite uma operação: '))
    if num == 3:
        n1 = int(input('Digite um valor: '))
        n2 = int(input('Digite outro valor: '))
        print('[ 0 ] Somar \n[ 1 ] Multiplicar \n[ 2 ] Maior \n[ 3 ] Novos Numeros \n[ 4 ] Sair ')
        num = int(input('Digite uma operação: '))
    elif num > 4:
        print('Operação inválida!')
        print('[ 0 ] Somar \n[ 1 ] Multiplicar \n[ 2 ] Maior \n[ 3 ] Novos Numeros \n[ 4 ] Sair ')
        num = int(input('Digite uma operação: '))
    elif num == 1:
        print('{} multiplicado com {} é {}'.format(n1, n2, n1 * n2))
    elif num == 2:
        if n1 > n2:
            print('{} é maior que {}'.format(n1, n2))
        elif n1 < n2:
            print('{} é maior que {}'.format(n2, n1))
        else:
            print('Os 2 numeros são iguais.')
    elif num == 0:
        print('{} somado com {} é {}'.format(n1, n2, n1 + n2))

print('Operação finalizada!')
