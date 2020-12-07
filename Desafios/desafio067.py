from time import sleep
while True:
    n = int(input('Digite um numero para saber sua tabuada, (digite um numero negativo para parar): '))
    if n < 0:
        break
    print('CALCULANDO . . .')
    sleep(0.6)
    print('Pra que esses numeros tão grandes?')
    sleep(0.8)
    for c in range(1, 11):
        print(f'{n} x {c} = {n * c}')
print('Processo cancelado, Volte Sempre!')
