from random import randint
from time import sleep
sena = []
dado = []
jogo = int(input('Quantos jogos quer que eu sorteie? '))
tot = 1
while tot <= jogo:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in dado:
            dado.append(num)
            cont += 1
        if cont >= 6:
            break
    dado.sort()
    sena.append(dado[:])
    dado.clear()
    tot += 1
print('-=' * 5, f'< SORTEANDO {jogo} JOGOS >', '-=' * 5)
for i, l in enumerate(sena):
    print(f'Jogo {i + 1}: {l}')
    sleep(0.4)
print('-=' * 5, '< BOA SORTE! >', '-=' * 5)
