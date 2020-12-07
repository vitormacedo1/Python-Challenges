sa = float(input('Digite seu salário: '))
if sa > 1250:
    print('Seu aumento será de R${:.2f}'.format(sa + (sa * 10 / 100)))
else:
    print('Seu aumento será de R${:.2f}'.format(sa + (sa * 15 /100)))