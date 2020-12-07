from ex109 import moeda

## Main Program ##
num = float(input('Digite um preço: R$'))
print(f'A metade de {moeda.moeda(num)} é {moeda.metade(num, True)}\n'
      f'O dobro de {moeda.moeda(num)} é {moeda.dobro(num, True)}\n'
      f'Aumentando 10%, temos {moeda.aumentar(num, 10, True)}\n'
      f'Diminuindo 13%, temos {moeda.diminuir(num, 13, True)}')