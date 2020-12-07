exp = str(input('Digite uma expressão matemática: '))
if exp.count('(') == exp.count(')'):
    print('A expressão é valida!')
else:
    print('A expressão é inválida')