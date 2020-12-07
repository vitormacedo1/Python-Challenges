from random import randint
print('='*5, 'JOGO DA ADIVINHAÇÃO', '='*5)
num = 11
ran = randint(0, 10)
soma = 0
while num != ran:
    num = int(input('Digite um numero inteiro entre 1 e 10: '))
    if num > ran:
        print('Mais Baixo!')
    if num < ran:
        print('Mais Alto!')
    soma += 1
print('Jogador Ganhou em {} tentativa!'.format(soma))
