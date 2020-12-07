'''from datetime import date
data = date.today().year
for c in range(1, 7):
        pessoa = int(input('Que ano a {}º pessoa nasceu?'.format(c)))
if data - pessoa >= 18:
    print('Tem {} pessoas maiores de idade'.format(c))
elif data - pessoa < 18:
    print('Tem {} pessoas menores de idade'.format(c))'''
from datetime import date
data = date.today().year
totmaior = 0
total = 0
for c in range(1, 8):
    r = int(input('Qual a ano que a {}º pessoa nasceu? '.format(c)))
    idade = data - r
    if idade >= 21:
       totmaior += 1
    elif idade < 21:
        total += 1
print('Tem {} maiores de idade'.format(totmaior))
print('Tem {} menores de idade'.format(total))

