print('Consulte se será possivel o emprestimo!')
vcasa = float(input('Qual o valor da casa? R$'))
salario = float(input('Qual o seu salário? R$'))
anos = int(input('Em quantos anos pretende pagar? '))
mes = anos * 12
prest = vcasa / mes
if prest <= (salario * 30 /100):
    print('PARABÉNS, seu empréstimo foi aprovado com uma prestação de R${:.2f}'.format(prest))
else:
    print('Inflizmente seu empréstimo não foi aprovado, pois a prestação seria de R${:.2f}.'.format(prest))