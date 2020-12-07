sequencia = 's'
soma = 0
num1 = 0
media = 0
maior = 0
menor = 0
while sequencia == 's':
    num = int(input('Digite um numero inteiro: '))
    sequencia = str(input('Quer continuar [S/N]: ')).strip().lower()
    soma += 1
    num1 += num
    if soma == 1:
        maior = menor = num
    else:
        if num > maior:
            num = maior
        if num < menor:
            num = menor
media = num1 / soma
print('O maior numero é {} e o menor é {}'.format(maior, menor))
print('Você digitou {} numeros e a média deles é {}'.format(soma, media))
