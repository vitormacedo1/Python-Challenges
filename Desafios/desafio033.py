n1 = float(input('Digite um numero: '))
n2 = float(input('Digite outro numero: '))
n3 = float(input('Digite outro numero: '))
menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3
print('O menor numero digitado foi {}'.format(menor))
maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3
print('O maior numero digitado foi {}'.format(maior))
import emoji
if n1 == n2 == n3:
    print(emoji.emojize('Ta achando que eu sou otário? :sob:', use_aliases=True))
