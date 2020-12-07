num = 0
soma = 0
somanum = 0
while num != 999:
    num = int(input('Digite uma numero inteiro: [999 para parar] '))
    soma += num
    somanum += 1
print('A soma dos {} numeros digitados foi {}'.format(somanum - 1, soma - 999))
