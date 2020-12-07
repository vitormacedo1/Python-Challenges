from ex107 import moeda

num = int(input('Digite um preço: R$'))
print(f'O dobro de R${num} é R${moeda.dobro(num)}\n'
      f'A metade de R${num} é R${moeda.metade(num)}\n'
      f'Aumentando 10%, temos R${moeda.aumentar(num, 10)}\n'
      f'Diminuindo 13%, temos R${moeda.diminuir(num, 13)}')