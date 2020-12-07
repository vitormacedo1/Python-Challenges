
print('=-' * 15)
print(f'{"CALCULADOR DE MÉDIAS!":^30}')
print('=-' * 15)
nota = [float(input('Digite o valor da Nota: ')), float(input('Digite o valor da Nota: '))]
med = (nota[0] + nota[1]) / 2
print(f'A média das notas é {med}')
if med >= 7:
    print('APROVADO!')
elif 5.9 <= med < 7:
    print('RECUPERAÇÃO')
else:
    print('REPROVADO')