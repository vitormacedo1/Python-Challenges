n = input('Digite seu nome completo: ')
nM = n.upper()
nm = n.lower()
ns = n.split()
nl = len(ns)
np = n.split()

npp = len(np[0])

print('Letras Maiusculas: {}\nLetras Minusculas: {}\nNumero de Letras: {}\nNumero de Letra do Primeiro Nome {}'.format(nM, nm, len(n) - n.count(' '), npp))