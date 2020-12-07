pessoas = {}
nome = []
idade = []
sexo = []
while True:
    nome.append(str(input('Nome: ')).lower().capitalize())
    sex = str(input('Sexo:[M/F] ')).upper()
    if sex not in 'MmFf':
        print('ERROR. DIGITE APENAS M OU F')
        sex = str(input('Sexo:[M/F] '))
    else:
        sexo.append(sex)
    idade.append(int(input('Idade: ')))
    seq = str(input('Quer continuar:[S/N] '))
    if seq not in 'SsNn':
        print('ERROR. DIGITE APENAS S OU N')
    if seq in 'Nn':
        break

pessoas['nome'] = nome[:]
pessoas['sexo'] = sexo[:]
pessoas['idade'] = idade[:]
media = (sum(pessoas['idade']) / len(pessoas['idade']))

print('-=' * 27)
print(f'A) Ao todo temos {len(pessoas["nome"])} pessoas cadastradas.')
print(f'B) A média de idade é {media:.2f} anos')
print(f'C) A(s) mulher(es) cadastrada(s) foram: ', end='')
for x, c in enumerate(pessoas['sexo']):
    if c == 'F':
        print(f'{pessoas["nome"][x]}', end=', ')
print(f'\nD) Lista de pessoas que estão acima da média:')
for l, m in enumerate(pessoas['idade']):
    if m > media:
        print(f'-Nome: {pessoas["nome"][l]}, sexo: {pessoas["sexo"][l]}, idade: {pessoas["idade"][l]}.')
print('-=' * 27)
