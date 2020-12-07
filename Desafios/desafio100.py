from random import randint
from time import sleep


def sort(sot):
    print('-=' * 27)
    for c in range(0, 5):
        sot.append(randint(1, 100))
    print(f'Sorteando 5 valores da lista: ', end='')    
    for r in sot:
        print(f'{r}', end=' ')
        sleep(0.3)
    print('PRONTO!')


def somaPar(lista):
    plus = 0
    print(f'Somando os valores pares de ', end='')
    for n in lista:
        if n % 2 == 0:
            plus += n
        print(f'{n}', end=', ')
    print(f'temos {plus}')
    print('-=' * 27)


numero = list()
sort(numero)
somaPar(numero)
