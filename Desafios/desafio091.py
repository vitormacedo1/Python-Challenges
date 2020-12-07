from random import randint
from time import sleep
from operator import itemgetter
dado = {'jogador1': randint(1, 6),
        'jogador2': randint(1, 6),
        'jogador3': randint(1, 6),
        'jogador4': randint(1, 6)}

print('-=' * 3, '< JOGOS DE DADOS >', '-=' * 4) 
for k, v in dado.items():
    print(f'    {k} tirou {v} nos dados.')
    sleep(0.5)
print('-=' * 17) 

ranking = list()
ranking = sorted(dado.items(), key=itemgetter(1), reverse=True)
print(f"{'RANKING':^35}")
for l, m in enumerate(ranking):
    print(f'    {l+1}º lugar: {m[0]} jogou {m[1]}')
print('-=' * 17)
