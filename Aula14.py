from random import  randint
print('='*5, 'JOGO DA ADIVINHAÇÃO',  '='*5)
ran = randint(1, 150)
num = 1
while num != ran:
    num = int(input('Digite um numero entre 1 e 150: '))

    if num > ran:
        print('Mais Baixo!')
    if num < ran:
        print('Mais Alto!')
print('Acertou!')