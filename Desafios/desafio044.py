print('{:=^40}'.format(' Loja de roupas! '))

preco = float(input('Digite o valor do produto: '))

pay = str(input('Digite a forma de pagamento: ')).lower().strip()

if pay == 'dinheiro' or pay == 'cheque':
    print('O valor a ser pago é R${:.2f}'.format(preco - (preco * 10 / 100)))

elif pay == 'cartao':

    prest = float(input('Em quantas vezes? '))

    if prest == 1:

         print('O valor a ser pago é R${:.2f}'.format(preco - (preco * 5 / 100)))

    elif prest == 2:

         print('O valor a ser pago é R${:.2f}'.format(preco))

    elif prest >= 3:

        print('O valor a ser pago é R${.:2f}'.format(preco + (preco + 20 / 100)))
else:
    print('Opção pagamento inválida! Tente outra vez.')
print('MUITO OBRIGADO POR COMPRAR AQUI!')
