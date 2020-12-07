num1 = int(input('Digite um numero inteiro: '))
num2 = int(input('Digite outro numero inteiro: '))
print('O primeiro valor é {}\nO segundo valor é {}'.format(num1, num2))
print('-*-'*10)
if num1 > num2:
    print('O primeiro valor é maior')
elif num1 < num2:
    print('O segundo numero é maior')
else:
    print('Querendo me enganar? Eles são iguais')

