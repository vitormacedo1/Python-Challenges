n = s = c = 0
while True:
    n = int(input('Digite um numero inteiro (999 para parar): '))
    if n == 999:
        break
    s += n
    c += 1
print('Acabou!')
print(f'A soma foi {s}, e o total de valores digitados foram {c}. ')