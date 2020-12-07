from random import randint
s = 0
while True:
    pc = randint(1, 5)
    jogador = str(input('PAR ou IMPAR: ')).strip().lower()
    num = int(input('Qual numero vai jogar (1 a 5)? '))
    rodada = num + pc
    s += 1
    if jogador == 'par':
        if rodada % 2 == 0:
            print(f'O computador jogou {pc} e o jogador {num} que somados resultam em {rodada}')
            print('Jogador venceu. Quer mais uma?')
            print('-'*60)
        else:
            break
    elif jogador == 'impar':
        if rodada % 2 == 0:
            break
        else:
            print(f'O computador jogou {pc} e o jogador {num} que somados resultam em {rodada}.')
            print('Jogador venceu. Quer mais uma?')
            print('-'*60)
print(f'o computador jogou {pc} e o jogador {num} que somados resultam em {rodada}')
print(f'PC ganhou. A TECNOLOGIA TE SUPEROU EM {s} RODADAS!')
print('-'*60)
