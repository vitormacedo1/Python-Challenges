# conversão de algoritimos
num = int(input('Digite um numero inteiro: '))
print('''Escolha uma das bases de converção
[ 1 ] converter para BINÁRIO: 
[ 2 ] converter para OCTAL
[ 3 ] converter para EXADECIMAL: ''')
op = int(input('Qual sua opção? '))
if op == 1:
    print('Para o numero {} o seu valor em BINÁRIO é {}'.format(num, bin(num)[2:]))
elif op == 2:
    print('Para o numero {} o seu valor em OCTAL é {}'.format(num, oct(num)[2:]))
elif op == 3:
    print('Para o numero {} o seu valor em EXADECIMAL é {}'.format(num, hex(num)[2:]))
else:
    print('OPÇÃO INVALIDA! ENCERRANDO. . .')