def ajuda(com):
    help(com)


def titulo(msg):
    tam = len(msg) + 4
    print('~' * tam)
    print(f'  {msg}')
    print('~' * tam)


while True:
    titulo('SISTEMA DE AJUDA PyHELP!')
    quest = str(input('Função ou Biblioteca > ')).strip().lower()
    if quest in 'fim':
        break
    else:
        ajuda(quest)
print('See You later!')
