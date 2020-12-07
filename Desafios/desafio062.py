print('Gerador de P.A')
primeiro = int(input('Primeiro termo da P.A: '))
razao = int(input('Razão da P.A: '))
termo = primeiro
mais = 10
cont = 1
total = 0
while mais != 0:
    total = total + mais
    while cont <= total:
        print('{}'.format(cont), end='-')
        termo += razao
        cont += 1
    print('\nPausa')
    mais = int(input('Quantos termos quer mostrar a mais? '))
print('Progressão finalizda com {} termos.'.format(total))
