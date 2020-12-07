dado = [[], []]
valor = 0
for c in range(1, 8):
    valor = int(input(f'Digite o {c}º numero: '))
    if valor % 2 == 0:
        dado[0].append(valor)
    else:
        dado[1].append(valor)
dado[0].sort()
dado[1].sort()
print(f'Os valores pares digitados foram: {dado[0]}')
print(f'Os numeros impares digitados forma: {dado[1]}')
