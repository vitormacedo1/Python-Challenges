'''soma = 0
for c in range(1, 500, 2):
    multiplo = (c % 3 == 0)
    if multiplo == True:
        print(c, 'é multiplo ')
        soma =
    else:
        print(c, 'não multiplo')
    soma = soma + multiplo
print('O valor do somatório dos numeros primos divisiveis por 3 é {}'.format(soma))'''
soma = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        soma = soma + c
        print(c, 'É multiplo,', end=' ')
print('\nA soma é {}'.format(soma))


