boletin = [[]]
ficha = []
while True:
    nome = str(input('NOME: ')).lower().capitalize()
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    boletin.append([nome], [nota1, nota2], [media])
    perg = str(input('Quer continuar? [S/N] '))
    if perg in 'Nn':
        break
    ficha.append(boletin[:])
    boletin.clear()
print('-=' * 30)
print(f'{"No.":<4}{"NOME":^10}{"Nota":>8}')
print('-' * 30)
'''for i, l in enumerate(boletin):
    print(f'{i:<4}{l[0]:^10}{l[2]:>8.1f}')'''
print(boletin)