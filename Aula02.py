n1 = int(input('Um valor: '))
n2 = int(input('Outro valor: '))
s = n1+n2
m = n1*n2
d = n1/n2
di = n1//n2
p = n1**n2
print('A soma é {:=>500}, \n a multiplicação é {:_<500}, a divisão \n é {:.3f} '.format(s, m, d), end=' ')
print('A divisão inteira é {} e a potenciação é {}'.format(di, p))