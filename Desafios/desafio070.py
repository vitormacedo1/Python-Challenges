s = sm = sp = menor =0
barato = ''
while True:
    print('-'*30)
    product = str(input('Digite o nome do produto: ')).strip().lower()
    price = float(input('Digite o valor do pruduto: '))
    print('-'*30)
    repeat = ' '
    while repeat not in 'sn':
        repeat = str(input('Quer continuar a compra? [S/N] ')).strip().lower()
    s += price
    sp += 1
    if repeat == 'n':
        break
    if price > 1000:
        sm += 1
    if sp == 1 or price < menor:
        menor = price
        barato = product
print(f'O total da compra foi R${s}.')
print(f'Foram {sm} produtos acima de mil reais')
print(f'O produto mais barato foi {barato} custando R${menor}.')
