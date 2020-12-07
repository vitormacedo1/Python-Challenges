from time import sleep
from random import randint
print(f'{"VAMOS RAVISAR!":^30}')
nome = str(input('Digite seu nome: '))
nx = 0
while True:
    rand = randint(5, 77) # mude conforme os desafios.
    print(f'Olá {nome.capitalize()} seu exercício a ser revisado é o {rand}')
    cont = str(input('Quer continuar? [S/N] ')).lower()
    if cont == 'n':
        break
    elif cont == 's':
        nx += 1
print(f'Você refez {nx + 1} exercícios. Continue estudando!')
