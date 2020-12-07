n1 = str(input('Primeiro aluno: '))
n2 = str(input('Segundo aluno: '))
n3 = str(input('Terceiro aluno: '))
n4 = str(input('Quarto aluno: '))
l = [n1, n2, n3, n4]
import random
e = random.choice(l)
print('O escolhido é {}'.format(e))