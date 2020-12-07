import random
from time import sleep
n = random.randint(0, 5)
num = 0
print('PROCESSANDO...')
sleep(4)
while num != n:
    num = int(input('Escolha um numero entre 0 e 5: '))
    if n == num:
        print('Tu é o bixão mesmo')
    else:
        if n > num:
            print('Mais Alto!')
        else:
            print('Mais Baixo!')

