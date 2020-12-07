import math
num = int(input('Digite um numero: '))
re = num % 2 # Por que quando se divide por dois e o numero é par resta zero mas se é impar é 1!
if re == 0:
    print('É um numero par!')
else:
    print('É um numero impar!')
