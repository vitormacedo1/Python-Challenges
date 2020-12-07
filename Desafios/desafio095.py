time = {}
jogador = []
gols = []
jogos = []
dado = []

while True:
    player = (str(input('Nome do jogador: '))).upper()
    jogador.append(player)
    jogo = (int(input(f'Quantos jogos {player} jogou? ')))
    jogos.append(jogo)
    for k in range(0, jogo):
        dado.append(int(input(f'  Quantos gols fez na {k + 1}º partida? ')))
    gols.append(dado[:])
    dado.clear()
    quest = str(input('Quer continuar?[S/N] '))
    if quest not in 'SsNn':
        print('ERROR. USE SOMENTE S ou N')
        quest = str(input('Quer continuar?[S/N] '))
    if quest in 'Nn':
        break
time['jogador'] = jogador[:]
time['gols'] = gols[:]
time['jogos'] = jogos[:]
print(time)

print(f'cod nome', f'{"gols":>15}', f'{"total":>20}')
print('--' * 27)
for v, n in enumerate(time['jogador']):
    gol = sum(gols[v])
    print(f'{v} {n}', f'             {time["gols"][v]:}', f'{gol:>18}')
print('--' * 27)

while True:
    
    busca = int(input('Qual jogador quer buscar dados?[999 P/ PARAR] '))
    if busca == 999:
        break
    if busca > len(jogador):
        print(f'Não existe jogador com códiogo {busca}')
        busca = int(input('Qual jogador quer buscar dados?[999 P/ PARAR] '))
    else:
        print('--' * 27)
        print(f'    -LEVANTAMENTO DO JOGAR {time["jogador"][busca]}-')
        for k, l in enumerate(time["gols"][busca]):
            print(f'        No jogo {k + 1} fez {l} gols')
    print('--' * 27)
print('PROGRAMA ENCERRADO!')
