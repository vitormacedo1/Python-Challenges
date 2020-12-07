from ex108 import moeda

## Main Program ##
num = float(input('Digite um preço: R$'))
print(f'A metade de {moeda(num, clean=False)} é {moeda.moeda(moeda.metade(num))}\n'
      f'O dobro de {moeda.moeda(num)} é {moeda.moeda(moeda.dobro(num))}\n'
      f'Aumentando 10%, temos {moeda.moeda(moeda.aumentar(num, 10))}\n'
      f'Diminuindo 13%, temos {moeda.moeda(moeda.diminuir(num, 13))}')