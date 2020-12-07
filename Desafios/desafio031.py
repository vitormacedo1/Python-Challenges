p = float(input('Quantos Km são de viagem? '))
if p <= 200:
    print('A sua passagem custará R${:.2f} e boa viagem!'.format(p*0.5))
else:
    print('A sua passagem custará R${:.2f} e boa viagem'.format((p*0.45)))

