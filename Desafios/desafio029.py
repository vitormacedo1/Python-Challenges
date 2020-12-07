velo = float(input('Velocidade do Automovel: '))
if velo > 80:
    print('Parabens Speed Racer você foi multado')
    m = (velo - 80) * 7
    print('Sua multa é de R${:.2f}'.format(m))
else:
    print('Parabéns, você é um motorista top!')