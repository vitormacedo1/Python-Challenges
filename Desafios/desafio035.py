print('\033[1;31m-=\033[m'*30)
print('Descubra se os segmentos de retas formam um triangulo!')
print('E se são isóceles, escaleno ou equilátero')
print('-='*30)
l1 = float(input('Primeiro segmento: '))
l2 = float(input('Segundo segmento: '))
l3 = float(input('Terceiro segmento: '))
if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l1 + l2:
    print('Com {}, {} e {} pode-se fazer um triangulo!'.format(l1, l2, l3))
    if l1 == l2 == l3:
        print('E ainda é um triangulo equilátero!')
    elif l1 == l2 or l2 == l3 or l1 == l3:
        print('E ainda é um triangulo isóceles!')
    elif l1 != l2 != l3 != l1:
        print('E ainda é um triangulo escaleno!')
else:
    print('Com esses valores não se pode fazer um triangulo')
