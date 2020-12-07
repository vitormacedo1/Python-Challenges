def lin():
    print('-=' * 27)


def analise(*num):
    lin()
    print('Analisando os valores passados...')
    for c in num:
        print(f'{c}', end=' ')
    print(f'Foram analisados {len(num)} numeros')
    if len(num) == 0:
        print('O maior valor informado foi 0')
    else:
        print(f'O maior valor informado foi {max(num)}')



analise(2, 9, 4, 5, 7, 2)
analise(1, 2)
analise(4, 7, 0)
analise(6)
analise()
