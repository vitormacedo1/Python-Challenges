def lin() :
    print('-' * 35)


def red(msg):
    print(f'\033[0;31m{msg}\033[m')


def yellow(msg):
    print(f'\033[0;33m{msg}\033[m',end='')


def blue(msg):
    print(f'\033[0;34m{msg}\033[m')


def erro(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            red('ERROR. Digite uma opção válida!')
            continue
        else:
            return n


