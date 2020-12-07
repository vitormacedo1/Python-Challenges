def partida(a='<desconhecido>', b=0):
    """
    -> The function print 'a' for the soccer's player's name
    and b for how many goals he scored.
    """
    print(f'O {a} fez {b} gol(s) no campeonato')

### MAIN PROGRAM ###

jogador = str(input('Nome do jogador: ')).lower().capitalize()
gols = str(input('Números de gols: '))
if gols.isnumeric():
    g = int(gols)
else:
    g = 0
if jogador.strip() == '':
    partida(b=g)
else:
    partida(jogador, g)
help(partida)