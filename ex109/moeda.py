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
    res = f'{p}{n}'.replace('.', ',')
    return res