def aumentar(n=0, p=0):
    res = n + (n * p / 100)
    return res


def diminuir(n=0, p=0):
    res = n - (n * p / 100)
    return res


def dobro(n=0):
    res = n * 2
    return res


def metade(n=0):
    res = n / 2
    return res


def moeda(n=0, p='R$'):
    res = f'{p}{n}'.replace('.', ',')
    return res