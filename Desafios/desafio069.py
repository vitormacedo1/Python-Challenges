si = sm = sh = sp = 0
while True:
    print('-'*20)
    idade = int(input('Digite sua idade: '))
    sexo = ''
    while sexo != 'f' and sexo != 'm':
        sexo = str(input('Digite seu sexo [M/F] ')).strip().lower()[0]
    parar = ''
    while parar != 's' and parar != 'n':
        parar = str(input('Desaja parar? [S/N] ')).strip().lower()[0]
    sp += 1
    if idade > 18:
        si += 1
    if sexo == 'm':
        sh += 1
    if sexo == 'f' and idade < 20:
        sm += 1
    if parar == 's':
        break
print(f'Foram cadastradas {sp} pessoa, sendo delas {si} tem mais de 18 anos, {sh} homens e {sm} mulheres com menos de 20 anos')
