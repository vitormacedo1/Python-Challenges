num = 'zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte'
n = int(input('DIgite um numero de 0 a 20: '))
while True:
    if n > 20 or n < 0:
        n = int(input('Tente Novamente! Digite um numero entre 0 e 20: '))
    print(f'O numero {n} escrito por extenso é {num[n]}')
    stop = str(input('Quer continuar? [S/N] ')).strip().lower()
    if stop == 'n':
        print('Obrigado, volte sempre!')
        break
    elif stop == 's':
        n = int(input('Digite um numero entre 0 e 20: '))
