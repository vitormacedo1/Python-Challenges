def lin():
    print('-' * 29)


def aumentar(n=0, p=0, clean=False):
    res = n + (n * p / 100)
    return res if not clean else moeda(res)


def diminuir(n=0, p=0, clean=False):
    res = n - (n * p / 100)
    return res if not clean else moeda(res)


def dobro(n=0, clean=False):
    res = n * 2
    return res if not clean else moeda(res)


def metade(n=0, clean=False):
    res = n / 2
    return res if not clean else moeda(res)


def moeda(n=0, p='R$', clean=False):
    res = f'{p}{n:>.2f}'.replace('.', ',')
    return res


def resumo(n=0, p=0, c=0):
    lin()
    print(f'{"RESUMO DO VALOR":^29}')
    lin()
    print(f'Preço analisado: \t{moeda(n)}')
    print(f'Dobro do preço: \t{dobro(n, True)}')
    print(f'{p}% de aumento: \t{aumentar(n, p, True)}')
    print(f'{c}% de redução: \t{diminuir(n, c, True)}')
    lin()
