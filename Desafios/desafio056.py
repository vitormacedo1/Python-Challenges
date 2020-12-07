ano = 0
anom = 0
nomevelho = ''
soma = 0
for c in range(1, 5):
    print('-'*5, '{}º pessoa'.format(c), '-'*5)
    nome = str(input('Nome: ')).strip().lower()
    idade = float(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip().lower()
    soma += idade
    if sexo == 'f':
        if idade < 20:
            ano += 1

    elif sexo == 'm':
        if c == 1:
            anom = idade
            nomevelho = nome
        else:
            if idade > anom:
                anom = idade
                nomevelho = nome
media = soma / 4
print('A média de idade é {}'.format(media))
print('O homem mais velho tem {} anos e se chama {}'.format(anom, nomevelho.capitalize()))
print('Tem {} meninas menor de 20 anos'.format(ano))