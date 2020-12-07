print('CONTROLE DE TERRENOS')


def area(larg, comp):
    area = larg * comp
    print(f'A área de um terreno {larg} x {comp} é de {area}m²')

# main program 
l = float(input('Largura do terreno: '))
c = float(input('Comprimento do terreno: '))
area(l, c)