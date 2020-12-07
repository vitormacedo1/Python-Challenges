import emoji
import random
from time import sleep
print('Jogue jokenpô comigo')
n0 = str(input('Digite se que PEDRA, PAPEL ou TESOURA: ')).lower().strip()

joke = random.randint(1, 3)

""" PRA FAZER COM PALAVRAS DO JEITO FACIL:
item = (Pedra, Papel, Tesoura)
computer = random.randint(0, 2)
print('O computado escolheu {}'.format(item[computador])"""

print('JO')
sleep(0.8)
print('KEN')
sleep(0.8)
print('PO !!!!!!')

print('=*'*10)


if n0 == 'pedra':
    if joke == 2:
        print(emoji.emojize(':punch: x :raised_hand: : GANHEI!', use_aliases=True))
    elif joke == 3:
        print(emoji.emojize(':punch: x :v: : GANHOU!', use_aliases=True))
    else:
        print(emoji.emojize(':punch: x :punch: : EMPATAMO!', use_aliases=True))
elif n0 == 'papel':
    if joke == 1:
        print(emoji.emojize(':raised_hand: x :punch: : GANHOU!', use_aliases=True))
    elif joke == 3:
        print(emoji.emojize(':raised_hand: x :v: : GANHEI!', use_aliases=True))
    else:
        print(emoji.emojize(':raised_hand: x :raised_hand: : EMPATAMO', use_aliases=True))
elif n0 == 'tesoura':
    if joke == 1:
        print(emoji.emojize(':v: x :punch: : GANHEI!', use_aliases=True))
    elif joke == 2:
        print(emoji.emojize(':v: x raised_hand : GANHOU!', use_aliases=True))
    else:
        print(emoji.emojize(':v: x :v: : EMPATAMO!', use_aliases=True))
else:
    print('TA QUERENDO ROUBAR? JOGA CERTO!')
print('=*'*10)
