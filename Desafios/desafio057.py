sexo = str(input('Digite o seu sexo [M/F]: ')).lower()
while sexo != 'm' and sexo !='f':
    print('Erro de digitação, tente novamente.')
    sexo = str(input('Digite seu sexo [M/F]: '))
if sexo == 'm':
    print('Você é do sexo Masculino')
else:
    print('Você é do sexo Feminino')