num = int(input('Digite um numero inteiro: '))
tot = 0
for c in range(1, num + 1):
    if num % c == 0:
        print('\033[33m', end='')
        tot += 1
    else:
        print('\033[31m', end='')
    print(c, end=' ')
if tot == 2:
    print('\033[m\nO numero {} é PRIMO'.format(num))
else:
    print('\033[m\nO numero {} NÃO É PRIMO'.format(num))