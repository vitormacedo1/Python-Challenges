fut = {}
lista = []

fut['nome'] = str(input('Digite o nome do jogador: ')).strip().capitalize()
jogo = int(input(f'Quantos jogos {fut["nome"]} jogou? '))
for c in range(0, jogo):
    lista.append(int(input(f'  Quantos gols no {c + 1}º jogo? ')))
    
fut['gols'] = lista[:]
fut['total'] = sum(lista)
print('-=' * 25)
print(fut)
print('-=' * 25)

for l, n in fut.items():
    print(f'O campo {l} tem o valor {n}')
print('-=' * 25)

print(f'O jogador {fut["nome"]} jogou {jogo} jogos.')
for x, c in enumerate(lista):
    print(f'    => Na partida {x + 1}, fez {c} gols.')
print('-=' * 25)
