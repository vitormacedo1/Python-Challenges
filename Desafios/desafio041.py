from datetime import date
idade = date.today().year
print('=' * 40)
print(f'{"DETECTOR DE CATEGORIAS":^40}')
print('=' * 40)
ano = int(input('Digite o seu ano de nascimento: '))
cat = idade - ano
print(f'A sua idade é {cat}')
if cat <= 9:
    print('A sua categoria é MIRIM')
elif 9 < cat <= 14:
    print('A sua categoria é INFATIL')
elif 14 < cat <= 19:
    print('A sua categoria é JUNIOR')
elif 19 < cat < 25:
    print('A sua categoria é SÊNIOR')
else:
    print('A sua categoria é MASTER')
