from random import randint
'''r1 = randint(0, 100)
r2 = randint(0, 100)
r3 = randint(0, 100)
r4 = randint(0, 100)
r5 = randint(0, 100)'''
num = (randint(1, 100), randint(1, 100), randint(1, 100),
       randint(1, 100), randint(1, 100), )
print(f'os numeros sorteados foram: {num}')
print(f'O maior numero sorteado foi: {max(num)}')
print(f'O menor numero sorteado foi: {min(num)}')