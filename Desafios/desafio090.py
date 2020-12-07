escola = {}
escola['nome'] = str(input('Nome: ')).strip().lower().capitalize()
escola['media'] = float(input(f'A média de {escola["nome"]}: '))

print('-=' * 17)

print(f'{"O nome é":>16}', f'{escola["nome"]}')
print(f'{"A média é":>17}', f'{escola["media"]}')
if escola['media'] >= 7:
    print(f"{'Situação: APROVADO.':>25}")
elif 5 <= escola['media'] < 7:
    print(f"{'Situação: RECUPERAÇÃO.':>27}")
else:
    print(f"{'Situação: REPROVADO.':>26}")

print('-=' * 17)
