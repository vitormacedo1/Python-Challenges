'''from math import (pow, sqrt)
co = float(input('Valor do cateto oposto: '))
ca = float(input('Valor do cateto adjacente: '))
d = (co**2) + (ca**2)
h = sqrt(d)
print('Com o cateto oposto valendo {} e o adjacente valendo {} sua hipotenusa é: {}'.format(co, ca, h))'''
from math import hypot
co = float(input('Valor do cateto oposto: '))
ca = float(input('Valor do cateto adjacente: '))
h = hypot(co, ca)
print('Com o cateto {} e {} a hipotenusa é {:.2f}'.format(co, ca, h))
