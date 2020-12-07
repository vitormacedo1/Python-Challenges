print('Descubra os 10 primeiros termos de uma P.A')
termo = float(input('Digite o primeiro termo da P.A desejada: '))
razao = float(input('digite a razão dessa P.A: '))
print('Os 10 primeiros termos da P.A são: ', end='')
for c in range(0, 10):
    print(termo + c *razao, ', ', end='')
